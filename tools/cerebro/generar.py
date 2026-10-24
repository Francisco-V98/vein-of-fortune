#!/usr/bin/env python3
"""Orquestador del cerebro: ejecuta los módulos, resuelve los enlaces y escribe el vault.

Uso:
    python3 tools/cerebro/generar.py [--destino DIR] [--sin-plantilla]

`generar_vault(repo, destino)` es lo que llama studio/hub/build.py. Cada módulo es `mod_<nombre>.py` con
`generar(registro, repo)`; para añadir uno, crea el archivo y añade su nombre a `MODULOS`.
"""
import importlib
import pathlib
import sys
import time
import traceback

if __package__ in (None, ""):  # ejecución directa: `python3 tools/cerebro/generar.py`
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
    __package__ = "cerebro"

from . import nucleo  # noqa: E402

# Orden de ejecución: los módulos posteriores pueden contar con los IDs de los anteriores (documentos, tareas).
MODULOS = ["documentos", "tareas", "equipo", "memoria", "mundo", "economia", "narrativa", "qa", "simulador", "glosario", "arte"]
PLANTILLA = pathlib.Path(__file__).resolve().parent / "obsidian"


class Resultado:
    def __init__(self):
        self.avisos, self.info, self.conteo = [], [], {}
        self.notas = self.escritos = self.sin_cambio = self.borrados = 0
        self.segundos = 0.0


def construir_registro(repo, modulos=None, opciones=None):
    """Ejecuta los módulos sobre un registro nuevo. Un módulo que falla se avisa y se sigue con el resto."""
    registro = nucleo.Registro(opciones)
    for nombre in modulos if modulos is not None else MODULOS:
        try:
            modulo = importlib.import_module("." + ("mod_" + nombre if isinstance(nombre, str) else nombre.__name__), __package__) \
                if isinstance(nombre, str) else nombre
            modulo.generar(registro, pathlib.Path(repo))
        except Exception as exc:  # noqa: BLE001 - un módulo roto no debe tirar el resto del vault
            ultima = traceback.extract_tb(exc.__traceback__)[-1]
            registro.aviso("el módulo %s falló: %s (%s:%d)" % (nombre, exc, pathlib.Path(ultima.filename).name, ultima.lineno))
    return registro


def generar_vault(repo, destino, modulos=None, plantilla=PLANTILLA, opciones=None):
    """Regenera el vault `destino` desde `repo`. Devuelve un `Resultado`; no lanza por datos incompletos."""
    t0 = time.time()
    repo, destino = pathlib.Path(repo).resolve(), pathlib.Path(destino)
    registro = construir_registro(repo, modulos, opciones)
    archivos = registro.construir()
    nucleo.preparar_vault(destino, plantilla)
    res = Resultado()
    res.escritos, res.sin_cambio, res.borrados = nucleo.escribir(destino, archivos)
    res.avisos, res.info = list(registro.avisos), list(registro.info)
    res.conteo, res.notas = registro.conteo(), len(registro.notas)
    res.segundos = time.time() - t0
    return res


def main(argv):
    repo = pathlib.Path(__file__).resolve().parents[2]
    destino = repo / "studio" / "cerebro"
    if "--destino" in argv:
        destino = pathlib.Path(argv[argv.index("--destino") + 1])
    res = generar_vault(repo, destino, plantilla=None if "--sin-plantilla" in argv else PLANTILLA)
    for linea in res.info:
        print(linea)
    for aviso in res.avisos:
        print("AVISO:", aviso)
    print("Cerebro: %d notas (%s) en %.1f s -> %s" % (res.notas, ", ".join("%s %d" % kv for kv in sorted(res.conteo.items())), res.segundos, destino))
    return 1 if res.avisos and "--strict" in argv else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
