#!/usr/bin/env python3
"""Genera studio/hub/data.js a partir de los documentos, el roadmap, la actividad
de cada tarea (historial, comentarios y evidencias) y los assets de referencia.

Uso:
    python3 studio/hub/build.py            # genera y muestra avisos
    python3 studio/hub/build.py --strict   # falla (código 1) si hay avisos

Sin dependencias externas. Todo el estado vive en archivos de datos:
  - studio/data/roadmap.json        plan y estado actual de cada tarea
  - studio/data/tasks/<ID>.json     historial, comentarios y evidencias de la tarea
  - studio/evidence/<ID>/...        archivos de evidencia

Regla de coherencia: si el estado de una tarea no es "backlog", debe existir su
archivo de actividad y el último movimiento del historial debe llevar a ese estado.
Así, que una tarea esté "En proceso" siempre implica que alguien editó sus datos.
"""
import datetime
import json
import pathlib
import re
import sys

HUB = pathlib.Path(__file__).resolve().parent
STUDIO = HUB.parent
DOCS = STUDIO / "docs"
DATA = STUDIO / "data"
TASKS_DIR = DATA / "tasks"
EVIDENCE = STUDIO / "evidence"

VALID_STATUS = ["backlog", "sprint", "doing", "review", "done", "dropped"]
VALID_PRIO = ["P0", "P1", "P2", "P3"]
MAX_EST = 20  # una tarea más grande debe desglosarse
VALID_EVIDENCE = ["image", "link", "note", "file", "doc"]
VALID_AUTHORS = ["autor", "claude"]
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

GROUPS = [
    ("Diseño del juego", ["00", "01", "02", "03", "04", "09"]),
    ("Mundo y narrativa", ["05", "07", "08"]),
    ("Marca y arte", ["12", "13"]),
    ("Técnico y legal", ["10", "11"]),
    ("Plan y decisiones", ["06"]),
]

warnings = []


def warn(msg):
    warnings.append(msg)
    print("AVISO:", msg)


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print("ERROR leyendo %s: %s" % (path, exc))
        sys.exit(1)


def build_docs():
    docs = []
    for path in sorted(DOCS.glob("[0-9][0-9]-*.md")):
        text = path.read_text(encoding="utf-8")
        match = re.search(r"^#\s+(.+)$", text, re.M)
        title = match.group(1).strip() if match else path.stem
        prefix = path.stem[:2]
        group = next((g for g, ids in GROUPS if prefix in ids), "Otros")
        docs.append(
            {
                "id": path.stem,
                "title": title,
                "group": group,
                "md": text,
                "counts": {
                    "ok": text.count("✅"),
                    "prop": text.count("🟡"),
                    "open": text.count("❓"),
                },
            }
        )
    return docs


def load_activity():
    activity = {}
    if not TASKS_DIR.exists():
        return activity
    for path in sorted(TASKS_DIR.glob("*.json")):
        data = load_json(path)
        tid = data.get("id")
        if tid != path.stem:
            warn("El archivo %s declara id %s" % (path.name, tid))
        activity[path.stem] = data
    return activity


def check_activity(tid, status, act):
    """Valida historial, comentarios y evidencias de una tarea."""
    hist = act.get("history", [])
    if status != "backlog":
        if not hist:
            warn("%s está en '%s' pero no tiene historial" % (tid, status))
        elif hist[-1].get("to") != status:
            warn(
                "%s: el estado del roadmap ('%s') no coincide con el último movimiento ('%s')"
                % (tid, status, hist[-1].get("to"))
            )
    prev = "backlog"
    for i, h in enumerate(hist):
        if h.get("from") != prev:
            warn("%s: el movimiento %d parte de '%s' pero el anterior terminó en '%s'" % (tid, i + 1, h.get("from"), prev))
        for key in ("from", "to"):
            if h.get(key) not in VALID_STATUS:
                warn("%s: estado inválido '%s' en el historial" % (tid, h.get(key)))
        if not DATE_RE.match(str(h.get("at", ""))):
            warn("%s: fecha inválida en el historial: %s" % (tid, h.get("at")))
        if not h.get("note"):
            warn("%s: movimiento %d sin nota" % (tid, i + 1))
        prev = h.get("to", prev)
    for c in act.get("comments", []):
        if c.get("by") not in VALID_AUTHORS:
            warn("%s: autor de comentario inválido: %s" % (tid, c.get("by")))
        if not DATE_RE.match(str(c.get("at", ""))):
            warn("%s: fecha inválida en un comentario" % tid)
    for e in act.get("evidence", []):
        kind = e.get("type")
        if kind not in VALID_EVIDENCE:
            warn("%s: tipo de evidencia inválido: %s" % (tid, kind))
            continue
        if kind in ("image", "file"):
            rel = e.get("path", "")
            if not rel or not (STUDIO / rel).exists():
                warn("%s: falta el archivo de evidencia %s" % (tid, rel))
            e["exists"] = bool(rel) and (STUDIO / rel).exists()


def check_roadmap(roadmap, activity):
    seen = set()
    targets = roadmap["meta"]["targets"]
    for phase in roadmap["phases"]:
        if phase["target"] not in targets:
            warn("Fase %s con objetivo desconocido: %s" % (phase["id"], phase["target"]))
        for ms in phase["milestones"]:
            for task in ms["tasks"]:
                tid = task["id"]
                if tid in seen:
                    warn("ID de tarea repetido: %s" % tid)
                seen.add(tid)
                if task["status"] not in VALID_STATUS:
                    warn("Estado inválido en %s: %s" % (tid, task["status"]))
                if task.get("target") and task["target"] not in targets:
                    warn("Objetivo inválido en %s: %s" % (tid, task["target"]))
                if "est" not in task:
                    warn("Falta 'est' en %s" % tid)
                elif task["est"] > MAX_EST:
                    warn("%s tiene %s h: desglosar (máximo %s h por tarea)" % (tid, task["est"], MAX_EST))
                if task.get("prio") not in VALID_PRIO:
                    warn("Prioridad inválida o ausente en %s: %s" % (tid, task.get("prio")))
                act = activity.get(tid, {})
                check_activity(tid, task["status"], act)
                task["history"] = act.get("history", [])
                task["comments"] = act.get("comments", [])
                task["evidence"] = act.get("evidence", [])
    for tid in activity:
        if tid not in seen:
            warn("Hay actividad para una tarea que no existe en el roadmap: %s" % tid)


def build_assets(assets):
    for img in assets["images"]:
        path = STUDIO / img["file"]
        img["exists"] = path.exists()
        if not img["exists"]:
            warn("Falta el archivo: %s" % img["file"])
        else:
            img["kb"] = round(path.stat().st_size / 1024)
    audio = []
    audio_dir = STUDIO / "assets-ref" / "audio"
    if audio_dir.exists():
        for p in sorted(audio_dir.rglob("*")):
            if p.suffix.lower() in (".mp3", ".wav", ".ogg"):
                audio.append({"file": str(p.relative_to(STUDIO)), "name": p.stem})
    assets["audio"] = audio
    return assets


def main():
    strict = "--strict" in sys.argv
    roadmap = load_json(DATA / "roadmap.json")
    activity = load_activity()
    check_roadmap(roadmap, activity)
    hub = {
        "generated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "config": load_json(DATA / "config.json"),
        "docs": build_docs(),
        "groups": [g for g, _ in GROUPS],
        "roadmap": roadmap,
        "assets": build_assets(load_json(DATA / "assets.json")),
        "palette": load_json(DATA / "palette.json"),
    }
    out = HUB / "data.js"
    out.write_text(
        "// Archivo generado por build.py. No editar a mano.\nwindow.HUB = "
        + json.dumps(hub, ensure_ascii=False)
        + ";\n",
        encoding="utf-8",
    )
    tasks = [t for p in roadmap["phases"] for m in p["milestones"] for t in m["tasks"]]
    counts = {}
    for t in tasks:
        counts[t["status"]] = counts.get(t["status"], 0) + 1
    resumen = ", ".join("%s: %d" % (s, counts[s]) for s in VALID_STATUS if s in counts)
    print(
        "OK: %d documentos, %d tareas (%s), %d imágenes -> %s"
        % (len(hub["docs"]), len(tasks), resumen, len(hub["assets"]["images"]), out.relative_to(STUDIO.parent))
    )
    if warnings:
        print("%d aviso(s)." % len(warnings))
        if strict:
            sys.exit(1)


if __name__ == "__main__":
    main()
