"""Informe: convierte los resultados de las reglas en resultados.json (esquema del hub) y prepara las series."""
import datetime
import json
import math

from . import campana as C
from . import mundo

def limpio(x, d, inf):
    """Redondea y evita valores no JSON (infinitos, NaN)."""
    if isinstance(x, float):
        if math.isnan(x):
            return None
        if math.isinf(x):
            return inf if x > 0 else -inf
        return round(x, d)
    if isinstance(x, dict):
        return {k: limpio(v, d, inf) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [limpio(v, d, inf) for v in x]
    return x


def entrada(regla_def, res, d, inf):
    """Una regla del esquema de resultados.json a partir del resultado de la regla."""
    pr = res["principal"]
    valor = pr["valor"] if pr and pr["valor"] is not None else inf
    out = {
        "id": regla_def["id"], "grupo": regla_def["grupo"], "titulo": regla_def["titulo"], "docs": regla_def["docs"],
        "estado": res["estado"], "metrica": (pr["nombre"] if pr else regla_def["metrica"]), "valor": valor,
        "ic95": pr["ic95"] if pr and pr["ic95"] and pr["ic95"][0] != pr["ic95"][1] else None, "n": pr["n"] if pr else None,
        "umbral": regla_def["umbral"], "origen": regla_def["origen"], "unidad": pr["unidad"] if pr else "",
        "por_perfil": {}, "condiciones": [
            {k: v for k, v in s.items() if k in ("nombre", "valor", "ic95", "n", "lo", "hi", "estado", "unidad", "perfil")}
            for s in res["subs"]],
        "metrica_general": regla_def["metrica"],
    }
    if out["ic95"] is not None:
        out["ic95"] = [min(out["ic95"]), max(out["ic95"])]
    for pid, cell in (res["por_perfil"] or {}).items():
        c = {"valor": cell.get("valor") if cell.get("valor") is not None else inf}
        for k in ("estado", "ic95", "n", "detalle"):
            if k in cell and cell[k] is not None:
                c[k] = cell[k]
        out["por_perfil"][pid] = c
    # estado por perfil a partir de las condiciones de ese perfil
    for pid, c in out["por_perfil"].items():
        ests = [s["estado"] for s in res["subs"] if s.get("perfil") == pid]
        if ests and "estado" not in c:
            c["estado"] = max(ests, key=lambda e: {"falla": 2, "incierto": 1, "pasa": 0}[e])
    if res.get("extra"):
        out["extra"] = res["extra"]
    return limpio(out, d, inf)


def mediana(xs):
    xs = sorted(xs)
    n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2.0


def serie_patrimonio(c):
    """Patrimonio por día (mediana de las corridas) de cada perfil, con los días de inicio de cada acto del perfil medio."""
    P, S = c.P, c.S
    nsem = min(len(c.semillas), c.tam["serie_semillas"])
    sem = c.semillas[:nsem]
    paso = S["campana"]["paso_serie"]
    total = 0
    durs = {}
    for pid in S["perfiles"]:
        d = C.duraciones(P, S, pid)
        durs[pid] = d
        total = max(total, P["deuda"]["dia1"] + sum(d.values()))
    dias = list(range(0, total + 1, paso))
    perfiles = {}
    for pid in S["perfiles"]:
        propio = P["deuda"]["dia1"] + sum(durs[pid].values())
        filas = []
        for s in sem:
            cam = C.Campana(P, S, pid, s, dias_extra=total - propio).correr()
            filas.append(dict(cam.pat_serie))
            a1 = cam.a1
            filas[-1][0] = float(P["deuda"]["caja0"])
            filas[-1][P["deuda"]["dia1"]] = a1["caja"] - (a1["cuota"] if a1["paga"] else 0.0)
        out = []
        ultimo = None
        for d in dias:
            v = [f[d] for f in filas if d in f]
            if v:
                ultimo = mediana(v)
            out.append(ultimo if ultimo is not None else float(P["deuda"]["caja0"]))
        perfiles[pid] = out
    medio = durs["medio"]
    ini = P["deuda"]["dia1"] + 1
    actos = []
    for a in ("II", "III", "IV"):
        actos.append({"acto": a, "dia": ini})
        ini += medio[a]
    refs = dict(P["ritmo"]["estatus"])
    return {"dias": dias, "perfiles": perfiles, "actos": actos, "referencias": refs}


def serie_ingreso(c):
    P, S = c.P, c.S
    objetivo = {"I": P["ritmo"]["hora"]["I"]["medium"], "II": P["ritmo"]["hora"]["II"]["target"],
                "III": P["ritmo"]["hora"]["III"]["target"], "IV": P["ritmo"]["hora"]["IV"]["target"]}
    perfiles = {}
    for pid in S["perfiles"]:
        camps = c.camps(pid)
        a1 = c.acto1(pid)
        v = {"I": C.media(a1["netos"])}
        for a in ("II", "III", "IV"):
            v[a] = C.media([r["acto"][a]["neto_hora"] for r in camps])
        perfiles[pid] = v
    return {"actos": list(P["actos"]), "objetivo": objetivo, "banda": S["estadistica"]["banda_ritmo"], "perfiles": perfiles}


def serie_caja(c):
    P, S = c.P, c.S
    out = {}
    casos = {"lento": ("lento", {}), "medio": ("medio", {}), "rapido": ("rapido", {}), "optimizador": ("optimizador", {"mejora": True})}
    for pid, (p_, kw) in casos.items():
        r = c.acto1(p_, **kw)
        out[pid] = {"p10": r["caja_p10"], "p50": r["caja_p50"], "p90": r["caja_p90"]}
    return {"cuota": float(P["deuda"]["cuota1"]), "perfiles": out}


def construir(c, resultados, R, modo, semillas, extras=None):
    P, S = c.P, c.S
    d = S["estadistica"]["decimales"]
    mapa = {r["id"]: r for r in R["reglas"]}
    inf = S["estadistica"]["infinito"]
    reglas = [entrada(mapa[r["id"]], r, d, inf) for r in resultados]
    series = {"ingreso_hora_por_acto": serie_ingreso(c), "patrimonio_por_dia": serie_patrimonio(c),
              "acto1_caja_antes_de_cuota": serie_caja(c)}
    series.update(extras or {})
    world = mundo.cargar_world()
    sup = json.dumps(S, sort_keys=True, ensure_ascii=False)
    reg = json.dumps(R, sort_keys=True, ensure_ascii=False)
    out = {
        "version": 1, "generado": datetime.date.today().isoformat(), "modo": modo, "huella": mundo.huella(world),
        "huella_supuestos": mundo.huella_texto(sup), "huella_reglas": mundo.huella_texto(reg),
        "tamanos": c.tam, "semillas": list(semillas),
        "perfiles": [{"id": pid, "nombre": S["perfiles"][pid]["nombre"]} for pid in S["perfiles"]],
        "reglas": reglas, "series": limpio(series, d, inf),
    }
    return out
