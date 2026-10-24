"""Pruebas de la narrativa y el glosario del cerebro (F0-90, parte 2B): tools/cerebro/mod_narrativa.py, mod_glosario.py y narr_fuentes.py.

Unas pruebas usan fragmentos mínimos (tablas de los documentos 18, 25 y 27, referencias de hilos); otras recorren el repo real:
conteos por tipo, enlaces que resuelven, nombres únicos, alias y salida idéntica entre pasadas. Ejecutar:
    python3 -m unittest discover -s tools/ci -p "test_cerebro_narrativa.py" -v
"""
import json
import pathlib
import re
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from cerebro import generar, narr_fuentes as F, nucleo  # noqa: E402

PROHIBIDOS = set('#^[]|:/\\?*"<>')
PREFIJOS_DEL_MUNDO = ("pj-", "npc-", "ed-", "fac-", "acto-")  # los crea la parte del mundo; aquí solo se enlazan de forma opcional
MODULOS = ["documentos", "tareas", "equipo", "memoria", "mundo", "narrativa", "glosario"]
TIPOS_NARRATIVA = {"nodo", "opcion", "bandera", "medidor", "cuello", "cinta", "hilo", "escena", "pieza", "carril", "historia", "termino"}

DOC_18 = """# 18 · Biblia

## 6 · Glosario ES/EN

### 6.2 Mundo

| Español | English | Estado | Nota de uso |
|---|---|---|---|
| Aetherita | Aetherite | ✅ | Siempre el mineral ([13](13-marca.md)) |
| 1 · Galerías del Hollín | Hollín Galleries | ✅ | Zona 1 |
| Altafría | Highchill | ✅ en español · ⏳ F1-20 en inglés | Pueblo de empresa |
| Paseo Marítimo · Colina de la Bolsa | sin traducir ⏳ F1-20 | ✅ en español · ⏳ F1-20 en inglés | Mansiones |

### 6.3 Minerales

| Español | English | Estado | Nota de uso |
|---|---|---|---|
| Carbón | Coal | ✅ | Directo |
| Aetherita | Aetherite | ✅ | Ver 6.2 |

### 6.13 Reglas

1. Nunca se traduce Valdoria.
"""
DOC_25 = """# 25 · Finales

## 4 · La cabecera

| ID | Cuándo | Lee | Medio | Ejemplo (guía) |
|---|---|---|---|---|
| H-01 | Revelas y la Unión está alta | `f-destino`, `e-union` | Voz | **Narrador:** Dijiste la verdad. |

## 5 · Las 54 piezas

| ID | Cuándo | Lee | Medio | Ejemplo (guía) |
|---|---|---|---|---|
| LU-01 | Revelas y su tramo es alto | `e-lucia` | Teletipo | «LUCÍA PUBLICA. SIN CONFIRMAR» |
| FM-01 | Se lo contaste todo | `f-familia` | Narrador | «Llega una carta.» |

## 6 · Cobertura

| Camino | Salida | Unión | Alianza | Piezas |
|---|---|---|---|---|
| 1 | Revelar | alto | Consorcio | H-01 LU-01 FM-01 |
"""
DOC_27 = """# 27 · Guion

## 21 · Esquema de escenas y textos

### 21.2 Tabla maestra

| Escena | Título | Bloque | Peso | Lugar | Personajes | C | U | K | Total |
|---|---|---|---|---|---|---|---|---|---|
| `d1.1` | Llegada | Mañana | F3-16 | `calle` | `protagonista` | 6 | 4 | 0 | 10 |
| `d1.4` | Las Galerías | Tarde | 1 | `ed-vb-mina-galerias` | `teo`, `protagonista` | 14 | 5 | 0 | 19 |

### 21.3 Disparadores

| Escena | Disparador y requisitos | Opcional y cola | Mecánica que enseña | Decisión |
|---|---|---|---|---|
| `d1.1` | Al empezar | No | Ninguna | — |
| `d1.4` | Tras `d1.3` | No | Expedición | `n-i-herencia` |

### 21.8 Botones

| Botón | Opción | Texto del botón | Caracteres | Fija |
|---|---|---|---|---|
| `n-i-herencia.b1` | `todo` | «Contarles todo» | 14 | `f-familia` |
"""


def escribir(ruta, texto):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(texto, encoding="utf-8")


class FuentesTest(unittest.TestCase):
    def test_tablas_devuelven_cabecera_y_filas(self):
        filas = list(F.tablas(DOC_25.split("\n")))
        self.assertEqual([c[0] for _, _, c in filas if len(c) == 5 and c[0] != "Camino"][:3], ["H-01", "LU-01", "FM-01"])
        self.assertEqual(filas[0][1][0], "ID")

    def test_piezas_caminos_y_botones(self):
        piezas = F.piezas_epilogo(DOC_25)
        self.assertEqual([p["codigo"] for p in piezas], ["H-01", "LU-01", "FM-01"])
        self.assertEqual(piezas[0]["medio"], "Voz")
        self.assertEqual(F.caminos_prueba(DOC_25), [(1, "Revelar", "alto", ["H-01", "LU-01", "FM-01"])])
        self.assertEqual(F.botones_acto1(DOC_27), {("n-i-herencia", "todo"): "Contarles todo"})

    def test_escenas_del_acto_i_juntan_las_tablas_por_escena(self):
        datos, orden = F.escenas_acto1(DOC_27)
        self.assertEqual(orden, ["d1.1", "d1.4"])
        self.assertEqual(datos["d1.4"]["titulo"], "Las Galerías")
        self.assertEqual(datos["d1.4"]["decision"], "`n-i-herencia`")
        self.assertEqual(datos["d1.1"]["personajes"], "`protagonista`")

    def test_rangos_de_piezas_y_cintas(self):
        self.assertEqual(F.expandir_piezas("piezas LU-01 a LU-03 · FM-02"), ["LU-01", "LU-02", "LU-03", "FM-02"])
        self.assertEqual(F.numeros_de_cintas("cintas 6 y 7 · cinta 1 · cintas 2, 3 y 4"), [6, 7, 1, 2, 3, 4])
        self.assertEqual(F.numeros_de_cintas("h-lampara-y-cinta-1"), [])

    def test_extraer_refs_enlaza_secciones_nodos_cintas_y_escenas(self):
        reg = nucleo.Registro()
        reg.nueva("doc-21", "documento", "Doc 21", "docs", arriba="x")
        for n in (5, 11):
            reg.nueva("doc-21-s%02d" % n, "seccion", "%d · S" % n, "secciones", arriba="doc-21")
        reg.nueva("doc-18", "documento", "Doc 18", "docs", arriba="x")
        reg.nueva("doc-18-anexo", "seccion", "Anexo · Cronología", "secciones", arriba="doc-18")
        reg.nueva("doc-19", "documento", "Doc 19", "docs", arriba="x")
        reg.nueva("n-ii-certificado", "nodo", "Certificado", "narrativa", arriba="x")
        reg.nueva("f-certificado", "bandera", "Bandera", "narrativa", arriba="x")
        reg.nueva("cinta-6", "cinta", "Cinta 6", "narrativa", arriba="x")
        reg.nueva("esc-d1.3", "escena", "Libro", "narrativa", arriba="x")
        reg.nueva("F4-139", "tarea", "F4-139", "roadmap", arriba="x")
        reg.nueva("ep-LU-02", "pieza", "LU-02", "narrativa", arriba="x")
        texto = ("doc 21 §5 y §11 · doc 18 Anexo «Dónde está» · doc 19 «Pistas» · doc 22 §1 · nodo n-ii-certificado · bandera f-certificado · "
                 "cinta 6 · doc 27 §4 (día 1, d1.3) · tarea F4-139 · piezas LU-01 a LU-02 · doc 26 ed-vb-tienda · m-nuevo-desconocido")
        r = F.extraer_refs(texto, reg)
        self.assertEqual(r["docs"], ["doc-21-s05", "doc-21-s11", "doc-18-anexo", "doc-19"])  # doc 22 y doc 27 no existen en este registro
        self.assertEqual((r["nodos"], r["banderas"], r["cintas"], r["escenas"], r["tareas"], r["piezas"]),
                         (["n-ii-certificado"], ["f-certificado"], ["cinta-6"], ["esc-d1.3"], ["F4-139"], ["ep-LU-02"]))
        self.assertEqual(r["edificaciones"], ["ed-vb-tienda"])
        self.assertEqual(r["desconocidos"], ["m-nuevo-desconocido"])


class GlosarioTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        base = pathlib.Path(cls.tmp.name)
        escribir(base / "studio" / "docs" / "18-biblia-narrativa.md", DOC_18)
        cls.reg = generar.construir_registro(base, ["glosario"])
        cls.archivos = cls.reg.construir()

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_un_termino_por_fila_y_los_repetidos_se_unen(self):
        terminos = self.reg.por_tipo("termino")
        self.assertEqual([t.id for t in terminos], ["term-aetherita", "term-galerias-del-hollin", "term-altafria", "term-paseo-maritimo-colina-de-la-bolsa", "term-carbon"])
        self.assertEqual(terminos[0].props["tambien_en"], ["6.3 Minerales"])

    def test_ingles_estado_y_nombre_de_archivo(self):
        t = {n.id: n for n in self.reg.por_tipo("termino")}
        self.assertEqual(t["term-carbon"].props["ingles"], "Coal")
        self.assertEqual(t["term-galerias-del-hollin"].titulo, "Galerías del Hollín")  # sin el «1 ·» de la tabla
        self.assertEqual(t["term-altafria"].props["estado_glosario"], "ingles-pendiente")
        self.assertNotIn("ingles", t["term-paseo-maritimo-colina-de-la-bolsa"].props)
        self.assertEqual(t["term-paseo-maritimo-colina-de-la-bolsa"].nombre, "Paseo Marítimo y Colina de la Bolsa")
        self.assertTrue(t["term-carbon"].fuente.startswith("studio/docs/18-biblia-narrativa.md:"))

    def test_moc_agrupa_por_capitulo(self):
        moc = self.reg.nota("moc-glosario")
        self.assertIn("## 6.2 Mundo", moc.cuerpo)
        self.assertIn("## 6.3 Minerales", moc.cuerpo)
        self.assertEqual(len(self.reg.por_tipo("moc")), 1)


class SinDatosTest(unittest.TestCase):
    def test_sin_datos_de_narrativa_ni_glosario_se_omiten_sin_avisos(self):
        with tempfile.TemporaryDirectory() as tmp:
            reg = generar.construir_registro(pathlib.Path(tmp), ["narrativa", "glosario"])
            self.assertEqual(reg.avisos, [])
            self.assertEqual(len(reg.notas), 0)


class RepoRealTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reg = generar.construir_registro(ROOT, MODULOS)
        cls.archivos = cls.reg.construir()
        cls.datos = json.loads((ROOT / "studio/data/decisions.json").read_text(encoding="utf-8"))
        cls.hilos = json.loads((ROOT / "studio/data/hilos.json").read_text(encoding="utf-8"))["hilos"]

    def mias(self):
        return [n for n in self.reg.notas.values() if n.tipo in TIPOS_NARRATIVA or n.id in ("moc-narrativa", "moc-decisiones", "moc-hilos", "moc-escenas", "moc-finales", "moc-cintas", "moc-glosario")]

    def test_conteos_por_tipo(self):
        c = self.reg.conteo()
        self.assertEqual(c["nodo"], len(self.datos["nodes"]))
        self.assertEqual(c["nodo"], 27)
        self.assertEqual(c["opcion"], sum(len(n["opciones"]) for n in self.datos["nodes"]))
        self.assertEqual(c["opcion"], 81)
        self.assertEqual(c["bandera"] + c["medidor"], len(self.datos["flags"]))
        self.assertEqual(c["medidor"], sum(1 for f in self.datos["flags"] if f["tipo"] == "medidor"))
        self.assertEqual(c["cuello"], len(self.datos["cuellos"]))
        self.assertEqual(c["cinta"], 8)
        self.assertEqual(c["hilo"], len(self.hilos))
        self.assertEqual(c["hilo"], 45)
        self.assertEqual(c["escena"], 28)
        self.assertEqual(c["pieza"], 54)
        self.assertEqual(c["carril"], len(json.loads((ROOT / "studio/data/story.json").read_text(encoding="utf-8"))["lanes"]))
        self.assertEqual(c["historia"], 4)
        self.assertGreaterEqual(c["termino"], 150)
        for moc in ("moc-narrativa", "moc-decisiones", "moc-hilos", "moc-escenas", "moc-finales", "moc-cintas", "moc-glosario"):
            self.assertTrue(self.reg.existe(moc), moc)

    def test_ninguna_nota_del_modulo_falla_ni_avisa(self):
        propios = [a for a in self.reg.avisos if "narrativa" in a or "glosario" in a or "hilo h-" in a]
        self.assertEqual(propios, [])

    def test_enlaces_obligatorios_resuelven_y_los_del_mundo_son_opcionales(self):
        sin_resolver, opcionales = [], set()
        for nota in self.mias():
            for m in nucleo.MARCADOR.finditer(nota.previo()):
                destino = m.group("id")
                if m.group("suave"):
                    opcionales.add(destino)
                elif self.reg.resolver_id(destino) is None:
                    sin_resolver.append((nota.id, destino))
        self.assertEqual(sin_resolver, [])
        self.assertTrue({"pj-reme", "pj-teo", "ed-vb-reme"} <= opcionales)  # los enlaces al mundo son opcionales, no avisan

    def test_enlaces_al_mundo_resuelven_si_el_mundo_existe(self):
        if not self.reg.existe("pj-reme"):
            self.skipTest("la parte del mundo todavía no crea los personajes")
        faltan = set()
        for nota in self.mias():
            for m in nucleo.MARCADOR.finditer(nota.previo()):
                destino = m.group("id")
                if destino.startswith(("pj-", "npc-", "ed-")) and self.reg.resolver_id(destino) is None:
                    faltan.add(destino)
        self.assertEqual(sorted(faltan), [])

    def test_nombres_unicos_y_validos(self):
        nombres = set()
        for archivo in self.archivos:
            nombre = pathlib.PurePosixPath(archivo).stem
            self.assertFalse(PROHIBIDOS & set(nombre), nombre)
            self.assertNotIn(nombre.casefold(), nombres, nombre)
            nombres.add(nombre.casefold())

    def test_toda_nota_tiene_arriba_y_los_mapas_listan_sus_hijos(self):
        for nota in self.mias():
            if nota.tipo != "moc":
                self.assertTrue(nota.arriba and self.reg.existe(nota.arriba), nota.id)
        self.assertIn("n-i-herencia", self.reg.nota("moc-decisiones").extra + self.reg.nota("moc-decisiones").cuerpo)
        for h in self.hilos:
            self.assertIn(h["id"], self.reg.nota("moc-hilos").cuerpo)
        for i in range(1, 9):
            self.assertIn("cinta-%d" % i, self.reg.nota("moc-cintas").cuerpo)

    def test_alias_resuelven_ids_de_los_documentos(self):
        self.assertEqual(self.reg.resolver_id("d1.2"), "esc-d1.2")
        self.assertEqual(self.reg.resolver_id("d7.4"), "esc-d7.4")
        self.assertEqual(self.reg.resolver_id("n-i-herencia.b1"), "n-i-herencia.todo")
        self.assertEqual(self.reg.resolver_id("n-i-reme-plazo.b3"), "n-i-reme-plazo.tarde")
        self.assertEqual(self.reg.resolver_id("LU-04"), "ep-LU-04")
        self.assertEqual(self.reg.resolver_id("f-certificado"), "f-certificado")
        self.assertEqual(self.reg.resolver_id("h-abono-anonimo"), "h-abono-anonimo")

    def test_cada_hilo_se_enlaza_a_personajes_y_documentos(self):
        for h in self.hilos:
            nota = self.reg.nota(h["id"])
            self.assertEqual(nota.props["tipo_hilo"], h["tipo"])
            self.assertEqual(len(nota.props["personajes"]), len(h["personajes"]))
            self.assertIn("## Dónde se siembra", self.archivos[nota.archivo])
            tipos = {self.reg.notas[d].tipo for d in nota.enlaces}
            self.assertTrue(tipos & {"seccion", "documento"}, "%s no enlaza a ningún documento" % h["id"])
        if self.reg.existe("pj-anselmo"):
            self.assertIn("pj-anselmo", self.reg.notas["h-anselmo-sigue-vivo"].enlaces)

    def test_enlaces_cruzados_clave(self):
        r = self.reg
        enlaces = lambda id_: set(r.notas[id_].enlaces)  # noqa: E731
        self.assertTrue({"n-ii-certificado", "f-certificado", "doc-21-s05"} <= enlaces("h-certificado-sin-cremacion"))
        self.assertTrue({"n-i-herencia.todo", "n-i-herencia.parte", "n-i-herencia.nada", "f-familia", "c-i-cierre", "historia-I", "esc-d1.6"} <= enlaces("n-i-herencia"))
        self.assertIn("f-pago-reme", enlaces("n-i-reme-plazo.antes"))
        self.assertTrue({"n-i-reme-plazo.antes", "n-ii-orden"} <= enlaces("f-pago-reme"))
        self.assertTrue({"n-i-reme-plazo", "h-deuda-del-protagonista", "doc-27-s10"} <= enlaces("esc-d7.2"))
        self.assertTrue({"esc-d2.4", "doc-23-s07", "moc-cintas"} <= enlaces("cinta-1") | {"moc-cintas"})
        self.assertIn("f-destino", enlaces("ep-H-01"))
        hilos_de_lucia = [h["id"] for h in self.hilos if {"ep-LU-01", "ep-LU-04"} <= enlaces(h["id"])]
        self.assertTrue(hilos_de_lucia, "ningún hilo enlaza a las piezas LU-01 a LU-04")
        self.assertEqual(len([e for e in enlaces("moc-finales") if e.startswith("ep-")]), 54)
        self.assertEqual(len([e for e in enlaces("moc-escenas") if e.startswith("esc-")]), 28)
        self.assertTrue({"moc-decisiones", "moc-hilos", "moc-escenas", "moc-finales", "moc-cintas"} <= enlaces("moc-narrativa"))

    def test_las_escenas_y_las_cintas_enlazan_donde_deben(self):
        r = self.reg
        self.assertIn("cinta-1", r.notas["esc-d2.4"].enlaces)
        self.assertIn("n-i-lucia-rumor", r.notas["esc-d5.2"].enlaces)
        self.assertEqual(r.notas["esc-d1.4"].props["dia"], 1)
        self.assertEqual(r.notas["esc-d1.4"].props["peso"], 1)
        self.assertTrue(r.notas["esc-d1.1"].props["peso"].startswith("por asignar"))
        self.assertEqual(r.notas["esc-d1.2"].props["siguiente"], "⟦esc-d1.3⟧")

    def test_las_piezas_del_epilogo_leen_banderas_reales(self):
        for nota in self.reg.por_tipo("pieza"):
            for b in re.findall(r"`(f-[a-z-]+|m-[a-z]+)`", nota.cuerpo):
                self.assertTrue(self.reg.existe(b), "%s lee %s, que no existe" % (nota.id, b))
        codigos = {n.props["codigo"] for n in self.reg.por_tipo("pieza")}
        self.assertTrue({"H-01", "H-06", "RE-03", "ES-04", "DU-04", "FM-03", "ME-05", "MU-06", "FC-06", "UN-03"} <= codigos)

    def test_el_modulo_es_idempotente_sobre_el_repo_real(self):
        otra = generar.construir_registro(ROOT, MODULOS)
        otros = otra.construir()
        for archivo, texto in self.archivos.items():
            nota = next(n for n in self.reg.notas.values() if n.archivo == archivo)
            if nota.tipo in TIPOS_NARRATIVA or nota.id.startswith("moc-"):
                self.assertEqual(otros.get(archivo), texto, archivo)
        with tempfile.TemporaryDirectory() as tmp:
            destino = pathlib.Path(tmp) / "vault"
            generar.generar_vault(ROOT, destino, modulos=MODULOS, plantilla=None)
            segunda = generar.generar_vault(ROOT, destino, modulos=MODULOS, plantilla=None)
            self.assertEqual((segunda.escritos, segunda.borrados), (0, 0))
            carpetas = {p.name for p in (destino / "generado" / "narrativa").iterdir()}
            self.assertTrue({"decisiones", "opciones", "banderas", "hilos", "escenas", "epilogos", "cintas", "carriles", "actos"} <= carpetas)
            self.assertTrue((destino / "generado" / "glosario").is_dir())


if __name__ == "__main__":
    unittest.main()
