"""Pruebas de las validaciones de asentamientos y edificaciones (F0-83): integridad y comprobación C33 contra el documento 26. Ejecutar:
    python3 -m unittest discover -s tools/ci -v
"""
import copy
import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("coherence", ROOT / "studio" / "hub" / "coherence.py")
coherence = importlib.util.module_from_spec(spec)
spec.loader.exec_module(coherence)

# 1 aduana evolutiva + 45 edificaciones se simulan con la cuenta del propio fixture: el documento de prueba declara «2 filas: las 1 edificaciones».
WORLD = {
    "acts": ["I", "II"],
    "zones": [{"id": "z1", "name": "Zona 1", "act": "I", "place": "villa-brasa"}],
    "minigames": [{"id": "picado", "name": "Picado", "act": "I"}],
    "minerals": [{"id": "carbon", "name": "Carbón", "zones": {"z1": "principal"}, "minigames": ["picado"]}],
    "recipes": [{"id": "acero", "name": "Acero", "inputs": [["carbon"]]}],
    "factions": [{"id": "union", "name": "Unión"}],
    "characters": [{"id": "teo", "name": "Teo", "act": "I", "faction": "union"}],
    "npcs": [{"id": "capataz", "name": "Capataz", "group": "g", "faction": "union"}],
    "settlements": [{"id": "villa-brasa", "name": "Villa Brasa", "region": "R", "act": "I", "zones": ["z1"]}],
    "buildings": [
        {"id": "ed-vb-mina", "name": "Boca", "settlement": "villa-brasa", "roles": ["minijuego"], "minigames": ["picado"], "version": "MVP",
         "improvable": False, "evolutivo": False, "mine_zone": "z1", "minerals": ["carbon"], "recipes": [], "factions": ["union"],
         "characters": ["teo"], "npcs": ["capataz"], "tasks": ["F4-1"]},
        {"id": "ed-vb-aduana", "name": "Aduana", "settlement": "villa-brasa", "roles": ["gastar"], "minigames": [], "version": "evolutivo",
         "improvable": False, "evolutivo": True, "minerals": [], "recipes": [], "factions": [], "characters": [], "npcs": [], "tasks": [],},
    ],
}
DOC = """El catálogo tiene 2 filas: las **1 edificaciones** de MVP y la aduana.
| ID | Edificación | Rol | Qué | Versión | Marca |
|---|---|---|---|---|---|
| `ed-vb-mina` | Boca | minijuego (Picado) | Carbón. | MVP | ✅ |
| `ed-vb-aduana` | Aduana | gastar (impuestos) | Impuestos. | evolutivo | ✅ |
"""
TASKS = {"F4-1": "todo"}


def mundo(**cambios):
    w = copy.deepcopy(WORLD)
    for clave, valor in cambios.items():
        w[clave] = valor(w[clave]) if callable(valor) else valor
    return w


def edit(index, **campos):
    def aplicar(lista):
        lista[index].update(campos)
        return lista
    return aplicar


def c33(world, doc=DOC, tasks=TASKS):
    res = coherence.check(world, {"lanes": []}, task_status=tasks, doc26=doc)
    return next(c for c in res["checks"] if c["id"] == "C33")


def texto(hallazgos):
    return " | ".join(hallazgos)


class Integridad(unittest.TestCase):
    def test_registro_bueno(self):
        self.assertEqual(coherence.integrity(WORLD), [])

    def test_id_repetido(self):
        w = mundo(buildings=lambda b: b + [copy.deepcopy(b[0])])
        self.assertTrue(any("buildings: id repetido (ed-vb-mina)" in e for e in coherence.integrity(w)))

    def test_asentamiento_inexistente(self):
        w = mundo(buildings=edit(0, settlement="nada"))
        self.assertTrue(any("asentamiento inexistente: nada" in e for e in coherence.integrity(w)))

    def test_rol_y_version_invalidos(self):
        errores = texto(coherence.integrity(mundo(buildings=edit(0, roles=["vender", "robar"], version="V9"))))
        self.assertIn("rol desconocido (robar)", errores)
        self.assertIn("versión desconocida (V9)", errores)

    def test_enlaces_rotos(self):
        w = mundo(buildings=edit(0, minerals=["oro"], recipes=["x"], factions=["y"], characters=["z"], npcs=["n"], minigames=["m"]))
        errores = texto(coherence.integrity(w))
        for ref in ("mineral inexistente: oro", "receta inexistente: x", "facción inexistente: y", "personaje inexistente: z",
                    "PNJ inexistente: n", "minijuego inexistente: m"):
            self.assertIn(ref, errores)

    def test_zona_sin_asentamiento_o_no_declarada(self):
        errores = texto(coherence.integrity(mundo(zones=lambda z: z + [{"id": "z2", "name": "Z2", "act": "I", "place": "nada"}])))
        self.assertIn("zona z2 sin asentamiento válido (nada)", errores)
        errores = texto(coherence.integrity(mundo(settlements=lambda s: [dict(s[0], zones=[])])))
        self.assertIn("zona z1 no figura entre las zonas de su asentamiento", errores)

    def test_boca_de_zona_ajena_y_prefijo(self):
        self.assertIn("boca de una zona de minado inexistente", texto(coherence.integrity(mundo(buildings=edit(0, mine_zone="zz")))))
        self.assertIn("prefijo del ID", texto(coherence.integrity(mundo(buildings=edit(0, id="ed-af-mina")))))

    def test_evolutivo_coherente_con_la_version(self):
        self.assertIn("«evolutivo» no coincide", texto(coherence.integrity(mundo(buildings=edit(1, evolutivo=False)))))


class ContraElDocumento26(unittest.TestCase):
    def test_coincide(self):
        c = c33(WORLD)
        self.assertEqual((c["failed"], c["findings"]), (0, []))

    def test_id_que_falta_o_sobra(self):
        self.assertIn("ed-vb-aduana está en el documento 26 y falta", texto(c33(mundo(buildings=lambda b: b[:1]))["findings"]))
        extra = DOC + "| `ed-vb-nueva` | Nueva | gastar | X. | V1 | ✅ |\n"
        self.assertIn("ed-vb-nueva está en el documento 26 y falta", texto(c33(WORLD, extra)["findings"]))

    def test_la_prosa_del_documento_no_cuenta(self):
        self.assertEqual(c33(WORLD, DOC.replace("Carbón.", "Otra redacción."))["findings"], [])

    def test_version_rol_y_nombre_distintos(self):
        hallazgos = texto(c33(mundo(buildings=edit(0, version="V1", roles=["vender"], name="Otra")))["findings"])
        self.assertIn("versión distinto", hallazgos)
        self.assertIn("roles distintos", hallazgos)
        self.assertIn("nombre distinto", hallazgos)

    def test_cuenta_incoherente(self):
        malo = DOC.replace("2 filas: las **1 edificaciones**", "46 filas: las **45 edificaciones**")
        self.assertIn("La cuenta del documento 26", texto(c33(WORLD, malo)["findings"]))

    def test_cuenta_45_mas_aduana_sin_documento(self):
        self.assertIn("45 edificaciones más la aduana", texto(c33(WORLD, None)["findings"]))

    def test_zona_sin_boca_o_con_dos(self):
        self.assertIn("z1 debe tener una sola boca", texto(c33(mundo(buildings=edit(0, mine_zone=None)))["findings"]))
        dos = mundo(buildings=lambda b: b + [dict(b[0], id="ed-vb-mina2")])
        self.assertIn("z1 debe tener una sola boca de mina y tiene 2", texto(c33(dos)["findings"]))

    def test_tareas_inexistentes_o_terminadas(self):
        self.assertIn("la tarea F4-1 no existe", texto(c33(WORLD, tasks={})["findings"]))
        self.assertIn("está terminada", texto(c33(WORLD, tasks={"F4-1": "done"})["findings"]))


class RegistroDelProyecto(unittest.TestCase):
    def test_world_json_cuadra_con_el_documento_26(self):
        world = json.loads((ROOT / "studio" / "data" / "world.json").read_text(encoding="utf-8"))
        doc = next((ROOT / "studio" / "docs").glob("26-*.md")).read_text(encoding="utf-8")
        self.assertEqual(len(world["settlements"]), 6)
        self.assertEqual(len(world["buildings"]), 46)
        self.assertEqual(coherence.integrity(world), [])
        self.assertEqual(c33(world, doc, None)["findings"], [])

    def test_tareas_de_las_edificaciones_existen_y_solo_faltan_las_conocidas(self):
        world = json.loads((ROOT / "studio" / "data" / "world.json").read_text(encoding="utf-8"))
        roadmap = json.loads((ROOT / "studio" / "data" / "roadmap.json").read_text(encoding="utf-8"))
        estado = {t["id"]: t["status"] for p in roadmap["phases"] for m in p["milestones"] for t in m["tasks"]}
        self.assertEqual(c33(world, None, estado)["findings"], [])
        # Sin tarea que las construya (el roadmap no la tiene): la aduana (evolutiva) y la oficina de la Comisión.
        self.assertEqual([b["id"] for b in world["buildings"] if not b["tasks"]], ["ed-sb-aduana", "ed-pm-comision"])


if __name__ == "__main__":
    unittest.main()
