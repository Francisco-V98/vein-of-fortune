"""Pruebas de la validación del árbol de decisiones (decisions.json) y de sus cruces de coherencia. Ejecutar:
    python3 -m unittest discover -s tools/ci -v
Los casos usan un árbol de prueba mínimo definido aquí: no tocan los datos reales.
"""
import copy
import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]


def load_module(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


hub = load_module("hub_build_decisiones", "studio/hub/build.py")
coherence = load_module("coherence_decisiones", "studio/hub/coherence.py")

ACTS = ["I", "II", "III", "IV"]
WORLD = {
    "acts": ACTS,
    "characters": [
        {"id": "p", "name": "Protagonista", "act": "I", "aka": []},
        {"id": "r", "name": "Reme", "act": "I", "aka": ["Doña Reme"]},
        {"id": "e", "name": "Esteban", "act": "II", "aka": []},
    ],
}
STORY = {"lanes": [
    {"id": "narrativa", "cells": [[], [], [], ["Oyes las cintas, que fuiste recogiendo desde el Acto I"]]},
    {"id": "arte", "cells": [[], [], [], ["Escenas de las cintas"]]},
]}
# Pequeñas por acto y niveles mayores, en el orden en que aparecen.
LAYOUT = [("I", "pequena")] * 3 + [("II", "pequena")] * 5 + [("III", "pequena")] * 5 + [("IV", "pequena")] * 5 + \
         [("II", "grande"), ("III", "grande"), ("IV", "grande")] + [("II", "mediana")] * 2 + [("III", "mediana")] * 2 + [("IV", "mediana")] * 2


def tree():
    """Árbol válido: cada nodo fija una bandera y el siguiente de su acto o posterior la lee."""
    order = sorted(enumerate(LAYOUT), key=lambda x: (ACTS.index(x[1][0]), x[0]))
    nodes, flags = [], []
    for i, (_, (act, level)) in enumerate(order):
        nid = "n%02d" % i
        last = i == len(order) - 1
        option = lambda k: {"id": "o%d" % k, "texto": "Opción %d" % k, "mundo": "m", "mercado": "—", "personajes": "p", "fija": [] if last else ["f%02d" % i]}
        nodes.append({"id": nid, "acto": act, "nivel": level, "titulo": "Decisión %d" % i, "dispara": "d",
                      "opciones": [option(1), option(2)], "lee": [] if i == 0 else ["f%02d" % (i - 1)], "estado": "prop"})
        if not last:
            flags.append({"id": "f%02d" % i, "tipo": "eleccion", "descripcion": "b", "personajes": ["Protagonista"]})
    necks = [{"id": "c-%s" % a, "acto": a, "titulo": "Cuello %s" % a, "recibe": [n["id"] for n in nodes if n["acto"] == a]} for a in ACTS]
    tapes = [{"n": n, "acto": a, "lugar": "l", "estado": "prop"} for n, a in zip(range(1, 9), "I II III III III IV IV IV".split())]
    return {
        "meta": {"cupos": {"grande": 3, "mediana": 6, "pequena": 18}, "por_acto_pequenas": {"I": 3, "II": 5, "III": 5, "IV": 5}},
        "nodes": nodes, "flags": flags, "cuellos": necks, "cintas": tapes,
        "pruebas_iv": [{"variante": v, "prueba": "p"} for v in ("consorcio", "ministerio", "faroleros")],
    }


def avisos(data, world=WORLD):
    hub.warnings.clear()
    hub.check_decisions(data, world)
    return list(hub.warnings)


def node(data, nid):
    return next(n for n in data["nodes"] if n["id"] == nid)


class Validacion(unittest.TestCase):
    def test_arbol_valido(self):
        self.assertEqual(avisos(tree()), [])

    def test_bandera_que_no_se_fija(self):
        data = tree()
        for o in node(data, "n00")["opciones"]:
            o["fija"] = []
        self.assertTrue(any("f00 no la fija" in w for w in avisos(data)))

    def test_bandera_que_no_se_lee(self):
        data = tree()
        node(data, "n01")["lee"] = []
        self.assertTrue(any("f00 no la lee" in w for w in avisos(data)))

    def test_cupo_roto(self):
        data = tree()
        node(data, "n00")["nivel"] = "mediana"
        found = avisos(data)
        self.assertTrue(any("'pequena'" in w for w in found))
        self.assertTrue(any("'mediana'" in w for w in found))
        self.assertTrue(any("Acto I tiene 2 pequeñas" in w for w in found))

    def test_cuello_con_una_sola_rama(self):
        data = tree()
        data["cuellos"][0]["recibe"] = data["cuellos"][0]["recibe"][:1]
        self.assertTrue(any("recibe 1 rama" in w for w in avisos(data)))

    def test_cuello_con_nodo_inexistente_o_de_otro_acto(self):
        data = tree()
        data["cuellos"][0]["recibe"] += ["no-existe", node(data, "n03")["id"]]
        found = avisos(data)
        self.assertTrue(any("inexistente: no-existe" in w for w in found))
        self.assertTrue(any("es del Acto II" in w for w in found))

    def test_nodo_que_lee_una_bandera_de_un_acto_posterior(self):
        data = tree()
        node(data, "n00")["lee"] = ["f20"]  # n00 es del Acto I y f20 la fija un nodo del IV
        self.assertTrue(any("solo se fija en un acto posterior" in w for w in avisos(data)))

    def test_personaje_inexistente(self):
        data = tree()
        data["flags"][0]["personajes"] = ["Nadie"]
        self.assertTrue(any("Nadie" in w for w in avisos(data)))

    def test_personaje_por_alias(self):
        data = tree()
        data["flags"][0]["personajes"] = ["Doña Reme"]
        self.assertEqual(avisos(data), [])

    def test_ids_repetidos_y_referencias(self):
        data = tree()
        data["nodes"][1]["id"] = "n00"
        node(data, "n02")["opciones"][0]["fija"] = ["f-fantasma"]
        found = avisos(data)
        self.assertTrue(any("nodo repetido" in w for w in found))
        self.assertTrue(any("bandera inexistente: f-fantasma" in w for w in found))

    def test_cintas_y_pruebas(self):
        data = tree()
        data["cintas"][7]["n"] = 7
        data["pruebas_iv"].pop()
        found = avisos(data)
        self.assertTrue(any("cintas deben numerarse" in w for w in found))
        self.assertTrue(any("pruebas_iv" in w for w in found))

    def test_datos_reales(self):
        data = json.loads((ROOT / "studio" / "data" / "decisions.json").read_text(encoding="utf-8"))
        world = json.loads((ROOT / "studio" / "data" / "world.json").read_text(encoding="utf-8"))
        self.assertEqual(avisos(data, world), [])
        self.assertEqual(len(data["nodes"]), 27)


def failed(data, story=STORY, world=WORLD):
    result = coherence.check({**world, "rules": {}, "zones": [], "minigames": [], "minerals": [], "mechanics": [], "recipes": []}, story, data)
    return {c["id"]: c["failed"] for c in result["checks"] if int(c["id"][1:]) >= 12}


class Coherencia(unittest.TestCase):
    def test_arbol_coherente(self):
        self.assertEqual(failed(tree()), {"C12": 0, "C13": 0, "C14": 0, "C15": 0})

    def test_sin_arbol_no_hay_comprobaciones_nuevas(self):
        self.assertEqual(failed(None), {})

    def test_bandera_leida_antes_de_fijarse(self):
        data = tree()
        node(data, "n00")["lee"] = ["f20"]
        self.assertEqual(failed(data)["C12"], 1)

    def test_cuello_con_rama_de_otro_acto(self):
        data = tree()
        data["cuellos"][0]["recibe"].append("n03")
        self.assertEqual(failed(data)["C13"], 1)

    def test_acto_sin_cuello(self):
        data = tree()
        data["cuellos"].pop()
        self.assertEqual(failed(data)["C13"], 1)

    def test_personaje_que_aparece_despues_de_la_bandera(self):
        data = tree()
        data["flags"][0]["personajes"] = ["Esteban"]  # aparece en el II y f00 se fija en el I
        self.assertEqual(failed(data)["C14"], 1)

    def test_cintas_contra_el_mapa_de_historia(self):
        story = copy.deepcopy(STORY)
        story["lanes"][0]["cells"][1] = ["Oyes las cintas"]
        story["lanes"][0]["cells"][3] = ["Oyes las cintas, que fuiste recogiendo desde el Acto II"]
        self.assertEqual(failed(tree(), story)["C15"], 2)

    def test_datos_reales_coherentes(self):
        load = lambda name: json.loads((ROOT / "studio" / "data" / name).read_text(encoding="utf-8"))
        result = coherence.check(load("world.json"), load("story.json"), load("decisions.json"))
        nuevos = {c["id"]: c["failed"] for c in result["checks"] if c["id"] in ("C12", "C13", "C14", "C15")}
        self.assertEqual(nuevos, {"C12": 0, "C13": 0, "C14": 0, "C15": 0})


if __name__ == "__main__":
    unittest.main()
