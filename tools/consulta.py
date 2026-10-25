#!/usr/bin/env python3
"""Consulta corta del estudio: evita leer documentos y datos enteros.

  python3 tools/consulta.py limpieza [doc]            tabla de limpieza (✅ 🟡 ❓ ⏳ %) por documento y total
  python3 tools/consulta.py abiertos [doc] [--tipo prop|open|wait]   puntos 🟡/❓/⏳ con archivo:línea
  python3 tools/consulta.py indice 23                 encabezados con número de línea
  python3 tools/consulta.py seccion 23 "Día 1"        solo la sección cuyo encabezado contiene el texto
  python3 tools/consulta.py ficha 23                  ficha breve de un documento
  python3 tools/consulta.py ficha F0-88               ficha breve de una tarea
  python3 tools/consulta.py tarea F0-88               una tarea en una línea
  python3 tools/consulta.py tareas --estado doing --fase F0
  python3 tools/consulta.py mundo economy.rates       navega studio/data/world.json

`doc` es el prefijo numérico («23») o el id completo. `--max N` limita las líneas (40 por defecto).
Reutiliza studio/hub/build.py, así que las cifras coinciden con `build.py --strict`.
Solo usa la biblioteca estándar.
"""
import argparse
import contextlib
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "studio" / "hub"))
with contextlib.redirect_stdout(io.StringIO()):
    import build  # noqa: E402

MAX_POR_DEFECTO = 40
MARCAS = {"prop": "🟡", "open": "❓", "wait": "⏳"}


class Error(Exception):
    """Error de uso con mensaje en español."""


def _silencio(fn, *a, **k):
    with contextlib.redirect_stdout(io.StringIO()):
        return fn(*a, **k)


def cargar_roadmap():
    return json.loads((build.DATA / "roadmap.json").read_text(encoding="utf-8"))


def tareas_todas(roadmap=None):
    roadmap = roadmap or cargar_roadmap()
    return [dict(t, fase=p["id"]) for p in roadmap["phases"] for m in p["milestones"] for t in m["tasks"]]


def cargar_docs():
    """Documentos con limpieza calculada igual que build_hub (avisos silenciados)."""
    docs = _silencio(build.build_docs)
    estado = {t["id"]: t["status"] for t in tareas_todas()}
    total = _silencio(build.analyze_docs, docs, estado)
    return docs, total


def buscar_doc(docs, ref):
    ref = ref.strip()
    exactos = [d for d in docs if d["id"] == ref]
    if exactos:
        return exactos[0]
    pref = [d for d in docs if d["id"].startswith(ref.zfill(2) + "-" if ref.isdigit() else ref)]
    if len(pref) == 1:
        return pref[0]
    if not pref:
        raise Error("No existe el documento «%s». Prueba con el prefijo numérico (p. ej. 23)." % ref)
    raise Error("«%s» es ambiguo: %s" % (ref, ", ".join(d["id"] for d in pref)))


def ruta_doc(doc):
    base = build.DOCS / "adr" if doc["id"].startswith("adr-") else build.DOCS
    nombre = doc["id"][4:] if doc["id"].startswith("adr-") else doc["id"]
    return (base / (nombre + ".md")).relative_to(ROOT)


def encabezados(md):
    """[(línea, nivel, texto)] ignorando bloques de código."""
    res, en_codigo = [], False
    for n, linea in enumerate(md.splitlines(), start=1):
        if linea.strip().startswith("```"):
            en_codigo = not en_codigo
            continue
        m = None if en_codigo else re.match(r"^(#{1,6})\s+(.*\S)\s*$", linea)
        if m:
            res.append((n, len(m.group(1)), m.group(2)))
    return res


def _pct(c):
    return "-" if c["pct"] is None else "%d%%" % c["pct"]


# ---- comandos: cada uno devuelve una lista de líneas ----

def cmd_limpieza(args):
    docs, total = cargar_docs()
    if args.doc:
        docs = [buscar_doc(docs, args.doc)]
    cab = "%-34s %4s %4s %4s %4s %5s" % ("documento", "✅", "🟡", "❓", "⏳", "%")
    out = []
    if not args.doc:
        out.append("%-34s %4d %4d %4d %4d %5s" % ("TOTAL", total["ok"], total["prop"], total["open"], total["wait"], _pct(total)))
        out.append("Meta: %d %% por documento · conexiones rotas: %d" % (total["target"], total["problems"]))
    out.append(cab)
    for d in docs:
        c = d["counts"]
        out.append("%-34s %4d %4d %4d %4d %5s" % (d["id"][:34], c["ok"], c["prop"], c["open"], d["clean"]["wait"], _pct(d["clean"])))
    return out


def cmd_abiertos(args):
    docs, _ = cargar_docs()
    if args.doc:
        docs = [buscar_doc(docs, args.doc)]
    out = []
    for d in docs:
        for it in d["clean"]["items"]:
            if args.tipo and args.tipo not in it["kinds"]:
                continue
            marcas = "".join(MARCAS[k] for k in it["kinds"])
            out.append("%s:%d %s [%s] %s" % (ruta_doc(d), it["line"], marcas, it["heading"][:40], it["text"][:140]))
    return out or ["Sin puntos abiertos."]


def cmd_indice(args):
    docs, _ = cargar_docs()
    d = buscar_doc(docs, args.doc)
    return ["%5d %s%s" % (n, "  " * (nivel - 1), t) for n, nivel, t in encabezados(d["md"])] or ["Sin encabezados."]


def cmd_seccion(args):
    docs, _ = cargar_docs()
    d = buscar_doc(docs, args.doc)
    return seccion_de(d["md"], args.texto)


def seccion_de(md, texto):
    if not texto.strip():
        raise Error("Indica el texto del encabezado; usa `indice` para verlos.")
    hs = encabezados(md)
    lineas = md.splitlines()
    for i, (n, nivel, t) in enumerate(hs):
        if texto.lower() in t.lower():
            fin = len(lineas) + 1
            for n2, nivel2, _ in hs[i + 1:]:
                if nivel2 <= nivel:
                    fin = n2
                    break
            return ["%5d  %s" % (k, lineas[k - 1]) for k in range(n, fin)]
    raise Error("Ningún encabezado contiene «%s». Usa `indice` para verlos." % texto)


def _tarea(tid):
    for t in tareas_todas():
        if t["id"] == tid:
            return t
    raise Error("No existe la tarea %s." % tid)


def linea_tarea(t):
    return "%s · %s · %s · %s" % (t["id"], t["status"], t.get("prio", "-"), t["title"])


def ficha_doc(d):
    c, cl = d["counts"], d["clean"]
    hs = encabezados(d["md"])
    out = ["%s · %s" % (d["id"], d["title"]), "Archivo: %s" % ruta_doc(d),
           "Limpieza: %s · ✅ %d · 🟡 %d · ❓ %d · ⏳ %d" % (_pct(cl), c["ok"], c["prop"], c["open"], cl["wait"]),
           "Encabezados: %d · líneas: %d" % (len(hs), len(d["md"].splitlines()))]
    n2 = [(n, t) for n, nivel, t in hs if nivel == 2]
    out.append("Secciones (nivel 2):")
    out += ["  %d %s" % (n, t[:70]) for n, t in n2[:8]]
    if len(n2) > 8:
        out.append("  … %d más (usa `indice`)" % (len(n2) - 8))
    out.append("Abiertos: %d" % len(cl["items"]))
    for it in cl["items"][:3]:
        out.append("  %d %s %s" % (it["line"], "".join(MARCAS[k] for k in it["kinds"]), it["text"][:90]))
    return out


def ficha_tarea(t):
    out = [linea_tarea(t), "Fase: %s · estimación: %s h" % (t["fase"], t.get("est", "-")),
           "Desc: %s" % (t.get("desc", "")[:200]), "Hecha cuando: %s" % (t.get("done_when", "")[:160])]
    ruta = build.TASKS_DIR / (t["id"] + ".json")
    pipe = json.loads(ruta.read_text(encoding="utf-8")).get("pipeline") if ruta.exists() else None
    if pipe:
        out.append("Pipeline (%s):" % pipe.get("especialista", "-"))
        out += ["  %-11s %s" % (e["etapa"], e["estado"]) for e in pipe.get("etapas", [])[:8]]
    else:
        out.append("Pipeline: sin registrar")
    return out


def cmd_ficha(args):
    if re.match(r"^F\d-\d{2,3}$", args.ref):
        return ficha_tarea(_tarea(args.ref))
    docs, _ = cargar_docs()
    return ficha_doc(buscar_doc(docs, args.ref))


def cmd_tarea(args):
    t = _tarea(args.id)
    return [linea_tarea(t), "  %s" % t.get("desc", "")[:200]]


def cmd_tareas(args):
    ts = tareas_todas()
    if args.estado:
        ts = [t for t in ts if t["status"] == args.estado]
    if args.fase:
        ts = [t for t in ts if t["fase"] == args.fase or t["id"].startswith(args.fase + "-")]
    return [linea_tarea(t) for t in ts] or ["Sin tareas con ese filtro."]


def _tam(v):
    return "%d claves" % len(v) if isinstance(v, dict) else "%d elementos" % len(v) if isinstance(v, list) else type(v).__name__


def _hijo(nodo, clave, ruta):
    if isinstance(nodo, dict) and clave in nodo:
        return nodo[clave]
    if isinstance(nodo, list):
        if clave.isdigit() and int(clave) < len(nodo):
            return nodo[int(clave)]
        for e in nodo:  # busca por id o name
            if isinstance(e, dict) and clave in (e.get("id"), e.get("name")):
                return e
    vecinas = list(nodo) if isinstance(nodo, dict) else ["0..%d" % (len(nodo) - 1)] if isinstance(nodo, list) and nodo else []
    if isinstance(nodo, list):
        vecinas += [str(e["id"]) for e in nodo if isinstance(e, dict) and "id" in e][:15]
    raise Error("No existe «%s» en «%s». Claves vecinas: %s" % (clave, ruta or "(raíz)", ", ".join(map(str, vecinas[:20])) or "ninguna"))


def listar(nodo):
    if isinstance(nodo, dict):
        return ["%s: %s" % (k, _tam(v)) for k, v in nodo.items()]
    return ["%d: %s%s" % (i, _tam(v), " (%s)" % v["id"] if isinstance(v, dict) and "id" in v else "") for i, v in enumerate(nodo)]


def navegar(world, ruta):
    nodo, camino = world, ""
    for clave in [p for p in ruta.split(".") if p]:
        nodo = _hijo(nodo, clave, camino)
        camino += ("." if camino else "") + clave
    return nodo


def cmd_mundo(args):
    ruta = args.ruta or ""
    world = json.loads((build.DATA / "world.json").read_text(encoding="utf-8"))
    nodo = navegar(world, ruta)
    compacto = json.dumps(nodo, ensure_ascii=False, separators=(",", ":"))
    if not isinstance(nodo, (dict, list)) or (ruta and len(compacto) <= 600):
        return [compacto]
    return listar(nodo)


def ayuda():
    return __doc__.strip().splitlines()


def crear_parser():
    ap = argparse.ArgumentParser(prog="consulta.py", add_help=False)
    ap.add_argument("--max", type=int, default=MAX_POR_DEFECTO)
    sub = ap.add_subparsers(dest="cmd")
    for nombre, fn, args in [
        ("limpieza", cmd_limpieza, [("doc", "?")]),
        ("abiertos", cmd_abiertos, [("doc", "?")]),
        ("indice", cmd_indice, [("doc", None)]),
        ("seccion", cmd_seccion, [("doc", None), ("texto", None)]),
        ("ficha", cmd_ficha, [("ref", None)]),
        ("tarea", cmd_tarea, [("id", None)]),
        ("tareas", cmd_tareas, []),
        ("mundo", cmd_mundo, [("ruta", "?")]),
    ]:
        p = sub.add_parser(nombre, add_help=False)
        p.add_argument("--max", type=int, default=argparse.SUPPRESS)
        for a, nargs in args:
            p.add_argument(a, nargs=nargs) if nargs else p.add_argument(a)
        if nombre == "abiertos":
            p.add_argument("--tipo", choices=["prop", "open", "wait"])
        if nombre == "tareas":
            p.add_argument("--estado", choices=build.VALID_STATUS)
            p.add_argument("--fase")
        p.set_defaults(fn=fn)
    return ap


def main(argv=None):
    ap = crear_parser()
    try:
        args = ap.parse_args(argv)
    except SystemExit as e:
        if e.code:
            print("Uso incorrecto. Ejecuta `python3 tools/consulta.py` para ver la ayuda.", file=sys.stderr)
            return 1
        raise
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # emojis en consolas Windows
    if not args.cmd:
        print("\n".join(ayuda()))
        return 0
    if args.max < 1:
        print("Error: --max debe ser 1 o mayor.", file=sys.stderr)
        return 1
    try:
        lineas = args.fn(args)
    except Error as e:
        print("Error: %s" % e, file=sys.stderr)
        return 1
    if len(lineas) > args.max:
        lineas = lineas[:args.max] + ["… %d líneas más (usa --max N)" % (len(lineas) - args.max)]
    print("\n".join(lineas))
    return 0


if __name__ == "__main__":
    sys.exit(main())
