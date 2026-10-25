#!/usr/bin/env python3
"""Registro de sesiones de trabajo: número correlativo y nombre claro.

  python3 tools/sesion.py nueva "F0-25 Flujo de pantallas"   -> registra y muestra «S-02 · F0-25 Flujo de pantallas»
  python3 tools/sesion.py nueva "Vistas del hub (F0-74, F0-75)" -> un bloque de tareas afines: «S-NN · <bloque o tema> (<IDs>)»
  python3 tools/sesion.py lista                               -> muestra todas
  python3 tools/sesion.py siguiente                           -> muestra el próximo número sin registrar
  python3 tools/sesion.py resumen 2 "Qué hizo" --tareas F0-25,F2-41 --pr 66 --docs 30 --decisiones "una|otra"
                                                              -> guarda qué hizo la sesión (añade a lo que ya hubiera)
  python3 tools/sesion.py ver 2                               -> detalle de una sesión
  python3 tools/sesion.py buscar F0-25                        -> sesiones que mencionan un texto, tarea, PR o documento
  python3 tools/sesion.py md                                  -> regenera studio/SESIONES.md (también lo hace `resumen`)

El registro vive en studio/data/sesiones.json (solo biblioteca estándar).
"""
import json
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RUTA = RAIZ / "studio" / "data" / "sesiones.json"
RUTA_MD = RAIZ / "studio" / "SESIONES.md"
CAMPOS_LISTA = ("tareas", "prs", "docs", "decisiones")


def cargar(ruta=RUTA):
    if not Path(ruta).exists():
        return {"sesiones": []}
    return json.loads(Path(ruta).read_text(encoding="utf-8"))


def titulo(sesion):
    return "S-%02d · %s" % (sesion["n"], sesion["tema"])


def siguiente(datos):
    return max([s["n"] for s in datos["sesiones"]] or [0]) + 1


def nueva(tema, ruta=RUTA, hoy=None):
    tema = " ".join(tema.split())
    if not tema:
        raise ValueError("la sesión necesita un tema")
    datos = cargar(ruta)
    sesion = {"n": siguiente(datos), "tema": tema, "fecha": hoy or date.today().isoformat()}
    datos["sesiones"].append(sesion)
    guardar(datos, ruta)
    return sesion


def guardar(datos, ruta=RUTA):
    Path(ruta).write_text(json.dumps(datos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def buscar_sesion(datos, n):
    for s in datos["sesiones"]:
        if s["n"] == n:
            return s
    raise ValueError("no existe la sesión S-%02d" % n)


def _sin_repetir(actual, nuevos):
    return actual + [x for x in nuevos if x not in actual]


def resumen(n, texto=None, tareas=(), prs=(), docs=(), decisiones=(), ruta=RUTA):
    """Guarda qué hizo la sesión; lo ya anotado se conserva y las listas no repiten."""
    datos = cargar(ruta)
    s = buscar_sesion(datos, n)
    if texto:
        s["resumen"] = " ".join(texto.split())
    for campo, nuevos in zip(CAMPOS_LISTA, (tareas, prs, docs, decisiones)):
        nuevos = [str(x).strip() for x in nuevos if str(x).strip()]
        if nuevos or campo in s:
            s[campo] = _sin_repetir(s.get(campo, []), nuevos)
    guardar(datos, ruta)
    return s


def detalle(s):
    lineas = [titulo(s) + "  (%s)" % s["fecha"]]
    if s.get("resumen"):
        lineas.append("Qué hizo: " + s["resumen"])
    for etiqueta, campo, union in (("Tareas", "tareas", ", "), ("PR", "prs", ", #"), ("Documentos", "docs", ", ")):
        if s.get(campo):
            prefijo = "#" if campo == "prs" else ""
            lineas.append("%s: %s%s" % (etiqueta, prefijo, union.join(s[campo])))
    for d in s.get("decisiones", []):
        lineas.append("  · " + d)
    return "\n".join(lineas)


def buscar(datos, texto):
    t = texto.lower().lstrip("#")
    return [s for s in datos["sesiones"] if t in json.dumps(s, ensure_ascii=False).lower()]


def markdown(datos):
    salida = [
        "# Registro de sesiones",
        "",
        "Generado por `python3 tools/sesion.py md` desde `studio/data/sesiones.json`; no lo edites a mano.",
        "Para saber qué se hizo en una sesión: `python3 tools/sesion.py ver N` o `buscar <tarea, PR o texto>`.",
        "",
        "| Sesión | Fecha | Tareas | PR | Qué hizo |",
        "|---|---|---|---|---|",
    ]
    for s in datos["sesiones"]:
        salida.append("| %s | %s | %s | %s | %s |" % (
            titulo(s), s["fecha"], ", ".join(s.get("tareas", [])) or "—",
            ", ".join("#%s" % p for p in s.get("prs", [])) or "—",
            (s.get("resumen") or "—").replace("|", "/")))
    for s in datos["sesiones"]:
        if s.get("decisiones") or s.get("docs"):
            salida += ["", "## " + titulo(s)]
            if s.get("docs"):
                salida.append("- Documentos: " + ", ".join(s["docs"]))
            salida += ["- " + d for d in s.get("decisiones", [])]
    return "\n".join(salida) + "\n"


def escribir_md(ruta=RUTA_MD, datos=None):
    Path(ruta).write_text(markdown(datos or cargar()), encoding="utf-8")


def _numero(texto):
    try:
        return int(texto.lstrip("Ss-"))
    except ValueError:
        raise ValueError("número de sesión no válido: %s" % texto) from None


def _lista(valor):
    return [x for x in (valor or "").replace("|", ",").split(",") if x.strip()]


def main(argv):
    orden = argv[1] if len(argv) > 1 else "lista"
    datos = cargar()
    if orden == "nueva" and len(argv) > 2:
        print(titulo(nueva(" ".join(argv[2:]))))
    elif orden == "siguiente":
        print("S-%02d" % siguiente(datos))
    elif orden == "resumen" and len(argv) > 3:
        args = argv[3:]
        extra = {}
        texto = []
        i = 0
        while i < len(args):
            if args[i] in ("--tareas", "--pr", "--docs", "--decisiones") and i + 1 < len(args):
                extra[args[i]] = args[i + 1]
                i += 2
            else:
                texto.append(args[i])
                i += 1
        decisiones = [d.strip() for d in extra.get("--decisiones", "").split("|") if d.strip()]
        s = resumen(_numero(argv[2]), " ".join(texto) or None, _lista(extra.get("--tareas")),
                    _lista(extra.get("--pr")), _lista(extra.get("--docs")), decisiones)
        escribir_md()
        print(detalle(s))
    elif orden == "ver" and len(argv) > 2:
        print(detalle(buscar_sesion(datos, _numero(argv[2]))))
    elif orden == "buscar" and len(argv) > 2:
        encontradas = buscar(datos, " ".join(argv[2:]))
        for s in encontradas:
            print("%s  (%s)" % (titulo(s), s["fecha"]))
        if not encontradas:
            print("Ninguna sesión menciona eso.")
    elif orden == "md":
        escribir_md()
        print("Escrito %s" % RUTA_MD.relative_to(RAIZ))
    elif orden == "lista":
        for s in datos["sesiones"]:
            print("%s  (%s)" % (titulo(s), s["fecha"]))
    else:
        print(__doc__)
        return 1
    return 0


def ejecutar(argv):
    try:
        return main(argv)
    except ValueError as error:
        print("Error: %s" % error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(ejecutar(sys.argv))
