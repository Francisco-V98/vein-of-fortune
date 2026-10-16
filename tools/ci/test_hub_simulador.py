"""Pruebas de la parte del hub del simulador de economía (F0-53): validación y huella en build.py
y vista #/simulador de app.js (con un arnés de Node, sin navegador). Ejecutar:
    python3 -m unittest discover -s tools/ci -v
"""
import copy
import importlib.util
import json
import pathlib
import shutil
import subprocess
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
FIXTURES = pathlib.Path(__file__).resolve().parent / "fixtures"
spec = importlib.util.spec_from_file_location("hub_build", ROOT / "studio" / "hub" / "build.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)

HUELLA = "abc123def4567890"


def fixture(name):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def problems(res=None, reglas=None, huella=HUELLA):
    res = fixture("sim_resultados.json") if res is None else res
    reglas = fixture("sim_reglas.json") if reglas is None else reglas
    return build.sim_problems(res, reglas, huella)


def estados(msgs):
    return [m for m in msgs if m.startswith("simulador:")]


class Validacion(unittest.TestCase):
    def test_fixture_valido_solo_avisa_de_falla_e_incierto(self):
        msgs = problems()
        self.assertEqual(len(msgs), 2, msgs)
        self.assertIn("A5", msgs[0])
        self.assertIn("falla", msgs[0])
        self.assertIn("B5", msgs[1])
        self.assertIn("incierto", msgs[1])

    def test_todo_pasa_sin_avisos(self):
        res = fixture("sim_resultados.json")
        for r in res["reglas"]:
            r["estado"] = "pasa"
            for cell in r["por_perfil"].values():
                cell.pop("estado", None)
        self.assertEqual(problems(res), [])

    def test_resultado_caducado(self):
        msgs = problems(huella="otra-huella-distinta")
        self.assertTrue(any("caducado" in m for m in msgs), msgs)

    def test_sin_huella_calculable_solo_valida_la_forma(self):
        msgs = problems(huella=None)
        self.assertFalse(any("caducado" in m for m in msgs), msgs)

    def test_mutaciones_del_esquema(self):
        def mutar(fn, texto, solo_reglas=False):
            res, reglas = fixture("sim_resultados.json"), fixture("sim_reglas.json")
            fn(res, reglas)
            msgs = problems(res, reglas)
            self.assertTrue(any(texto in m for m in msgs), (texto, msgs))

        mutar(lambda r, _: r["reglas"][0].update(estado="regular"), "estado inválido")
        mutar(lambda r, _: r["reglas"][0].update(origen="intuicion"), "origen inválido")
        mutar(lambda r, _: r["reglas"][0].update(ic95=[5, 1]), "ic95")
        mutar(lambda r, _: r["reglas"][0].update(n=-3), "la n de")
        mutar(lambda r, _: r["reglas"][1].update(id="A1"), "repetida")
        mutar(lambda r, _: r["reglas"][0].update(docs=[]), "'docs'")
        mutar(lambda r, _: r["reglas"][0]["por_perfil"].update(fantasma={"valor": 1}), "perfil desconocido")
        mutar(lambda r, _: r.update(huella=""), "falta 'huella'")
        mutar(lambda r, _: r.update(semillas=[]), "falta 'semillas'")
        mutar(lambda r, _: r["series"].pop("patrimonio_por_dia"), "falta la serie")
        mutar(lambda r, _: r["series"]["patrimonio_por_dia"]["perfiles"]["medio"].pop(), "un número por día")
        mutar(lambda r, _: r["series"]["ingreso_hora_por_acto"]["objetivo"].pop("II"), "un número por acto")
        mutar(lambda r, _: r["series"]["acto1_caja_antes_de_cuota"]["perfiles"]["medio"].update(p10=9999), "p10 <= p50 <= p90")

    def test_mutaciones_de_reglas_json(self):
        def mutar(fn, texto):
            res, reglas = fixture("sim_resultados.json"), fixture("sim_reglas.json")
            fn(reglas)
            msgs = problems(res, reglas)
            self.assertTrue(any(texto in m for m in msgs), (texto, msgs))

        mutar(lambda g: g["trazabilidad"][0].update(reglas=[]), "no tiene ninguna regla")
        mutar(lambda g: g["trazabilidad"][0].update(reglas=["Z9"]), "regla inexistente")
        mutar(lambda g: g["reglas"].append({"id": "Z9"}), "no tiene resultado")
        mutar(lambda g: g["reglas"].pop(), "no está definida en reglas.json")
        mutar(lambda g: g["trazabilidad"][0].pop("fuente"), "'requisito' y 'fuente'")

    def test_referencias_como_dict_o_como_lista(self):
        for refs in ({"comerciante": 15000, "magnate": 250000}, [{"valor": 15000, "etiqueta": "Comerciante"}]):
            res = fixture("sim_resultados.json")
            res["series"]["patrimonio_por_dia"]["referencias"] = refs
            self.assertEqual(len(problems(res)), 2, refs)

    def test_referencias_invalidas(self):
        for refs in ({}, [], {"comerciante": "15000"}, {"comerciante": -1}, [{"valor": 5}], 7):
            res = fixture("sim_resultados.json")
            res["series"]["patrimonio_por_dia"]["referencias"] = refs
            self.assertTrue(any("referencias" in m for m in problems(res)), refs)

    def test_conteo(self):
        self.assertEqual(build.sim_conteo(fixture("sim_resultados.json")), {"pasa": 4, "falla": 1, "incierto": 1, "total": 6})


class Carga(unittest.TestCase):
    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.antes = len(build.warnings)

    def nuevos(self):
        return build.warnings[self.antes:]

    def copiar(self):
        shutil.copy(FIXTURES / "sim_resultados.json", self.tmp / "resultados.json")
        shutil.copy(FIXTURES / "sim_reglas.json", self.tmp / "reglas.json")

    def test_sin_resultados_no_falla_el_build(self):
        sim = build.load_sim({}, sim_dir=self.tmp, huella_actual=None)
        self.assertFalse(sim["disponible"])
        self.assertEqual(self.nuevos(), [])

    def test_sin_resultados_falla_si_es_requerido(self):
        build.SIM_REQUERIDO = True
        self.addCleanup(setattr, build, "SIM_REQUERIDO", False)
        build.load_sim({}, sim_dir=self.tmp, huella_actual=None)
        self.assertEqual(len(self.nuevos()), 1)

    def test_resultados_vigentes(self):
        self.copiar()
        sim = build.load_sim({}, sim_dir=self.tmp, huella_actual=HUELLA)
        self.assertTrue(sim["disponible"] and sim["huella_verificada"] and not sim["caducado"])
        self.assertEqual(sim["conteo"]["pasa"], 4)
        self.assertEqual(len(self.nuevos()), 2)  # A5 en falla y B5 incierta

    def test_resultados_caducados(self):
        self.copiar()
        sim = build.load_sim({}, sim_dir=self.tmp, huella_actual="cambio")
        self.assertTrue(sim["caducado"])
        self.assertTrue(any("caducado" in m for m in self.nuevos()))

    def test_huella_de_mundo_py(self):
        mundo = self.tmp / "tools" / "sim"
        mundo.mkdir(parents=True)
        (mundo / "mundo.py").write_text("def huella(world):\n    return 'h' + str(sorted(world))\n", encoding="utf-8")
        original = build.SIM_MUNDO
        build.SIM_MUNDO = mundo / "mundo.py"
        self.addCleanup(setattr, build, "SIM_MUNDO", original)
        self.assertEqual(build.sim_huella({"b": 1, "a": 2}), "h['a', 'b']")
        build.SIM_MUNDO = self.tmp / "no-existe.py"
        self.assertIsNone(build.sim_huella({}))


@unittest.skipUnless(shutil.which("node"), "Node no está instalado")
class Vista(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = pathlib.Path(tempfile.mkdtemp())
        sim_dir = cls.tmp / "sim"
        sim_dir.mkdir()
        shutil.copy(FIXTURES / "sim_resultados.json", sim_dir / "resultados.json")
        shutil.copy(FIXTURES / "sim_reglas.json", sim_dir / "reglas.json")
        antes = len(build.warnings)
        hub = build.build_hub()
        cls.hub = hub
        cls.sim_vigente = build.load_sim({}, sim_dir=sim_dir, huella_actual=HUELLA)
        cls.sim_caducado = build.load_sim({}, sim_dir=sim_dir, huella_actual="cambio")
        del build.warnings[antes:]

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, True)

    def render(self, sim, hash_, *clicks):
        hub = copy.copy(self.hub)
        hub["sim"] = sim
        path = self.tmp / "hub.json"
        path.write_text(json.dumps(hub, ensure_ascii=False), encoding="utf-8")
        out = subprocess.run(["node", str(FIXTURES / "hub_harness.js"), str(path), hash_] + list(clicks),
                             capture_output=True, text=True, timeout=60)
        self.assertEqual(out.returncode, 0, out.stderr)
        return json.loads(out.stdout)

    def test_vista_completa(self):
        r = self.render(self.sim_vigente, "#/simulador")
        html = r["html"]
        self.assertIn("Simulador de economía y progresión", html)
        self.assertEqual(html.count('class="sim-chart"'), 3)
        for rid in ("A1", "A3", "A5", "B1", "B5", "E1"):
            self.assertIn("<b>%s</b>" % rid, html)
        self.assertIn("IC 95 %", html)
        self.assertIn("4/6", html)
        self.assertIn("Trazabilidad", html)
        self.assertIn("La cuota del día 7 (960)", html)
        self.assertNotIn("sim-stale", html)
        self.assertIn("#/simulador", r["sidebar"])

    def sim_con_referencias(self, refs):
        res = fixture("sim_resultados.json")
        res["series"]["patrimonio_por_dia"]["referencias"] = refs
        sim = copy.deepcopy(self.sim_vigente)
        sim["resultados"] = res
        return sim

    def test_pisos_de_estatus_como_dict_se_leen_de_los_datos(self):
        html = self.render(self.sim_con_referencias({"magnate": 250000, "comerciante": 15000}), "#/simulador")["html"]
        self.assertEqual(html.count('class="sim-chart"'), 3)
        self.assertIn("Comerciante 15", html)
        self.assertIn("Magnate 250", html)
        self.assertIn("pisos de estatus de 15", html)
        for viejo in ("25.000", "120.000", "500.000"):
            self.assertNotIn(viejo, html)
        self.assertNotIn("NaN", html)

    def test_pisos_de_estatus_como_lista(self):
        html = self.render(self.sim_con_referencias([{"valor": 90000, "etiqueta": "Empresario"}]), "#/simulador")["html"]
        self.assertIn("Empresario 90", html)

    def test_vista_con_el_resultados_json_real(self):
        antes = len(build.warnings)
        sim = build.load_sim({}, huella_actual=None)
        del build.warnings[antes:]
        if not sim["disponible"]:
            self.skipTest("resultados.json todavía no existe")
        html = self.render(sim, "#/simulador")["html"]
        self.assertEqual(html.count('class="sim-chart"'), 3)
        self.assertIn("Trazabilidad", html)
        for malo in ("NaN", "undefined", "[object Object]"):
            self.assertNotIn(malo, html)
        for nombre in ("Comerciante", "Empresario", "Magnate"):
            self.assertIn(nombre, html)

    def test_aviso_de_caducidad(self):
        html = self.render(self.sim_caducado, "#/simulador")["html"]
        self.assertIn("sim-stale", html)
        self.assertIn("Resultado caducado", html)
        self.assertIn("resultado caducado", self.render(self.sim_caducado, "")["html"])

    def test_filtros_y_fila_desplegable(self):
        html = self.render(self.sim_vigente, "#/simulador", "sim-estado=falla")["html"]
        self.assertIn("<b>A5</b>", html)
        self.assertNotIn("<b>A1</b>", html)
        self.assertIn("Rápido", html)  # perfil que falla
        html = self.render(self.sim_vigente, "#/simulador", "sim-grupo=B · Ritmo y progresión")["html"]
        self.assertIn("<b>B1</b>", html)
        self.assertNotIn("<b>A1</b>", html)
        html = self.render(self.sim_vigente, "#/simulador", "sim-row=A5")["html"]
        self.assertIn("sim-detail", html)
        self.assertIn('aria-expanded="true"', html)

    def test_portada(self):
        self.assertIn("4 de 6 reglas pasan", self.render(self.sim_vigente, "")["html"])

    def test_sin_resultados(self):
        sim = {"disponible": False, "motivo": "resultados.json todavía no existe"}
        self.assertIn("todavía no existe", self.render(sim, "#/simulador")["html"])
        self.assertIn("sin resultados todavía", self.render(sim, "")["html"])


if __name__ == "__main__":
    unittest.main()
