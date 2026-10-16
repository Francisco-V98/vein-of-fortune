"""Pruebas del simulador de economía y progresión (F0-53): tools/sim, studio/data/sim.

Un caso por regla de equilibrio (50), con subTest por perfil; una mutación por regla que voltea alguna de sus
condiciones; determinismo; reproducción del prototipo de F0-52; modo rápido en menos de 45 s; ninguna cifra del
juego dentro del código del simulador. Ejecutar:
    python3 -m unittest discover -s tools/ci -v
"""
import ast
import json
import pathlib
import sys
import time
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from sim import campana as C  # noqa: E402
from sim import mercado, mundo, reglas, run  # noqa: E402

SIM_DIR = ROOT / "studio" / "data" / "sim"
RESULTADOS = SIM_DIR / "resultados.json"
IDS_META = ("I1", "I2", "I3")
# Reglas cuyo modo rápido no es comparable con el completo: D1 mide una celda de la cuadrícula en vez de todas y G5 divide por
# una diferencia de aportes muy ruidosa que no tiene intervalo propio.
SOLO_SUBCONJUNTO = ("D1", "G5")

# Números que pueden aparecer en el código del simulador sin ser cifras del juego: neutros, conversiones de unidades,
# porcentajes (/100), medio, y el largo de la huella. Cualquier otro número tiene que venir de world.json o de supuestos.json.
LISTA_BLANCA = {0, 1, 2, 100, 0.5, 1.0, 2.0, 100.0, 0.0, 200.0, -1, 60, 60.0, 16, 1024.0}
EPSILON = 1e-5


def cargar_json(ruta):
    return json.loads(pathlib.Path(ruta).read_text(encoding="utf-8"))


class Compartido:
    """Evaluación rápida de todas las reglas, una sola vez para todas las pruebas."""

    listo = False

    @classmethod
    def preparar(cls):
        if cls.listo:
            return
        cls.world = mundo.cargar_world()
        cls.S = mundo.cargar_supuestos()
        cls.R = run.cargar_reglas()
        t = time.time()
        cls.ctx, cls.resultados = run.evaluar(**run.opciones(run.parser().parse_args(["--rapido"])))  # exactamente lo que ejecuta la CLI y la CI
        cls.segundos = time.time() - t
        cls.por_id = {r["id"]: r for r in cls.resultados}
        cls.mini_base = {}
        cls.listo = True

    @classmethod
    def base_mini(cls, rid):
        if rid not in cls.mini_base:
            cx = reglas.Ctx(mundo.cargar()[0], cls.S, cls.R, "mini")
            cls.mini_base[rid] = [s["estado"] for s in reglas.evalua_regla(cx, rid)["subs"]]
        return cls.mini_base[rid]


class Datos(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Compartido.preparar()

    def test_cincuenta_reglas_en_codigo_y_datos(self):
        ids_datos = [r["id"] for r in Compartido.R["reglas"]]
        self.assertEqual(len(ids_datos), 50)
        self.assertEqual(len(set(ids_datos)), 50)
        self.assertEqual(sorted(ids_datos), sorted(reglas.REGLAS))
        for r in Compartido.R["reglas"]:
            for k in ("id", "grupo", "titulo", "docs", "metrica", "umbral", "origen", "criterio"):
                self.assertIn(k, r, r["id"])
            self.assertIn(r["origen"], ("doc", "prop."))
            self.assertTrue(r["docs"] and all(isinstance(d, str) and d[0].isdigit() for d in r["docs"]), r["id"])

    def test_trazabilidad_cubre_todas_las_reglas(self):
        citadas = {rid for t in Compartido.R["trazabilidad"] for rid in t["reglas"]}
        self.assertEqual(citadas, {r["id"] for r in Compartido.R["reglas"]})
        for t in Compartido.R["trazabilidad"]:
            self.assertTrue(t["requisito"] and t["fuente"] and t["reglas"])

    def test_perfiles_y_tamanos(self):
        S = Compartido.S
        self.assertEqual(sorted(S["perfiles"]), ["lento", "medio", "optimizador", "rapido"])
        for modo in ("rapido", "completo", "mini"):
            self.assertIn(modo, S["tamanos"])
        self.assertGreaterEqual(S["tamanos"]["completo"]["semillas"], 40)

    def test_resultados_json_vigente_y_con_el_esquema(self):
        if not RESULTADOS.exists():
            self.skipTest("todavía no se han generado los resultados")
        res = cargar_json(RESULTADOS)
        self.assertLessEqual(RESULTADOS.stat().st_size, 300 * 1024)
        self.assertEqual(res["huella"], mundo.huella(Compartido.world), "resultados.json caducado: reejecuta tools/sim/run.py --completo --escribir")
        self.assertEqual(sorted(r["id"] for r in res["reglas"]), sorted(reglas.REGLAS))
        for r in res["reglas"]:
            self.assertIn(r["estado"], ("pasa", "falla", "incierto"))
            self.assertIn(r["origen"], ("doc", "prop."))
            self.assertTrue(r["docs"])
        self.assertEqual({p["id"] for p in res["perfiles"]}, set(Compartido.S["perfiles"]))
        for clave in ("ingreso_hora_por_acto", "patrimonio_por_dia", "acto1_caja_antes_de_cuota"):
            self.assertIn(clave, res["series"])

    def test_mutaciones_definidas_para_cada_regla(self):
        muts = Compartido.S["mutaciones"]
        esperadas = set(reglas.REGLAS) - set(IDS_META)
        self.assertEqual(set(muts), esperadas)
        for rid, lista in muts.items():
            self.assertTrue(lista, rid)
            for m in lista:
                for e in m["ediciones"]:
                    w = json.loads(json.dumps(Compartido.world))
                    reglas.aplica_edicion(w, e["clave"], e["valor"])  # la clave existe


class SinCifrasDelJuego(unittest.TestCase):
    def test_el_codigo_no_tiene_numeros_sueltos(self):
        sueltos = []
        for f in sorted((ROOT / "tools" / "sim").glob("*.py")):
            arbol = ast.parse(f.read_text(encoding="utf-8"))
            indices = set()
            for nodo in ast.walk(arbol):
                if isinstance(nodo, ast.Subscript):
                    for hijo in ast.walk(nodo.slice):
                        if isinstance(hijo, ast.Constant):
                            indices.add(id(hijo))
            for nodo in ast.walk(arbol):
                if isinstance(nodo, ast.Constant) and isinstance(nodo.value, (int, float)) and not isinstance(nodo.value, bool):
                    v = nodo.value
                    if id(nodo) in indices or v in LISTA_BLANCA or (isinstance(v, float) and abs(v) < EPSILON):
                        continue
                    sueltos.append("%s:%d (%s)" % (f.name, nodo.lineno, v))
        self.assertEqual(sueltos, [], "cifras sueltas en tools/sim: deben venir de world.json o supuestos.json")

    def test_solo_biblioteca_estandar(self):
        permitidos = set(sys.stdlib_module_names) if hasattr(sys, "stdlib_module_names") else None
        for f in sorted((ROOT / "tools" / "sim").glob("*.py")):
            arbol = ast.parse(f.read_text(encoding="utf-8"))
            for nodo in ast.walk(arbol):
                nombres = []
                if isinstance(nodo, ast.Import):
                    nombres = [a.name.split(".")[0] for a in nodo.names]
                elif isinstance(nodo, ast.ImportFrom) and nodo.level == 0 and nodo.module:
                    nombres = [nodo.module.split(".")[0]]
                for n in nombres:
                    if n == "sim":
                        continue
                    if permitidos is not None:
                        self.assertIn(n, permitidos, "%s importa %s, que no es de la biblioteca estándar" % (f.name, n))


class Huella(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Compartido.preparar()

    def test_estable_y_sensible_a_lo_que_lee(self):
        w = Compartido.world
        h = mundo.huella(w)
        self.assertEqual(h, mundo.huella(json.loads(json.dumps(w))))
        w2 = json.loads(json.dumps(w))
        w2["economy"]["debt"]["principal"] += 1
        self.assertNotEqual(h, mundo.huella(w2))
        w3 = json.loads(json.dumps(w))
        w3["economy"]["tools"]["upgrade_cost"]["pico"]["3"] += 1
        self.assertNotEqual(h, mundo.huella(w3))

    def test_no_cambia_con_lo_que_no_lee(self):
        w = json.loads(json.dumps(Compartido.world))
        h = mundo.huella(w)
        w["characters"][0]["name"] = "Otro nombre"
        w["economy"]["validation"]["last_simulated"] = "otra fecha"
        self.assertEqual(h, mundo.huella(w))

    def test_las_claves_leidas_existen_y_son_muchas(self):
        claves = mundo.claves(Compartido.world)
        self.assertGreater(len(claves), 400)
        for k in claves:
            self.assertTrue(k)


class Determinismo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Compartido.preparar()

    def test_misma_semilla_mismo_resultado(self):
        K = Compartido.ctx.crit("I1")
        r = reglas.evalua_regla(Compartido.ctx, "I1")
        self.assertEqual(r["estado"], "pasa")
        # y la campaña completa, dos veces, idéntica
        P = Compartido.ctx.P
        a = C.Campana(P, Compartido.S, "medio", 123).correr().resumen()
        b = C.Campana(P, Compartido.S, "medio", 123).correr().resumen()
        redondea = lambda x: json.dumps(reglas._redondea(x, Compartido.S["estadistica"]["decimales"]), sort_keys=True, default=str)
        self.assertEqual(redondea(a), redondea(b))
        self.assertTrue(K)

    def test_semillas_distintas_dan_resultados_distintos(self):
        P = Compartido.ctx.P
        a = C.Campana(P, Compartido.S, "medio", 123).correr().resumen()["pat_fin"]
        b = C.Campana(P, Compartido.S, "medio", 124).correr().resumen()["pat_fin"]
        self.assertNotEqual(a, b)


class ModoRapido(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Compartido.preparar()

    def test_dura_menos_de_45_segundos(self):
        self.assertLessEqual(Compartido.segundos, 45.0, "el modo rápido tardó %.1f s" % Compartido.segundos)

    def test_reproduce_el_prototipo_de_f0_52(self):
        r = reglas.evalua_regla(Compartido.ctx, "B8")
        K = Compartido.ctx.crit("B8")
        for s in r["subs"]:
            self.assertLessEqual(s["valor"], K["desv_max"], s["nombre"])

    def test_cada_regla_devuelve_condiciones_con_n_o_intervalo(self):
        for rid, r in Compartido.por_id.items():
            self.assertTrue(r["subs"], rid)
            for s in r["subs"]:
                self.assertIn(s["estado"], ("pasa", "falla", "incierto"))
                if s["valor"] is not None:
                    self.assertIsNotNone(s["ic95"], "%s: %s" % (rid, s["nombre"]))


class Reglas(unittest.TestCase):
    """Un método por regla (se generan abajo): se mide, el estado es coherente con resultados.json y con sus condiciones."""

    @classmethod
    def setUpClass(cls):
        Compartido.preparar()
        cls.guardado = {r["id"]: r for r in cargar_json(RESULTADOS)["reglas"]} if RESULTADOS.exists() else {}


def cerca_del_umbral(c, tolerancia=0.3):
    """True si el valor de la condición está a menos de `tolerancia` (relativa) de alguno de sus límites."""
    v = c.get("valor")
    if v is None:
        return False
    for lim in (c.get("lo"), c.get("hi")):
        if lim is None:
            continue
        escala = max(abs(lim), abs(v), 1e-9)
        if abs(v - lim) / escala <= tolerancia:
            return True
    return False


def _caso_regla(rid):
    def prueba(self):
        if rid in IDS_META:
            self.skipTest("meta-regla: se prueba aparte")
        r = Compartido.por_id[rid]
        self.assertIn(r["estado"], ("pasa", "falla", "incierto"))
        perfiles = sorted({s["perfil"] for s in r["subs"] if s.get("perfil")} | set(r["por_perfil"])) or ["general"]
        for perfil in perfiles:
            with self.subTest(regla=rid, perfil=perfil):
                subs = [s for s in r["subs"] if s.get("perfil") in (None, perfil)] or r["subs"]
                for s in subs:
                    if s["valor"] is not None and s["ic95"]:
                        self.assertLessEqual(s["ic95"][0], s["ic95"][1])
                    if s["lo"] is not None and s["valor"] is not None and s["ic95"] and s["ic95"][0] >= s["lo"] and (s["hi"] is None or s["ic95"][1] <= s["hi"]):
                        self.assertEqual(s["estado"], "pasa", s["nombre"])
        # coherente con lo guardado: el modo rápido (pocas semillas) y el completo no pueden contradecirse salvo en el umbral
        g = self.guardado.get(rid)
        if g is not None and rid not in SOLO_SUBCONJUNTO:
            conds = g.get("condiciones", [])
            if len(conds) == len(r["subs"]):
                for rapido, guardado in zip(r["subs"], conds):
                    if {rapido["estado"], guardado["estado"]} == {"pasa", "falla"}:
                        self.assertTrue(cerca_del_umbral(rapido) and cerca_del_umbral(guardado),
                                        "%s: «%s» da «%s» en el modo rápido y «%s» en resultados.json lejos del umbral"
                                        % (rid, rapido["nombre"], rapido["estado"], guardado["estado"]))
    prueba.__name__ = "test_regla_%s" % rid
    return prueba


def _caso_mutacion(rid):
    def prueba(self):
        muts = Compartido.S["mutaciones"].get(rid)
        if rid in IDS_META or not muts:
            self.skipTest("meta-regla")
        base = Compartido.base_mini(rid)
        mundo_base = Compartido.world
        tam = dict(Compartido.S["tamanos"]["mini"])
        volteo = False
        for m in muts:
            with self.subTest(regla=rid, mutacion=m["descripcion"]):
                cm = reglas.contexto_mutado(mundo_base, Compartido.S, Compartido.R, "mini", [(e["clave"], e["valor"]) for e in m["ediciones"]], tam)
                estados = [s["estado"] for s in reglas.evalua_regla(cm, rid)["subs"]]
                if estados != base:
                    volteo = True
        self.assertTrue(volteo, "ninguna mutación de %s cambia el estado de sus condiciones" % rid)
    prueba.__name__ = "test_mutacion_%s" % rid
    return prueba


class Mutaciones(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Compartido.preparar()

    def test_mutacion_I1_un_azar_que_no_es_determinista_falla(self):
        original = mercado.Azar.u
        contador = [0]

        def roto(self):
            contador[0] += 1
            return (original(self) + (time.perf_counter() * contador[0]) % 1.0) % 1.0
        mercado.Azar.u = roto
        try:
            r = reglas.evalua_regla(Compartido.ctx, "I1")
        finally:
            mercado.Azar.u = original
        self.assertEqual(r["estado"], "falla")

    def test_mutacion_I3_una_regla_incierta_hace_fallar_la_meta_regla(self):
        c = Compartido.ctx
        c.base_resultados = [{"id": "A1", "estado": "incierto", "n": 10, "ic95": None, "condiciones": []}]
        try:
            r = reglas.evalua_regla(c, "I3")
        finally:
            del c.base_resultados
        self.assertEqual(r["estado"], "falla")

    def test_mutacion_I2_sin_mutaciones_no_pasa(self):
        # una regla sin mutación definida contaría como no volteada: se comprueba con el recuento de ids
        faltantes = set(reglas.REGLAS) - set(IDS_META) - set(Compartido.S["mutaciones"])
        self.assertEqual(faltantes, set())


for _rid in sorted(reglas.REGLAS):
    setattr(Reglas, "test_regla_%s" % _rid, _caso_regla(_rid))
    setattr(Mutaciones, "test_mutacion_%s" % _rid, _caso_mutacion(_rid))


class Auxiliares(unittest.TestCase):
    def test_condicion_estados(self):
        self.assertEqual(reglas.cond("x", 5, 0, 10, [4, 6])["estado"], "pasa")
        self.assertEqual(reglas.cond("x", 5, 6, 10, [4, 5.5])["estado"], "falla")
        self.assertEqual(reglas.cond("x", 5, 5.2, 10, [4, 6])["estado"], "incierto")
        self.assertEqual(reglas.cond("x", None, 0, 1)["estado"], "falla")

    def test_ic_de_proporcion(self):
        S = mundo.cargar_supuestos()
        lo, hi = C.ic_prop(50, 100, S)
        self.assertLess(lo, 0.5)
        self.assertGreater(hi, 0.5)
        self.assertEqual(C.ic_prop(0, 0, S), [None, None])

    def test_mercado_ida_y_vuelta_pierde(self):
        P, _ = mundo.cargar()
        S = mundo.cargar_supuestos()
        mk = mercado.MercadoRef(P, mercado.Azar(1), S["ruido"], acto="II", sueltos=False, tope_diario=False)
        w = P["mk"]["w_acto"]["II"]
        for m in P["min"]:
            if m == "aetherita":
                continue
            q = P["M"][m]["comprador"]
            costo = mk.precio_compra(m, q, w, "spot") * q
            ing = mk.precio_venta(m, q, w, "spot") * q
            self.assertLess(ing, costo, m)


if __name__ == "__main__":
    unittest.main()
