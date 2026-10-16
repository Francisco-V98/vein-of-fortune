"""Las reglas de equilibrio como casos medibles (A a I).

Cada regla recibe el contexto `Ctx` (mundo, supuestos, tamaños de corrida y caché de simulaciones) y sus criterios
(`reglas.json`, campo `criterio`). Devuelve condiciones medidas con su intervalo de confianza; el estado de la regla
sale de ellas: «pasa» si todo el intervalo cae del lado bueno, «falla» si cae entero del lado malo, «incierto» si cruza el umbral.
"""
import json
import math
import statistics

from . import campana as C
from . import mundo
from .mercado import Azar, MercadoRef

REGLAS = {}


def regla(rid):
    def deco(fn):
        REGLAS[rid] = fn
        return fn
    return deco


# ------------------------------------------------------------------ condiciones y estados
def cond(nombre, valor, lo=None, hi=None, ic=None, n=None, unidad="%", perfil=None):
    """Una condición medida: valor con su intervalo y la franja aceptable [lo, hi]."""
    if valor is None or (isinstance(valor, float) and (math.isnan(valor) or math.isinf(valor))):
        return {"nombre": nombre, "valor": None, "ic95": None, "n": n, "lo": lo, "hi": hi, "estado": "falla", "unidad": unidad,
                "perfil": perfil}
    if ic is None or ic[0] is None or ic[1] is None:
        ic = [valor, valor]
    ic = [min(ic[0], valor), max(ic[1], valor)]
    dentro = (lo is None or ic[0] >= lo) and (hi is None or ic[1] <= hi)
    if dentro:
        estado = "pasa"
    else:
        fuera = (lo is not None and ic[1] < lo) or (hi is not None and ic[0] > hi)
        estado = "falla" if fuera else "incierto"
    return {"nombre": nombre, "valor": valor, "ic95": ic, "n": n, "lo": lo, "hi": hi, "estado": estado, "unidad": unidad,
            "perfil": perfil}


PESO = {"falla": 2, "incierto": 1, "pasa": 0}


def estado_de(subs):
    return max((s["estado"] for s in subs), key=lambda e: PESO[e]) if subs else "incierto"


def margen(s):
    """Margen relativo de una condición (negativo = fuera)."""
    v, lo, hi = s["valor"], s["lo"], s["hi"]
    if v is None:
        return -float("inf")
    m = float("inf")
    esc = max(abs(v), abs(lo or 0), abs(hi or 0), 1e-9)
    if lo is not None:
        m = min(m, (v - lo) / esc)
    if hi is not None:
        m = min(m, (hi - v) / esc)
    return m


def principal(subs):
    """La condición que mejor resume la regla: la peor (falla, incierto) o la de menor margen."""
    if not subs:
        return None
    peor = max(PESO[s["estado"]] for s in subs)
    cand = [s for s in subs if PESO[s["estado"]] == peor]
    return min(cand, key=margen)


def media_ic(valores, S):
    n = len(valores)
    m = C.media(valores)
    return m, C.ic95(valores, S), n


# ------------------------------------------------------------------ contexto
class Ctx:
    def __init__(self, P, S, R, modo="rapido", tam=None):
        self.P, self.S, self.R, self.modo = P, S, R, modo
        self.tam = dict(S["tamanos"][modo]) if tam is None else tam
        self.cache = {}
        self.semillas = [C.semilla(S, i) for i in range(self.tam["semillas"])]
        self.mapa = {r["id"]: r for r in R["reglas"]}

    def crit(self, rid):
        return self.mapa[rid]["criterio"]

    def perfil(self, pid):
        return C.perfil_de(self.P, self.S, pid)

    def memo(self, clave, fn):
        if clave not in self.cache:
            self.cache[clave] = fn()
        return self.cache[clave]

    # --- Acto I
    def acto1(self, pid, n=None, **kw):
        n = self.tam["acto1"] if n is None else n
        clave = ("a1", pid, n, json.dumps(kw, sort_keys=True))

        def f():
            res = C.lote_acto1(self.P, self.S, self.perfil(pid), n, **kw)
            out = C.resumen_acto1(res, self.S)
            out["max_caja"] = max(r["caja"] for r in res)
            out["netos"] = [r["neto_hora"] for r in res]
            out["cajas"] = [r["caja"] for r in res]
            out["pagos"] = [1 if r["paga"] else 0 for r in res]
            return out
        return self.memo(clave, f)

    # --- campañas completas
    def camps(self, pid, via=True, extra=0, variante=None, descarte=None, mejora_a1=None, n=None):
        clave = ("camp", pid, via, extra, variante, descarte, mejora_a1, n)
        semillas = self.semillas if n is None else [C.semilla(self.S, i) for i in range(n)]

        def f():
            out = []
            for sem in semillas:
                c = C.Campana(self.P, self.S, pid, sem, dias_extra=extra, via_deuda=via, variante=variante,
                              descarte=descarte, mejora_a1=mejora_a1).correr()
                out.append(c.resumen())
            return out
        return self.memo(clave, f)

    # --- etapas estacionarias
    def etapa(self, eid, pid, dias=None, cal=None, semillas=None, proto=False, **kw):
        dias = self.tam["dias_etapa"] if dias is None else dias
        cal = self.S["estadistica"]["calentamiento_dias"] if cal is None else cal
        semillas = self.semillas[: self.tam["semillas_etapa"]] if semillas is None else semillas
        perfil_proto = kw.pop("perfil_proto", False)
        clave = ("etapa", eid, pid, dias, cal, tuple(semillas), proto, json.dumps(kw, sort_keys=True, default=str), perfil_proto)

        def f():
            out = []
            for sem in semillas:
                cfg = C.cfg_etapa(self.P, self.S, eid, proto=proto, **kw)
                perfil = dict(self.perfil(pid), eps=0.0) if perfil_proto else self.perfil(pid)
                out.append(C.correr_etapa(self.P, self.S, cfg, perfil, sem, dias, cal))
            return out
        return self.memo(clave, f)


def per_hour(P):
    return 60.0 / P["t"]["dia_min"]


def pct_dev(x, objetivo):
    return abs(x - objetivo) / objetivo * 100.0


def ic_dev(ic, objetivo, S=None):
    """Intervalo de la desviación absoluta en % a partir del intervalo de la media."""
    if ic is None or ic[0] is None:
        return None
    lo, hi = ic
    ds = [abs(lo - objetivo) / objetivo * 100.0, abs(hi - objetivo) / objetivo * 100.0]
    if lo <= objetivo <= hi:
        return [0.0, max(ds)]
    return [min(ds), max(ds)]


def r_final(subs, por_perfil=None, extra=None):
    return {"subs": subs, "por_perfil": por_perfil or {}, "extra": extra or {}}


PERFILES = ("lento", "medio", "rapido")
ACT3 = ("II", "III", "IV")


# ================================================================== A · Acto I y deuda
@regla("A1")
def A1(c, K):
    r = c.acto1("medio")
    ic = [x * 100 for x in r["paga_ic"]]
    subs = [cond("pago a tiempo", r["paga"] * 100, K["pago_min"], K["pago_max"], ic, r["n"]),
            cond("margen sobre la cuota", r["margen_pct"], K["margen_min"], K["margen_max"], r["margen_pct_ic"], r["n"])]
    return r_final(subs, {"medio": {"valor": r["paga"] * 100, "ic95": ic, "n": r["n"]}})


@regla("A2")
def A2(c, K):
    sin = c.acto1("medio")
    con = c.acto1("medio", mejora=True)
    n = sin["n"]
    d = (sin["paga"] - con["paga"]) * 100
    se = math.sqrt(sin["paga"] * (1 - sin["paga"]) / n + con["paga"] * (1 - con["paga"]) / con["n"]) * 100
    z = c.S["estadistica"]["z95"]
    subs = [cond("margen con la mejora", con["margen_pct"], K["margen_con_min"], None, con["margen_pct_ic"], con["n"]),
            cond("diferencia de pago sin y con mejora (pp)", d, K["dif_min"], K["dif_max"], [d - z * se, d + z * se], n, "pp"),
            cond("pago a tiempo con mejora", con["paga"] * 100, K["pago_con_min"], None, [x * 100 for x in con["paga_ic"]], con["n"])]
    return r_final(subs, {"medio": {"valor": con["paga"] * 100, "n": con["n"]}})


@regla("A3")
def A3(c, K):
    P = c.P
    l4 = c.acto1("lento", n_exp=K["exp_lento"])
    l5 = c.acto1("lento", n_exp=K["exp_lento"] + 1)
    camps = c.camps("lento", via=True, n=c.tam["semillas_tasas"])
    prorrogaron = [r for r in camps if not r["cuota7_pagada"]]
    k = sum(1 for r in prorrogaron if r["pago14"])
    n = len(prorrogaron)
    ic = [x * 100 if x is not None else None for x in C.ic_prop(k, n, c.S)]
    subs = [cond("pago del lento con %d expediciones" % K["exp_lento"], l4["paga"] * 100, K["pago4_min"], K["pago4_max"],
                 [x * 100 for x in l4["paga_ic"]], l4["n"]),
            cond("pago del lento con %d expediciones" % (K["exp_lento"] + 1), l5["paga"] * 100, K["pago5_min"], None,
                 [x * 100 for x in l5["paga_ic"]], l5["n"]),
            cond("el acto cierra aunque no pague (la mora no cierra puertas)", 0.0 if P["deuda"]["mora"]["cierra"] else 100.0, 100.0, 100.0),
            cond("paga el día 14 tras prorrogar", (k / n * 100) if n else None, K["pago14_min"], None, ic, n)]
    return r_final(subs, {"lento": {"valor": l4["paga"] * 100, "ic95": [x * 100 for x in l4["paga_ic"]], "n": l4["n"]}})


@regla("A4")
def A4(c, K):
    r = c.acto1("rapido")
    ic = [x * 100 for x in r["paga_ic"]]
    subs = [cond("pago a tiempo", r["paga"] * 100, K["pago_min"], None, ic, r["n"]),
            cond("margen sobre la cuota", r["margen_pct"], K["margen_min"], K["margen_max"], r["margen_pct_ic"], r["n"])]
    return r_final(subs, {"rapido": {"valor": r["paga"] * 100, "ic95": ic, "n": r["n"]}})


@regla("A5")
def A5(c, K):
    P, S = c.P, c.S
    obj = P["ritmo"]["hora"]["I"]
    pares = [("lento", "slow"), ("medio", "medium"), ("rapido", "fast")]
    subs, pp = [], {}
    for pid, clave in pares:
        r = c.acto1(pid)
        m, ic, n = media_ic(r["netos"], S)
        d = pct_dev(m, obj[clave])
        subs.append(cond("desviación del ingreso/h (%s)" % pid, d, None, K["desv_max"], ic_dev(ic, obj[clave]), n, perfil=pid))
        pp[pid] = {"valor": m, "ic95": ic, "n": n}
    return r_final(subs, pp)


@regla("A6")
def A6(c, K):
    P = c.P
    D = P["deuda"]
    camps = c.camps("medio", via=True)
    sem2 = [r["semana2"] for r in camps]
    subs = []
    cuota = float(D["cuota1"])
    rec = {d: cuota * D["recargo"][d] / 100.0 for d in P["dif"]["orden"]}
    for i, d in enumerate(P["dif"]["orden"]):
        suma = "suma" in D["atraso"][d]
        total14 = cuota + rec[d] + (cuota if suma else 0.0)
        pesos = [total14 / x * 100 for x in sem2]
        m, ic, n = media_ic(pesos, c.S)
        tope = K["leve_max"] if d in ("novato", "intermedio") else (K["dificil_max"] if d == "dificil" else K["duro_max"])
        subs.append(cond("peso de la cuota del día 14 (%s)" % d, m, None, tope, ic, n))
    subs.append(cond("recargo de Intermedio menos 6 % de la cuota (esquirlas)", abs(round(rec["intermedio"]) - D["recargo"]["intermedio"] / 100.0 * cuota), None, 0.5, None, None, "esq"))
    return r_final(subs, {"medio": {"valor": subs[1]["valor"], "ic95": subs[1]["ic95"], "n": subs[1]["n"]}})


@regla("A7")
def A7(c, K):
    P = c.P
    r = c.acto1("rapido", mejora=True, urgente=True)
    mx = r["max_caja"] / P["deuda"]["K"] * 100
    return r_final([cond("caja máxima del Acto I frente al capital", mx, None, K["tope_pct"], None, r["n"])],
                   {"rapido": {"valor": mx, "n": r["n"]}})


# ================================================================== B · Ritmo, progresión, estatus
def _horas_acto(P, r, a):
    return r["acto"][a]["neto_hora"]


def _por_acto_ing(c, pid, via=True, n=None):
    camps = c.camps(pid, via=via, n=n)
    out = {}
    for a in ACT3:
        out[a] = [r["acto"][a]["neto_hora"] for r in camps]
    return out


@regla("B1")
def B1(c, K):
    P, S = c.P, c.S
    obj = {"I": P["ritmo"]["hora"]["I"]["medium"], "II": P["ritmo"]["hora"]["II"]["target"],
           "III": P["ritmo"]["hora"]["III"]["target"], "IV": P["ritmo"]["hora"]["IV"]["target"]}
    subs, pp = [], {}
    med = _por_acto_ing(c, "medio")
    med_g = _por_acto_ing(c, "medio", n=c.tam["semillas_ritmo"])
    a1 = c.acto1("medio")
    m, ic, n = media_ic(a1["netos"], S)
    subs.append(cond("desviación del ritmo del Acto I (medio)", pct_dev(m, obj["I"]), None, K["desv_max"], ic_dev(ic, obj["I"]), n, perfil="medio"))
    for a in ACT3:
        m, ic, n = media_ic(med_g[a], S)
        subs.append(cond("desviación del ritmo del Acto %s (medio)" % a, pct_dev(m, obj[a]), None, K["desv_max"], ic_dev(ic, obj[a]), n, perfil="medio"))
    opt = _por_acto_ing(c, "optimizador")
    lento = _por_acto_ing(c, "lento")
    rap = _por_acto_ing(c, "rapido")
    ratios = []
    for i in range(len(med["II"])):
        ratios.append(C.media([med[a][i] / opt[a][i] for a in ACT3]) * 100)
    m, ic, n = media_ic(ratios, S)
    subs.append(cond("ritmo del medio frente al optimizador", m, K["opt_min"], K["opt_max"], ic, n))
    orden = all(C.media(lento[a]) < C.media(med[a]) < C.media(rap[a]) for a in ACT3)
    subs.append(cond("orden lento < medio < rápido en II, III y IV (1 = sí)", 1.0 if orden else 0.0, 1.0, 1.0, None, None, ""))
    rl = max(C.media(rap[a]) / C.media(lento[a]) for a in ACT3)
    subs.append(cond("razón máxima rápido / lento", rl, None, K["rapido_lento_max"], None, None, "x"))
    for pid, d in (("lento", lento), ("rapido", rap), ("optimizador", opt), ("medio", med)):
        horas = {a: C.media(d[a]) for a in ACT3}
        pp[pid] = {"valor": max(pct_dev(horas[a], obj[a]) for a in ACT3), "detalle": horas}
    return r_final(subs, pp, {"objetivo": obj})


@regla("B2")
def B2(c, K):
    S = c.S
    camps = c.camps("medio")
    a1 = c.acto1("medio")
    medias = {"I": C.media(a1["netos"])}
    for a in ACT3:
        medias[a] = C.media([r["acto"][a]["neto_hora"] for r in camps])
    subs = [cond("crece I < II < III < IV (1 = sí)", 1.0 if medias["I"] < medias["II"] < medias["III"] < medias["IV"] else 0.0, 1.0, 1.0, None, None, "")]
    r12 = medias["II"] / medias["I"]
    subs.append(cond("razón I→II", r12, K["razon_min"], K["razon_12_max"], None, None, "x"))
    for a, b in (("II", "III"), ("III", "IV")):
        rr = [r2["acto"][b]["neto_hora"] / r2["acto"][a]["neto_hora"] for r2 in camps]
        m, ic, n = media_ic(rr, S)
        subs.append(cond("razón %s→%s" % (a, b), m, K["razon_min"], K["razon_max"], ic, n, "x"))
    peor = None
    for a in ACT3:
        rr = []
        for r2 in camps:
            nd = r2["neto_dia"]
            i0 = r2["inicio"][a] - r2["inicio"]["II"]
            dias = r2["dur"][a]
            q = max(1, dias // K["tramo_div"])
            ini = sum(nd[i0:i0 + q]) / q
            fin = sum(nd[i0 + dias - q:i0 + dias]) / q
            rr.append(fin / ini if ini > 0 else float("inf"))
        m, ic, n = media_ic(rr, S)
        if peor is None or m > peor[0]:
            peor = (m, ic, n, a)
    subs.append(cond("rampa fin/inicio dentro de un acto (peor: %s)" % peor[3], peor[0], None, K["rampa_max"], peor[1], peor[2], "x"))
    return r_final(subs, {"medio": {"valor": r12, "detalle": medias}})


@regla("B3")
def B3(c, K):
    P, S = c.P, c.S
    objetivos = {a: P["ritmo"]["actos"][a]["patrimonio"] for a in ACT3}
    med = c.camps("medio")
    subs, pp = [], {}
    a1 = c.acto1("medio")
    rango1 = P["ritmo"]["patrimonio_I"]
    cuota = a1["cuota"]
    pat1 = [(x - cuota) if x >= cuota else x for x in a1["cajas"]]
    m, ic, n = media_ic(pat1, S)
    subs.append(cond("patrimonio al cierre del Acto I (medio), en esquirlas", m, rango1[0], rango1[1], ic, n, "esq", "medio"))
    rap = c.acto1("rapido")
    pr = [(x - cuota) if x >= cuota else x for x in rap["cajas"]]
    m2, ic2, n2 = media_ic(pr, S)
    obj_r = P["ritmo"]["patrimonio_rapido_I"]
    subs.append(cond("patrimonio al cierre del Acto I (rápido), desviación", pct_dev(m2, obj_r), None, K["desv_max"], ic_dev(ic2, obj_r), n2, perfil="rapido"))
    for a in ACT3:
        vals = [r["pat_fin"][a] for r in med]
        m, ic, n = media_ic(vals, S)
        subs.append(cond("patrimonio al cierre del Acto %s (medio), desviación" % a, pct_dev(m, objetivos[a]), None, K["desv_max"], ic_dev(ic, objetivos[a]), n, perfil="medio"))
    cats = ("compras", "tienda_mejora", "almacen", "detector", "info", "estilo", "estilo_fijo", "licencias", "prensa", "cuotas", "extra_deuda")
    for a in ACT3:
        sm = [-sum(r["acto"][a]["f"].get(k, 0.0) for k in cats) for r in med]
        m, ic, n = media_ic(sm, S)
        obj = P["ritmo"]["sumideros"][a]
        subs.append(cond("sumideros del Acto %s frente al objetivo, desviación" % a, pct_dev(m, obj), None, K["sumideros_max"], ic_dev(ic, obj), n, "%", "medio"))
    lento = c.camps("lento")
    rr = [min(lento[i]["pat_fin"][a] / med[i]["pat_fin"][a] for a in ACT3) * 100 for i in range(len(med))]
    m, ic, n = media_ic(rr, S)
    subs.append(cond("patrimonio del lento frente al medio (peor acto)", m, K["lento_min"], None, ic, n))
    pp["medio"] = {"valor": C.media([r["pat_fin"]["IV"] for r in med]), "detalle": {a: C.media([r["pat_fin"][a] for r in med]) for a in ACT3}}
    pp["lento"] = {"valor": m, "ic95": ic, "n": n}
    return r_final(subs, pp)


@regla("B4")
def B4(c, K):
    P, S = c.P, c.S
    med = c.camps("medio", n=c.tam["semillas_ritmo"])
    subs = []
    for nombre, acto in (("comerciante", "II"), ("empresario", "III")):
        ok = [1 if nombre in r["estatus_dia"] and r["estatus_dia"][nombre] < r["inicio"][acto] + r["dur"][acto] else 0 for r in med]
        k = sum(ok)
        subs.append(cond("%s alcanzado dentro del acto" % nombre, k / len(ok) * 100, K["alcanza_min"], None,
                         [x * 100 for x in C.ic_prop(k, len(ok), S)], len(ok)))
        fr = [(r["estatus_dia"][nombre] - r["inicio"][acto]) / float(r["dur"][acto]) * 100 for r in med if nombre in r["estatus_dia"]]
        if fr:
            m, ic, n = media_ic(fr, S)
            subs.append(cond("%s: momento del acto en que se alcanza" % nombre, m, K["momento_min"], K["momento_max"], ic, n))
        else:
            subs.append(cond("%s: momento del acto en que se alcanza" % nombre, None, K["momento_min"], K["momento_max"]))
    ok = [1 if "magnate" in r["estatus_dia"] and r["estatus_dia"]["magnate"] <= r["fin"] else 0 for r in med]
    k = sum(ok)
    subs.append(cond("Magnate alcanzado antes del cierre del Acto IV", k / len(ok) * 100, K["magnate_min"], None,
                     [x * 100 for x in C.ic_prop(k, len(ok), S)], len(ok)))
    return r_final(subs, {"medio": {"valor": subs[0]["valor"]}})


@regla("B5")
def B5(c, K):
    P, S = c.P, c.S
    camps = c.camps("optimizador", n=c.tam["semillas_tasas"])
    subs = []
    for a in ("II", "III"):
        techo = max(P["herr"]["niveles_acto"][a]) + K["margen_techo"]
        ok = [1 if r["nivel_pico"][a] <= techo else 0 for r in camps]
        k = sum(ok)
        subs.append(cond("corridas con el nivel de pico ≤ %d al cerrar el Acto %s" % (techo, a), k / len(ok) * 100, K["bajo_techo_min"], None,
                         [x * 100 for x in C.ic_prop(k, len(ok), S)], len(ok), perfil="optimizador"))
    return r_final(subs, {"optimizador": {"valor": min(s["valor"] for s in subs)}})


def _ratio_acto(r, a, num, den):
    f = r["acto"][a]["f"]
    return -f.get(num, 0.0), den


@regla("B6")
def B6(c, K):
    P, S = c.P, c.S
    camps = c.camps("medio", n=c.tam["semillas_ritmo"])
    subs = []
    dias_mes = P["t"]["mes"]

    def mensual(r, a):
        ing = r["acto"][a]["neto"] / r["acto"][a]["dias"] * dias_mes
        return ing

    def por_mes(r, a, cat):
        f = r["acto"][a]["f"]
        return -f.get(cat, 0.0) / r["acto"][a]["dias"] * dias_mes

    pr = [por_mes(r, "II", "prensa") / mensual(r, "II") * 100 for r in camps]
    m, ic, n = media_ic(pr, S)
    subs.append(cond("prensa sobre el ingreso mensual (Acto II)", m, K["prensa_min"], K["prensa_max"], ic, n))
    escalon = {"II": "comerciante", "III": "empresario", "IV": "magnate"}
    for a in ACT3:
        li = [P["mk"]["licencias"][escalon[a]] / mensual(r, a) * 100 for r in camps]
        m, ic, n = media_ic(li, S)
        subs.append(cond("licencia del escalón del acto (%s) sobre el ingreso mensual (Acto %s)" % (escalon[a], a), m, K["lic_min"], K["lic_max"], ic, n))
    for a, lo, hi in (("II", K["viaje_II_min"], K["viaje_II_max"]), ("IV", K["viaje_IV_min"], K["viaje_IV_max"])):
        vv = []
        for r in camps:
            ca = r["acto"][a]["c"]
            f = r["acto"][a]["f"]
            if ca["bruto"] > 0:
                vv.append(-f.get("viaje", 0.0) / ca["bruto"] * 100)
        m, ic, n = media_ic(vv, S)
        subs.append(cond("viaje sobre el valor bruto de las expediciones (Acto %s)" % a, m, lo, hi, ic, n))
    for a in ACT3:
        rp = []
        for r in camps:
            ca = r["acto"][a]["c"]
            f = r["acto"][a]["f"]
            if ca["bruto"] > 0:
                rp.append(-f.get("desgaste", 0.0) / ca["bruto"] * 100)
        m, ic, n = media_ic(rp, S)
        subs.append(cond("reparación sobre el valor bruto (Acto %s)" % a, m, K["rep_min"], K["rep_max"], ic, n))
    for a in ("III", "IV"):
        rr = [(-r["acto"][a]["f"].get("renta", 0.0) / r["acto"][a]["dias"] * dias_mes) / mensual(r, a) * 100 for r in camps]
        m, ic, n = media_ic(rr, S)
        subs.append(cond("renta del almacén sobre el ingreso mensual (Acto %s)" % a, m, None, K["renta_max"], ic, n))
    return r_final(subs, {"medio": {"valor": subs[0]["valor"]}})


@regla("B7")
def B7(c, K):
    P, S = c.P, c.S
    n_largas = min(c.tam["semillas_largas"], len(c.semillas))
    largas = []
    for sem in c.semillas[:n_largas]:
        cam = c.memo(("larga", sem, c.tam["dias_largo"]), lambda s=sem: C.Campana(P, S, "medio", s, dias_extra=c.tam["dias_largo"]).correr())
        largas.append(cam)
    crec, ident, techo = [], [], []
    for cam in largas:
        nd = cam.neto_dia
        total = len(nd)
        a0 = int(total * K["ventana_a"][0] / 100.0)
        a1 = int(total * K["ventana_a"][1] / 100.0)
        b0 = int(total * K["ventana_b"][0] / 100.0)
        b1 = int(total * K["ventana_b"][1] / 100.0)
        ia = C.media(nd[a0:a1])
        ib = C.media(nd[b0:b1])
        crec.append((ib / ia - 1) * 100 if ia > 0 else float("inf"))
        p = cam.p
        suma = sum(p.f.values())
        ident.append(abs((p.cash - cam.cash_inicial) - suma))
        # techo físico: 3 bloques con el mejor valor por bloque posible (nivel 5, riqueza 100 %, sin impacto)
        p2 = C.Partida(P, S, 1, C.perfil_de(P, S, "medio"), C.cfg_etapa(P, S, "IV", patrimonio_fijo=1.0))
        p2.mk.nuevo_dia(1)
        p2.mk.paso()
        mejor = 0.0
        for z in P["zonas"]:
            pl = p2.plan_zona(z, P["mk"]["w_min"], 1.0)
            if pl:
                mejor = max(mejor, pl["valor"] / P["Z"][z]["bloques"])
        tope = P["t"]["bloques_dia"] * mejor * K["techo_holgura"]
        w7 = P["t"]["semana"]
        movil = max(sum(nd[i:i + w7]) / w7 for i in range(b0, max(b0 + 1, b1 - w7)))
        techo.append(movil / tope * 100)
    m, ic, n = media_ic(crec, S)
    subs = [cond("crecimiento del ingreso diario entre las dos ventanas", m, None, K["crec_max"], ic, n),
            cond("identidad contable (diferencia máxima en esquirlas)", max(ident), None, K["ident_max"], None, len(ident), "esq"),
            cond("ingreso semanal máximo frente al techo físico", max(techo), None, 100.0, None, len(techo))]
    return r_final(subs, {"medio": {"valor": m, "ic95": ic, "n": n}}, {"dias": c.tam["dias_largo"]})


@regla("B8")
def B8(c, K):
    P, S = c.P, c.S
    objetivos = {"IIe": P["ritmo"]["hora"]["II"]["start"], "II": P["ritmo"]["hora"]["II"]["end"],
                 "III": P["ritmo"]["hora"]["III"]["attentive"], "IV": P["ritmo"]["hora"]["IV"]["attentive"]}
    dph = per_hour(P)
    subs = []
    for eid, obj in objetivos.items():
        res = c.etapa(eid, "medio", dias=S["prototipo"]["dias"], cal=0, proto=True, perfil_proto=True)
        vals = [r["neto_dia"] * dph for r in res]
        m, ic, n = media_ic(vals, S)
        subs.append(cond("prototipo %s frente a %d esq/h" % (eid, obj), pct_dev(m, obj), None, K["desv_max"], ic_dev(ic, obj), n))
    return r_final(subs, {"medio": {"valor": max(s["valor"] for s in subs)}})


# ================================================================== C · Herramientas
def eid_de_nivel(P, S, k):
    """Etapa del prototipo cuyo nivel de herramienta es k (la del acto en que se compra esa mejora)."""
    for eid, e in S["prototipo"]["etapas"].items():
        if C.nivel_etapa(P, e["nivel"]) == k:
            return eid
    return None


def valores_por_zona(c, eid, niveles, **kw):
    """Valor esperado por bloque de la expedición a cada zona accesible con esos niveles (mercado neutro, riqueza 100 %)."""
    P, S = c.P, c.S
    cfg = C.cfg_etapa(P, S, eid, **kw)
    cfg["niveles"] = dict(niveles)
    p = C.Partida(P, S, 1, C.perfil_de(P, S, "medio"), cfg)
    w = p.w()
    out = {}
    for z in P["zonas"]:
        if not p.zona_acceso(z):
            continue
        pl = p.plan_zona(z, w, 1.0)
        out[z] = pl["ev"] / P["Z"][z]["bloques"] if pl else 0.0
    return out


def mejor_bloque(c, eid, niveles, **kw):
    return max(valores_por_zona(c, eid, niveles, **kw).values())


@regla("C1")
def C1(c, K):
    P, S = c.P, c.S
    propios, comprados = [], []
    for t in P["herr"]["tipos"]:
        for k in range(2, len(P["herr"]["niveles"]) + 1):
            eid = eid_de_nivel(P, S, k)
            base = {x: k - 1 for x in P["herr"]["tipos"]}
            nuevo = dict(base)
            nuevo[t] = k
            v_nuevo = valores_por_zona(c, eid, nuevo)
            v_base = valores_por_zona(c, eid, base)
            ganancia = max(v_nuevo[z] - v_base[z] for z in v_nuevo)
            money = float(P["herr"]["costo"][t][str(k)])
            req = P["herr"]["minerales"][t][str(k)]
            mat = req["qty"] * P["M"][req["mineral"]]["precio"]
            if ganancia <= 0:
                propios.append(float("inf"))
                comprados.append(float("inf"))
            else:
                propios.append((money + mat) / ganancia)
                comprados.append((money + mat * P["herr"]["mercado"]) / ganancia)
    if K.get("modo") == "mejor_por_nivel":
        n_tipos = len(P["herr"]["tipos"])
        nl = len(P["herr"]["niveles"]) - 1
        por_nivel_p = [min(propios[j + t * nl] for t in range(n_tipos)) for j in range(nl)]
        por_nivel_c = [min(comprados[j + t * nl] for t in range(n_tipos)) for j in range(nl)]
        propios, comprados = por_nivel_p, por_nivel_c
    subs = [cond("expediciones para pagar la mejora más rápida", min(propios), K["exp_min"], None, None, len(propios), "exp"),
            cond("expediciones para pagar la mejora más lenta (mineral propio)", max(propios), None, K["exp_max"], None, len(propios), "exp"),
            cond("expediciones para pagar la mejora más lenta (mineral comprado)", max(comprados), None, K["exp_max"], None, len(comprados), "exp")]
    return r_final(subs, {}, {"propios": [round(x, 2) if x != float("inf") else None for x in propios]})


@regla("C2")
def C2(c, K):
    P, S = c.P, c.S
    orden = list(S["prototipo"]["etapas"].keys())
    ingreso_h = {}
    for eid in orden:
        res = c.etapa(eid, "medio")
        ingreso_h[eid] = C.media([r["neto_dia"] for r in res]) * per_hour(P)
    ingreso_h["I"] = C.media(c.acto1("medio")["netos"])
    horas = []
    for t in P["herr"]["tipos"]:
        for k in range(2, len(P["herr"]["niveles"]) + 1):
            eid = eid_de_nivel(P, S, k)
            previo = "I" if orden.index(eid) == 0 else orden[orden.index(eid) - 1]
            req = P["herr"]["minerales"][t][str(k)]
            costo = P["herr"]["costo"][t][str(k)] + req["qty"] * P["M"][req["mineral"]]["precio"]
            horas.append((costo / ingreso_h[previo], t, k))
    lo = min(horas)
    hi = max(horas)
    subs = [cond("horas de ingreso para pagar la mejora más barata (%s a nivel %d)" % (lo[1], lo[2]), lo[0], K["horas_min"], None, None, len(horas), "h"),
            cond("horas de ingreso para pagar la mejora más cara (%s a nivel %d)" % (hi[1], hi[2]), hi[0], None, K["horas_max"], None, len(horas), "h")]
    return r_final(subs, {"medio": {"valor": hi[0]}})


@regla("C3")
def C3(c, K):
    S = c.S
    camps = c.camps("medio")
    subs = []
    for a in ACT3:
        vals = []
        for r in camps:
            ca = r["acto"][a]["c"]
            if ca["bruto"] > 0:
                vals.append(-r["acto"][a]["f"].get("desgaste", 0.0) / ca["bruto"] * 100)
        m, ic, n = media_ic(vals, S)
        subs.append(cond("reparación sobre el valor bruto de la expedición (Acto %s)" % a, m, K["rep_min"], K["rep_max"], ic, n))
    return r_final(subs, {"medio": {"valor": subs[0]["valor"]}})


@regla("C4")
def C4(c, K):
    P = c.P
    bono = P["herr"]["expl_bono"]
    rows = []
    por_perfil = {}
    for clave, pr in P["exp"]["probs"].items():
        b = 0.0
        for p_, r in zip(pr, P["resultados"]):
            b += p_ / 100.0 * (bono[r] if bono[r] is not None else -100.0)
        por_perfil[clave] = b
    subs = []
    for clave, tope in (("medio", K["medio_max"]), ("rapido", K["rapido_max"])):
        peor = None
        for pot in P["herr"]["expl_potencias"]:
            ms = [m for m in P["min"] if P["M"][m]["tier"] == pot["for_tier"]]
            if not ms:
                continue
            valor_mena = C.media([P["M"][m]["rend"] * P["M"][m]["precio"] for m in ms])
            neto = por_perfil[clave] - pot["cost"] / valor_mena * 100.0
            if peor is None or neto > peor[0]:
                peor = (neto, pot["power"])
        subs.append(cond("rendimiento neto del explosivo, perfil %s (peor: potencia %d)" % (clave, peor[1]), peor[0], None, tope, None, None, "%", clave))
    return r_final(subs, {k: {"valor": v} for k, v in por_perfil.items()})


@regla("C5")
def C5(c, K):
    S = c.S
    dph = per_hour(c.P)
    dc = c.P["exp"]["descarte_pct"] / 100.0
    base = {}
    for etiqueta, v in (("0", 0.0), ("25", dc), ("50", dc * 2)):
        res = c.etapa("III", "optimizador", descarte=v)
        base[etiqueta] = res
    pares = [1 - b["neto_dia"] / a["neto_dia"] for a, b in zip(base["0"], base["25"])]
    m, ic, n = media_ic([x * 100 for x in pares], S)
    pares2 = [1 - b["neto_dia"] / a["neto_dia"] for a, b in zip(base["25"], base["50"])]
    m2, ic2, n2 = media_ic([x * 100 for x in pares2], S)
    desc = [r["cont"]["descartes"] / max(1, r["cont"]["descartes"] + r["cont"]["menas"]) * 100 for r in base["25"]]
    m3, ic3, n3 = media_ic(desc, S)
    subs = [cond("pérdida de ingreso de descartar a coste normal frente a descartar gratis", m, K["perdida_min"], K["perdida_max"], ic, n),
            cond("pérdida adicional al doblar el costo de descartar", m2, K["doble_min"], None, ic2, n2),
            cond("mena descartada sobre las escaneadas (coste normal)", m3, None, K["descartes_max"], ic3, n3)]
    return r_final(subs, {"optimizador": {"valor": m, "ic95": ic, "n": n}},
                   {"ingreso_h": {k: C.media([r["neto_dia"] for r in v]) * dph for k, v in base.items()}})


# ================================================================== D · Zonas
def cfg_celda(c, eid, nivel, energia, **kw):
    P, S = c.P, c.S
    cfg = C.cfg_etapa(P, S, eid, **kw)
    cfg["niveles"] = {t: nivel for t in P["herr"]["tipos"]}
    cfg["energia"] = (lambda p, e=float(energia): e)
    return cfg


def celdas_d1(c):
    """Cuadrícula nivel × Aguante de cada acto: (acto, nivel, energía)."""
    P = c.P
    out = []
    orden = P["actos"]
    for a in ACT3:
        niveles = P["herr"]["niveles_acto"][a]
        e_prev = P["energia"]["por_acto"][orden[orden.index(a) - 1]]
        e_prev = e_prev[1] if isinstance(e_prev, list) else e_prev
        e_fin = P["energia"]["por_acto"][a]
        e_fin = e_fin[1] if isinstance(e_fin, list) else e_fin
        if c.tam["d1_celdas"] == "alta":
            out.append((a, niveles[1], e_fin))
        else:
            for nv in niveles:
                for e in (e_prev, e_fin):
                    out.append((a, nv, e))
    return out


def _d1_sets(c):
    def f():
        P, S = c.P, c.S
        sem = c.semillas[: c.tam["d1_semillas"]]
        dias, cal = c.tam["d1_dias"], S["estadistica"]["calentamiento_dias"]
        res = {}
        for (a, nv, e) in celdas_d1(c):
            zonas = [z for z in P["zonas"] if P["actos"].index(P["Z"][z]["acto"]) <= P["actos"].index(a)]
            alta = (nv == P["herr"]["niveles_acto"][a][1])
            pids = PERFILES if (alta and c.tam["d1_perfiles"] == "todos") else ("medio",)
            for pid in pids:
                clave = (a, nv, e, pid)
                adapt = [C.correr_etapa(P, S, cfg_celda(c, a, nv, e), c.perfil(pid), s, dias, cal) for s in sem]
                fijas = {}
                for z in zonas:
                    fijas[z] = [C.correr_etapa(P, S, cfg_celda(c, a, nv, e, fija=z), c.perfil(pid), s, dias, cal) for s in sem]
                res[clave] = (adapt, fijas)
        return res
    return c.memo(("d1", c.modo, c.tam["d1_celdas"], c.tam["d1_semillas"], c.tam["d1_dias"]), f)


@regla("D1")
def D1(c, K):
    P, S = c.P, c.S
    sets = _d1_sets(c)
    peor_share = (0.0, None)
    peor_fija = (0.0, None, None)
    min_zonas = None
    for clave, (adapt, fijas) in sets.items():
        a = clave[0]
        tot = {z: sum(r["zonas"][z] for r in adapt) for z in P["zonas"]}
        n_exp = sum(tot.values())
        if n_exp <= 0:
            continue
        shares = {z: v / n_exp * 100 for z, v in tot.items()}
        z_top = max(shares, key=shares.get)
        if shares[z_top] > peor_share[0]:
            peor_share = (shares[z_top], clave)
        if clave[3] == "medio":
            nz = sum(1 for v in shares.values() if v >= K["uso_min"])
            if min_zonas is None or nz < min_zonas[0]:
                min_zonas = (nz, clave)
        for z, rs in fijas.items():
            rat = [rs[i]["neto_dia"] / adapt[i]["neto_dia"] * 100 for i in range(len(adapt))]
            m, ic, n = media_ic(rat, S)
            if m > peor_fija[0]:
                peor_fija = (m, (ic, n), (clave, z))
    subs = [cond("mejor zona: parte de las expediciones de la política adaptativa", peor_share[0], None, K["zona_max"], None, len(sets), "%"),
            cond("mejor zona fija frente a la adaptativa (peor caso)", peor_fija[0], None, K["fija_max"], peor_fija[1][0] if peor_fija[1] else None,
                 peor_fija[1][1] if peor_fija[1] else None),
            cond("zonas con uso ≥ %d %% (mínimo de los actos)" % K["uso_min"], min_zonas[0] if min_zonas else 0, K["zonas_min"], None, None, None, "zonas")]
    detalle = {}
    for clave, (adapt, fijas) in sets.items():
        if True:
            tot = {z: sum(r["zonas"][z] for r in adapt) for z in P["zonas"]}
            n_exp = max(1, sum(tot.values()))
            detalle["%s/%s/%s/%s" % clave] = {z: round(v / n_exp * 100, 1) for z, v in tot.items() if v}
    return r_final(subs, {"medio": {"valor": peor_share[0]}}, {"reparto": detalle})


@regla("D2")
def D2(c, K):
    S, P = c.S, c.P
    subs = []
    for a in ACT3:
        res = c.etapa(a, "medio")
        vals = [r["cont"]["rich_sum"] / r["cont"]["rich_n"] for r in res if r["cont"]["rich_n"]]
        m, ic, n = media_ic(vals, S)
        obj = P["exp"]["rico_salida"][a]
        subs.append(cond("riqueza media al salir, desviación frente al objetivo (Acto %s)" % a, abs(m - obj), None, K["pp_max"], [abs(x - obj) if x is not None else None for x in (ic or [None, None])], n, "pp"))
    sets = _d1_sets(c)
    perdidas = []
    for clave, (adapt, fijas) in sets.items():
        if clave[3] != "medio":
            continue
        if fijas:
            mejor = max(C.media([r["neto_dia"] for r in rs]) for rs in fijas.values())
            perdidas.append((100 - mejor / C.media([r["neto_dia"] for r in adapt]) * 100, clave[0]))
    if perdidas:
        # la menor pérdida entre actos de quien repite la mejor zona fija
        porac = {}
        for v, a in perdidas:
            porac.setdefault(a, []).append(v)
        peor = min(C.media(v) for v in porac.values())
        subs.append(cond("pérdida de quien repite una sola zona (acto con menor pérdida)", peor, K["perdida_min"], None, None, len(perdidas)))
    return r_final(subs, {"medio": {"valor": subs[0]["valor"]}})


@regla("D3")
def D3(c, K):
    S = c.S
    res = c.etapa("IV", "medio")
    mx = max(r["max_fosa_semana"] for r in res)
    porc = []
    for r in res:
        total = sum(r["flujo"].get(k, 0.0) for k in ("v_spot", "v_tienda", "v_pedidos", "v_negro", "v_legal", "v_especial"))
        porc.append((r["flujo"].get("v_legal", 0.0) + r["flujo"].get("v_especial", 0.0)) / total * 100 if total > 0 else 0.0)
    m, ic, n = media_ic(porc, S)
    subs = [cond("expediciones a La Fosa en una semana (máximo)", mx, None, K["fosa_semana_max"], None, len(res), "exp"),
            cond("parte de la Aetherita en las ventas del Acto IV", m, None, K["aeth_max"], ic, n)]
    return r_final(subs, {"medio": {"valor": m, "ic95": ic, "n": n}})


# ================================================================== E · Mercado y bucles
def mercado_neutro(c, acto, ruido=None, semilla=1, **kw):
    mk = MercadoRef(c.P, Azar(semilla), ruido or c.S["ruido"], acto=acto, **kw)
    mk.caida_max = c.S["mercado"]["caida_max_pct"]
    return mk


def valor_bloque(c, acto):
    res = c.etapa(acto, "medio")
    return C.media([r["neto_dia"] for r in res]) / c.P["t"]["bloques_dia"]


def mejor_tanda(mk, m, comprar, vender, w, tope_q, grilla):
    """Mejor ganancia (en esquirlas) de comprar por `comprar` y vender por `vender` una tanda de hasta tope_q unidades."""
    mejor = -float("inf")
    for f in grilla:
        q = tope_q * f
        if q <= 0:
            continue
        pres, vend = mk.presion[m], mk.vendido[m]
        costo = mk.comprar(m, q, w, comprar)
        ing = mk.precio_venta(m, q, w, vender) * q
        mk.presion[m], mk.vendido[m] = pres, vend
        mejor = max(mejor, ing - costo)
    return mejor


@regla("E1")
def E1(c, K):
    P, S = c.P, c.S
    propia = P["mk"]["tienda"]["propia"] and P["pedidos"]["propia"]
    grilla = S["politica"]["e1_grilla"]
    V = P["vig"]
    mejor_seguro = (-float("inf"), None)
    mejor_negro = (-float("inf"), None)
    noche = (0.0, None)
    for a in ACT3:
        mk = mercado_neutro(c, a, sueltos=False, tope_diario=False)
        w = P["mk"]["w_acto"][a]
        bloque = valor_bloque(c, a)
        dia = bloque * P["t"]["bloques_dia"]
        nivel_tienda = S["prototipo"]["etapas"][a]["tienda"]
        con_bolsa = P["actos"].index(a) >= P["actos"].index(P["mk"]["bolsa"]["acto"])
        for m in P["min"]:
            if m == "aetherita":
                continue
            cap = P["M"][m]["comprador"] * P["mk"]["compradores"][a]
            compras = ["spot", "marketplace"] + (["bolsa"] if con_bolsa else [])
            ventas = ["spot", "bolsa"] if con_bolsa else ["spot"]
            if not propia:
                ventas = ventas + ["tienda"]
            for cb in compras:
                for vb in ventas:
                    tope = P["tienda"][nivel_tienda]["unidades"] if vb == "tienda" else cap
                    g = mejor_tanda(mk, m, cb, vb, w, tope, grilla)
                    ratio = g / bloque * 100 if bloque > 0 else 0.0
                    if ratio > mejor_seguro[0]:
                        mejor_seguro = (ratio, (a, m, cb, vb))
                # hacia el negro: la vigilancia limita cuántas noches se pueden hacer (la bajada natural entre lo que sube cada noche)
                lote_max = V["tope_noche"][a] / P["M"][m]["precio"]
                for f in grilla:
                    q = lote_max * f
                    pres, vend = mk.presion[m], mk.vendido[m]
                    costo = mk.comprar(m, q, w, cb)
                    ing = mk.precio_venta(m, q, w, "negro") * q
                    mk.presion[m], mk.vendido[m] = pres, vend
                    g = ing - costo
                    dv = min(max(V["op_base"] + V["op_span"] * f, V["op_min"]), V["op_max"])
                    por_dia = g * V["decae"] / dv
                    r_dia = por_dia / dia * 100 if dia > 0 else 0.0
                    if r_dia > mejor_negro[0]:
                        mejor_negro = (r_dia, (a, m, cb, f))
                    if g / bloque * 100 > noche[0]:
                        noche = (g / bloque * 100, (a, m, cb, f))
    subs = [cond("mayor ganancia de comprar y revender sin pasar por el mercado negro (% de un bloque)", mejor_seguro[0], None, 0.0, None, None, "% bloque"),
            cond("mayor ganancia diaria sostenible de comprar para vender en negro (% del ingreso diario)", max(mejor_negro[0], 0.0), None, K["negro_max"], None, None, "% del día")]
    return r_final(subs, {}, {"seguro": mejor_seguro[1], "negro": mejor_negro[1], "noche_negra_en_bloques": noche[0] / 100.0,
                              "tienda_y_pedidos_solo_propia": bool(propia)})


@regla("E2")
def E2(c, K):
    P, S = c.P, c.S
    k = P["mk"]
    w = lambda x: min(k["w_min"] + k["w_span"] * x / (x + k["w_mitad"]), k["w_max"])
    grilla = K["grilla_patrimonio"]
    ws = [w(x) for x in grilla]
    mono = all(b > a for a, b in zip(ws, ws[1:]))
    rango = (ws[0], ws[-1])
    subs = [cond("w(P) estrictamente creciente (1 = sí)", 1.0 if mono else 0.0, 1.0, 1.0, None, None, ""),
            cond("w en patrimonio 0 menos w mínimo", abs(ws[0] - k["w_min"]), None, 1e-9, None, None, ""),
            cond("w máximo alcanzable frente al tope", rango[1] / k["w_max"] * 100, None, 100.0, None, None)]
    camps = c.camps("medio")
    razon = {}
    for a in ACT3:
        # coste de la profundidad del mercado si todo se vende al spot (la tienda no tiene slippage)
        res = c.etapa(a, "medio", tienda_activa=False)
        vals = [r["cont"]["slip"] / r["cont"]["bruto"] * 100 for r in res if r["cont"]["bruto"] > 0]
        razon[a] = media_ic(vals, S)
    r23 = razon["III"][0] / razon["II"][0] if razon["II"][0] > 0 else float("inf")
    r34 = razon["IV"][0] / razon["III"][0] if razon["III"][0] > 0 else float("inf")
    subs.append(cond("razón mínima del coste de slippage entre actos consecutivos (crece o se mantiene)", min(r23, r34), K["razon_min"], None, None, None, "x"))
    m, ic, n = razon["IV"]
    subs.append(cond("coste de slippage sobre el ingreso bruto vendiendo todo al spot (Acto IV)", m, None, K["slip_IV_max"], ic, n))
    for a in ACT3:
        devs = []
        for r in camps:
            serie = [p for d, p in r["pat_serie"] if r["inicio"][a] <= d < r["inicio"][a] + r["dur"][a]]
            if serie:
                devs.append(w(C.media(serie)))
        m, ic, n = media_ic(devs, S)
        subs.append(cond("w del acto frente al w del patrimonio medio (Acto %s)" % a, pct_dev(k["w_acto"][a], m), None, K["w_acto_max"],
                         ic_dev(ic, k["w_acto"][a]) if False else [pct_dev(k["w_acto"][a], x) for x in ic] if ic[0] is not None else None, n))
    return r_final(subs, {"medio": {"valor": razon["IV"][0]}})


def _tanda_simple(mk, m, w, q):
    pres, vend = mk.presion[m], mk.vendido[m]
    ing = mk.vender(m, q, w, "spot")
    costo = mk.comprar(m, q, w, "spot")
    mk.presion[m], mk.vendido[m] = pres, vend
    return (ing - costo) / costo * 100


@regla("E3")
def E3(c, K):
    P, S = c.P, c.S
    n = c.tam["e3_pruebas"]
    mks = {a: mercado_neutro(c, a, semilla=C.semilla_flujo(S, "e3"), sueltos=True) for a in ACT3}
    az = Azar(C.semilla_flujo(S, "e3_azar"))
    esperas = S["politica"]["e3_esperas"]
    mins = [m for m in P["min"] if m != "aetherita"]
    acum = {}
    for i in range(n):
        a = ACT3[i % len(ACT3)]
        mk = mks[a]
        for _ in range(S["politica"]["e3_salto"]):
            mk.paso()
        m = mins[int(az.u() * len(mins))]
        cap = P["M"][m]["comprador"] * P["mk"]["compradores"][a]
        q = cap * S["politica"]["e3_fracciones"][int(az.u() * len(S["politica"]["e3_fracciones"]))]
        w = P["mk"]["w_acto"][a]
        k = esperas[int(az.u() * len(esperas))]
        if k == 0:
            g = _tanda_simple(mk, m, w, q)
        else:
            pres, vend = mk.presion[m], mk.vendido[m]
            costo = mk.comprar(m, q, w, "spot")
            for _ in range(k):
                mk.paso()
            ing = mk.vender(m, q, w, "spot")
            mk.presion[m], mk.vendido[m] = 0.0, 0.0
            g = (ing - costo) / costo * 100
        acum.setdefault((a, k), []).append(g)
    peor = None
    for clave, v in acum.items():
        if len(v) < S["estadistica"]["min_muestra"]:
            continue
        m_, ic, n_ = media_ic(v, S)
        if peor is None or m_ > peor[0]:
            peor = (m_, ic, n_, clave)
    subs = [cond("mayor ganancia media de un bucle de impacto (acto %s, espera %d bloques)" % peor[3], peor[0], None, -1e-9, peor[1], peor[2])]
    return r_final(subs, {})


def _especulacion(c, canal, dias):
    """Rendimiento neto por operación de comprar con aviso perfecto de un evento y vender después."""
    P, S = c.P, c.S
    mk = mercado_neutro(c, "II", semilla=C.semilla_flujo(S, "e4"), sueltos=True)
    cierres, nuevos = [], []
    for d in range(1, dias + 1):
        antes = dict(mk.eventos)
        mk.nuevo_dia(d)
        nuevos.append({m: mk.eventos[m] - antes[m] * (1.0 - P["mk"]["decae"]) for m in P["min"]})
        for _ in range(P["t"]["bloques_dia"]):
            mk.paso()
        cierres.append(dict(mk.cur))
    return mk, cierres, nuevos


@regla("E4")
def E4(c, K):
    P, S = c.P, c.S
    dias = c.tam["dias_especulacion"]
    mk, cierres, nuevos = c.memo(("esp", dias), lambda: _especulacion(c, "spot", dias))
    w = P["mk"]["w_acto"]["II"]
    res = {}
    for canal in ("spot", "bolsa"):
        for umbral in K["umbrales"]:
            for espera in K["esperas"]:
                v = []
                for d in range(2, dias - espera - 1):
                    for m in P["min"]:
                        if m == "aetherita" or nuevos[d][m] < umbral:
                            continue
                        q = P["M"][m]["comprador"]
                        pres = mk.presion[m]
                        guardado = mk.cur[m]
                        mk.cur[m] = cierres[d - 1][m]
                        costo = mk.precio_compra(m, q, w, canal)
                        mk.cur[m] = cierres[d + espera][m]
                        ing = mk.precio_venta(m, q, w, canal)
                        mk.cur[m] = guardado
                        mk.presion[m] = pres
                        guarda = (espera + 1) * P["M"][m]["precio"] * P["M"][m]["guardar"] / 100.0
                        v.append((ing - guarda - costo) / costo * 100)
                if len(v) > S["estadistica"]["min_muestra"]:
                    res[(canal, umbral, espera)] = media_ic(v, S)
    subs = []
    for canal, tope in (("spot", K["spot_max"]), ("bolsa", K["bolsa_max"])):
        cand = [(v[0], v[1], v[2], k) for k, v in res.items() if k[0] == canal]
        peor = max(cand, key=lambda x: x[0])
        subs.append(cond("mejor rendimiento neto de especular con aviso perfecto (%s; evento ≥ %d, espera %d)" % (canal, peor[3][1], peor[3][2]),
                         peor[0], None, tope, peor[1], peor[2]))
    # estacional: comprar en el valle y vender en el pico
    mejor = (-float("inf"), None)
    mk2 = mercado_neutro(c, "II", sueltos=False, tope_diario=False)
    for m in P["min"]:
        if m == "aetherita":
            continue
        for d0 in range(1, P["t"]["anio"] + 1):
            for esp in K["esperas_estacion"]:
                mk2.dia = d0
                comp = mk2.justo(m) * (1.0 + mk2.M[m]["spread"] / 200.0)
                mk2.dia = d0 + esp
                vend = mk2.justo(m) * (1.0 - mk2.M[m]["spread"] / 200.0) * (1.0 - P["mk"]["impuesto"] / 100.0)
                guarda = esp * P["M"][m]["precio"] * P["M"][m]["guardar"] / 100.0
                g = (vend - guarda - comp) / comp * 100
                if g > mejor[0]:
                    mejor = (g, (m, d0, esp))
    subs.append(cond("mejor rendimiento neto de especular con la estación (%s, espera %d días)" % (mejor[1][0], mejor[1][2]), mejor[0], None, K["estacion_max"], None, None))
    # trader puro frente al ingreso minero
    trader = 0.0
    for a in ACT3:
        capital = P["ritmo"]["actos"][a]["patrimonio"] / 2.0
        canal = "bolsa" if P["actos"].index(a) >= P["actos"].index(P["mk"]["bolsa"]["acto"]) else "spot"
        wa = P["mk"]["w_acto"][a]
        ing_dia = 0.0
        prom = valor_bloque(c, a) * P["t"]["bloques_dia"]
        eventos = 0
        for m in P["min"]:
            if m == "aetherita":
                continue
            ev = sum(1 for d in range(dias) if nuevos[d][m] >= K["umbrales"][0]) / float(dias)
            q = P["M"][m]["comprador"] * P["mk"]["compradores"][a]
            q = min(q, capital / 2.0 / P["M"][m]["precio"])
            mk2.acto = a
            costo = mk2.precio_compra(m, q, wa, canal) * q
            ing = mk2.precio_venta(m, q, wa, canal) * q
            ing_dia += ev * max(0.0, ing - costo)
        trader = max(trader, ing_dia / prom * 100 if prom > 0 else 0.0)
    subs.append(cond("ingreso de un trader puro frente al ingreso minero (peor acto)", trader, None, K["trader_max"], None, None))
    return r_final(subs, {})


@regla("E5")
def E5(c, K):
    P, S = c.P, c.S
    dias = c.tam["dias_volatilidad"]
    nb = S["politica"]["vol_bloques"]

    def f():
        mk = mercado_neutro(c, "II", semilla=C.semilla_flujo(S, "e5"), sueltos=True)
        cambios = {m: [] for m in P["min"]}
        tope = {m: 0 for m in P["min"]}
        for d in range(1, dias + 1):
            mk.nuevo_dia(d)
            o = dict(mk.cur)
            for _ in range(P["t"]["bloques_dia"]):
                mk.paso()
            for m in P["min"]:
                ch = (mk.cur[m] / o[m] - 1) * 100
                cambios[m].append(ch)
                if abs(ch) >= P["M"][m]["tope"] - K["eps_tope"]:
                    tope[m] += 1
        return cambios, tope
    cambios, tope = c.memo(("vol", dias), f)
    peor = (0.0, None, None)
    medidas = {}
    for m in P["min"]:
        trozos = [statistics.pstdev(cambios[m][i:i + dias // nb]) for i in range(0, dias - dias // nb + 1, dias // nb)]
        dm = statistics.pstdev(cambios[m])
        ic = [dm - S["estadistica"]["z95"] * statistics.pstdev(trozos) / len(trozos) ** 0.5, dm + S["estadistica"]["z95"] * statistics.pstdev(trozos) / len(trozos) ** 0.5]
        obj = P["M"][m]["vol"]
        medidas[m] = dm
        d = pct_dev(dm, obj)
        if d >= peor[0]:
            peor = (d, [pct_dev(x, obj) for x in ic], m)
    orden_ok = True
    ids = list(P["min"])
    for i in ids:
        for j in ids:
            if P["M"][i]["vol"] > P["M"][j]["vol"] * (1 + K["desv_max"] / 100.0) and not medidas[i] > medidas[j]:
                orden_ok = False
    dt = max(tope[m] / dias * 100 for m in P["min"])
    subs = [cond("mayor desviación de la volatilidad diaria frente a la objetivo (%s)" % peor[2], peor[0], None, K["desv_max"], [min(peor[1]), max(peor[1])], nb),
            cond("orden de volatilidad entre minerales respetado (1 = sí)", 1.0 if orden_ok else 0.0, 1.0, 1.0, None, None, ""),
            cond("días en el tope diario (peor mineral)", dt, None, K["tope_max"], None, dias)]
    return r_final(subs, {}, {"desv_diaria": {m: round(v, S["estadistica"]["decimales"]) for m, v in medidas.items()}})


@regla("E6")
def E6(c, K):
    P, S = c.P, c.S
    subs = []
    for a in ("III", "IV"):
        con = c.etapa(a, "medio")
        sin = c.etapa(a, "medio", buyer_cap=False, almacen_activo=False)
        d = [(x["neto_dia"] / y["neto_dia"] - 1) * 100 for x, y in zip(con, sin)]
        m, ic, n = media_ic(d, S)
        subs.append(cond("cambio del ritmo con tope por comprador y almacén (Acto %s)" % a, abs(m), None, K["cambio_max"], [min(abs(ic[0]), abs(ic[1])) if ic[0] * ic[1] > 0 else 0.0, max(abs(ic[0]), abs(ic[1]))], n))
    mk = mercado_neutro(c, "IV", sueltos=False, tope_diario=False)
    m = "oro"
    cap = P["M"][m]["comprador"] * P["mk"]["compradores"]["IV"]
    w = P["mk"]["w_acto"]["IV"]
    p1 = mk.precio_venta(m, cap, w, "spot")
    p2 = mk.precio_venta(m, cap * 2, w, "spot")
    subs.append(cond("el excedente sobre el tope se vende más barato (1 = sí)", 1.0 if p2 < p1 else 0.0, 1.0, 1.0, None, None, ""))
    return r_final(subs, {})


@regla("E7")
def E7(c, K):
    S = c.S
    camps = c.camps("medio")
    subs = []
    for a in ACT3:
        vals = []
        hechos = []
        for r in camps:
            ing = r["acto"][a]["neto"]
            vals.append(r["acto"][a]["c"]["pedidos"] / ing * 100 if ing > 0 else 0.0)
        m, ic, n = media_ic(vals, S)
        subs.append(cond("ganancia extra de los pedidos sobre el ingreso (Acto %s)" % a, m, K["extra_min"], K["extra_max"], ic, n))
    return r_final(subs, {"medio": {"valor": subs[-1]["valor"]}})


# ================================================================== F · Mercado negro y vigilancia
def _negro_runs(c, eid, politica, extra=None, semillas=None):
    """Corre la etapa con una política de mercado negro y devuelve la ganancia neta semanal frente a la honesta (pareada)."""
    P, S = c.P, c.S
    dias, cal = c.tam["negro_dias"], S["estadistica"]["calentamiento_dias"]
    sem = c.semillas[: c.tam["negro_semillas"]] if semillas is None else [C.semilla(S, i) for i in range(semillas)]
    kw = dict(extra or {})
    pol = {"umbral": politica["umbral"], "soborno": politica.get("soborno", False), "comprar": politica.get("comprar", False),
           "margen_soborno": S["politica"]["margen_soborno"]}
    kw.update({"negro": pol, "guardias": politica.get("guardias", 0), "faroleros": politica.get("faroleros", False)})
    honestas = c.etapa(eid, "medio", dias=dias, cal=cal, semillas=sem, **(extra or {}))
    negras = c.etapa(eid, "medio", dias=dias, cal=cal, semillas=sem, **kw)
    gan, absol = [], []
    for h, n in zip(honestas, negras):
        extra_costos = sum(n["flujo"].get(k, 0.0) for k in ("multas", "soborno", "salarios", "compras"))
        d = n["neto_dia"] + extra_costos - h["neto_dia"]
        gan.append(d / h["neto_dia"] * 100 if h["neto_dia"] > 0 else 0.0)
        absol.append(d)
    return gan, absol, negras, honestas


@regla("F1")
def F1(c, K):
    S = c.S
    subs = []
    for a in ACT3:
        gan, _, _, _ = _negro_runs(c, a, K["politica"], semillas=c.tam["negro_semillas_final"])
        m, ic, n = media_ic(gan, S)
        subs.append(cond("ganancia semanal del mercado negro prudente sobre el ingreso honesto (Acto %s)" % a, m, K["min"], K["max"], ic, n))
    return r_final(subs, {"medio": {"valor": subs[-1]["valor"], "ic95": subs[-1]["ic95"], "n": subs[-1]["n"]}})


@regla("F2")
def F2(c, K):
    S = c.S
    barrido = S["politica"]["barrido_negro"][c.modo if c.modo in S["politica"]["barrido_negro"] else "rapido"]
    cribado = []
    for a in ACT3:
        for pol in barrido:
            gan, _, _, _ = _negro_runs(c, a, pol)
            cribado.append((C.media(gan), a, pol))
    cribado.sort(key=lambda x: -x[0])
    # las mejores políticas se vuelven a medir con más semillas para no premiar la suerte
    peor = None
    for _, a, pol in cribado[: S["politica"]["negro_finalistas"]]:
        gan, _, _, _ = _negro_runs(c, a, pol, semillas=c.tam["negro_semillas_final"])
        m, ic, n = media_ic(gan, S)
        if peor is None or m > peor[0]:
            peor = (m, ic, n, a, pol)
    subs = [cond("mayor ganancia semanal entre %d políticas (acto %s, umbral %s)" % (len(cribado), peor[3], peor[4]["umbral"]), peor[0], None, K["max"], peor[1], peor[2])]
    return r_final(subs, {"medio": {"valor": peor[0], "ic95": peor[1], "n": peor[2]}}, {"politica_peor": peor[4]})


@regla("F3")
def F3(c, K):
    S = c.S
    subs = []
    mx = None
    for a in ACT3:
        gan, _, negras, _ = _negro_runs(c, a, K["politica"], semillas=c.tam["negro_semillas_final"])
        m, ic, n = media_ic(gan, S)
        if mx is None or m > mx[0]:
            mx = (m, ic, n, a)
        red = sum(r["cont"]["redadas"] for r in negras)
        dias = sum(r["dias"] for r in negras)
        intervalo = dias / red if red else float("inf")
        subs.append(cond("días entre redadas del jugador abusivo (Acto %s)" % a, intervalo, K["intervalo_min"], K["intervalo_max"], None, red, "días"))
    subs.insert(0, cond("ganancia del jugador abusivo (peor acto: %s)" % mx[3], mx[0], None, K["max"], mx[1], mx[2]))
    return r_final(subs, {"medio": {"valor": mx[0], "ic95": mx[1], "n": mx[2]}})


@regla("F4")
def F4(c, K):
    P, S = c.P, c.S
    lc = P["exp"]["aeth_legal"]
    sp = P["vig"]["especial"]
    res = c.etapa("IV", "medio", especiales=True, negro={"umbral": K["umbral_politica"], "soborno": False, "comprar": False, "margen_soborno": S["politica"]["margen_soborno"]})
    legal = C.media([r["flujo"].get("v_legal", 0.0) for r in res])
    esp = C.media([r["flujo"].get("v_especial", 0.0) for r in res])
    parte_legal = legal / (legal + esp) * 100 if legal + esp > 0 else 0.0
    vig_dia = C.media([r["vig_aeth"] for r in res])
    subs = [cond("canal legal de la Aetherita: viales por día (1 = existe y tiene tope)", lc["tope"], 1.0, K["tope_max"], None, None, "viales"),
            cond("parte de la Aetherita que se vende por el canal legal", parte_legal, K["legal_min"], None, None, len(res)),
            cond("encargos especiales: días entre uno y otro", sp["cada"], K["cada_min"], None, None, None, "días"),
            cond("encargos especiales: viales por encargo (máximo)", sp["viales"][1], None, K["viales_max"], None, None, "viales"),
            cond("encargos especiales: es un canal rutinario (0 = no)", 1.0 if sp["rutina"] else 0.0, None, 0.0, None, None, ""),
            cond("vigilancia diaria que añade la Aetherita frente a la bajada natural", vig_dia / P["vig"]["decae"] * 100, None, K["vig_max"], None, len(res))]
    rc = c.etapa("IV", "medio", especiales=True, casilda=True, negro={"umbral": K["umbral_politica"], "soborno": False, "comprar": False, "margen_soborno": S["politica"]["margen_soborno"]})
    legal_c = C.media([r["flujo"].get("v_legal", 0.0) for r in rc])
    esp_c = C.media([r["flujo"].get("v_especial", 0.0) for r in rc])
    subs.append(cond("variante Casilda: encargos especiales: días entre uno y otro", sp["cada_casilda"], K["cada_min"], None, None, None, "días"))
    subs.append(cond("variante Casilda: parte de la Aetherita que se vende por el canal legal", legal_c / (legal_c + esp_c) * 100 if legal_c + esp_c > 0 else 0.0, K["legal_min"], None, None, len(rc)))
    subs.append(cond("variante Casilda: vigilancia diaria que añade la Aetherita frente a la bajada natural", C.media([r["vig_aeth"] for r in rc]) / P["vig"]["decae"] * 100, None, K["vig_max"], None, len(rc)))
    return r_final(subs, {"medio": {"valor": parte_legal}})


@regla("F5")
def F5(c, K):
    S = c.S
    subs, pp = [], {}
    for a in ACT3:
        gan, absol, negras, _ = _negro_runs(c, a, K["politica"], semillas=c.tam["negro_semillas_final"])
        noches = sum(r["cont"]["noches_negras"] for r in negras)
        dias = sum(r["dias"] for r in negras)
        gan_noche = sum(absol) * (dias / len(absol)) / max(1, noches)
        bloque = valor_bloque(c, a)
        eq = gan_noche / bloque if bloque > 0 else 0.0
        pp[a] = {"valor": eq, "n": noches}
        subs.append(cond("bloques que puede costar una noche negra sin perder (Acto %s)" % a, eq, K["min"], None, None, noches, "bloques"))
    return r_final(subs, {"medio": {"valor": subs[-1]["valor"]}}, {"por_acto": pp})


# ================================================================== G · Empleados
def _pareado(res_a, res_b, clave="neto_dia"):
    return [b[clave] - a[clave] for a, b in zip(res_a, res_b)]


def aporte(c, acto, niveles, **kw):
    """Aporte bruto por día de la plantilla `niveles` (jugador presente), pareado por semilla. Devuelve (media, ic, n, detalle)."""
    S = c.S
    n_ = c.tam["g_semillas"]
    sem = c.semillas[:n_]
    dias = c.tam["g_dias"]
    cal = S["estadistica"]["calentamiento_dias"]
    base = c.etapa(acto, "medio", dias=dias, cal=cal, semillas=sem, sin_riesgo=True, **{k: v for k, v in kw.items() if k in ("tienda",)})
    con = c.etapa(acto, "medio", dias=dias, cal=cal, semillas=sem, empleados=list(niveles), sin_riesgo=True, **kw)
    d = _pareado(base, con)
    m, ic, n = media_ic(d, S)
    sal = C.media([-r["flujo"].get("salarios", 0.0) for r in con])
    return m, ic, n, {"base": C.media([r["neto_dia"] for r in base]), "salarios": sal}


def mundo_ultimo_acto(P):
    return P["actos"][-1]


def tienda_de(c, acto):
    return c.S["prototipo"]["etapas"][acto]["tienda"]


@regla("G1")
def G1(c, K):
    P, S = c.P, c.S
    emp = P["emp"]
    pares = [tuple(x) for x in K["previstos"]]
    todos = pares + [tuple(x) for x in K["siempre"]] + [tuple(x) for x in (K["otros"] if c.tam["g_todos"] else [])]
    rel_prev, rel_todos, rel7, netoIV = [], [], [], []
    detalle = {}
    for (a, n) in todos:
        m, ic, nn, det = aporte(c, a, [n], tienda=max(tienda_de(c, a), 1))
        sueldo = emp["niveles"][n - 1]["sueldo"]
        r30 = sueldo / m * 100 if m > 0 else float("inf")
        ric = [sueldo / ic[1] * 100 if ic[1] and ic[1] > 0 else float("inf"), sueldo / ic[0] * 100 if ic[0] and ic[0] > 0 else float("inf")]
        detalle["%s/N%d" % (a, n)] = {"aporte": round(m, 1), "sueldo": sueldo, "cociente": round(r30, 1)}
        if a == mundo_ultimo_acto(P):
            netoIV.append((m - sueldo, [ic[0] - sueldo, ic[1] - sueldo], nn))
            continue
        rel_todos.append((r30, ric, nn))
        rel7.append(r30 * emp["contrato"]["7"])
        if (a, n) in pares:
            rel_prev.append((r30, ric, nn, a, n))
    subs = []
    if rel_prev:
        lo = min(rel_prev, key=lambda x: x[0])
        hi = max(rel_prev, key=lambda x: x[0])
        subs.append(cond("salario ÷ aporte, par previsto más bajo (%s N%d)" % (lo[3], lo[4]), lo[0], K["prev_min"], None, lo[1], lo[2]))
        subs.append(cond("salario ÷ aporte, par previsto más alto (%s N%d)" % (hi[3], hi[4]), hi[0], None, K["prev_max"], hi[1], hi[2]))
    worst = max(rel_todos, key=lambda x: x[0])
    subs.append(cond("salario ÷ aporte, el peor de todos los pares", worst[0], None, K["todos_max"], worst[1], worst[2]))
    subs.append(cond("con contrato de 7 días, el peor cociente", max(rel7), None, K["siete_max"], None, None))
    if netoIV:
        peor = max(netoIV, key=lambda x: x[0])
        subs.append(cond("aporte neto de un Minero en el Acto IV (esquirlas por día)", peor[0], None, 0.0, peor[1], peor[2], "esq/día"))
    return r_final(subs, {}, {"pares": detalle})


def _plantilla(c, acto):
    P = c.P
    nivel_t = max(tienda_de(c, acto), 1)
    maxmin = P["emp"]["max_mineros"][nivel_t]
    return [c.S["politica"]["plantilla_nivel"][acto]] * maxmin, nivel_t


@regla("G2")
def G2(c, K):
    S, P = c.S, c.P
    sem = c.semillas[: c.tam["g_semillas"]]
    dias, cal = c.tam["g_dias"], S["estadistica"]["calentamiento_dias"]
    peor_b, peor_n = None, None
    for a in ACT3:
        niv, nt = _plantilla(c, a)
        base = c.etapa(a, "medio", dias=dias, cal=cal, semillas=sem, tienda=nt, sin_riesgo=True)
        con = c.etapa(a, "medio", dias=dias, cal=cal, semillas=sem, tienda=nt, empleados=niv, dependiente=True, sin_riesgo=True)
        brutos = [(y["neto_dia"] - x["neto_dia"]) / x["neto_dia"] * 100 for x, y in zip(base, con)]
        netos = [(y["neto_dia"] + y["flujo"].get("salarios", 0.0) - x["neto_dia"]) / x["neto_dia"] * 100 for x, y in zip(base, con)]
        mb = media_ic(brutos, S)
        mn = media_ic(netos, S)
        if peor_b is None or mb[0] > peor_b[0]:
            peor_b = mb + (a,)
        if peor_n is None or mn[0] > peor_n[0]:
            peor_n = mn + (a,)
    subs = [cond("aporte bruto de la plantilla máxima sobre el jugador solo (peor: Acto %s)" % peor_b[3], peor_b[0], None, K["bruto_max"], peor_b[1], peor_b[2]),
            cond("aporte neto de la plantilla máxima sobre el jugador solo (peor: Acto %s)" % peor_n[3], peor_n[0], None, K["neto_max"], peor_n[1], peor_n[2])]
    return r_final(subs, {"medio": {"valor": peor_n[0], "ic95": peor_n[1], "n": peor_n[2]}})


@regla("G3")
def G3(c, K):
    S, P = c.S, c.P
    sem = c.semillas[: c.tam["g_semillas"]]
    dias, cal = c.tam["g_dias"], S["estadistica"]["calentamiento_dias"]
    peor_aus, menor_gan = None, None
    for a in ACT3:
        niv, nt = _plantilla(c, a)
        solo = c.etapa(a, "medio", dias=dias, cal=cal, semillas=sem, tienda=nt, sin_riesgo=True)
        aus = c.etapa(a, "medio", dias=dias, cal=cal, semillas=sem, tienda=nt, empleados=niv, dependiente=True, ausente=True, sin_riesgo=True)
        con = c.etapa(a, "medio", dias=dias, cal=cal, semillas=sem, tienda=nt, empleados=niv, dependiente=True, sin_riesgo=True)
        ra = [y["neto_dia"] / x["neto_dia"] * 100 for x, y in zip(solo, aus)]
        gn = [(y["neto_dia"] + y["flujo"].get("salarios", 0.0) - x["neto_dia"]) / x["neto_dia"] * 100 for x, y in zip(solo, con)]
        ma, mg = media_ic(ra, S), media_ic(gn, S)
        if peor_aus is None or ma[0] > peor_aus[0]:
            peor_aus = ma + (a,)
        if a in K["actos_conjunto"] and (menor_gan is None or mg[0] < menor_gan[0]):
            menor_gan = mg + (a,)
    subs = [cond("ingreso de la plantilla sola frente al jugador solo (peor: Acto %s)" % peor_aus[3], peor_aus[0], None, K["ausente_max"], peor_aus[1], peor_aus[2]),
            cond("ganancia neta de jugador + plantilla frente al jugador solo (peor: Acto %s)" % menor_gan[3], menor_gan[0], K["conjunto_min"], None, menor_gan[1], menor_gan[2])]
    return r_final(subs, {"medio": {"valor": menor_gan[0], "ic95": menor_gan[1], "n": menor_gan[2]}})


@regla("G4")
def G4(c, K):
    S, P = c.S, c.P
    sem = c.semillas[: c.tam["g_semillas"]]
    dias, cal = c.tam["g_dias"], S["estadistica"]["calentamiento_dias"]
    subs = []
    for a in K["actos"]:
        nt = max(tienda_de(c, a), 1)
        base = c.etapa(a, "medio", dias=dias, cal=cal, semillas=sem, tienda=nt, sin_riesgo=True)
        con = c.etapa(a, "medio", dias=dias, cal=cal, semillas=sem, tienda=nt, dependiente=True, sin_riesgo=True)
        sueldo = P["emp"]["apoyo"]["dependiente"][a]
        netos = [(y["neto_dia"] - sueldo - x["neto_dia"]) for x, y in zip(base, con)]
        pct = [(y["neto_dia"] - sueldo - x["neto_dia"]) / x["neto_dia"] * 100 for x, y in zip(base, con)]
        m, ic, n = media_ic(netos, S)
        subs.append(cond("aporte neto del Dependiente en esquirlas por día (Acto %s)" % a, m, 0.0, None, ic, n, "esq/día"))
        m2, ic2, n2 = media_ic(pct, S)
        subs.append(cond("aporte neto del Dependiente sobre el ingreso del jugador (Acto %s)" % a, m2, None, K["max_pct"], ic2, n2))
    return r_final(subs, {"medio": {"valor": subs[1]["valor"], "ic95": subs[1]["ic95"], "n": subs[1]["n"]}})


@regla("G5")
def G5(c, K):
    P, S = c.P, c.S
    emp = P["emp"]
    aportes = {}
    for (a, n) in [tuple(x) for x in K["niveles"]]:
        aportes[(a, n)] = aporte(c, a, [n], tienda=max(tienda_de(c, a), 1))[0]
    subs = []
    for (a, n) in aportes:
        if (a, n + 1) not in aportes:
            continue
        s0, s1 = emp["niveles"][n - 1]["sueldo"], emp["niveles"][n]["sueldo"]
        dif = (aportes[(a, n + 1)] - s1) - (aportes[(a, n)] - s0)
        costo = emp["entreno_dias"] * s1
        dias = costo / dif if dif > 0 else float("inf")
        subs.append(cond("días para recuperar el entrenamiento de N%d a N%d (Acto %s)" % (n, n + 1, a), dias, K["min"], K["max"], None, None, "días"))
    subs.append(cond("el salario sigue al nivel (1 = sí)", 1.0 if emp["asignacion"]["sueldo_sigue"] else 0.0, 1.0, 1.0, None, None, ""))
    return r_final(subs, {})


@regla("G6")
def G6(c, K):
    P = c.P
    e = P["emp"]
    peor = None
    for z, rz in e["riesgo"].items():
        f = 1.0
        dias_perdidos = rz["injury_pct"] / 100.0 * rz["sick_days"] * 100.0
        carga = rz["lose_load_pct"]
        robo = e["robo"]["media"] / P["t"]["semana"] * e["robo_valor"] / 100.0
        total = dias_perdidos + carga * rz["injury_pct"] / 100.0 + robo
        if peor is None or total > peor[0]:
            peor = (total, z)
    return r_final([cond("pérdida esperada de un Minero por riesgo (peor zona: %s), en %% del aporte" % peor[1], peor[0], None, K["max"], None, None)], {})


# ================================================================== H · Deuda, mora, rescate
class _Caja:
    """Caja mínima para probar la deuda sin jugador."""

    def __init__(self, cash):
        self.cash = cash

    def mover(self, cat, monto):
        self.cash += monto


@regla("H1")
def H1(c, K):
    P, S = c.P, c.S
    meta = P["deuda"]["via"]["a5_monto"]
    subs, pp = [], {}
    for pid in PERFILES:
        sin = c.camps(pid, via=False)
        horas = []
        for r in sin:
            falta = max(0.0, meta - r["cap_fin"]["II"])
            horas.append(falta / r["acto"]["II"]["neto_hora"])
        m, ic, n = media_ic(horas, S)
        subs.append(cond("horas de ingreso del Acto II que faltan para el 25 %% sin pagos extra (%s)" % pid, m, None, K["horas_max"], ic, n, "h", pid))
        pp[pid] = {"valor": m, "ic95": ic, "n": n}
    con = c.camps("medio", via=True, n=c.tam["semillas_tasas"])
    k = sum(1 for r in con if r["cap_fin"]["II"] >= meta - 1e-6)
    subs.append(cond("corridas del medio que alcanzan el 25 % al cerrar el Acto II", k / len(con) * 100, K["alcanza_min"], None,
                     [x * 100 for x in C.ic_prop(k, len(con), S)], len(con)))
    hs = []
    for r in con:
        dia_com = r["estatus_dia"].get("comerciante")
        dia_cap = r["dia_cap"].get("a5")
        if dia_com is None or dia_cap is None:
            hs.append(float("inf"))
        else:
            hs.append(C.horas_de(P, max(dia_com, dia_cap) - r["inicio"]["II"] + 1))
    hs_f = [x for x in hs if x != float("inf")]
    if len(hs_f) == len(hs):
        m, ic, n = media_ic(hs, S)
        subs.append(cond("horas del Acto II para ser Comerciante y llevar el 25 % pagado", m, None, K["combinado_max"], ic, n, "h"))
    else:
        subs.append(cond("horas del Acto II para ser Comerciante y llevar el 25 % pagado", float("inf"), None, K["combinado_max"], None, len(hs), "h"))
    return r_final(subs, pp)


@regla("H2")
def H2(c, K):
    P, S = c.P, c.S
    meta = P["deuda"]["via"]["circulo_monto"]
    subs, pp = [], {}
    for pid in PERFILES:
        sin = c.camps(pid, via=False)
        horas = []
        for r in sin:
            falta = max(0.0, meta - r["cap_fin"]["III"])
            horas.append(falta / r["acto"]["III"]["neto_hora"])
        m, ic, n = media_ic(horas, S)
        subs.append(cond("horas de ingreso del Acto III que faltan para el 50 %% sin pagos extra (%s)" % pid, m, None, K["horas_max"], ic, n, "h", pid))
        pp[pid] = {"valor": m, "ic95": ic, "n": n}
    return r_final(subs, pp)


@regla("H3")
def H3(c, K):
    P = c.P
    d = P["deuda"]
    semanas = K["semanas"]

    def correr(con_abono):
        D = C.Deuda(P)
        caja = _Caja(float("inf"))
        for sdx in range(semanas):
            dia = d["dia1"] + sdx * P["t"]["semana"]
            ab = d["abono"]
            if not con_abono:
                D.credito_sem_restantes = 0
            D.pagar(caja, dia)
            if not con_abono:
                D.credito_sem_restantes = 0
        return D
    a, b = correr(True), correr(False)
    interes_50 = d["K"] * (1 - d["via"]["circulo"] / 100.0) * 0 + d["K"] * d["via"]["circulo"] / 100.0 * d["int_mes"] / 100.0
    subs = [cond("diferencia de capital pagado con y sin abono (esquirlas)", abs(a.pagado_cap - b.pagado_cap), None, 0.5, None, None, "esq"),
            cond("abono mensual frente al interés mensual con el 50 % pagado", d["abono"]["monto"] / interes_50 * 100, None, K["abono_max"], None, None),
            cond("capital máximo que asume el Consorcio frente a K", d["via"]["consorcio_monto"] / d["K"] * 100, None, d["via"]["consorcio"] + 1e-9, None, None),
            cond("capital que queda tras la asunción del Consorcio frente a K", 100 - d["via"]["consorcio_monto"] / d["K"] * 100, K["queda_min"], None, None, None)]
    return r_final(subs, {})


@regla("H4")
def H4(c, K):
    P, S = c.P, c.S
    d = P["deuda"]
    lento = c.camps("lento", via=False)
    ing_sem = C.media([r["acto"]["II"]["neto"] / r["acto"]["II"]["dias"] * P["t"]["semana"] for r in lento])
    subs = []
    cuota = float(d["cuota1"])
    for dif in P["dif"]["orden"]:
        for nsem in K["atrasos"]:
            D = C.Deuda(P, dif)
            caja = _Caja(0.0)
            for i in range(nsem):
                D.pagar(caja, d["dia1"] + i * P["t"]["semana"])
            debo = sum(x["monto"] for x in D.atrasadas)
            q, am, it, cr = D.cuota(0)
            libre = ing_sem - q
            semanas = (debo / libre) if libre > 0 else float("inf")
            semanas = math.ceil(semanas) if semanas != float("inf") else semanas
            tope = K["semanas"][str(nsem)] + (K["extra_dificiles"] if dif in ("dificil", "hardcore") else 0)
            subs.append(cond("semanas para ponerse al corriente tras %d de atraso (%s)" % (nsem, dif), semanas, None, tope, None, None, "semanas"))
    rec = d["recargo"]["hardcore"] / 100.0 * cuota
    dia14 = cuota * 2 + rec
    subs.append(cond("cuota del día 14 de Hardcore frente al ingreso semanal del lento", dia14 / ing_sem * 100, None, K["hardcore_max"], None, len(lento)))
    subs.append(cond("algún estado de la mora cierra una puerta (0 = no)", 1.0 if d["mora"]["cierra"] else 0.0, None, 0.0, None, None, ""))
    mayor = max(subs[:-2], key=lambda s: margen(s) * -1)
    return r_final(subs, {"lento": {"valor": ing_sem}}, {"ingreso_semana_lento": ing_sem})


@regla("H5")
def H5(c, K):
    P, S = c.P, c.S
    d = P["deuda"]
    subs = []
    for var in ("cuota_extra", "adelanto"):
        camps = c.camps("lento", via=True, variante=var, n=c.tam["semillas_tasas"])
        ok = [1 if r["dias_caja_neg"] <= P["t"]["semana"] else 0 for r in camps]
        k = sum(ok)
        subs.append(cond("corridas del lento con caja negativa a lo sumo una semana (%s)" % var, k / len(ok) * 100, K["caja_min"], None,
                         [x * 100 for x in C.ic_prop(k, len(ok), S)], len(ok)))
        alc = sum(1 for r in camps if r["cap_fin"]["II"] >= d["via"]["a5_monto"] - 1e-6)
        subs.append(cond("corridas del lento que alcanzan el 25 %% al cerrar el Acto II (%s)" % var, alc / len(camps) * 100, K["via_min"], None,
                         [x * 100 for x in C.ic_prop(alc, len(camps), S)], len(camps)))
    crece = d["luz"]["mes"] < d["int_mes"]
    subs.append(cond("la deuda de luz crece más despacio que la deuda principal (1 = sí)", 1.0 if crece else 0.0, 1.0, 1.0, None, None, ""))
    return r_final(subs, {"lento": {"valor": subs[0]["valor"]}})


@regla("H6")
def H6(c, K):
    P, S = c.P, c.S
    camps = c.camps("lento", via=True, n=c.tam["semillas_tasas"])
    out = {}
    subs = []
    for puerta, acto, monto_clave, piso in (("A5", "II", "a5_monto", "comerciante"), ("circulo", "III", "circulo_monto", "empresario")):
        horas = []
        for r in camps:
            dia_cap = r["dia_cap"].get("a5" if puerta == "A5" else "circulo")
            dia_pat = r["estatus_dia"].get(piso)
            if dia_cap is None or dia_pat is None:
                horas.append(float("inf"))
            else:
                horas.append(C.horas_de(P, max(dia_cap, dia_pat)))
        horas.sort()
        p95 = horas[min(len(horas) - 1, int(math.ceil(K["percentil"] * len(horas))) - 1)]
        rescate = math.ceil(K["margen"] * p95 / K["paso"]) * K["paso"] if p95 != float("inf") else float("inf")
        out[puerta] = {"p95": p95, "rescate": rescate}
        subs.append(cond("horas de la misión de rescate para la puerta %s (1,25 × p95 del lento, a 0,5 h)" % puerta, rescate, 0.0, K["max"], None, len(horas), "h"))
    return r_final(subs, {"lento": {"valor": max(v["rescate"] for v in out.values())}}, {"puertas": out})


# ================================================================== I · Meta-casos
@regla("I1")
def I1(c, K):
    P, S, R = c.P, c.S, c.R
    texto = []
    for _ in range(2):
        cx = Ctx(P, S, R, c.modo, tam=dict(c.tam, acto1=K["acto1"], semillas=K["semillas"], dias_etapa=K["dias"]))
        r1 = cx.acto1("medio")
        cp = C.Campana(P, S, "medio", cx.semillas[0]).correr().resumen()
        et = cx.etapa("III", "medio")
        mk = mercado_neutro(cx, "II", semilla=C.semilla_flujo(S, "i1"))
        for _ in range(K["pasos"]):
            mk.nuevo_dia(1)
            mk.paso()
        paquete = {"a1": [r1["paga"], r1["margen"], r1["neto_hora"]], "camp": [cp["pat_fin"], cp["nivel_pico"]],
                   "etapa": [e["neto_dia"] for e in et], "mk": mk.cur}
        texto.append(json.dumps(paquete, sort_keys=True, default=lambda x: round(x, S["estadistica"]["decimales"]),
                                separators=(",", ":")))
    redondear = lambda t: json.dumps(_redondea(json.loads(t), S["estadistica"]["decimales"]), sort_keys=True)
    iguales = redondear(texto[0]) == redondear(texto[1])
    return r_final([cond("misma semilla, mismo resultado (1 = sí)", 1.0 if iguales else 0.0, 1.0, 1.0, None, None, "")], {})


def _redondea(x, d):
    if isinstance(x, float):
        return round(x, d)
    if isinstance(x, list):
        return [_redondea(v, d) for v in x]
    if isinstance(x, dict):
        return {k: _redondea(v, d) for k, v in x.items()}
    return x


def aplica_edicion(world, clave, valor):
    """Cambia en memoria una clave de world.json (ruta con puntos; los segmentos son claves, índices o ids)."""
    nodo = world
    segs = clave.split(".")
    for sgm in segs[:-1]:
        if isinstance(nodo, list):
            nodo = nodo[int(sgm)] if sgm.lstrip("-").isdigit() else next(e for e in nodo if e.get("id") == sgm)
        else:
            nodo = nodo[sgm]
    ult = segs[-1]
    if isinstance(nodo, list):
        nodo[int(ult) if ult.lstrip("-").isdigit() else next(i for i, e in enumerate(nodo) if e.get("id") == ult)] = valor
    else:
        nodo[ult] = valor


def contexto_mutado(world, S, R, modo, ediciones, tam):
    w = json.loads(json.dumps(world))
    for clave, valor in ediciones:
        aplica_edicion(w, clave, valor)
    P, _ = mundo.cargar(w)
    return Ctx(P, S, R, modo, tam=tam)


def evalua_regla(c, rid):
    K = c.crit(rid)
    r = REGLAS[rid](c, K)
    return resultado_regla(rid, c, r)


def resultado_regla(rid, c, r):
    subs = r["subs"]
    est = estado_de(subs)
    pr = principal(subs)
    return {"id": rid, "estado": est, "principal": pr, "subs": subs, "por_perfil": r["por_perfil"], "extra": r["extra"]}


@regla("I2")
def I2(c, K):
    """Mutaciones: cambiar una cifra de world.json en memoria cambia el estado de alguna condición de su regla."""
    P, S, R = c.P, c.S, c.R
    world = mundo.cargar_world()
    tam = dict(S["tamanos"][K["modo"]])
    base = Ctx(P, S, R, K["modo"], tam=tam)
    ok, total, sin_volteo = 0, 0, []
    for rid, muts in S["mutaciones"].items():
        total += 1
        estados0 = [x["estado"] for x in evalua_regla(base, rid)["subs"]]
        volteo = False
        for mut in muts:
            cm = contexto_mutado(world, S, R, K["modo"], [(e["clave"], e["valor"]) for e in mut["ediciones"]], tam)
            if [x["estado"] for x in evalua_regla(cm, rid)["subs"]] != estados0:
                volteo = True
                break
        if volteo:
            ok += 1
        else:
            sin_volteo.append(rid)
    pct = ok / total * 100 if total else 0.0
    return r_final([cond("reglas cuya mutación cambia el estado de alguna condición", pct, K["min"], None, None, total)], {}, {"sin_volteo": sin_volteo})


@regla("I3")
def I3(c, K):
    base = c.base_resultados if hasattr(c, "base_resultados") else []
    sin_ic = []
    inciertas = []
    for r in base:
        if r["estado"] == "incierto":
            inciertas.append(r["id"])
        informativa = c.mapa[r["id"]]["criterio"].get("informativa")
        if not informativa and r["id"] not in K["deterministas"]:
            if r.get("n") is None and r.get("ic95") is None and not any(x.get("n") for x in r.get("condiciones", [])):
                sin_ic.append(r["id"])
    subs = [cond("reglas en «incierto»", len(inciertas), None, 0.0, None, len(base), "reglas"),
            cond("reglas medidas sin n ni intervalo", len(sin_ic), None, 0.0, None, len(base), "reglas")]
    return r_final(subs, {}, {"inciertas": inciertas, "sin_ic": sin_ic})
