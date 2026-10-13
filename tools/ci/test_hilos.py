"""Pruebas del registro de hilos narrativos (hilos.json): su validación en el build y las comprobaciones C16 a C19. Ejecutar:
    python3 -m unittest discover -s tools/ci -v
Los casos usan un registro de prueba mínimo definido aquí: no tocan los datos reales.
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


hub = load_module("hub_build_hilos", "studio/hub/build.py")
coherence = load_module("coherence_hilos", "studio/hub/coherence.py")

WORLD = {
    "acts": ["I", "II", "III", "IV"],
    "characters": [
        {"id": "r", "name": "Reme", "act": "I", "aka": ["Doña Reme"]},
        {"id": "t", "name": "Teo", "act": "I", "aka": []},
    ],
}
# Reme sale en los cuatro actos; Teo solo en el I y el IV.
STORY = {"lanes": [{"id": "personajes", "cells": [["Doña Reme", "Teo"], ["Reme"], ["Reme"], ["Reme", "Teo"]]}]}
DECISIONS = {
    "nodes": [{"id": "n-i-herencia", "acto": "I", "opciones": []}, {"id": "n-iv-aetherita", "acto": "IV", "opciones": []}],
    "cintas": [{"n": n, "acto": "I"} for n in range(1, 9)],
}


def hilo(**cambios):
    h = {
        "id": "h-certificado", "titulo": "El certificado sin cremación", "tipo": "pista", "personajes": ["Reme"],
        "siembra": [{"acto": "I", "donde": "El cajón del puesto", "ref": "doc 19 §3 · n-i-herencia · cinta 3", "estado": "prop"}],
        "resuelve": [{"acto": "IV", "donde": "La Fosa", "ref": "n-iv-aetherita", "estado": "ok"}],
        "cambia": "El mercado se entera", "estado": "resuelto",
    }
    h.update(cambios)
    return h


def registro(*hilos):
    return {"meta": {"actos": ["I", "II", "III", "IV", "despues"], "tipos": ["pista", "promesa", "secreto", "conflicto"],
                     "estados": ["resuelto", "abierto", "aplazado"]}, "hilos": list(hilos) or [hilo()]}


def avisos(data, world=WORLD, decisions=DECISIONS):
    hub.warnings.clear()
    hub.check_hilos(data, world, decisions)
    return list(hub.warnings)


def hay(found, texto):
    return any(texto in w for w in found)


class Validacion(unittest.TestCase):
    def test_registro_valido(self):
        self.assertEqual(avisos(registro()), [])

    def test_hilo_abierto_con_motivo_es_valido(self):
        abierto = hilo(id="h-segunda-parte", resuelve=[], estado="abierto", motivo="Abierto por diseño para una segunda parte")
        self.assertEqual(avisos(registro(hilo(), abierto)), [])

    def test_id_repetido_o_mal_formado(self):
        found = avisos(registro(hilo(), hilo(), hilo(id="Hilo_Raro")))
        self.assertTrue(hay(found, "hilo repetido: h-certificado"))
        self.assertTrue(hay(found, "Hilo_Raro debe empezar por 'h-'"))

    def test_tipo_estado_y_acto_invalidos(self):
        h = hilo(tipo="rumor", estado="perdido")
        h["siembra"][0]["acto"] = "V"
        found = avisos(registro(h))
        self.assertTrue(hay(found, "tipo inválido: rumor"))
        self.assertTrue(hay(found, "estado inválido: perdido"))
        self.assertTrue(hay(found, "acto desconocido en 'siembra': V"))

    def test_siembra_vacia(self):
        self.assertTrue(hay(avisos(registro(hilo(siembra=[]))), "no tiene ninguna siembra"))

    def test_resuelto_sin_resolucion(self):
        self.assertTrue(hay(avisos(registro(hilo(resuelve=[]))), "marcado como resuelto y no tiene resolución"))

    def test_abierto_o_aplazado_sin_motivo(self):
        for estado in ("abierto", "aplazado"):
            self.assertTrue(hay(avisos(registro(hilo(resuelve=[], estado=estado))), "no dice el motivo"))

    def test_resuelve_sin_sembrar(self):
        self.assertTrue(hay(avisos(registro(hilo(siembra=[]))), "se resuelve y no se siembra"))

    def test_resuelve_antes_de_sembrar(self):
        h = hilo()
        h["siembra"][0]["acto"] = "III"
        h["resuelve"][0]["acto"] = "II"
        self.assertTrue(hay(avisos(registro(h)), "se resuelve en el Acto II, antes de sembrarse en el Acto III"))

    def test_personaje_inexistente_y_alias(self):
        self.assertTrue(hay(avisos(registro(hilo(personajes=["Nadie"]))), "Nadie"))
        self.assertEqual(avisos(registro(hilo(personajes=["Doña Reme"]))), [])

    def test_referencias_a_nodos_y_cintas(self):
        h = hilo()
        h["siembra"][0]["ref"] = "n-i-fantasma · cinta 9"
        found = avisos(registro(h))
        self.assertTrue(hay(found, "nodo inexistente en decisions.json: n-i-fantasma"))
        self.assertTrue(hay(found, "cinta inexistente: 9"))

    def test_estado_de_entrada_invalido(self):
        h = hilo()
        h["resuelve"][0]["estado"] = "quizas"
        self.assertTrue(hay(avisos(registro(h)), "estado inválido en 'resuelve': quizas"))

    def test_sin_archivo_es_vacio(self):
        anterior = hub.DATA
        try:
            hub.DATA = ROOT / "no-existe"
            hub.warnings.clear()
            data = hub.load_hilos(WORLD, DECISIONS, STORY)
        finally:
            hub.DATA = anterior
        self.assertEqual(data["hilos"], [])
        self.assertEqual(data["resumen"]["total"], 0)
        self.assertEqual(hub.warnings, [])

    def test_resumen(self):
        antes = hilo(id="h-antes", resuelve=[{"acto": "I", "donde": "x", "estado": "ok"}], siembra=[{"acto": "II", "donde": "y", "estado": "ok"}])
        sin_motivo = hilo(id="h-suelto", resuelve=[], estado="abierto")
        r = coherence.hilos_analisis(registro(hilo(), antes, sin_motivo), WORLD, STORY, DECISIONS)
        self.assertEqual(r["total"], 3)
        self.assertEqual(r["por_estado"], {"resuelto": 2, "abierto": 1})
        self.assertEqual(len(r["sin_resolver"]), 1)
        self.assertEqual(len(r["antes"]), 1)

    def test_datos_reales(self):
        path = ROOT / "studio" / "data" / "hilos.json"
        if not path.exists():
            self.skipTest("todavía no existe studio/data/hilos.json")
        load = lambda name: json.loads((ROOT / "studio" / "data" / name).read_text(encoding="utf-8"))
        self.assertEqual(avisos(load("hilos.json"), load("world.json"), load("decisions.json")), [])


def failed(hilos, story=STORY, world=WORLD, decisions=DECISIONS):
    result = coherence.check({**world, "rules": {}, "zones": [], "minigames": [], "minerals": [], "mechanics": [], "recipes": []},
                             story, decisions, hilos)
    return {c["id"]: c["failed"] for c in result["checks"] if int(c["id"][1:]) >= 16}


class Coherencia(unittest.TestCase):
    def test_registro_coherente(self):
        self.assertEqual(failed(registro()), {"C16": 0, "C17": 0, "C18": 0, "C19": 0})

    def test_sin_hilos_no_hay_comprobaciones_nuevas(self):
        self.assertEqual(failed(None), {})
        self.assertEqual(failed({"hilos": []}), {})

    def test_sembrado_sin_resolver(self):
        self.assertEqual(failed(registro(hilo(resuelve=[])))["C16"], 1)
        self.assertEqual(failed(registro(hilo(resuelve=[], estado="aplazado")))["C16"], 1)
        self.assertEqual(failed(registro(hilo(resuelve=[], estado="aplazado", motivo="⏳ F0-60")))["C16"], 0)

    def test_resuelto_sin_sembrar_y_antes_de_sembrar(self):
        self.assertEqual(failed(registro(hilo(siembra=[])))["C17"], 1)
        h = hilo()
        h["siembra"][0]["acto"] = "III"
        h["resuelve"][0]["acto"] = "II"
        self.assertEqual(failed(registro(h))["C17"], 1)

    def test_personaje_que_desaparece(self):
        # Teo sale en el I y el IV, pero no en el II ni el III.
        found = failed(registro(hilo(personajes=["Teo"])))
        self.assertEqual(found["C18"], 1)
        r = coherence.hilos_analisis(registro(hilo(personajes=["Teo"])), WORLD, STORY, DECISIONS)
        self.assertEqual(r["faltan"][0]["actos"], ["II", "III"])

    def test_personaje_que_debuta_despues_de_la_siembra_no_desaparece_antes(self):
        # Teo no está en el II ni el III. Si el hilo se siembra en el II y se resuelve en el IV, Teo debuta en el IV: no se le echa de menos antes.
        h = hilo(personajes=["Teo"])
        h["siembra"][0]["acto"] = "II"
        r = coherence.hilos_analisis(registro(h), WORLD, STORY, DECISIONS)
        self.assertEqual(r["faltan"], [])

    def test_personaje_que_nunca_sale_en_el_tramo_falta_todo_el_tramo(self):
        world = copy.deepcopy(WORLD)
        world["characters"].append({"id": "q", "name": "Quiroga", "act": "I", "aka": []})
        r = coherence.hilos_analisis(registro(hilo(personajes=["Quiroga"])), world, STORY, DECISIONS)
        self.assertEqual(r["faltan"][0]["actos"], ["I", "II", "III", "IV"])

    def test_fila_en_escena_manda_sobre_la_de_entradas(self):
        # Con la fila «En escena», Teo está presente en los cuatro actos y no desaparece.
        story = {"lanes": STORY["lanes"] + [{"id": "enescena", "cells": [["Teo"]] * 4}]}
        r = coherence.hilos_analisis(registro(hilo(personajes=["Teo"])), WORLD, story, DECISIONS)
        self.assertEqual(r["faltan"], [])

    def test_personaje_por_alias_no_desaparece(self):
        self.assertEqual(failed(registro(hilo(personajes=["Doña Reme"])))["C18"], 0)

    def test_hilo_dentro_de_un_solo_acto_no_comprueba_personajes(self):
        h = hilo(personajes=["Teo"])
        h["resuelve"][0]["acto"] = "I"
        self.assertEqual(failed(registro(h))["C18"], 0)

    def test_resolucion_despues_no_mira_el_mapa(self):
        h = hilo(personajes=["Reme"])
        h["resuelve"][0]["acto"] = "despues"
        self.assertEqual(failed(registro(h))["C18"], 0)

    def test_referencias_inexistentes(self):
        h = hilo()
        h["siembra"][0]["ref"] = "n-ii-fantasma · cintas 3 y 12"
        self.assertEqual(failed(registro(h))["C19"], 2)

    def test_datos_reales_coherentes(self):
        path = ROOT / "studio" / "data" / "hilos.json"
        load = lambda name: json.loads((ROOT / "studio" / "data" / name).read_text(encoding="utf-8"))
        hilos = load("hilos.json") if path.exists() else None
        result = coherence.check(load("world.json"), load("story.json"), load("decisions.json"), hilos)
        nuevos = {c["id"]: c["failed"] for c in result["checks"] if c["id"] in ("C16", "C17", "C19")}
        self.assertTrue(all(v == 0 for v in nuevos.values()), nuevos)


if __name__ == "__main__":
    unittest.main()
