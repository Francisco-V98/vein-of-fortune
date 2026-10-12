"""Pruebas de las comprobaciones de coherencia del registro del mundo. Ejecutar:
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

WORLD = {
    "rules": {"mineral_zones_min": 2, "mineral_zones_max": 3, "fuente": "prueba"},
    "acts": ["I", "II"],
    "zones": [{"id": "z1", "name": "Zona 1", "act": "I"}, {"id": "z2", "name": "Zona 2", "act": "II"}],
    "minigames": [{"id": "g1", "name": "G1", "act": "I"}],
    "minerals": [{"id": "m1", "name": "M1", "base_price": 5, "sectors": ["s"], "minigames": ["g1"], "zones": {"z1": "principal", "z2": "principal"}}],
    "mechanics": [],
    "recipes": [],
    "factions": [{"id": "f1", "name": "F1"}],
    "characters": [{"id": "c1", "name": "C1", "act": "I", "faction": "f1", "aka": []}],
}
STORY = {"lanes": []}


def failed(world, story=STORY):
    return {c["id"]: c["failed"] for c in coherence.check(world, story)["checks"]}


class Integridad(unittest.TestCase):
    def test_registro_valido(self):
        self.assertEqual(coherence.integrity(WORLD), [])

    def test_referencias_inexistentes(self):
        w = copy.deepcopy(WORLD)
        w["minerals"][0]["zones"]["zz"] = "principal"
        w["minerals"][0]["minigames"].append("gg")
        w["recipes"] = [{"id": "r", "name": "R", "inputs": [["no"]]}]
        w["characters"][0]["faction"] = "no"
        self.assertEqual(len(coherence.integrity(w)), 4)

    def test_npc_con_faccion_inexistente_o_sin_grupo(self):
        w = copy.deepcopy(WORLD)
        w["npcs"] = [{"id": "n1", "name": "N1", "group": "G", "faction": "no"}, {"id": "n2", "name": "N2", "faction": None}]
        self.assertEqual(len(coherence.integrity(w)), 2)

    def test_id_repetido(self):
        w = copy.deepcopy(WORLD)
        w["zones"].append(dict(w["zones"][0]))
        self.assertTrue(any("repetido" in e for e in coherence.integrity(w)))


class Coherencia(unittest.TestCase):
    def test_todo_en_orden(self):
        self.assertTrue(all(v == 0 for v in failed(WORLD).values()))
        self.assertEqual(coherence.check(WORLD, STORY)["pct"], 100)

    def test_mineral_en_una_zona_incumple_la_regla(self):
        w = copy.deepcopy(WORLD)
        w["minerals"][0]["zones"] = {"z1": "principal"}
        self.assertEqual(failed(w)["C2"], 1)

    def test_zona_sin_mineral_principal(self):
        w = copy.deepcopy(WORLD)
        w["minerals"][0]["zones"] = {"z1": "secundario", "z2": "secundario"}
        f = failed(w)
        self.assertEqual(f["C1"], 1)
        self.assertEqual(f["C3"], 2)

    def test_minijuego_llega_tarde(self):
        w = copy.deepcopy(WORLD)
        w["minigames"][0]["act"] = "II"
        self.assertEqual(failed(w)["C4"], 1)

    def test_numeros_base_sin_definir(self):
        w = copy.deepcopy(WORLD)
        w["minerals"][0]["base_price"] = None
        w["minerals"][0]["sectors"] = []
        f = failed(w)
        self.assertEqual((f["C5"], f["C6"]), (1, 1))

    def test_mecanica_necesita_mineral_que_llega_despues(self):
        w = copy.deepcopy(WORLD)
        w["minerals"][0]["zones"] = {"z2": "principal"}
        w["mechanics"] = [{"id": "x", "name": "X", "act": "I", "needs_minerals": ["m1"]}]
        self.assertEqual(failed(w)["C7"], 1)

    def test_mapa_de_historia_contradice_al_registro(self):
        story = {"lanes": [
            {"id": "minerales", "cells": [[], ["M1"]]},
            {"id": "zonas", "cells": [["Zona 2"], []]},
            {"id": "personajes", "cells": [[], ["C1"]]},
        ]}
        f = failed(WORLD, story)
        self.assertEqual((f["C9"], f["C10"], f["C11"]), (1, 1, 1))


class DatosReales(unittest.TestCase):
    def test_el_registro_del_proyecto_es_integro(self):
        world = json.loads((ROOT / "studio" / "data" / "world.json").read_text(encoding="utf-8"))
        self.assertEqual(coherence.integrity(world), [])


if __name__ == "__main__":
    unittest.main()
