"""QA: los casos de prueba de studio/data/qa/cases.json, uno por nota (`qa-TC-001`), enlazados a sus tareas y al documento 16.

El mapa MOC QA los agrupa por área con su prioridad y su estado de ejecución.
"""
from .ayudas import cargar, existente, linea_de, lineas_de, tabla
from .nucleo import ref

NOMBRE = "qa"
CASOS = "studio/data/qa/cases.json"
ESTADOS = {"not-run": ("sin ejecutar", "estado/pendiente"), "pass": ("pasa", "estado/hecho"), "fail": ("falla", "estado/fallo"),
           "blocked": ("bloqueado", "estado/bloqueado")}


def generar(registro, repo):
    datos = cargar(repo, CASOS)
    if not datos:
        registro.info.append("qa: no hay cases.json, se omite")
        return
    lineas = lineas_de(repo, CASOS)
    doc16 = existente(registro, "doc-16")
    moc = registro.moc("moc-qa", "QA", "Casos de prueba de la estrategia de QA (documento 16) por área, prioridad y estado.", orden=80, auto_hijos=False)
    por_area = {}
    for c in datos.get("cases", []):
        res = c.get("result", {})
        estado, tag = ESTADOS.get(res.get("status"), (res.get("status") or "sin ejecutar", None))
        cuerpo = ["**Área:** %s · **Tipo:** %s · **Nivel:** %s · **Automatizable:** %s · **Prioridad:** %s" % (
            c["area"], c["type"], c["level"], "sí" if c.get("auto") else "no", c["prio"]), "", "## Pasos", ""]
        cuerpo += ["%d. %s" % (i, p) for i, p in enumerate(c.get("steps", []), 1)]
        cuerpo += ["", "## Resultado esperado", "", c.get("expected", ""), "", "## Última ejecución", "",
                   "Estado: **%s**%s%s%s" % (estado, " · fecha %s" % res["at"] if res.get("at") else "", " · compilación %s" % res["build"] if res.get("build") else "",
                                              " · por %s" % res["by"] if res.get("by") else "")]
        if res.get("note"):
            cuerpo += ["", res["note"]]
        nota = registro.nueva(
            "qa-" + c["id"], "caso-qa", c["title"], "qa", nombre="%s %s" % (c["id"], c["title"]), sufijo="QA", alias=[c["id"]], arriba="moc-qa",
            tags=[t for t in (tag, "prio/" + c["prio"]) if t], fuente="%s:%d" % (CASOS, linea_de(lineas, '"id": "%s"' % c["id"])),
            props={"area": c["area"], "tipo_prueba": c["type"], "nivel": c["level"], "automatizable": bool(c.get("auto")), "prio": c["prio"],
                   "estado": estado, "tareas": [ref(t) for t in c.get("tasks", [])]},
            resumen="%s · %s · %s · %s" % (c["area"], c["prio"], c["type"], estado), cuerpo="\n".join(cuerpo))
        nota.relacion("Tareas", [ref(t) for t in c.get("tasks", [])])
        nota.relacion("Documento", [doc16] if doc16 else [])
        por_area.setdefault(c["area"], []).append(c)
    cuerpo = ["%d casos de prueba en %d áreas (`%s`). La estrategia está en %s." % (
        sum(len(v) for v in por_area.values()), len(por_area), CASOS, doc16 or "el documento 16")]
    for area in datos.get("areas", list(por_area)):
        if area in por_area:
            cuerpo += ["", "## " + area, ""]
            cuerpo += tabla(["Caso", "Prioridad", "Tipo", "Nivel", "Tareas"],
                            [(ref("qa-" + c["id"], "%s %s" % (c["id"], c["title"])), c["prio"], c["type"], c["level"], ", ".join(ref(t) for t in c.get("tasks", []))) for c in por_area[area]])
    moc.cuerpo = "\n".join(cuerpo)
    registro.info.append("qa: %d casos en %d áreas" % (sum(len(v) for v in por_area.values()), len(por_area)))
