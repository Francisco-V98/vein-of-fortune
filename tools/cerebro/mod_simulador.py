"""Simulador de economía (F0-53): las 50 reglas de equilibrio con su resultado, los perfiles de jugador, los supuestos y el
resumen de resultados.

IDs: sim-A1... (regla con su resultado), simperfil-lento..., sim-supuestos, sim-resultados. Cada regla enlaza a las
secciones del documento 28 que cita, a los bloques de economía que mide y a los requisitos que protege.
"""
import re

from .ayudas import cargar, existente, id_doc, linea_de, lineas, lineas_de, ref_doc, sin_repetidos, tabla, valor
from .mod_economia import BLOQUES
from .nucleo import ref, ref_suave

NOMBRE = "simulador"
REGLAS = "studio/data/sim/reglas.json"
RESULTADOS = "studio/data/sim/resultados.json"
SUPUESTOS = "studio/data/sim/supuestos.json"
TAREA = "F0-53"
ETIQUETA = {"pasa": "sim/pasa", "falla": "sim/falla", "incierto": "sim/incierto"}


def _ic(v):
    return "[%s, %s]" % (valor(v[0]), valor(v[1])) if isinstance(v, (list, tuple)) and len(v) == 2 else "–"


def _limites(c):
    lo, hi = c.get("lo"), c.get("hi")
    return "%s a %s" % (valor(lo) if lo is not None else "…", valor(hi) if hi is not None else "…")


def _bloque_de_clave(clave):
    """«economy.energy.per_act.I» -> «eco-energy»."""
    partes = clave.split(".")
    return "eco-" + partes[1].replace("_", "-") if len(partes) > 1 and partes[0] == "economy" else None


def generar(registro, repo):
    reglas = (cargar(repo, REGLAS) or {}).get("reglas")
    if not reglas:
        registro.info.append("simulador: no hay reglas.json, se omite")
        return
    trazabilidad = (cargar(repo, REGLAS) or {}).get("trazabilidad", [])
    res = cargar(repo, RESULTADOS) or {}
    sup = cargar(repo, SUPUESTOS) or {}
    resultado = {r["id"]: r for r in res.get("reglas", [])}
    lr, ls = lineas_de(repo, REGLAS), lineas_de(repo, RESULTADOS)
    seccion_a_bloques = {}
    for clave, (_, sec, _) in BLOQUES.items():
        if sec == 13:  # la sección de validación la citan casi todas las reglas: no aporta relación
            continue
        seccion_a_bloques.setdefault(sec, []).append("eco-" + clave.replace("_", "-"))
    perfiles = res.get("perfiles", [])
    ids_perfil = {p["id"] for p in perfiles}
    moc = registro.moc("moc-simulador", "Simulador", "Las reglas de equilibrio de la economía y su resultado en el simulador.", orden=81, auto_hijos=False)
    grupos, conteo = {}, {}
    for r in reglas:
        rid, rs = r["id"], resultado.get(r["id"], {})
        estado = rs.get("estado", "sin resultado")
        conteo[estado] = conteo.get(estado, 0) + 1
        docs = [id_doc(d) for d in r.get("docs", [])]
        secciones_28 = [int(m.group(1)) for d in r.get("docs", []) for m in [re.match(r"28 §(\d+)", d)] if m]
        bloques = sin_repetidos(b for s in secciones_28 for b in seccion_a_bloques.get(s, []))
        mutaciones = (sup.get("mutaciones") or {}).get(rid, [])
        bloques = sin_repetidos(bloques + [_bloque_de_clave(e["clave"]) for mu in mutaciones for e in mu.get("ediciones", [])])
        protege = [t for t in trazabilidad if rid in t.get("reglas", [])]
        cuerpo = ["**Grupo:** %s · **Origen del umbral:** %s" % (r["grupo"], "documento aprobado" if r.get("origen") == "doc" else "propuesta del simulador"),
                  "", "## Qué mide", "", r.get("metrica", ""), "", "## Umbral", "", r.get("umbral", "")]
        cuerpo += ["", "## Resultado", ""]
        if rs:
            cuerpo += ["Estado: **%s**. %s: **%s %s** (IC95 %s, n = %s)." % (
                rs.get("estado"), rs.get("metrica", "valor"), valor(rs.get("valor")), rs.get("unidad", ""), _ic(rs.get("ic95")), valor(rs.get("n")))]
            if rs.get("por_perfil"):
                cuerpo += [""] + tabla(["Perfil", "Valor", "IC95", "n"], [
                    (ref("simperfil-" + p, p) if p in ids_perfil else p, valor(x.get("valor")), _ic(x.get("ic95")), valor(x.get("n")))
                    for p, x in rs["por_perfil"].items()])
            if rs.get("condiciones"):
                cuerpo += ["", "### Condiciones", ""] + tabla(["Condición", "Valor", "IC95", "Límites", "Estado"], [
                    (c["nombre"], "%s %s" % (valor(c.get("valor")), c.get("unidad") or ""), _ic(c.get("ic95")), _limites(c), c.get("estado", "")) for c in rs["condiciones"]])
            if isinstance(rs.get("extra"), dict) and rs["extra"]:
                cuerpo += ["", "### Datos adicionales", ""] + lineas(rs["extra"])
            elif rs.get("extra"):
                cuerpo += ["", "Datos adicionales: %s" % valor(rs["extra"])]
        else:
            cuerpo += ["Sin resultado en `%s`." % RESULTADOS]
        if r.get("criterio"):
            cuerpo += ["", "## Criterio", ""] + ["- **%s:** %s" % (k, valor(v)) for k, v in r["criterio"].items()]
        if protege:
            cuerpo += ["", "## Requisitos que protege", ""] + ["- %s (%s)" % (t["requisito"], ref_doc(registro, t["fuente"]) or t["fuente"]) for t in protege]
        if mutaciones:
            cuerpo += ["", "## Mutaciones de prueba", ""]
            for mu in mutaciones:
                cuerpo.append("- %s" % mu.get("descripcion", ""))
                cuerpo += ["  - `%s` = %s" % (e["clave"], valor(e["valor"])) for e in mu.get("ediciones", [])]
        nota = registro.nueva(
            "sim-" + rid, "regla-sim", r["titulo"], "simulador", nombre="%s %s" % (rid, r["titulo"]), sufijo="regla",
            arriba="moc-simulador", tags=[t for t in (ETIQUETA.get(estado),) if t], fuente="%s:%d" % (REGLAS, linea_de(lr, '"id": "%s"' % rid)),
            props={"grupo": r["grupo"], "estado": estado, "origen": r.get("origen"), "valor": rs.get("valor"), "unidad": rs.get("unidad"),
                   "documentos": [x for x in (ref_doc(registro, d) for d in r.get("docs", [])) if x]},
            resumen="%s · %s · %s" % (r["grupo"], estado, r.get("umbral", "")[:90]), cuerpo="\n".join(cuerpo))
        nota.relacion("Documentos", sin_repetidos(ref(d) for d in docs if d and registro.existe(d)))
        nota.relacion("Bloques de economía", [existente(registro, b) for b in bloques if b])
        nota.relacion("Perfiles", [ref("simperfil-" + p) for p in (rs.get("por_perfil") or {}) if p in ids_perfil])
        nota.relacion("Tarea", [ref_suave(TAREA, "", TAREA)])
        nota.relacion("Resumen de resultados", [ref("sim-resultados")])
        grupos.setdefault(r["grupo"], []).append((r, estado))
    # perfiles -----------------------------------------------------------------------------------------------------------------
    perf_sup = sup.get("perfiles", {})
    for p in perfiles:
        pid = p["id"]
        datos = perf_sup.get(pid, {})
        usan = [r["id"] for r in reglas if pid in (resultado.get(r["id"], {}).get("por_perfil") or {})]
        cuerpo = lineas({k: v for k, v in datos.items() if k != "nombre"}) if datos else []
        nota = registro.nueva("simperfil-" + pid, "perfil-sim", p["nombre"], "simulador", nombre="Perfil " + p["nombre"], sufijo="simulador",
                              arriba="moc-simulador", fuente=SUPUESTOS, props={"reglas": len(usan)},
                              resumen="Perfil de jugador simulado · medido en %d reglas" % len(usan), cuerpo="\n".join(cuerpo))
        nota.relacion("Reglas medidas con este perfil", [ref("sim-" + x) for x in usan])
        nota.relacion("Documento", [ref_doc(registro, "28 §13") or ref_doc(registro, "28")])
    # supuestos y resultados ----------------------------------------------------------------------------------------------------
    if sup:
        cuerpo = [sup.get("nota", ""), ""] + lineas({k: v for k, v in sup.items() if k not in ("nota", "perfiles", "mutaciones", "version")})
        nota = registro.nueva("sim-supuestos", "supuestos-sim", "Supuestos del simulador", "simulador", sufijo="simulador", arriba="moc-simulador",
                              fuente=SUPUESTOS, resumen="Cómo se simula: semillas, tamaños de corrida, ruido y política del jugador", cuerpo="\n".join(cuerpo))
        nota.relacion("Perfiles", [ref("simperfil-" + p["id"]) for p in perfiles])
        nota.relacion("Resultados", [ref("sim-resultados")])
    serie = (res.get("series") or {}).get("ingreso_hora_por_acto") or {}
    cuerpo = ["Corrida **%s** del %s (huella `%s`). %d reglas: %s." % (res.get("modo", "?"), res.get("generado", "?"), res.get("huella", "?"), len(reglas),
                                                                    ", ".join("%d %s" % (v, k) for k, v in sorted(conteo.items())))]
    if serie:
        cuerpo += ["", "## Ingreso neto por hora y acto", ""]
        cuerpo += tabla(["Perfil"] + serie["actos"], [("objetivo", *[valor(serie["objetivo"].get(a)) for a in serie["actos"]])] +
                        [(ref("simperfil-" + p, p) if p in ids_perfil else p, *[valor(round(v.get(a, 0))) for a in serie["actos"]])
                         for p, v in serie.get("perfiles", {}).items()])
    if res.get("tamanos"):
        cuerpo += ["", "## Tamaños de la corrida", ""] + lineas(res["tamanos"])
    nota = registro.nueva("sim-resultados", "resultados-sim", "Resultados del simulador", "simulador", sufijo="simulador", arriba="moc-simulador",
                          fuente=RESULTADOS, props={"modo": res.get("modo"), "generado_el": res.get("generado"), "reglas": len(reglas),
                                                    **{"reglas_" + k: v for k, v in sorted(conteo.items())}},
                          resumen="%s · %s · %s" % (res.get("modo"), res.get("generado"), ", ".join("%d %s" % (v, k) for k, v in sorted(conteo.items()))),
                          cuerpo="\n".join(cuerpo))
    nota.relacion("Tarea", [ref_suave(TAREA, "", TAREA)])
    nota.relacion("Documento", [ref_doc(registro, "28 §13")])
    nota.relacion("Bloque de validación", [existente(registro, "eco-validation")])
    # mapa -----------------------------------------------------------------------------------------------------------------------
    cuerpo = ["%d reglas de equilibrio medidas con el simulador (`tools/sim`, tarea %s): %s." % (
        len(reglas), ref_suave(TAREA, "", TAREA), ", ".join("%d %s" % (v, k) for k, v in sorted(conteo.items()))),
        "", "Resumen: %s · supuestos: %s." % (ref("sim-resultados"), ref("sim-supuestos") if sup else "–")]
    for g, items in grupos.items():
        cuerpo += ["", "## " + g, ""]
        cuerpo += tabla(["Regla", "Estado", "Umbral"], [(ref("sim-" + r["id"], "%s %s" % (r["id"], r["titulo"])), e, r.get("umbral", "")) for r, e in items])
    moc.cuerpo = "\n".join(cuerpo)
    moc.relacion("Perfiles", [ref("simperfil-" + p["id"]) for p in perfiles])
    moc.relacion("Documento", [ref_doc(registro, "28 §13")])
    registro.info.append("simulador: %d reglas (%s), %d perfiles" % (len(reglas), ", ".join("%d %s" % (v, k) for k, v in sorted(conteo.items())), len(perfiles)))
