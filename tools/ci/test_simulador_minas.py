"""Pruebas de las reglas del motor de minas (F0-93, parte 2): C5b, J1 a J6 en tools/sim/reglas_minas.py.

Una prueba por regla (estados e intervalos coherentes) y una mutación por regla (cambiar una cifra de world.json en
memoria o un criterio cambia lo medido). Las reglas que fallan con las cifras de partida quedan registradas: las calibra F0-92.
"""
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from sim import entradas as E  # noqa: E402
from sim import mundo, reglas, reglas_minas as RM, run  # noqa: E402

IDS = ("C5b", "J1", "J2", "J3", "J4", "J5", "J6")
HUELLA = "9dff70c2c639dbb5"


def valores(r):
    return [s["valor"] for s in r["subs"]]


class Compartido:
    world = mundo.cargar_world()
    S = mundo.cargar_supuestos()
    R = run.cargar_reglas()
    ctx = reglas.Ctx(mundo.cargar()[0], S, R, "mini")
    base = {}

    @classmethod
    def basal(cls, rid):
        if rid not in cls.base:
            cls.base[rid] = RM.evalua(cls.ctx, rid)
        return cls.base[rid]


def editar(*cambios):
    w = json.loads(json.dumps(Compartido.world))
    for clave, valor in cambios:
        reglas.aplica_edicion(w, clave, valor)
    return w


# (edición de world.json, criterio) que cambia lo medido por cada regla
MUTACIONES = {
    "C5b": ([("economy.mine_entrances.detector.battery_by_level", [99, 99, 99, 99])], {}),
    "J1": ([("economy.mine_entrances.closures.pressure_mult_by_closed", [1.0, 1.0, 1.0, 1.0])], {}),
    "J2": ([("economy.mine_entrances.quality_mult", {"escasa": 1.0, "media": 1.0, "abundante": 1.0})], {}),
    "J3": ([("economy.mine_entrances.detector.battery_by_level", [99, 99, 99, 99])], {}),
    "J4": ([("economy.mine_entrances.quality_mult", {"escasa": 1.0, "media": 1.0, "abundante": 1.0})], {}),
    "J5": ([], {"minutos": 0}),
    "J6": ([("economy.seasons_weather.season_effects.invierno.energy_delta", -10)], {}),
}


class Datos(unittest.TestCase):
    def test_reglas_v2_declaradas_y_las_50_intactas(self):
        ids = [r["id"] for r in Compartido.R["reglas_v2"]]
        self.assertEqual(sorted(ids), sorted(IDS))
        self.assertEqual(sorted(RM.REGLAS_V2), sorted(IDS))
        self.assertEqual(len(Compartido.R["reglas"]), 50)
        self.assertFalse(set(ids) & set(reglas.REGLAS))
        for r in Compartido.R["reglas_v2"]:
            for k in ("id", "grupo", "titulo", "docs", "metrica", "umbral", "origen", "criterio"):
                self.assertIn(k, r, r["id"])

    def test_la_huella_por_defecto_no_cambia(self):
        self.assertEqual(mundo.huella(Compartido.world), HUELLA)

    def test_calendario(self):
        cal = Compartido.S["minas_v2"]["calendario"]
        self.assertEqual(E.calendario(1, cal), ("otono", 22, 0))
        self.assertEqual(E.calendario(8, cal)[:2], ("invierno", 1))
        n = cal["dias_por_estacion"] * len(cal["orden"])
        self.assertEqual(E.calendario(1 + n, cal), ("otono", 22, 1))

    def test_eventos_sembrados_desde_el_acto_ii(self):
        P, S = E.cargar(), Compartido.S["minas_v2"]
        actos = mundo.cargar()[0]["actos"]
        self.assertEqual({E.severidad_sembrada(1, d, "z", "I", S, P, actos) for d in range(500)}, {0})
        sev = [E.severidad_sembrada(1, d, "z", "II", S, P, actos) for d in range(4000)]
        self.assertEqual(set(sev), {0, 1, 2, 3})
        self.assertAlmostEqual(sev.count(P["sev"]["suave"]) / len(sev), S["eventos_por_dia"]["suave"], delta=0.02)

    def test_mellada(self):
        P = E.cargar()
        self.assertEqual(E.mult_mellada(P["mellada"]["integrity_below_pct"], P), 1.0)
        self.assertLess(E.mult_mellada(0, P), 1.0)


def _caso(rid):
    def prueba(self):
        r = Compartido.basal(rid)
        self.assertIn(r["estado"], ("pasa", "falla", "incierto"))
        self.assertTrue(r["subs"])
        for s in r["subs"]:
            self.assertIn(s["estado"], ("pasa", "falla", "incierto"))
            if s["valor"] is not None and s["ic95"]:
                self.assertLessEqual(s["ic95"][0], s["ic95"][1])
        self.assertEqual(mundo.huella(Compartido.world), HUELLA)
    prueba.__name__ = "test_regla_%s" % rid
    return prueba


def _mutacion(rid):
    def prueba(self):
        ediciones, criterio = MUTACIONES[rid]
        mut = RM.evalua(Compartido.ctx, rid, world=editar(*ediciones) if ediciones else None, criterio=criterio)
        self.assertNotEqual(valores(mut), valores(Compartido.basal(rid)), "la mutación de %s no cambia lo medido" % rid)
    prueba.__name__ = "test_mutacion_%s" % rid
    return prueba


class Reglas(unittest.TestCase):
    pass


for _rid in IDS:
    setattr(Reglas, "test_regla_%s" % _rid, _caso(_rid))
    setattr(Reglas, "test_mutacion_%s" % _rid, _mutacion(_rid))


class Integracion(unittest.TestCase):
    def test_apagado_igual_que_antes_y_encendido_distinto(self):
        P0, _ = mundo.cargar()
        S = Compartido.S
        perfil = RM.C.perfil_de(P0, S, "medio")
        res = []
        for mot in (None, E.MotorMinas(3, E.cargar(), sup=S["minas_v2"], actos=P0["actos"])):
            cfg = RM.C.cfg_etapa(P0, S, "III", motor_minas=mot)
            res.append(RM.C.correr_etapa(P0, S, cfg, perfil, 5, 30)["neto_dia"])
        legado = RM.C.correr_etapa(P0, S, RM.C.cfg_etapa(P0, S, "III"), perfil, 5, 30)["neto_dia"]
        self.assertEqual(res[0], legado)
        self.assertNotEqual(res[1], legado)

    def test_linea_de_ordenes(self):
        self.assertEqual(run.main(["--minas", "--regla", "J4"]), 0)


if __name__ == "__main__":
    unittest.main()
