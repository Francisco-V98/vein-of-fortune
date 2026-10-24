"""Pruebas de los módulos de datos del cerebro (F0-90, parte 2A): mundo, economía, QA, simulador y arte.

Se ejecutan sobre el repo real (los datos de studio/data y el documento 26): conteos por tipo contra las fuentes, enlaces
sin resolver = 0, nombres de archivo únicos y válidos, relaciones cruzadas clave e idempotencia. Ejecutar:
    python3 -m unittest discover -s tools/ci -p "test_cerebro_mundo.py" -v
"""
import json
import pathlib
import re
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from cerebro import generar  # noqa: E402

MODULOS = ["documentos", "tareas", "equipo", "mundo", "economia", "qa", "simulador", "arte"]
PROHIBIDOS = set('#^[]|:/\\?*"<>')
TIPOS_PROPIOS = {"acto", "mineral", "zona", "asentamiento", "edificacion", "receta", "minijuego", "mecanica", "faccion", "personaje", "pnj",
                 "economia", "caso-qa", "regla-sim", "perfil-sim", "supuestos-sim", "resultados-sim", "politica-arte", "paleta", "arte-personaje",
                 "galeria", "arte-pieza", "audio"}


def datos(ruta):
    return json.loads((ROOT / ruta).read_text(encoding="utf-8"))


def construir():
    registro = generar.construir_registro(ROOT, MODULOS)
    archivos = registro.construir()
    return registro, archivos


class PruebasDatosDelCerebro(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registro, cls.archivos = construir()
        cls.world = datos("studio/data/world.json")
        cls.conteo = cls.registro.conteo()

    def test_ningun_modulo_falla_ni_hay_enlaces_sin_resolver(self):
        malos = [a for a in self.registro.avisos if "falló" in a or "sin resolver" in a or "alias" in a]
        self.assertEqual(malos, [])

    def test_sin_notas_huerfanas_en_los_tipos_de_datos(self):
        nombres = {self.registro.notas[i].nombre for i in self.registro.notas if self.registro.notas[i].tipo in TIPOS_PROPIOS | {"moc"}}
        huerfanas = [a for a in self.registro.avisos if a.startswith("nota huérfana") and a.split(": ", 1)[1] in nombres]
        self.assertEqual(huerfanas, [])

    def test_conteos_por_tipo_contra_las_fuentes(self):
        w, c = self.world, self.conteo
        docs26 = next((ROOT / "studio" / "docs").glob("26-*.md")).read_text(encoding="utf-8")
        filas_ed = len(set(re.findall(r"^\|\s*`(ed-[a-z0-9-]+)`", docs26, re.M)))
        esperado = {
            "acto": len(w["acts"]), "mineral": len(w["minerals"]), "zona": len(w["zones"]), "asentamiento": 6, "edificacion": filas_ed,
            "receta": len(w["recipes"]), "minijuego": len(w["minigames"]), "mecanica": len(w["mechanics"]), "faccion": len(w["factions"]),
            "personaje": len(w["characters"]), "pnj": len(w["npcs"]), "economia": len([k for k in w["economy"] if k != "nota"]),
            "caso-qa": len(datos("studio/data/qa/cases.json")["cases"]), "regla-sim": len(datos("studio/data/sim/reglas.json")["reglas"]),
            "perfil-sim": len(datos("studio/data/sim/resultados.json")["perfiles"]),
        }
        for tipo, n in esperado.items():
            self.assertEqual(c.get(tipo), n, tipo)
        self.assertGreaterEqual(filas_ed, 46)
        self.assertEqual((c["caso-qa"], c["regla-sim"]), (55, 50))
        arte = datos("studio/data/assets.json")
        self.assertEqual(c["galeria"], len(datos("studio/data/galeria.json")["secciones"]))
        self.assertEqual(c["arte-personaje"], len(datos("studio/data/galeria.json")["personajes"]))
        self.assertEqual(c["paleta"], 1)
        self.assertEqual(c["audio"], 1 if arte["sounds_planned"] else 0)

    def test_toda_imagen_registrada_esta_cubierta_por_una_nota_de_arte(self):
        arte = datos("studio/data/assets.json")
        cubiertas = 0
        for n in self.registro.notas.values():
            if n.tipo == "arte-pieza":
                cubiertas += 1
            elif n.tipo == "arte-personaje":
                cubiertas += n.props["hojas"]
        hojas_npc = sum(len(s["hojas"]) for s in datos("studio/data/galeria.json")["secciones"])
        self.assertEqual(cubiertas + hojas_npc, len(arte["images"]))

    def test_nombres_de_archivo_unicos_y_validos(self):
        self.assertEqual(len(self.archivos), len(self.registro.notas))
        self.assertEqual(len({r.casefold() for r in self.archivos}), len(self.archivos))
        for n in self.registro.notas.values():
            self.assertFalse(PROHIBIDOS & set(n.nombre), n.nombre)
            self.assertTrue(n.arriba or n.tipo in ("moc", "inicio"), "sin arriba: " + n.id)

    def test_nombres_legibles_y_desambiguados(self):
        r = self.registro
        self.assertEqual(r.nota("pj-reme").nombre, "Reme")
        self.assertEqual(r.nota("min-carbon").nombre, "Carbón")
        self.assertEqual(r.nota("asent-villa-brasa").nombre, "Villa Brasa")
        self.assertEqual(r.nota("ed-vb-taller").nombre, "Taller de Villa Brasa")
        self.assertEqual(r.nota("mec-taller").nombre, "Taller (mecánica)")
        self.assertEqual(r.nota("qa-TC-001").nombre[:6], "TC-001")
        self.assertEqual(r.nota("sim-A1").nombre[:2], "A1")

    def test_ids_estables_y_alias_de_personajes(self):
        r = self.registro
        for i in ("min-carbon", "zona-galerias-hollin", "ed-vb-tienda", "fac-union", "pj-reme", "npc-voceador", "rec-acero", "mj-picado",
                  "eco-debt", "qa-TC-001", "sim-A1", "acto-I", "moc-mundo", "moc-minerales", "moc-zonas", "moc-edificaciones", "moc-facciones",
                  "moc-personajes", "moc-economia", "moc-qa", "moc-simulador", "moc-arte"):
            self.assertTrue(r.existe(i), i)
        for c in self.world["characters"]:
            for nombre in [c["name"]] + c.get("aka", []):
                self.assertEqual(r.nota(nombre).id, "pj-" + c["id"], nombre)
        self.assertEqual(r.nota("Inspector Quiroga").id, "pj-quiroga")
        self.assertEqual(r.nota("TC-001").id, "qa-TC-001")

    def test_relaciones_cruzadas_clave(self):
        r = self.registro
        carbon = self.archivos[r.nota("min-carbon").archivo]
        for destino in ("Galerías del Hollín", "Acero", "Pólvora", "Picado", "Tienda de Villa Brasa"):
            self.assertIn("[[%s]]" % destino, carbon)
        tienda = self.archivos[r.nota("ed-vb-tienda").archivo]
        self.assertIn("[[Villa Brasa]]", tienda)
        self.assertIn("[[Regateo]]", tienda)
        boca = self.archivos[r.nota("ed-vb-mina-galerias").archivo]
        self.assertIn("[[Galerías del Hollín]]", boca)
        self.assertIn("[[Teo Cárdenas]]", boca)
        deuda = self.archivos[r.nota("eco-debt").archivo]
        self.assertIn("[[28 §7 Deuda del Acto I y sus nombres]]", deuda)
        self.assertIn("[[A1 Cuota del día 7 sin mejora]]", deuda)
        self.assertIn("[[Reme]]", deuda)
        caso = self.archivos[r.nota("qa-TC-001").archivo]
        self.assertIn("[[F2-02 ", caso)
        self.assertIn("[[16 Calidad y QA]]", caso)
        regla = self.archivos[r.nota("sim-A1").archivo]
        self.assertIn("[[28 §7 ", regla)
        self.assertIn("estado: \"pasa\"", regla)
        celda = self.archivos[r.nota("rec-celda-eter").archivo]
        self.assertIn("[[Comisión del Éter]]", celda)
        self.assertIn("[[Consorcio Arvel]]", celda)
        self.assertIn("[[Arte de Reme]]", self.archivos[r.nota("pj-reme").archivo])
        self.assertIn("[[Galería - NPC de las facciones]]", self.archivos[r.nota("npc-voceador").archivo] + self.archivos[r.nota("npc-escribiente").archivo])

    def test_el_arte_actual_es_provisional(self):
        for n in self.registro.por_tipo("arte-pieza") + self.registro.por_tipo("arte-personaje") + self.registro.por_tipo("galeria"):
            self.assertEqual(n.props["estado"], "provisional", n.id)

    def test_cada_mineral_en_dos_o_tres_zonas_salvo_excepciones(self):
        reglas = self.world["rules"]
        for m in self.world["minerals"]:
            n = len(m["zones"])
            if m["id"] not in reglas["mineral_zones_excepciones"]:
                self.assertTrue(reglas["mineral_zones_min"] <= n <= reglas["mineral_zones_max"], m["id"])
            self.assertEqual(len(self.registro.nota("min-" + m["id"]).props["zonas"]), n)

    def test_idempotencia_sobre_el_repo_real(self):
        _, otra = construir()
        self.assertEqual(self.archivos, otra)


if __name__ == "__main__":
    unittest.main()
