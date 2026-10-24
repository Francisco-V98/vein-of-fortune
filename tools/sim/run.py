"""Línea de órdenes del simulador de economía (F0-53).

    python3 tools/sim/run.py --rapido                 modo rápido (CI): pocas semillas, sin la regla I2 (mutaciones)
    python3 tools/sim/run.py --rapido --mutaciones    modo rápido más la regla I2 (la prueba de las pruebas; ≈ 80 s)
    python3 tools/sim/run.py --completo [--escribir]  modo completo (incluye I2): escribe studio/data/sim/resultados.json
    python3 tools/sim/run.py --regla A1,B2            solo esas reglas
    python3 tools/sim/run.py --huella                 huella actual de las cifras de world.json que lee el simulador
"""
import argparse
import json
import pathlib
import sys
import time

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent))

from sim import informe, mundo, reglas  # noqa: E402
from sim import campana as C  # noqa: E402

KB = 1024.0  # bytes por kilobyte
SIM_DIR = mundo.RAIZ / "studio" / "data" / "sim"


def cargar_reglas():
    return json.loads((SIM_DIR / "reglas.json").read_text(encoding="utf-8"))


def evaluar(modo="rapido", solo=None, mutaciones=True, mundo_dict=None, verbose=False, tam=None, criterios=None):
    """Evalúa las reglas. Devuelve (ctx, lista de resultados de regla)."""
    P, _ = mundo.cargar(mundo_dict)
    S = mundo.cargar_supuestos()
    R = cargar_reglas()
    c = reglas.Ctx(P, S, R, modo, tam=tam)
    for rid, cambios in (criterios or {}).items():
        c.mapa[rid]["criterio"].update(cambios)
    ids = [r["id"] for r in R["reglas"] if r["id"] not in ("I2", "I3")]
    if solo:
        ids = [i for i in ids if i in solo]
    out = []
    tiempos = {}
    for rid in ids:
        t = time.time()
        out.append(reglas.evalua_regla(c, rid))
        tiempos[rid] = time.time() - t
        if verbose:
            print("  %-3s %-8s %.1f s" % (rid, out[-1]["estado"], tiempos[rid]), flush=True)
    c.tiempos = tiempos
    if solo is None or {"I2", "I3"} & set(solo):
        c.base_estados = {r["id"]: r["estado"] for r in out}
        if mutaciones and (solo is None or "I2" in solo):
            t = time.time()
            out.append(reglas.evalua_regla(c, "I2"))
            tiempos["I2"] = time.time() - t
        c.base_resultados = [informe.entrada({k: v for k, v in c.mapa[r["id"]].items()}, r, S["estadistica"]["decimales"], S["estadistica"]["infinito"]) for r in out]
        if solo is None or "I3" in solo:
            out.append(reglas.evalua_regla(c, "I3"))
    return c, out


def imprimir(out, c):
    print("%-4s %-9s %s" % ("id", "estado", "métrica principal"))
    for r in out:
        pr = r["principal"]
        v = pr["valor"]
        txt = "%s = %s %s" % (pr["nombre"], ("%.2f" % v) if isinstance(v, float) else v, pr["unidad"]) if pr else ""
        print("%-4s %-9s %s" % (r["id"], r["estado"], txt))
        if r["estado"] != "pasa":
            for s in r["subs"]:
                if s["estado"] != "pasa":
                    print("       - %s: %s (%s) límites [%s, %s] -> %s" % (s["nombre"], s["valor"], s["ic95"], s["lo"], s["hi"], s["estado"]))
    cont = {e: sum(1 for r in out if r["estado"] == e) for e in ("pasa", "falla", "incierto")}
    print("Resumen: %d pasan, %d fallan, %d inciertas de %d" % (cont["pasa"], cont["falla"], cont["incierto"], len(out)))


def parser():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--rapido", action="store_true")
    ap.add_argument("--completo", action="store_true")
    ap.add_argument("--regla", default=None)
    ap.add_argument("--escribir", action="store_true", help="escribe studio/data/sim/resultados.json (solo con --completo)")
    ap.add_argument("--mutaciones", action="store_true", help="incluye la regla I2 también en el modo rápido (el completo siempre la incluye)")
    ap.add_argument("--huella", action="store_true")
    ap.add_argument("--minas", action="store_true", help="evalúa las reglas del motor de minas (C5b, J1 a J6; reglas_v2 de reglas.json)")
    ap.add_argument("--verbose", action="store_true")
    return ap


def opciones(a):
    """Argumentos de evaluar() que corresponden a las opciones de la línea de órdenes (los usa también la prueba de tiempo)."""
    solo = a.regla.split(",") if a.regla else None
    modo = "completo" if a.completo else "rapido"
    mutaciones = a.completo or a.mutaciones or bool(solo and "I2" in solo)
    return {"modo": modo, "solo": solo, "mutaciones": mutaciones, "verbose": a.verbose}


def minas(a):
    from sim import reglas_minas
    P, _ = mundo.cargar()
    c = reglas.Ctx(P, mundo.cargar_supuestos(), cargar_reglas(), "completo" if a.completo else "rapido")
    solo = a.regla.split(",") if a.regla else list(reglas_minas.REGLAS_V2)
    out = [reglas_minas.evalua(c, rid) for rid in solo]
    imprimir(out, c)
    return 0


def main(argv=None):
    a = parser().parse_args(argv)
    if a.huella:
        print(mundo.huella(mundo.cargar_world()))
        return 0
    if a.minas:
        return minas(a)
    op = opciones(a)
    modo, solo = op["modo"], op["solo"]
    t0 = time.time()
    c, out = evaluar(**op)
    imprimir(out, c)
    print("Tiempo: %.1f s (modo %s)" % (time.time() - t0, modo))
    if a.completo and a.escribir and solo is None:
        R = cargar_reglas()
        por_id = {r["id"]: r for r in out}
        extras = {}
        if "D1" in por_id:
            extras["zonas"] = por_id["D1"]["extra"].get("reparto", {})
        if "G1" in por_id:
            extras["empleados"] = por_id["G1"]["extra"].get("pares", {})
        if "F1" in por_id:
            extras["mercado_negro"] = {s["nombre"].split("(")[-1].rstrip(")"): s["valor"] for s in por_id["F1"]["subs"]}
        if "C5" in por_id:
            extras["descarte_ingreso_hora"] = por_id["C5"]["extra"].get("ingreso_h", {})
        if "H6" in por_id:
            extras["rescate_horas"] = por_id["H6"]["extra"].get("puertas", {})
        res = informe.construir(c, out, R, modo, c.semillas, extras)
        ruta = SIM_DIR / "resultados.json"
        texto = json.dumps(res, ensure_ascii=False, separators=(",", ":"))
        ruta.write_text(texto + "\n", encoding="utf-8")
        print("Escrito %s (%.0f KB)" % (ruta, len(texto) / 1024))
    fallos = sum(1 for r in out if r["estado"] != "pasa")
    return 0


if __name__ == "__main__":
    sys.exit(main())
