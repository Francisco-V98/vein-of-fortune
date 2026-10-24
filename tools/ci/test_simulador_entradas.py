"""Pruebas del motor de minas de cinco entradas (F0-93, parte 1): tools/sim/entradas.py."""
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from sim import campana as C  # noqa: E402
from sim import entradas as E  # noqa: E402
from sim import mundo  # noqa: E402

P = E.cargar()
HUELLA = "ee83d86daa1121d5"


class Sorteo(unittest.TestCase):
    def test_reparto_y_determinismo(self):
        a = E.sortear_entradas(1, 10, "z", P)
        self.assertEqual(sorted(a), ["abundante", "escasa", "escasa", "media", "media"])
        self.assertEqual(a, E.sortear_entradas(1, 10, "z", P))
        distintas = {tuple(E.sortear_entradas(1, d, "z", P)) for d in range(8, 40)}
        self.assertGreater(len(distintas), 1)

    def test_calidad_media_uno_y_abanico_del_acto_1(self):
        # la media de las cinco entradas es 1,0; el recorte de rendimiento (base_yield_mult) la multiplica en todos los actos
        for acto, k, recorte in (("II", "calidad", P["rend_base"]), ("I", "calidad_a1", P["rend_base"])):
            ent = E.sortear_entradas(3, 9, "z", P)
            media = sum(E.mult_calidad(c, acto, P) for c in ent) / len(ent)
            self.assertAlmostEqual(media, recorte * sum(P[k][c] * P["reparto"][c] for c in P["reparto"]) / P["n"])
            self.assertAlmostEqual(media, recorte, places=1)


class Cierres(unittest.TestCase):
    def test_orden_minimo_y_acto_1(self):
        ent = ["escasa", "media", "abundante", "media", "escasa"]
        self.assertEqual(E.cerrar(ent, 1, "II", P), [2])
        self.assertEqual([ent[i] for i in E.cerrar(ent, 2, "II", P)], ["abundante", "media"])
        for sev in range(0, 10):
            self.assertGreaterEqual(len(ent) - len(E.cerrar(ent, sev, "III", P)), P["min_abiertas"])
        self.assertEqual(E.cerrar(ent, 3, "I", P), [])

    def test_presion(self):
        self.assertEqual([E.mult_presion(n, P) for n in range(4)], P["presion"])
        self.assertEqual(E.mult_presion(99, P), P["presion"][-1])


class BateriaYCambio(unittest.TestCase):
    def test_bateria_por_nivel_y_nieve(self):
        self.assertEqual([E.carga_maxima(n, False, P) for n in (1, 2, 3, 4)], P["bateria"])
        self.assertEqual(E.carga_maxima(1, True, P), P["bateria"][0] + P["clima"]["nieve"]["detector_charge_delta"])

    def test_una_carga_por_clic_y_recarga(self):
        b = E.Bateria(E.carga_maxima(1, False, P), P["costo_escaneo"])
        n = 0
        while b.escanear():
            n += 1
        self.assertEqual(n, P["bateria"][0])
        b.recargar()
        self.assertEqual(b.cargas, P["bateria"][0])

    def test_cambio_una_vez_al_dia_y_empleados(self):
        ent = ["escasa", "media", "abundante", "media", "escasa"]
        m = E.Mina(ent, [2], P)
        self.assertTrue(m.cambiar(1))
        self.assertFalse(m.cambiar(3))
        self.assertFalse(E.Mina(ent, [2], P).cambiar(2))
        ab = m.abiertas()
        esperado = sum(E.mult_calidad(ent[i], "II", P) for i in ab) / len(ab) * E.mult_presion(1, P)
        self.assertAlmostEqual(m.mult_empleados("II"), esperado)


class ClimaYEstaciones(unittest.TestCase):
    def test_sin_clima_dias_1_a_7_y_tope_de_nieve(self):
        c = E.Clima(1, {"nieve": 1.0}, P, 2)
        lo, hi = P["sin_clima"]
        self.assertTrue(all(c.del_dia(d, "z", "invierno") == "despejado" for d in range(lo, hi + 1)))
        dias = [c.del_dia(d, "z", "invierno") for d in range(hi + 1, hi + 40)]
        self.assertEqual(dias.count("nieve"), P["clima"]["nieve"]["max_days_per_winter_per_zone"])
        self.assertEqual(E.Clima(1, {"nieve": 1.0}, P, 2).del_dia(20, "z", "verano"), "despejado")

    def test_el_acto_1_no_recibe_efectos_de_estacion(self):
        m = E.MotorMinas(1, P)
        m.nuevo_dia(3, "I", ["z"], estacion="otono")
        self.assertEqual(m.efectos(), {})
        lo, hi = P["sin_estacion"]
        m.nuevo_dia(hi + 1, "II", ["z"], estacion="otono")
        self.assertEqual(m.efectos(), E.efectos_estacion("otono", P))

    def test_lluvia_cierra_una_y_efectos(self):
        self.assertEqual(E.cierres_por_clima("lluvia", P), P["clima"]["lluvia"]["heavy_rain_closes_entrances"])
        self.assertEqual(E.cierres_por_clima("niebla", P), 0)
        base = E.menas_visibles("II", None, "despejado", P)
        self.assertEqual(E.menas_visibles("II", "otono", "despejado", P), base + P["estaciones"]["otono"]["visible_ores_delta"])
        self.assertEqual(E.menas_visibles("II", None, "niebla", P), base + P["clima"]["niebla"]["visible_ores_delta"])
        self.assertEqual(E.efectos_estacion("invierno", P)["energy_delta"], P["estaciones"]["invierno"]["energy_delta"])


class Interruptor(unittest.TestCase):
    def test_huella_intacta_y_motor_apagado_por_defecto(self):
        self.assertEqual(mundo.huella(mundo.cargar_world()), HUELLA)
        P0, _ = mundo.cargar()
        self.assertNotIn("entradas", P0)

    def test_motor_encendido_aplica_el_factor(self):
        P0, _ = mundo.cargar()
        S = mundo.cargar_supuestos()
        pid = next(iter(S["perfiles"]))
        perfil = C.perfil_de(P0, S, pid)
        eid = next(iter(S["prototipo"]["etapas"]))
        res = []
        for mot in (None, E.MotorMinas(7, P, severidad=lambda d, z: 3)):
            cfg = C.cfg_etapa(P0, S, eid, motor_minas=mot)
            res.append(C.correr_etapa(P0, S, cfg, perfil, 11, 20)["neto_dia"])
        base = C.correr_etapa(P0, S, C.cfg_etapa(P0, S, eid), perfil, 11, 20)["neto_dia"]
        self.assertEqual(res[0], base)       # apagado = igual que antes
        self.assertNotEqual(res[1], base)    # encendido cambia el rendimiento
        m = E.MotorMinas(7, P)
        m.nuevo_dia(10, "II", P0["zonas"])
        self.assertAlmostEqual(m.horas_caminando(2), 0.0)


if __name__ == "__main__":
    unittest.main()
