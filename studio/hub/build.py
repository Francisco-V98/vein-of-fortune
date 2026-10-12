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
  - studio/data/qa/cases.json       catálogo de casos de prueba y sus resultados
  - studio/data/qa/bugs/BUG-*.json  registro de errores
  - studio/data/presentation.json   láminas de la página «El juego» (resumen curado del diseño)
  - studio/data/story.json          mapa de historia: actos, carriles y tareas relacionadas
  - studio/data/world.json          registro del mundo: minerales, zonas, minijuegos, recetas, facciones y personajes

Limpieza del diseño (ver studio/docs/15-flujo-de-trabajo-y-calidad.md):
  limpieza = ✅ / (✅ + 🟡 + ❓)  por documento y en total. Meta: lo más cerca posible de 100 %.
  ⏳ <ID de tarea> marca algo que depende de una tarea posterior: no resta limpieza, pero
  debe nombrar una tarea que exista y que no esté terminada.
  Además se revisan las conexiones: enlaces entre documentos y referencias a tareas.

Regla de coherencia: si el estado de una tarea no es "backlog", debe existir su
archivo de actividad y el último movimiento del historial debe llevar a ese estado.
Así, que una tarea esté "En proceso" siempre implica que alguien editó sus datos.
"""
import datetime
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import coherence  # noqa: E402

HUB = pathlib.Path(__file__).resolve().parent
STUDIO = HUB.parent
DOCS = STUDIO / "docs"
DATA = STUDIO / "data"
TASKS_DIR = DATA / "tasks"
EVIDENCE = STUDIO / "evidence"

VALID_STATUS = ["backlog", "sprint", "doing", "review", "qa", "done", "dropped"]
VALID_PRIO = ["P0", "P1", "P2", "P3"]
MAX_EST = 20  # una tarea más grande debe desglosarse
SLIDE_LAYOUTS = [
    "cover", "agenda", "section", "statement", "specs", "cards", "day", "cycle", "showcase", "market", "ladder", "meter",
    "flow", "scale", "map", "crops", "feature", "acts", "palette", "mosaic", "brand", "arch", "plan", "status", "checklist", "closing",
]
VALID_RESULT = ["not-run", "pass", "fail", "blocked", "skipped"]
VALID_SEVERITY = ["S1", "S2", "S3", "S4"]
VALID_BUG_STATUS = ["abierto", "triaje", "en-correccion", "corregido", "verificado", "cerrado", "no-se-corrige"]
VALID_EVIDENCE = ["image", "link", "note", "file", "doc"]
VALID_AUTHORS = ["autor", "claude"]
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

GROUPS = [
    ("Diseño del juego", ["00", "01", "02", "03", "04", "09"]),
    ("Mundo y narrativa", ["05", "07", "08", "17", "19"]),
    ("Marca y arte", ["12", "13"]),
    ("Técnico y legal", ["10", "11"]),
    ("Arquitectura y calidad", ["14", "15"]),
    ("Plan y decisiones", ["06"]),
]
ADR_GROUP = "Decisiones de arquitectura (ADR)"

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
    for path in sorted((DOCS / "adr").glob("[0-9][0-9][0-9][0-9]-*.md")) if (DOCS / "adr").exists() else []:
        text = path.read_text(encoding="utf-8")
        match = re.search(r"^#\s+(.+)$", text, re.M)
        docs.append(
            {
                "id": "adr-" + path.stem,
                "title": match.group(1).strip() if match else path.stem,
                "group": ADR_GROUP,
                "md": text,
                "counts": {"ok": text.count("✅"), "prop": text.count("🟡"), "open": text.count("❓")},
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
        if "ref" in h and not isinstance(h["ref"], str):
            warn("%s: el campo 'ref' del movimiento %d debe ser texto (rama, PR o commit)" % (tid, i + 1))
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


def load_qa(task_ids):
    """Carga y valida el catálogo de casos de prueba y el registro de errores."""
    qa = {"areas": [], "types": [], "cases": [], "bugs": []}
    path = DATA / "qa" / "cases.json"
    if path.exists():
        data = load_json(path)
        qa["areas"] = data.get("areas", [])
        qa["types"] = data.get("types", [])
        seen = set()
        for c in data.get("cases", []):
            cid = c.get("id", "?")
            if cid in seen:
                warn("Caso de prueba repetido: %s" % cid)
            seen.add(cid)
            if c.get("area") not in qa["areas"]:
                warn("%s: área desconocida: %s" % (cid, c.get("area")))
            if c.get("prio") not in VALID_PRIO:
                warn("%s: prioridad inválida: %s" % (cid, c.get("prio")))
            if not c.get("steps") or not c.get("expected"):
                warn("%s: debe tener pasos y resultado esperado" % cid)
            status = c.get("result", {}).get("status")
            if status not in VALID_RESULT:
                warn("%s: resultado inválido: %s" % (cid, status))
            elif status != "not-run" and not c["result"].get("at"):
                warn("%s: un resultado ejecutado debe llevar fecha" % cid)
            for tid in c.get("tasks", []):
                if tid not in task_ids:
                    warn("%s cita una tarea inexistente: %s" % (cid, tid))
            qa["cases"].append(c)
    bugs_dir = DATA / "qa" / "bugs"
    for bp in sorted(bugs_dir.glob("BUG-*.json")) if bugs_dir.exists() else []:
        b = load_json(bp)
        if b.get("id") != bp.stem:
            warn("El archivo %s declara id %s" % (bp.name, b.get("id")))
        if b.get("severity") not in VALID_SEVERITY:
            warn("%s: severidad inválida: %s" % (bp.stem, b.get("severity")))
        if b.get("status") not in VALID_BUG_STATUS:
            warn("%s: estado inválido: %s" % (bp.stem, b.get("status")))
        if b.get("task") and b["task"] not in task_ids:
            warn("%s cita una tarea inexistente: %s" % (bp.stem, b["task"]))
        for k in ("title", "steps", "expected", "actual"):
            if not b.get(k):
                warn("%s: falta '%s'" % (bp.stem, k))
        qa["bugs"].append(b)
    return qa


def _walk_files(node):
    """Rutas de imagen (claves 'file' e 'image') dentro de una lámina o sección."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k in ("file", "image") and isinstance(v, str):
                yield v
            else:
                yield from _walk_files(v)
    elif isinstance(node, list):
        for v in node:
            yield from _walk_files(v)


def load_presentation(doc_ids):
    """Carga y valida las láminas de la presentación del juego."""
    path = DATA / "presentation.json"
    if not path.exists():
        return {"sections": [], "slides": []}
    data = load_json(path)
    sections = data.get("sections", [])
    section_ids = set()
    for sec in sections:
        section_ids.add(sec.get("id"))
        for key in ("id", "n", "title", "blurb", "accent", "image"):
            if not sec.get(key):
                warn("Sección %s sin '%s'" % (sec.get("id", "?"), key))
    seen = set()
    for s in data.get("slides", []):
        sid = s.get("id", "?")
        if sid in seen:
            warn("Lámina repetida: %s" % sid)
        seen.add(sid)
        layout = s.get("layout")
        if layout not in SLIDE_LAYOUTS:
            warn("Lámina %s con diseño desconocido: %s" % (sid, layout))
        if s.get("section") and s["section"] not in section_ids:
            warn("La lámina %s usa una sección inexistente: %s" % (sid, s["section"]))
        if layout not in ("section", "statement", "cover", "closing") and not s.get("title"):
            warn("La lámina %s no tiene título" % sid)
        if layout not in ("cover", "agenda", "closing") and not s.get("section"):
            warn("La lámina %s no pertenece a ninguna sección" % sid)
        for src in s.get("source", []):
            if src not in doc_ids:
                warn("La lámina %s cita un documento inexistente: %s" % (sid, src))
        for f in _walk_files(s):
            if not (STUDIO / f).exists():
                warn("La lámina %s usa una imagen que no existe: %s" % (sid, f))
    for f in _walk_files(sections):
        if not (STUDIO / f).exists():
            warn("Una sección usa una imagen que no existe: %s" % f)
    return {"sections": sections, "slides": data.get("slides", [])}


CLEAN_TARGET = 90  # meta orientativa de limpieza por documento (%)
WAIT_RE = re.compile(r"\u23f3\s*(F\d-\d{2,3})")
TASK_REF_RE = re.compile(r"\bF\d-\d{2,3}\b")
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")


def analyze_docs(docs, task_status):
    """Calcula la limpieza y las conexiones de cada documento (ver docstring)."""
    totals = {"ok": 0, "prop": 0, "open": 0, "wait": 0}
    problems_total = 0
    for doc in docs:
        in_code, heading = False, ""
        counts = {"ok": 0, "prop": 0, "open": 0, "wait": 0}
        items, problems = [], []
        for n, line in enumerate(doc["md"].splitlines(), start=1):
            if line.strip().startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            if line.startswith("#"):
                heading = line.lstrip("# ").strip()
            line = re.sub(r"`[^`]*`", "", line)  # los ejemplos entre comillas invertidas no cuentan
            counts["ok"] += line.count("✅")
            counts["prop"] += line.count("🟡")
            counts["open"] += line.count("❓")
            waits = WAIT_RE.findall(line)
            counts["wait"] += line.count("\u23f3")
            kinds = [k for k, m in (("prop", "🟡"), ("open", "❓"), ("wait", "\u23f3")) if m in line]
            if kinds:
                text = re.sub(r"[*_`]", "", line).strip(" |-•")
                items.append({"line": n, "kinds": kinds, "heading": heading, "text": text[:220]})
            if "\u23f3" in line:
                if not waits:
                    problems.append("línea %d: ⏳ sin tarea de la que dependa" % n)
                for tid in waits:
                    if tid not in task_status:
                        problems.append("línea %d: ⏳ depende de una tarea inexistente (%s)" % (n, tid))
                    elif task_status[tid] == "done":
                        problems.append("línea %d: ⏳ depende de %s, que ya está terminada: debe resolverse" % (n, tid))
        base = DOCS / "adr" if doc["id"].startswith("adr-") else DOCS
        for ref in sorted(set(TASK_REF_RE.findall(re.sub(r"`[^`]*`", "", re.sub(r"```.*?```", "", doc["md"], flags=re.S))))):
            if ref not in task_status:
                problems.append("cita una tarea que no existe: %s" % ref)
        for link in LINK_RE.findall(doc["md"]):
            target = link.split("#")[0]
            if target.endswith(".md") and not target.startswith("http") and not (base / target).exists():
                problems.append("enlace roto: %s" % link)
        decided = counts["ok"] + counts["prop"] + counts["open"]
        doc["counts"] = {"ok": counts["ok"], "prop": counts["prop"], "open": counts["open"]}
        doc["clean"] = {
            "pct": round(100 * counts["ok"] / decided) if decided else None,
            "wait": counts["wait"],
            "items": items,
            "problems": problems,
        }
        for k in totals:
            totals[k] += counts[k]
        problems_total += len(problems)
        for msg in problems:
            warn("%s: %s" % (doc["id"], msg))
    decided = totals["ok"] + totals["prop"] + totals["open"]
    return {
        "pct": round(100 * totals["ok"] / decided) if decided else None,
        "target": CLEAN_TARGET,
        "ok": totals["ok"],
        "prop": totals["prop"],
        "open": totals["open"],
        "wait": totals["wait"],
        "problems": problems_total,
    }


def load_story(task_ids):
    """Carga y valida el mapa de historia (actos y carriles)."""
    path = DATA / "story.json"
    if not path.exists():
        return {"acts": [], "lanes": [], "after": ""}
    data = load_json(path)
    acts = data.get("acts", [])
    for act in acts:
        for key in ("n", "title", "color", "place", "time", "closes"):
            if not act.get(key):
                warn("Acto %s sin '%s'" % (act.get("n", "?"), key))
        for tid in act.get("tasks", []):
            if tid not in task_ids:
                warn("El acto %s cita una tarea inexistente: %s" % (act.get("n", "?"), tid))
    lane_ids = set()
    for lane in data.get("lanes", []):
        if lane.get("id") in lane_ids:
            warn("Carril repetido en el mapa de historia: %s" % lane.get("id"))
        lane_ids.add(lane.get("id"))
        if len(lane.get("cells", [])) != len(acts):
            warn("El carril %s tiene %d celdas y hay %d actos" % (lane.get("id"), len(lane.get("cells", [])), len(acts)))
    return {"acts": acts, "lanes": data.get("lanes", []), "after": data.get("after", "")}


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


def build_hub():
    roadmap = load_json(DATA / "roadmap.json")
    activity = load_activity()
    check_roadmap(roadmap, activity)
    docs = build_docs()
    groups = [g for g, _ in GROUPS]
    if any(d["group"] == ADR_GROUP for d in docs):
        groups.append(ADR_GROUP)
    task_ids = {t["id"] for p in roadmap["phases"] for m in p["milestones"] for t in m["tasks"]}
    task_status = {t["id"]: t["status"] for p in roadmap["phases"] for m in p["milestones"] for t in m["tasks"]}
    cleanliness = analyze_docs(docs, task_status)
    world = load_json(DATA / "world.json")
    story = load_story(task_ids)
    for msg in coherence.integrity(world):
        warn("world.json: %s" % msg)
    return {
        "generated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "config": load_json(DATA / "config.json"),
        "docs": docs,
        "groups": groups,
        "roadmap": roadmap,
        "assets": build_assets(load_json(DATA / "assets.json")),
        "palette": load_json(DATA / "palette.json"),
        "qa": load_qa(task_ids),
        "presentation": load_presentation({d["id"] for d in docs}),
        "story": story,
        "cleanliness": cleanliness,
        "world": world,
        "coherence": coherence.check(world, story),
    }


def render(hub):
    return "// Archivo generado por build.py. No editar a mano.\nwindow.HUB = " + json.dumps(hub, ensure_ascii=False) + ";\n"


def main():
    strict = "--strict" in sys.argv
    hub = build_hub()
    roadmap = hub["roadmap"]
    out = HUB / "data.js"
    out.write_text(render(hub), encoding="utf-8")
    tasks = [t for p in roadmap["phases"] for m in p["milestones"] for t in m["tasks"]]
    counts = {}
    for t in tasks:
        counts[t["status"]] = counts.get(t["status"], 0) + 1
    resumen = ", ".join("%s: %d" % (s, counts[s]) for s in VALID_STATUS if s in counts)
    print(
        "OK: %d documentos, %d tareas (%s), %d imágenes -> %s"
        % (len(hub["docs"]), len(tasks), resumen, len(hub["assets"]["images"]), out.relative_to(STUDIO.parent))
    )
    c = hub["cleanliness"]
    print(
        "Limpieza del diseño: %s %% (meta %d %%) · ✅ %d · 🟡 %d · ❓ %d · ⏳ %d · conexiones rotas: %d"
        % (c["pct"], c["target"], c["ok"], c["prop"], c["open"], c["wait"], c["problems"])
    )
    co = hub["coherence"]
    print("Coherencia: %s %% · %d de %d comprobaciones con hallazgos" % (co["pct"], co["failed"], co["total"]))
    if warnings:
        print("%d aviso(s)." % len(warnings))
        if strict:
            sys.exit(1)


if __name__ == "__main__":
    main()
