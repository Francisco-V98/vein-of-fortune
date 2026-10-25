#!/usr/bin/env python3
"""Sincroniza .claude/agents/<agente>.md con studio/data/equipo.json.

Para cada rol con `agente` actualiza en el frontmatter `model:` y `effort:`
(conserva name, description y tools) y mantiene, entre los marcadores
BLOQUE-COMUN, el bloque de ahorro de tokens idéntico en todos los agentes.
Sustituye la sección larga «Decidir ahora o aplazar» (conserva el texto propio
de cada rol que la acompañe). Con --comprobar no escribe y devuelve 1 si algo
no coincide. Solo usa la biblioteca estándar.
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
INICIO = "<!-- BLOQUE-COMUN:inicio -->"
FIN = "<!-- BLOQUE-COMUN:fin -->"
BLOQUE = """## Cómo trabajar y reportar (ahorro de tokens)
- Lee lo mínimo: usa grep y rangos (offset y limit) antes de leer un documento entero; no leas studio/hub/data.js ni studio/data/sim/resultados.json enteros; usa tools/consulta.py (limpieza, abiertos, indice, seccion, ficha, tarea, mundo).
- No repitas lecturas completas de los documentos grandes (18, 21, 23, 25, 27, 28): lee solo la sección que necesitas.
- Si el encargo apunta a un archivo de briefing, léelo una vez y no lo copies.
- Informe final breve (máximo 60 líneas y 6.000 caracteres): Resultado (2 o 3 líneas), Archivos tocados, Hallazgos o cambios en tabla con archivo:línea, y Dudas para el autor. No repitas el encargo ni copies texto de los documentos.
- Regla de «decidir ahora o aplazar» (documento 15): un ⏳ solo apunta a una tarea que exista y no esté terminada, y solo si nada de lo ya hecho depende de ello; si no, se decide ahora con el autor.
- Tutorial y onboarding (decisión del autor, 2026-10-24): todo proceso que el jugador hace por primera vez y todo paso obligatorio para avanzar lleva tutorial guiado y compuerta (nada se puede saltar, nunca softlock); en tu entregable di qué se aprende, cómo se enseña, qué lo exige y qué pasa si falla, y avisa si algo choca con el tutorial."""
BLOQUE_MARCADO = "%s\n%s\n%s" % (INICIO, BLOQUE, FIN)

_BASE = ("Solo se aplaza (⏳) un punto abierto si una tarea ya existente lo va a resolver Y nada que se "
         "escriba o construya antes de esa tarea depende de la respuesta. Pregunta de control: «si la "
         "respuesta cambia después, ¿hay que rehacer algo ya hecho?». Si la respuesta es sí, se decide "
         "ahora con el autor, antes de producir.")
_ESTANDAR = (" No aplaces por comodidad lo que el analista marcó como «decidir ahora»: pídelo al "
             "coordinador para que lo decida el autor.")
_SECCION_VIEJA = re.compile(r"^## Decidir ahora o aplazar\n\n" + re.escape(_BASE) + r"([^\n]*)\n?", re.M)
_FRONT = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def cargar_equipo(root=ROOT):
    return json.loads((root / "studio/data/equipo.json").read_text(encoding="utf-8"))


def partir_frontmatter(texto):
    """Devuelve (líneas del frontmatter, cuerpo) o (None, texto)."""
    m = _FRONT.match(texto)
    if not m:
        return None, texto
    return m.group(1).split("\n"), texto[m.end():]


def valor_front(lineas, clave):
    for linea in lineas or []:
        if linea.startswith(clave + ":"):
            return linea.split(":", 1)[1].strip()
    return None


def _fijar(lineas, clave, valor, despues):
    nueva = "%s: %s" % (clave, valor)
    sin = [l for l in lineas if not l.startswith(clave + ":")]
    idx = next((i for i, l in enumerate(sin) if l.startswith(despues + ":")), len(sin) - 1)
    if valor_front(lineas, clave) is not None:
        return [nueva if l.startswith(clave + ":") else l for l in lineas]
    sin.insert(idx + 1, nueva)
    return sin


def sincronizar_texto(texto, modelo, esfuerzo):
    lineas, cuerpo = partir_frontmatter(texto)
    if lineas is None:
        raise ValueError("el agente no tiene frontmatter")
    lineas = _fijar(lineas, "model", modelo, "tools")
    lineas = _fijar(lineas, "effort", esfuerzo, "model")
    cuerpo = _poner_bloque(cuerpo)
    return "---\n%s\n---\n%s" % ("\n".join(lineas), cuerpo)


def _poner_bloque(cuerpo):
    if INICIO in cuerpo and FIN in cuerpo:
        ini = cuerpo.index(INICIO)
        fin = cuerpo.index(FIN) + len(FIN)
        return cuerpo[:ini] + BLOQUE_MARCADO + cuerpo[fin:]
    m = _SECCION_VIEJA.search(cuerpo)
    if m:
        extra = m.group(1).rstrip()
        if extra == _ESTANDAR.rstrip():
            extra = ""
        resto = cuerpo[m.end():].strip("\n")
        cola = "\n\n".join(p for p in (extra.strip(), resto) if p)
        antes = cuerpo[:m.start()].rstrip("\n")
        return antes + "\n\n" + BLOQUE_MARCADO + ("\n\n" + cola if cola else "") + "\n"
    return cuerpo.rstrip("\n") + "\n\n" + BLOQUE_MARCADO + "\n"


def agentes(equipo):
    return [(r["agente"], r.get("modelo"), r.get("esfuerzo")) for r in equipo.get("roles", []) if r.get("agente")]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--comprobar", action="store_true", help="no escribe; código 1 si algo no coincide")
    ap.add_argument("--raiz", default=str(ROOT), help="raíz del repositorio (para pruebas)")
    args = ap.parse_args(argv)
    root = pathlib.Path(args.raiz)
    desfase = 0
    for agente, modelo, esfuerzo in agentes(cargar_equipo(root)):
        ruta = root / ".claude" / "agents" / ("%s.md" % agente)
        if not ruta.exists():
            print("FALTA %s" % ruta)
            desfase += 1
            continue
        if not modelo or not esfuerzo:
            print("SIN modelo o esfuerzo en equipo.json: %s" % agente)
            desfase += 1
            continue
        viejo = ruta.read_text(encoding="utf-8")
        nuevo = sincronizar_texto(viejo, modelo, esfuerzo)
        if nuevo != viejo:
            desfase += 1
            if args.comprobar:
                print("DESINCRONIZADO %s" % ruta.name)
            else:
                ruta.write_text(nuevo, encoding="utf-8")
                print("actualizado %s" % ruta.name)
    if args.comprobar and desfase:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
