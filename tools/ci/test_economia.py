"""Pruebas de las comprobaciones económicas (C20 a C32) del registro del mundo. Ejecutar:
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


def mineral(mid, name, tier, price, volatility, vol_num, cap, sectors, zones):
    return {"id": mid, "name": name, "tier": tier, "base_price": price, "volatility": volatility, "volatility_num": vol_num,
            "daily_cap": cap, "liquidity": 5, "sectors": sectors, "minigames": ["g1"], "zones": {z: "principal" for z in zones}}


WORLD = {
    "acts": ["I"],
    "zones": [
        {"id": "z1", "name": "Zona 1", "act": "I", "zone_mix": {"carbon": 70, "hierro": 30}},
        {"id": "z2", "name": "Zona 2", "act": "I", "zone_mix": {"hierro": 50, "aetherita": 50}},
    ],
    "minigames": [{"id": "g1", "name": "G1", "act": "I"}],
    "minerals": [
        mineral("carbon", "Carbón", 1, 50, "baja", 1.8, 5, {"ferrocarril": 60, "energia": 40}, ["z1"]),
        mineral("hierro", "Hierro", 2, 100, "media", 3.0, 8, {"militar": 50, "agricultura": 50}, ["z1", "z2"]),
        mineral("aetherita", "Aetherita", 5, 6000, "muy alta", 5.7, 15, {"lujo": 80, "tecnologia": 20}, ["z2"]),
    ],
    "economy": {
        "tools": {
            "upgrade_cost": {"pico": {"2": 200, "3": 1100, "4": 13000}},
            "upgrade_minerals": {"pico": {"2": {"mineral": "carbon", "qty": 3}, "3": {"mineral": "hierro", "qty": 6},
                                          "4": {"mineral": "hierro", "qty": 8}}},
            "detector": {"levels": [{"level": 1, "cost": 0}, {"level": 2, "cost": 300}, {"level": 3, "cost": 900}]},
        },
        "surveillance": {"levels": [{"id": "a", "min": 0, "max": 29}, {"id": "b", "min": 30, "max": 59},
                                    {"id": "c", "min": 60, "max": 84}, {"id": "d", "min": 85, "max": 100}]},
        "employees": {
            "levels": [{"level": 1, "salary_per_day": 70}, {"level": 2, "salary_per_day": 90}],
            "support_salary_per_day": {"dependiente": {"II": 160, "III": 620, "IV": 2800}},
            "contract_salary_mult": {"7": 1.3, "14": 1.12, "30": 1.0},
            "dismissal_phi": {"7": 0.25, "14": 0.4, "30": 0.6},
        },
    },
}
TASKS = {"F0-52": "doing", "F0-53": "backlog", "F0-10": "done"}


def run(world, tasks=TASKS):
    result = coherence.check(world, {"lanes": []}, task_status=tasks)
    return {c["id"]: c for c in result["checks"] if int(c["id"][1:]) >= 20}


def failing(world, tasks=TASKS):
    return {cid: c["failed"] for cid, c in run(world, tasks).items() if c["failed"]}


class Preparacion(unittest.TestCase):
    def test_registro_correcto_sin_hallazgos(self):
        checks = run(WORLD)
        self.assertEqual(sorted(checks, key=lambda c: int(c[1:])), ["C%d" % n for n in range(20, 33)])
        self.assertEqual(failing(WORLD), {})

    def test_sin_campos_economicos_no_se_comprueba(self):
        w = {"acts": ["I"], "zones": [], "minerals": [{"id": "m", "name": "M", "base_price": 5, "sectors": ["s"], "minigames": [], "zones": {}}]}
        self.assertEqual(run(w), {})


class Minerales(unittest.TestCase):
    def setUp(self):
        self.w = copy.deepcopy(WORLD)

    def mut(self, mid, **kw):
        next(m for m in self.w["minerals"] if m["id"] == mid).update(kw)
        return failing(self.w)

    def test_precio_no_entero_o_cero(self):
        self.assertEqual(self.mut("hierro", base_price=0)["C20"], 1)
        self.assertEqual(self.mut("hierro", base_price=99.5)["C20"], 1)

    def test_todos_los_precios_iguales(self):
        for m in self.w["minerals"]:
            m["base_price"] = 100
        self.assertEqual(failing(self.w)["C20"], 1)

    def test_precio_no_sube_con_el_nivel(self):
        self.assertIn("C21", self.mut("hierro", base_price=40))

    def test_aetherita_no_es_la_mas_cara(self):
        self.assertIn("C21", self.mut("aetherita", base_price=90))

    def test_carbon_no_es_el_mas_barato(self):
        self.assertIn("C21", self.mut("carbon", base_price=500))

    def test_nivel_fuera_de_rango(self):
        self.assertEqual(self.mut("hierro", tier=6)["C22"], 1)
        self.assertEqual(self.mut("hierro", tier=0)["C22"], 1)
        self.assertEqual(self.mut("hierro", tier=None)["C22"], 1)

    def test_sectores(self):
        self.assertEqual(self.mut("carbon", sectors={"ferrocarril": 100})["C23"], 1)  # solo uno
        self.assertEqual(self.mut("carbon", sectors={"ferrocarril": 60, "energia": 30})["C23"], 1)  # suma 90
        self.assertEqual(self.mut("carbon", sectors={"ferrocarril": 60, "magia": 40})["C23"], 1)  # desconocido
        self.assertEqual(self.mut("carbon", sectors={"ferrocarril": 60.5, "energia": 39.5})["C23"], 1)  # no entero

    def test_sector_sin_minerales(self):
        self.assertEqual(self.mut("hierro", sectors={"militar": 50, "lujo": 50})["C24"], 1)  # agricultura queda sin mineral

    def test_tope_diario_contra_etiqueta(self):
        self.assertIn("C25", self.mut("hierro", daily_cap=4))  # media por debajo de baja
        self.assertIn("C25", self.mut("hierro", volatility="desconocida"))
        self.assertIn("C25", self.mut("carbon", volatility_num=4.0))

    def test_aetherita_con_el_mayor_tope(self):
        self.assertIn("C25", self.mut("aetherita", daily_cap=8))

    def test_liquidez(self):
        self.assertEqual(self.mut("hierro", liquidity=0)["C26"], 1)
        self.assertEqual(self.mut("hierro", liquidity=-3)["C26"], 1)


class Herramientas(unittest.TestCase):
    def setUp(self):
        self.w = copy.deepcopy(WORLD)
        self.tools = self.w["economy"]["tools"]

    def test_mineral_de_mejora_demasiado_alto(self):
        self.tools["upgrade_minerals"]["pico"]["3"]["mineral"] = "aetherita"
        self.assertEqual(failing(self.w)["C27"], 1)

    def test_mineral_de_mejora_justo_en_el_limite(self):
        self.tools["upgrade_minerals"]["pico"]["3"]["mineral"] = "hierro"  # nivel 2 = 3 − 1
        self.assertNotIn("C27", failing(self.w))

    def test_mineral_de_mejora_inexistente_o_cantidad_invalida(self):
        self.tools["upgrade_minerals"]["pico"]["2"]["mineral"] = "mithril"
        self.tools["upgrade_minerals"]["pico"]["3"]["qty"] = 0
        self.assertEqual(failing(self.w)["C27"], 2)

    def test_costos_no_crecientes(self):
        self.tools["upgrade_cost"]["pico"]["4"] = 1100
        self.assertEqual(failing(self.w)["C28"], 1)

    def test_costos_del_detector_no_crecientes(self):
        self.tools["detector"]["levels"][2]["cost"] = 300
        self.assertEqual(failing(self.w)["C28"], 1)

    def test_costo_cero(self):
        self.tools["upgrade_cost"]["pico"]["2"] = 0
        self.assertEqual(failing(self.w)["C28"], 1)


class VigilanciaYZonas(unittest.TestCase):
    def setUp(self):
        self.w = copy.deepcopy(WORLD)

    def test_solape_hueco_y_final(self):
        levels = self.w["economy"]["surveillance"]["levels"]
        levels[1]["min"] = 29  # solape
        self.assertEqual(failing(self.w)["C29"], 1)
        levels[1]["min"] = 31  # hueco
        self.assertEqual(failing(self.w)["C29"], 1)
        levels[1]["min"] = 30
        levels[3]["max"] = 99
        self.assertEqual(failing(self.w)["C29"], 1)

    def test_mezcla_que_no_suma_100(self):
        self.w["zones"][0]["zone_mix"] = {"carbon": 70, "hierro": 20}
        self.assertEqual(failing(self.w)["C30"], 1)

    def test_mezcla_con_mineral_de_otra_zona(self):
        self.w["zones"][0]["zone_mix"] = {"carbon": 60, "hierro": 30, "aetherita": 10}
        self.assertEqual(failing(self.w)["C30"], 1)

    def test_mezcla_que_olvida_un_mineral_de_la_zona(self):
        self.w["zones"][0]["zone_mix"] = {"carbon": 100}
        self.assertEqual(failing(self.w)["C30"], 1)


class Salarios(unittest.TestCase):
    def setUp(self):
        self.w = copy.deepcopy(WORLD)
        self.emp = self.w["economy"]["employees"]

    def test_salario_no_positivo(self):
        self.emp["levels"][0]["salary_per_day"] = 0
        self.assertEqual(failing(self.w)["C31"], 1)

    def test_salario_que_no_crece(self):
        self.emp["levels"][1]["salary_per_day"] = 60
        self.assertEqual(failing(self.w)["C31"], 1)

    def test_salario_de_apoyo_que_baja(self):
        self.emp["support_salary_per_day"]["dependiente"]["III"] = 100
        self.assertEqual(failing(self.w)["C31"], 1)

    def test_contrato_corto_mas_barato_o_phi_invalida(self):
        self.emp["contract_salary_mult"]["7"] = 0.9
        self.emp["dismissal_phi"]["30"] = 1.5
        self.assertEqual(failing(self.w)["C31"], 2)


class MarcasDeEspera(unittest.TestCase):
    def test_espera_de_tarea_pendiente(self):
        w = copy.deepcopy(WORLD)
        w["economy"]["currency"] = {"nota": "símbolo sin decidir ⏳ F0-53"}
        self.assertEqual(failing(w), {})
        self.assertEqual(run(w)["C32"]["total"], 1)

    def test_espera_de_tarea_terminada_o_inexistente(self):
        w = copy.deepcopy(WORLD)
        w["economy"]["currency"] = {"a": "⏳ F0-10", "b": "⏳ F9-99"}
        self.assertEqual(failing(w)["C32"], 2)

    def test_sin_estado_de_tareas_no_se_comprueba(self):
        w = copy.deepcopy(WORLD)
        w["economy"]["currency"] = {"a": "⏳ F0-10"}
        self.assertNotIn("C32", run(w, tasks=None))


class DatosReales(unittest.TestCase):
    def test_el_registro_del_proyecto_no_da_falsos_positivos(self):
        world = json.loads((ROOT / "studio" / "data" / "world.json").read_text(encoding="utf-8"))
        roadmap = json.loads((ROOT / "studio" / "data" / "roadmap.json").read_text(encoding="utf-8"))
        status = {t["id"]: t["status"] for p in roadmap["phases"] for m in p["milestones"] for t in m["tasks"]}
        found = {cid: c["findings"] for cid, c in run(world, status).items() if c["failed"]}
        self.assertEqual(found, {})
        self.assertEqual(len(run(world, status)), 13)


if __name__ == "__main__":
    unittest.main()
