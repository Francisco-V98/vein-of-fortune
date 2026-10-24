"""Reglas del motor de minas de cinco entradas (F0-93 y F0-92): C5b, J1 a J7.

Viven aparte de las 50 reglas de `reglas.py` y se declaran en `reglas_v2` de reglas.json. Todas corren con el
interruptor `motor_minas`; F0-92 calibró sus cifras. C5b es la regla de la carga del detector que sustituye al
descarte en el juego; C5 sigue midiendo el modelo sin entradas de las 50 reglas vigentes, que aún descuenta el 25 %
de la energía al descartar (quitarlo exige recalibrar todo el simulador).
"""
from . import campana as C
from . import entradas as E
from . import mundo
from . import reglas as R

REGLAS_V2 = {}
MIN_H = C.MIN_HORA


def regla(rid):
    def deco(fn):
        REGLAS_V2[rid] = fn
        return fn
    return deco


class Mundo:
    """Datos de las minas para una corrida: cifras de world.json, supuestos y contexto de la regla."""

    def __init__(self, c, world=None):
        self.c = c
        self.P = c.P
        self.EP = E.cargar(world)
        self.sup = c.S["minas_v2"]
        self.dph = R.per_hour(c.P)

    def minutos(self, K):
        """Minutos de caminata por entrada a la mina y por cambio de entrada (supuesto compartido por J2 y J5)."""
        return K.get("minutos", self.sup["minutos_caminar"])

    def motor(self, sem, **kw):
        if kw.pop("sin_eventos", False):  # sin problemas sociales ni políticos ni clima (las estaciones siguen)
            kw.setdefault("severidad", lambda dia, zona: 0)
            kw.setdefault("clima", E.Clima(sem, {}, self.EP, 0))
        return E.MotorMinas(sem, self.EP, sup=self.sup, actos=self.P["actos"], **kw)

    def correr(self, eid, pid, dias=None, hook=None, v2=True, **kw):
        """Una etapa por semilla. Devuelve [(resultado, motor)] (motor None si v2 es falso)."""
        c = self.c
        dias = c.tam["dias_etapa"] if dias is None else dias
        cal = c.S["estadistica"]["calentamiento_dias"]
        out = []
        for sem in c.semillas[: c.tam["semillas_etapa"]]:
            mot = self.motor(sem, **kw) if v2 else None
            cfg = C.cfg_etapa(self.P, c.S, eid, motor_minas=mot)
            h = hook(sem) if hook else None
            out.append((C.correr_etapa(self.P, c.S, cfg, c.perfil(pid), sem, dias, cal, hook=h), mot))
        return out


def pares_pct(a, b):
    """Diferencia relativa en % de b frente a a, semilla a semilla."""
    return [(y["neto_dia"] / x["neto_dia"] - 1.0) * 100.0 for (x, _), (y, _) in zip(a, b)]


def cond_media(c, nombre, valores, lo=None, hi=None, unidad="%", perfil=None):
    m, ic, n = R.media_ic(valores, c.S)
    return R.cond(nombre, m, lo, hi, ic, n, unidad, perfil)


# ------------------------------------------------------------------ C5b
@regla("C5b")
def C5b(c, K):
    W = Mundo(c, K.get("_world"))
    e, p = W.sup["etapa"], W.sup["perfil"]
    inf = W.correr(e, p, sin_eventos=True, cargas_extra=W.sup["bateria_infinita"])
    base = W.correr(e, p, sin_eventos=True)
    doble = W.correr(e, p, sin_eventos=True, cargas_extra=W.EP["bateria"][-1])
    ciegas = [m.cont["ciegas"] / max(1, m.cont["escaneos"] + m.cont["ciegas"]) * 100.0 for _, m in base]
    subs = [cond_media(c, "pérdida de ingreso por la batería de partida frente a una batería infinita", [-x for x in pares_pct(inf, base)],
                       K["perdida_min"], K["perdida_max"]),
            cond_media(c, "ganancia al añadir otra batería entera", pares_pct(base, doble), K["extra_min"]),
            cond_media(c, "menas picadas a ciegas sobre las encontradas", ciegas, None, K["ciegas_max"])]
    return R.r_final(subs, {p: {"valor": subs[0]["valor"], "ic95": subs[0]["ic95"], "n": subs[0]["n"]}})


# ------------------------------------------------------------------ J1
@regla("J1")
def J1(c, K):
    W = Mundo(c, K.get("_world"))
    e, p = W.sup["etapa"], W.sup["perfil"]
    tandas = [W.correr(e, p, severidad=lambda d, z, k=k: k) for k in range(max(W.EP["sev"].values()) + 1)]
    subs = []
    for k in range(1, len(tandas)):
        subs.append(cond_media(c, "pérdida al pasar de %d a %d entradas cerradas" % (k - 1, k), [-x for x in pares_pct(tandas[k - 1], tandas[k])],
                               K["paso_min"]))
    subs.append(cond_media(c, "pérdida total con %d cerradas frente a ninguna" % (len(tandas) - 1), [-x for x in pares_pct(tandas[0], tandas[-1])],
                           K["total_min"], K["total_max"]))
    return R.r_final(subs, {p: {"valor": subs[-1]["valor"], "ic95": subs[-1]["ic95"], "n": subs[-1]["n"]}})


# ------------------------------------------------------------------ J2
@regla("J2")
def J2(c, K):
    W = Mundo(c, K.get("_world"))
    e, p = W.sup["etapa"], W.sup["perfil"]
    sin = W.correr(e, p, sin_eventos=True, cambiar_entrada=False, minutos_caminar=W.minutos(K))
    con = W.correr(e, p, sin_eventos=True, minutos_caminar=W.minutos(K))
    # ingreso por hora de reloj: el jugador que cambia camina más (la entrada a la mina y cada cambio de entrada)
    dia_min = c.P["t"]["dia_min"]
    gan = []
    for (a, ma), (b, mb) in zip(sin, con):
        ea, eb = (m.horas_caminadas() * MIN_H / c.tam["dias_etapa"] for m in (ma, mb))
        gan.append((b["neto_dia"] / (dia_min + eb)) / (a["neto_dia"] / (dia_min + ea)) * 100.0 - 100.0)
    sub = cond_media(c, "ganancia de cambiar de entrada una vez al día, por hora de reloj", gan, K["ganancia_min"], K["ganancia_max"])
    return R.r_final([sub], {p: {"valor": sub["valor"], "ic95": sub["ic95"], "n": sub["n"]}})


# ------------------------------------------------------------------ J3
@regla("J3")
def J3(c, K):
    W = Mundo(c, K.get("_world"))
    e, p = W.sup["etapa"], W.sup["perfil"]
    subs = []
    for etiqueta, kw in (("días normales", {}), ("días de nieve", {"nieve_siempre": True})):
        res = W.correr(e, p, sin_eventos=True, **kw)
        clave = "nieve" if kw else "normal"
        fr = [m.cont["cortas_" + clave] / max(1, m.cont["dias_" + clave]) * 100.0 for _, m in res]
        subs.append(cond_media(c, "días con la batería corta, " + etiqueta, fr, K["corta_min"], K["corta_max"]))
    return R.r_final(subs, {p: {"valor": subs[0]["valor"], "ic95": subs[0]["ic95"], "n": subs[0]["n"]}})


# ------------------------------------------------------------------ J4
@regla("J4")
def J4(c, K):
    W = Mundo(c, K.get("_world"))
    EP, acto = W.EP, K["acto"]
    dias = c.tam["dias_etapa"] * len(c.semillas)
    exacto, jug, emp = [], [], []
    for sem in c.semillas:
        for d in range(dias):
            ent = E.sortear_entradas(sem, d, "z", EP)
            cerr = E.cerrar(ent, 0, acto, EP)
            m = E.Mina(ent, cerr, EP)
            ab = m.abiertas()
            esperado = sum(E.mult_calidad(ent[i], acto, EP) for i in ab) / len(ab)
            exacto.append(abs(m.mult_empleados(acto) - esperado))
            emp.append(m.mult_empleados(acto))
            jug.append(m.mult_jugador(acto))
    subs = [R.cond("error máximo de los empleados frente a la media de las entradas abiertas", max(exacto), None, K["error_max"], None, len(exacto), "x"),
            cond_media(c, "diferencia media entre empleados y jugador sin escanear", [(a - b) * 100.0 for a, b in zip(emp, jug)],
                       -K["dif_max"], K["dif_max"], "pp")]
    return R.r_final(subs, {})


# ------------------------------------------------------------------ J5
@regla("J5")
def J5(c, K):
    W = Mundo(c, K.get("_world"))
    e, p = W.sup["etapa"], W.sup["perfil"]
    base = W.correr(e, p, v2=False)
    con = W.correr(e, p, sin_eventos=True, minutos_caminar=W.minutos(K))
    dia_min = c.P["t"]["dia_min"]
    devs = []
    for (b, _), (v, m) in zip(base, con):
        extra = m.horas_caminadas() * MIN_H / c.tam["dias_etapa"]  # minutos de caminata por día
        devs.append(v["neto_dia"] / b["neto_dia"] * dia_min / (dia_min + extra) * 100.0 - 100.0)
    sub = cond_media(c, "ingreso por hora con %s minutos de caminar frente al modelo sin entradas" % W.minutos(K), devs, -K["desv_max"], K["desv_max"])
    return R.r_final([sub], {p: {"valor": sub["valor"], "ic95": sub["ic95"], "n": sub["n"]}})


# ------------------------------------------------------------------ J6
@regla("J6")
def J6(c, K):
    W = Mundo(c, K.get("_world"))
    e, p = W.sup["etapa"], W.sup["perfil"]
    cal = W.sup["calendario"]
    anio = cal["dias_por_estacion"] * len(cal["orden"])
    dias = max(c.tam["dias_etapa"], anio + c.S["estadistica"]["calentamiento_dias"])
    por_est = {s: [] for s in cal["orden"]}

    def hook(sem):
        previo = {}
        dia = {}

        def h(partida, d):
            acum = partida.ingreso_neto()
            est = E.calendario(partida.dia - 1, cal)[0]
            if "x" in previo and d >= c.S["estadistica"]["calentamiento_dias"]:
                dia.setdefault(est, []).append(acum - previo["x"])
            previo["x"] = acum
            if d == dias - 1:
                for s_, v in dia.items():
                    por_est[s_].append(C.media(v) * W.dph)
        return h
    W.correr(e, p, dias=dias, hook=hook, sin_eventos=True)
    media = C.media([C.media(v) for v in por_est.values() if v])
    subs = []
    for s_, v in por_est.items():
        dev = [(x / media - 1.0) * 100.0 for x in v]
        subs.append(cond_media(c, "ingreso por hora en %s frente a la media de las estaciones" % s_, dev, -K["desv_max"], K["desv_max"]))
    return R.r_final(subs, {})


# ------------------------------------------------------------------ J7
@regla("J7")
def J7(c, K):
    """La cuota del Acto I sigue pagándose con el abanico estrecho (A1, A3 y A4 con el jugador que escanea y cambia de entrada)."""
    W = Mundo(c, K.get("_world"))
    n = c.tam["acto1"]
    fab = lambda sem: W.motor(sem, sin_eventos=True, minutos_caminar=W.minutos(K))

    def lote(pid, **kw):
        return C.resumen_acto1(C.lote_acto1(c.P, c.S, c.perfil(pid), n, motor_fn=fab, **kw), c.S)
    a1, a3, a4 = c.crit("A1"), c.crit("A3"), c.crit("A4")
    med, len4, rap = lote("medio"), lote("lento", n_exp=a3["exp_lento"]), lote("rapido")
    pct = lambda r: [x * 100 for x in r["paga_ic"]]
    subs = [cond_pct("pago a tiempo del medio", med["paga"] * 100, a1["pago_min"], a1["pago_max"], pct(med), med["n"]),
            cond_pct("margen sobre la cuota del medio", med["margen_pct"], a1["margen_min"], a1["margen_max"], med["margen_pct_ic"], med["n"]),
            cond_pct("pago del lento con %d expediciones" % a3["exp_lento"], len4["paga"] * 100, a3["pago4_min"], a3["pago4_max"], pct(len4), len4["n"]),
            cond_pct("pago a tiempo del rápido", rap["paga"] * 100, a4["pago_min"], None, pct(rap), rap["n"]),
            cond_pct("margen sobre la cuota del rápido", rap["margen_pct"], a4["margen_min"], a4["margen_max"], rap["margen_pct_ic"], rap["n"])]
    return R.r_final(subs, {"medio": {"valor": subs[0]["valor"], "ic95": subs[0]["ic95"], "n": subs[0]["n"]}})


cond_pct = R.cond


def evalua(c, rid, world=None, criterio=None):
    K = dict(next(r for r in c.R["reglas_v2"] if r["id"] == rid)["criterio"])
    K.update(criterio or {})
    if world is not None:
        K["_world"] = world
    return R.resultado_regla(rid, c, REGLAS_V2[rid](c, K))
