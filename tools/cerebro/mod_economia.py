"""Economía: un bloque de `economy.*` de world.json por nota (cifras base) enlazado a la sección del documento 28.

IDs: eco-debt, eco-time, eco-tools... Cada nota vuelca todas las cifras de su bloque, enlaza a la sección del documento 28
que lo explica, a las reglas del simulador que la citan y a las entidades del mundo que nombra.
"""
from .ayudas import cargar, existente, id_doc, lineas, lineas_de, linea_de, sin_repetidos, tabla
from .mod_mundo import Mundo, WORLD
from .nucleo import ref, ref_suave

NOMBRE = "economia"

# clave del bloque -> (título visible, sección del documento 28, entidades relacionadas)
BLOQUES = {
    "currency": ("Moneda", 1, []),
    "punto": ("Punto de mercado", 1, []),
    "time": ("Tiempo", 1, []),
    "calendar": ("Calendario", 1, ["zona-fosa"]),
    "expedition": ("Expediciones", 1, ["mj-contencion", "fac-comision"]),
    "pace": ("Ritmo objetivo", 2, []),
    "energy": ("Energía", 4, []),
    "mine_entrances": ("Entradas de mina", 4, ["F0-92"]),
    "seasons_weather": ("Estaciones y clima", 1, ["F0-92"]),
    "tools": ("Herramientas", 5, ["mj-picado", "mj-perforacion", "mj-cribado", "mj-cincelado"]),
    "market": ("Mercado", 6, []),
    "debt": ("Deuda del Acto I", 7, ["pj-reme", "ed-vb-reme"]),
    "employees": ("Empleados", 8, ["ed-vb-union"]),
    "store_upgrades": ("Mejoras de la tienda", 8, ["ed-vb-tienda"]),
    "information": ("Información", 9, ["fac-teletipo", "ed-vb-periodico"]),
    "travel": ("Viaje", 9, []),
    "orders": ("Pedidos", 9, ["ed-vb-tienda"]),
    "orders_rules": ("Reglas de los pedidos", 9, []),
    "surveillance": ("Vigilancia", 10, ["pj-quiroga", "ed-vb-quiroga", "fac-faroleros"]),
    "lifestyle": ("Estilo de vida", 11, []),
    "difficulty": ("Dificultad", 12, []),
    "validation": ("Validación", 13, ["moc-simulador"]),
    "scripted_drift_act1": ("Deriva guionizada del Acto I", 6, ["doc-27", "min-carbon", "min-hierro"]),
    "act1_script": ("Guion económico del Acto I", 2, ["doc-27", "acto-I", "pj-anselmo"]),
    "rescue_mission": ("Misión de rescate", 13, ["F0-78"]),
}


def _n(v):
    """Número con espacio de millares: 24000 -> «24 000»."""
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    return "{:,}".format(v).replace(",", " ") if isinstance(v, int) else str(v)


def _rango(v):
    return "–".join(_n(x) for x in v) if isinstance(v, (list, tuple)) else _n(v)


def resumen_bloque(clave, b):
    """Cifras clave de un bloque en una línea."""
    g = b.get
    try:
        if clave == "currency":
            return "%s, solo enteros" % g("name")
        if clave == "punto":
            return "1 punto de mercado = %s %% del precio base" % g("market_pct_of_base")
        if clave == "time":
            return "Día de %s min, %s bloques, mes de %s días, año de %s" % (g("day_minutes"), g("blocks_per_day"), g("month_days"), g("year_days"))
        if clave == "calendar":
            return "Empieza el día %s en %s; la Fosa abre los días %s" % (g("start_day"), g("start_season"), ", ".join(str(x) for x in g("fosa_open_weekdays")))
        if clave == "expedition":
            return "%s bloque normal y %s profunda; hasta %s normales al día" % (g("normal_blocks"), g("deep_blocks"), g("max_normal_per_day"))
        if clave == "pace":
            medio = g("net_income_per_hour", {})
            return "Ingreso neto por hora, Acto I: %s / %s / %s (lento, medio, rápido)" % (
                _n(medio["I"]["slow"]), _n(medio["I"]["medium"]), _n(medio["I"]["fast"]))
        if clave == "energy":
            return "Aguante base %s; por acto: %s" % (g("base"), ", ".join("%s %s" % (a, _rango(v)) for a, v in g("per_act").items()))
        if clave == "tools":
            return "%d tipos, %d niveles; primer costo del pico %s" % (len(g("types")), len(g("levels")), _n(g("types")[0]["first_cost"]))
        if clave == "market":
            return "Impuesto de venta %s %%; eventos de %s a %s puntos" % (g("sale_tax_pct"), min(g("event_base_points").values()), max(g("event_base_points").values()))
        if clave == "debt":
            return "Principal %s, interés %s %% al mes, primer pago %s el día %s" % (_n(g("principal")), g("interest_monthly_pct"), _n(g("first_payment")), g("first_due_day"))
        if clave == "employees":
            n = g("levels")
            return "%d niveles; sueldo diario de %s a %s" % (len(n), _n(n[0]["salary_per_day"]), _n(n[-1]["salary_per_day"]))
        if clave == "store_upgrades":
            n = g("__lista__")
            return "%d niveles: %s" % (len(n), " → ".join("%s (%s)" % (x["name"], _n(x["cost"])) for x in n))
        if clave == "information":
            return "%d capas de información: %s" % (len(g("layers")), ", ".join(x["name"] for x in g("layers")))
        if clave == "travel":
            costes = [r["cost"] for r in g("routes")]
            return "%d trayectos de %s a %s esquirlas" % (len(costes), min(costes), max(costes))
        if clave == "orders":
            n = g("__lista__")
            return "Pedidos: " + ", ".join("%s +%s %%" % (x["id"], x["premium_pct"]) for x in n)
        if clave == "orders_rules":
            return "Solo bienes propios; como máximo el %s %% del ingreso" % g("income_share_cap_pct")
        if clave == "surveillance":
            return "Niveles: %s" % ", ".join(x["id"] for x in g("levels"))
        if clave == "lifestyle":
            return "%d casas de %s a %s esquirlas" % (len(g("houses")), _n(g("houses")[0]["price"]), _n(g("houses")[-1]["price"]))
        if clave == "difficulty":
            return "Dificultades: %s" % ", ".join(g("order"))
        if clave == "validation":
            return "Verificado en %s; última simulación: %s" % (g("verified_in"), g("last_simulated"))
        if clave == "scripted_drift_act1":
            n = g("__lista__")
            return "%d derivas guionizadas: %s" % (len(n), ", ".join(x["mineral"] for x in n))
        if clave == "act1_script":
            return "Expediciones los días %s; mejora el día %s" % (", ".join(str(x) for x in g("expedition_days")), g("upgrade_day"))
        if clave == "rescue_mission":
            return "Llega tras %s h (puerta A5) y %s h (círculo)" % (g("hours_accumulated")["A5"], g("hours_accumulated")["circle"])
    except (KeyError, TypeError, IndexError, ValueError):
        pass
    return "Bloque de cifras base de la economía"


def generar(registro, repo):
    w = cargar(repo, WORLD)
    eco = (w or {}).get("economy")
    if not eco:
        registro.info.append("economia: no hay economy en world.json, se omite")
        return
    ents = Mundo(w).entidades()
    lw = lineas_de(repo, WORLD)
    ini = linea_de(lw, '"economy": {')
    reglas = (cargar(repo, "studio/data/sim/reglas.json") or {}).get("reglas", [])
    citan = {}  # sección del 28 -> reglas del simulador que la citan
    for r in reglas:
        for d in r.get("docs", []):
            i = id_doc(d)
            if i and i.startswith("doc-28-s"):
                citan.setdefault(i, []).append(r["id"])
    moc = registro.moc("moc-economia", "Economía", "Los números base de la economía: un bloque de world.json por nota, enlazado al documento 28.",
                       intro=(eco.get("nota", "") + "\n\nFuente de verdad: `studio/data/world.json` (bloque `economy`); explicación en %s." %
                              (existente(registro, "doc-28") or "el documento 28")), orden=66, auto_hijos=False)
    filas = []
    for clave, (titulo, seccion, extra) in BLOQUES.items():
        if clave not in eco:
            continue
        bloque = eco[clave]
        datos = bloque if isinstance(bloque, dict) else {"__lista__": bloque}
        sec = "doc-28-s%02d" % seccion
        linea = linea_de(lw, '    "%s":' % clave, max(ini - 1, 0)) if ini else 0
        cuerpo = lineas(bloque if isinstance(bloque, dict) else {"niveles": bloque}, ents)
        reglas_citan = sin_repetidos("sim-" + x for x in citan.get(sec, []))
        resumen = resumen_bloque(clave, datos)
        nota = registro.nueva(
            "eco-" + clave.replace("_", "-"), "economia", titulo, "economia", sufijo="economía", arriba="moc-economia",
            alias=["economy." + clave], fuente="%s:%d" % (WORLD, linea) if linea else WORLD, resumen=resumen, cuerpo="\n".join(cuerpo),
            props={"bloque": "economy." + clave, "seccion_doc28": ref(sec) if registro.existe(sec) else "28 §%d" % seccion})
        nota.relacion("Documento 28", [existente(registro, sec)] if registro.existe(sec) else [])
        nota.relacion("Reglas del simulador", [ref(x) for x in reglas_citan])
        nota.relacion("Relacionado", [ref_suave(e, "", e) for e in extra])
        filas.append((ref("eco-" + clave.replace("_", "-")), resumen, existente(registro, sec) or "28 §%d" % seccion))
    moc.cuerpo += "\n\n## Bloques\n\n" + "\n".join(tabla(["Bloque", "Cifras clave", "Sección del 28"], filas))
    moc.relacion("Documento", [existente(registro, "doc-28")])
    registro.info.append("economia: %d bloques" % len(filas))
