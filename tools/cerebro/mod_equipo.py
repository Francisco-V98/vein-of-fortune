"""Equipo del estudio: roles (con su agente, modelo y esfuerzo), departamentos, las etapas del flujo y sus reglas.

Se ejecuta después de `mod_tareas`: cada rol lista las tareas en las que participó (las que lo enlazan desde su flujo).
"""
import json
import re

from .nucleo import ref

NOMBRE = "equipo"


def leer_agente(ruta):
    """Campos simples del encabezado YAML de un agente (`name`, `description`, `tools`, `model`, `effort`...)."""
    if not ruta.is_file():
        return {}
    m = re.match(r"^---\n(.*?)\n---", ruta.read_text(encoding="utf-8"), re.S)
    campos = {}
    for linea in (m.group(1).split("\n") if m else []):
        k, sep, v = linea.partition(":")
        if sep and k.strip() and not k.startswith(" "):
            campos[k.strip()] = v.strip().strip('"')
    return campos


def generar(registro, repo):
    ruta = repo / "studio" / "data" / "equipo.json"
    if not ruta.is_file():
        registro.info.append("equipo: no hay equipo.json, se omite")
        return
    equipo = json.loads(ruta.read_text(encoding="utf-8"))
    deptos = {d["id"]: d for d in equipo.get("deptos", [])}
    roles = equipo.get("roles", [])
    etapas = equipo.get("etapas", [])
    registro.moc("moc-equipo", "Equipo", "Los roles, los departamentos y las etapas del flujo de trabajo.", orden=30)
    entrantes = registro.indice_referencias()
    doc20 = "doc-20" if registro.existe("doc-20") else None
    for d in deptos.values():
        registro.nueva("dep-" + d["id"], "departamento", d["nombre"], "equipo", nombre="Departamento " + d["nombre"], arriba="moc-equipo",
                       fuente="studio/data/equipo.json", resumen="%d roles" % sum(1 for r in roles if r.get("depto") == d["id"]),
                       props={"roles": sum(1 for r in roles if r.get("depto") == d["id"])})
    por_etapa = {}
    for e in etapas:
        por_etapa.setdefault(e["rol"], []).append(e)
        for a in e.get("apoyo", []):
            por_etapa.setdefault(a, []).append(e)
    for r in roles:
        agente = leer_agente(repo / ".claude" / "agents" / ("%s.md" % r["agente"])) if r.get("agente") else {}
        props = {"rol": r["id"], "rol_tipo": r["tipo"], "departamento": ref("dep-" + r["depto"]) if r.get("depto") in deptos else r.get("depto"),
                 "desde": ref("fase-" + r["desde"]) if registro.existe("fase-" + r.get("desde", "")) else r.get("desde"),
                 "especialista": bool(r.get("especialista"))}
        if r.get("agente"):
            props["agente"] = r["agente"]
            props["modelo"] = agente.get("model", "sin definir")
            props["esfuerzo"] = agente.get("effort") or agente.get("esfuerzo") or "heredado"
        cuerpo = []
        if r.get("hace") and len(r["hace"]) > 160:
            cuerpo += [r["hace"], ""]
        if r.get("entrega"):
            cuerpo += ["**Entrega:** %s" % r["entrega"], ""]
        if agente.get("description"):
            cuerpo += ["**Agente** (`.claude/agents/%s.md`): %s" % (r["agente"], agente["description"]), ""]
        if agente.get("tools"):
            cuerpo += ["**Herramientas:** %s" % agente["tools"], ""]
        tareas = [o for o in entrantes.a("rol-" + r["id"]) if registro.notas[o].tipo == "tarea"]
        nota = registro.nueva("rol-" + r["id"], "rol", r["nombre"], "equipo", props=props, resumen=(r.get("hace") or r["nombre"])[:160],
                              cuerpo="\n".join(cuerpo), arriba="dep-" + r["depto"] if r.get("depto") in deptos else "moc-equipo",
                              fuente="studio/data/equipo.json")
        nota.relacion("Etapas", [ref("etapa-" + e["id"]) for e in por_etapa.get(r["id"], [])])
        nota.relacion("Documento", [ref(doc20)] if doc20 else [])
        nota.relacion("Tareas con su participación", [ref(t) for t in tareas])
    for i, e in enumerate(etapas, 1):
        rol = e["rol"]
        cuerpo = [e.get("que", ""), ""]
        if e.get("apoyo"):
            cuerpo += ["Con apoyo de: %s." % ", ".join(ref("rol-" + a) for a in e["apoyo"]), ""]
        cuerpo += ["Glifo: `%s`. Estados posibles: %s." % (e.get("glifo", ""), ", ".join(equipo.get("estados_etapa", [])))]
        nota = registro.nueva("etapa-" + e["id"], "etapa", e["nombre"], "equipo", nombre="Etapa " + e["nombre"], arriba="moc-equipo",
                              props={"orden_flujo": i, "responsable": ref("rol-" + rol) if rol in {x["id"] for x in roles} else rol},
                              resumen=e.get("que", ""), cuerpo="\n".join(cuerpo), fuente="studio/data/equipo.json")
        nota.relacion("Responsable", [ref("rol-" + rol)] if rol in {x["id"] for x in roles} else [])
        nota.relacion("Documento", [ref(doc20)] if doc20 else [])
    reglas = equipo.get("reglas", [])
    if reglas:
        cuerpo = ["- " + r for r in reglas]
        if equipo.get("nota"):
            cuerpo = [equipo["nota"], ""] + cuerpo
        nota = registro.nueva("equipo-reglas", "regla", "Reglas del flujo", "equipo", arriba="moc-equipo", cuerpo="\n".join(cuerpo),
                              resumen="Reglas que cumple cada tarea al pasar por las etapas.", fuente="studio/data/equipo.json")
        nota.relacion("Documento", [ref(doc20)] if doc20 else [])
    registro.info.append("equipo: %d roles, %d etapas, %d departamentos" % (len(roles), len(etapas), len(deptos)))
