#!/usr/bin/env python3
"""Registro de sesiones de trabajo: número correlativo y nombre claro.

  python3 tools/sesion.py nueva "F0-25 Flujo de pantallas"   -> registra y muestra «S-02 · F0-25 Flujo de pantallas»
  python3 tools/sesion.py lista                               -> muestra todas
  python3 tools/sesion.py siguiente                           -> muestra el próximo número sin registrar

El registro vive en studio/data/sesiones.json (solo biblioteca estándar).
"""
import json
import sys
from datetime import date
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "studio" / "data" / "sesiones.json"


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
    Path(ruta).write_text(json.dumps(datos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return sesion


def main(argv):
    orden = argv[1] if len(argv) > 1 else "lista"
    datos = cargar()
    if orden == "nueva" and len(argv) > 2:
        print(titulo(nueva(" ".join(argv[2:]))))
    elif orden == "siguiente":
        print("S-%02d" % siguiente(datos))
    elif orden == "lista":
        for s in datos["sesiones"]:
            print("%s  (%s)" % (titulo(s), s["fecha"]))
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
