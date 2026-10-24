"""Roadmap: fases, hitos y tareas (con su flujo por etapas, traspasos e historial) y su relación con los documentos.

Las tareas no declaran documentos: la relación se saca del texto (título, descripción y criterio de cierre) y de las
secciones de los documentos que citan la tarea. Se ejecuta después de `mod_documentos`.
"""
import json
import re

from . import texto as T
from .nucleo import ref

NOMBRE = "tareas"
ORIGEN_ENLACES = "studio/docs/roadmap.json"  # los enlaces `[NN](…md)` de las tareas se escriben como en los documentos
TAGS_ESTADO = {"backlog": "estado/pendiente", "sprint": "estado/en-curso", "doing": "estado/en-curso", "review": "estado/en-curso",
               "qa": "estado/en-curso", "done": "estado/hecho", "dropped": "estado/descartado"}
DOC_RE = re.compile(r"(?i)\b(?:documentos?|docs?\.?)\s+((?:\d{2}\b(?:\s*(?:,|y|e|a)\s*)?)+)")
ADR_RE = re.compile(r"\bADR-(\d{4})\b")
RUTA_DOC_RE = re.compile(r"studio/docs/(\d{2})-")
CORCHETE_RE = re.compile(r"\[(\d{2})\]\(")


def _json(ruta):
    return json.loads(ruta.read_text(encoding="utf-8"))


def titulo_corto(titulo, maximo=60):
    t = re.sub(r"\s+", " ", titulo).strip()
    if len(t) > maximo:
        corte = t.rfind(" ", 0, maximo)
        t = t[: corte if corte > maximo // 2 else maximo]
    return t.rstrip(" ,;:.—-")


def documentos_en_texto(texto, registro):
    """IDs de documentos y ADR que menciona un texto («documentos 14, 15 y 16», «ADR-0009», «[03](…)»)."""
    ids = []
    for m in DOC_RE.finditer(texto):
        ids += ["doc-" + n for n in re.findall(r"\d{2}", m.group(1))]
    ids += ["doc-" + n for n in RUTA_DOC_RE.findall(texto) + CORCHETE_RE.findall(texto)]
    ids += ["adr-" + n for n in ADR_RE.findall(texto)]
    visto = []
    for i in ids:
        if registro.existe(i) and i not in visto:
            visto.append(i)
    return visto


def _lineas(ruta, patron):
    """{valor del grupo 1: número de línea} de las líneas que casan con `patron`."""
    out = {}
    for n, linea in enumerate(ruta.read_text(encoding="utf-8").split("\n"), 1):
        m = patron.search(linea)
        if m:
            out.setdefault(m.group(1), n)
    return out


def _celda(t):
    return re.sub(r"\s+", " ", str(t)).replace("|", "/").strip()


def _rol(rid, roles):
    return ref("rol-" + rid) if rid in roles else _celda(rid or "")


def _cuerpo_tarea(t, act, roles):
    conv_desc, _ = T.convertir(t.get("desc", ""), ORIGEN_ENLACES)
    conv_hecho, _ = T.convertir(t.get("done_when", ""), ORIGEN_ENLACES)
    out = []
    if conv_desc:
        out += [conv_desc, ""]
    if conv_hecho:
        out += ["## Hecha cuando", "", conv_hecho, ""]
    pipe = act.get("pipeline") or {}
    if pipe.get("etapas"):
        out += ["## Flujo por etapas", ""]
        if pipe.get("especialista"):
            out += ["Especialista de producción: %s." % _rol(pipe["especialista"], roles), ""]
        out += ["| Etapa | Estado | Por | Fecha | Nota |", "|---|---|---|---|---|"]
        for e in pipe["etapas"]:
            out.append("| %s | %s | %s | %s | %s |" % (ref("etapa-" + e["etapa"], e["etapa"]) if e.get("etapa") else "", e.get("estado", ""),
                                                      _rol(e.get("por"), roles) if e.get("por") else "", e.get("at", ""), _celda(e.get("nota", ""))))
        hallazgos = [(e["etapa"], h) for e in pipe["etapas"] for h in e.get("hallazgos", [])]
        if hallazgos:
            out += ["", "### Hallazgos", ""]
            for etapa, h in hallazgos:
                cierre = " → resuelto por %s: %s" % (_rol(h.get("resuelto_por"), roles), _celda(h.get("como", ""))) if h.get("estado") == "resuelto" else ""
                out.append("- %s (%s, %s): %s%s" % (_rol(h.get("de"), roles), etapa, h.get("estado", ""), _celda(h.get("que", "")), cierre))
        out.append("")
    if pipe.get("traspasos"):
        out += ["## Traspasos", ""]
        for x in pipe["traspasos"]:
            out.append("- %s · %s → %s (%s): %s" % (x.get("at", ""), _rol(x.get("de"), roles), _rol(x.get("a"), roles), x.get("tipo", "entrega"), _celda(x.get("que", ""))))
        out.append("")
    if act.get("history"):
        out += ["## Historial", ""]
        for h in act["history"]:
            ref_h = " (%s)" % _celda(h["ref"]) if h.get("ref") else ""
            out.append("- %s · %s → %s · %s: %s%s" % (h.get("at", ""), h.get("from", ""), h.get("to", ""), h.get("by", ""), _celda(h.get("note", "")), ref_h))
        out.append("")
    if act.get("comments"):
        out += ["## Comentarios", ""] + ["- %s · %s: %s" % (c.get("at", ""), c.get("by", ""), _celda(c.get("text", ""))) for c in act["comments"]] + [""]
    if act.get("evidence"):
        out += ["## Evidencias", ""]
        for e in act["evidence"]:
            out.append("- %s: %s" % (e.get("type", ""), _celda(e.get("title") or e.get("path") or e.get("url") or e.get("doc") or "")))
        out.append("")
    return "\n".join(out)


def generar(registro, repo):
    datos = repo / "studio" / "data"
    ruta_rm = datos / "roadmap.json"
    roadmap = _json(ruta_rm)
    equipo = _json(datos / "equipo.json") if (datos / "equipo.json").exists() else {"roles": []}
    roles = {r["id"] for r in equipo.get("roles", [])}
    lineas = _lineas(ruta_rm, re.compile(r'"id":\s*"([^"]+)"'))
    actividad = {}
    for ruta in sorted((datos / "tasks").glob("*.json")) if (datos / "tasks").is_dir() else []:
        d = _json(ruta)
        actividad[d.get("id", ruta.stem)] = d
    moc = registro.moc("moc-roadmap", "Roadmap", "Fases, hitos y las tareas del plan con su estado.", orden=20, auto_hijos=False)
    por_citar = registro.indice_referencias()
    resumen_fases, en_curso, total = [], [], 0
    for fase in roadmap["phases"]:
        fid = "fase-" + fase["id"]
        hitos_notas, hechas_f, n_f = [], 0, 0
        for hito in fase["milestones"]:
            hid = "hito-" + hito["id"]
            filas, hechas_h = [], 0
            for t in hito["tasks"]:
                act = actividad.get(t["id"], {})
                estado = t["status"]
                hechas_h += estado == "done"
                version = t.get("target") or fase.get("target")
                tags = [TAGS_ESTADO.get(estado, "estado/pendiente"), "prio/" + t.get("prio", "P3"), "fase/" + fase["id"]]
                if estado == "backlog" and fase["id"] != "F0":
                    tags.append("backlog/futuro")
                if version:
                    tags.append("version/" + re.sub(r"\s+", "-", version))
                pipe = act.get("pipeline") or {}
                texto_base = " ".join([t["title"], t.get("desc", ""), t.get("done_when", "")])
                docs = documentos_en_texto(texto_base, registro)
                citada = [o for o in por_citar.a(t["id"]) if registro.notas[o].tipo in ("seccion", "documento", "adr")]
                for o in citada:
                    dueno = registro.notas[o].arriba if registro.notas[o].tipo == "seccion" else o
                    if dueno and dueno not in docs and registro.existe(dueno):
                        docs.append(dueno)
                props = {"fase": ref(fid), "hito": ref(hid), "prio": t.get("prio"), "est": t.get("est"), "status": estado}
                if version:
                    props["version"] = version
                if pipe.get("etapas"):
                    props["etapas"] = ["%s: %s" % (e.get("etapa"), e.get("estado")) for e in pipe["etapas"]]
                if pipe.get("especialista") and pipe["especialista"] in roles:
                    props["especialista"] = ref("rol-" + pipe["especialista"])
                props["docs"] = [ref(d) for d in docs]
                nota = registro.nueva(
                    t["id"], "tarea", "%s %s" % (t["id"], t["title"]), "roadmap/tareas", nombre="%s %s" % (t["id"], titulo_corto(t["title"])),
                    props=props, resumen=T.primera_frase(t.get("desc", "")) or t["title"], cuerpo=_cuerpo_tarea(t, act, roles), arriba=hid, tags=tags,
                    fuente="studio/data/roadmap.json:%d" % lineas.get(t["id"], 1))
                nota.relacion("Hito", [ref(hid)])
                nota.relacion("Documentos", [ref(d) for d in docs])
                nota.relacion("Citada en", [ref(o) for o in citada])
                filas.append(nota)
                if estado not in ("backlog", "done", "dropped"):
                    en_curso.append(nota)
            n_f += len(hito["tasks"])
            hechas_f += hechas_h
            cuerpo = ["Fase: %s. Hechas %d de %d." % (ref(fid), hechas_h, len(filas)), "", "## Tareas", ""]
            cuerpo += ["- [%s] %s · %s · %s · %s h" % ("x" if n.props["status"] == "done" else " ", ref(n.id), n.props["status"], n.props["prio"], n.props["est"]) for n in filas]
            hito_nota = registro.nueva(
                hid, "hito", "%s %s" % (hito["id"], hito["name"]), "roadmap", nombre="%s %s" % (hito["id"], hito["name"]),
                props={"fase": ref(fid), "tareas": len(filas), "hechas": hechas_h}, resumen="%d de %d tareas hechas" % (hechas_h, len(filas)),
                cuerpo="\n".join(cuerpo), arriba=fid, tags=["fase/" + fase["id"]], fuente="studio/data/roadmap.json:%d" % lineas.get(hito["id"], 1))
            hitos_notas.append(hito_nota)
        total += n_f
        cuerpo = [fase.get("goal") or "", ""]
        if fase.get("gate"):
            cuerpo += ["**Puerta de salida:** %s" % fase["gate"], ""]
        cuerpo += ["## Hitos", "", "| Hito | Hechas | Tareas |", "|---|---|---|"]
        cuerpo += ["| %s | %d | %d |" % (ref(h.id), h.props["hechas"], h.props["tareas"]) for h in hitos_notas]
        props = {"objetivo": fase.get("target"), "horas": fase.get("hours"), "confianza": fase.get("confidence"), "tareas": n_f, "hechas": hechas_f}
        props = {k: v for k, v in props.items() if v is not None}
        registro.nueva(fid, "fase", "%s %s" % (fase["id"], fase["name"]), "roadmap", nombre="%s %s" % (fase["id"], fase["name"]), props=props,
                       resumen="%d de %d tareas hechas" % (hechas_f, n_f), cuerpo="\n".join(cuerpo), arriba="moc-roadmap",
                       tags=["fase/" + fase["id"]], fuente="studio/data/roadmap.json:%d" % lineas.get(fase["id"], 1))
        resumen_fases.append((fid, hechas_f, n_f))
    cuerpo = ["| Fase | Hechas | Tareas |", "|---|---|---|"] + ["| %s | %d | %d |" % (ref(f), h, n) for f, h, n in resumen_fases]
    if en_curso:
        cuerpo += ["", "## En curso", ""] + ["- %s (%s)" % (ref(n.id), n.props["status"]) for n in en_curso]
    moc.cuerpo = "\n".join(cuerpo)
    moc.props["tareas"] = total
    registro.info.append("tareas: %d tareas en %d fases" % (total, len(resumen_fases)))
