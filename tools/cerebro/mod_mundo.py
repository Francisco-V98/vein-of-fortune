"""Mundo: actos, zonas de minado, asentamientos, edificaciones, minerales, recetas, minijuegos, mecánicas, facciones,
personajes y PNJ (studio/data/world.json) y las edificaciones `ed-*` del catálogo del documento 26.

IDs: acto-I, zona-galerias-hollin, asent-villa-brasa, ed-vb-tienda, min-carbon, rec-acero, mj-picado, mec-taller,
fac-union, pj-reme, npc-voceador. Las relaciones cruzadas (mineral <-> zona <-> edificación <-> facción <-> personaje) se
calculan aquí; los demás módulos (economía, arte, narrativa) se enganchan a estos IDs.
"""
import re

from . import texto as T
from .ayudas import (ACTOS, cargar, existente, lineas_de, linea_de, menciona, norm, sin_repetidos, tabla, valor)
from .nucleo import ref, ref_suave

NOMBRE = "mundo"
WORLD = "studio/data/world.json"
GENERICOS = {"tienda", "taller", "almacen"}  # nombres de edificación que llevan siempre su asentamiento
STOP_NOMBRE = {"dona", "don", "ministro", "inspector", "protagonista", "el", "la", "los", "las", "de", "del", "y", "en"}
FAC_PALABRAS = {
    "ministerio": ["ministerio", "licencias"],
    "comision": ["comision"],
    "consorcio": ["consorcio"],
    "union": ["union", "sindical"],
    "faroleros": ["farolero", "farol"],
    "teletipo": ["teletipo"],
}
MINERAL_PALABRAS = {"aetherita": ["aetherita"], "esmeralda": ["esmeralda"], "diamante": ["diamante"]}  # el resto: su nombre
ASENT = {  # ID del lugar en world.json -> nombre del asentamiento (documento 26, secciones 1.2 y 1.3)
    "villa-brasa": ("Villa Brasa",),
    "altafria": ("Altafría",),
    "salinas-blancas": ("Salinas Blancas",),
    "cavernas": ("Campamento de las Cavernas",),
    "fosa": ("Campamento de la Comisión",),
    "puerto-meridiano": ("Puerto Meridiano",),
}
PERSONAJE_NOMBRE = {"reme": "Reme", "montenegro": "Ministro Montenegro"}
PERSONAJE_DOCS = {"reme": ["doc-22"], "anselmo": ["doc-21"], "montenegro": ["doc-25"]}
MECANICA_NOMBRE = {"escaner": "Escáner", "mejora-detector": "Mejora del detector", "taller": "Taller (mecánica)"}
ACTO_DOCS = {"I": ["doc-27", "doc-24"], "II": ["doc-22", "doc-24"], "III": ["doc-24", "doc-25"], "IV": ["doc-25", "doc-24"]}
FILA_ED = re.compile(r"^\|\s*`(ed-[a-z0-9-]+)`\s*\|")
VERSION = re.compile(r"MVP|V2\.[0-9]|V1|evolutivo")


# --- lectura del catálogo de edificaciones (documento 26, sección 2) --------------------------------------------------
def leer_catalogo(repo):
    """[{id, nombre, rol, desc, version, marca, place, linea, ruta, intro}] de las filas `ed-*` de la sección 2."""
    ruta = next(iter(sorted((repo / "studio" / "docs").glob("26-*.md"))), None)
    if ruta is None:
        return [], None
    rel = ruta.relative_to(repo).as_posix()
    lineas = ruta.read_text(encoding="utf-8").split("\n")
    dentro, place, intros, filas = False, None, {}, []
    for n, linea in enumerate(lineas, 1):
        if linea.startswith("## "):
            dentro = linea.startswith("## 2 ")
            continue
        if not dentro:
            continue
        if linea.startswith("### "):
            titulo = norm(linea)
            place = next((p for clave, p in (("hollin", "villa-brasa"), ("sierra alta", "altafria"), ("salares", "salinas-blancas"),
                                             ("cavernas", "cavernas"), ("fosa", "fosa"), ("puerto meridiano", "puerto-meridiano"))
                          if clave in titulo), None)
            intros[place] = ""
            continue
        if place is not None and not intros.get(place) and linea.strip() and not linea.startswith(("|", "**", "#")):
            intros[place] = linea.strip()
        if FILA_ED.match(linea):
            c = [x.strip() for x in re.split(r"(?<!\\)\|", linea.strip().strip("|"))]
            if len(c) >= 6:
                v = VERSION.search(c[4])
                filas.append({"id": c[0].strip("`"), "nombre": c[1], "rol": c[2], "desc": c[3], "version": v.group(0) if v else c[4],
                              "version_texto": c[4], "marca": c[5], "place": place, "linea": n, "ruta": rel})
    for f in filas:
        f["intro"] = intros.get(f["place"], "")
    return filas, rel


def nombre_visible_ed(nombre):
    return re.sub(r"\s*\([^)]*\)", "", nombre).strip()


# --- relaciones por texto ------------------------------------------------------------------------------------------------
class Mundo:
    """Datos de world.json y tablas de búsqueda por texto."""

    def __init__(self, w):
        self.w = w
        self.minerales = {m["id"]: m for m in w.get("minerals", [])}
        self.zonas = {z["id"]: z for z in w.get("zones", [])}
        self.minijuegos = {m["id"]: m for m in w.get("minigames", [])}
        self.mecanicas = {m["id"]: m for m in w.get("mechanics", [])}
        self.recetas = {r["id"]: r for r in w.get("recipes", [])}
        self.facciones = {f["id"]: f for f in w.get("factions", [])}
        self.personajes = {c["id"]: c for c in w.get("characters", [])}
        self.npcs = {n["id"]: n for n in w.get("npcs", [])}
        self.tokens_pj = self._tokens_personajes()

    def _tokens_personajes(self):
        """Palabras del nombre que identifican a un personaje (se descartan las que comparte con otra entidad)."""
        por_entidad = {}
        for tipo, d in (("pj", self.personajes), ("npc", self.npcs), ("fac", self.facciones)):
            for i, e in d.items():
                por_entidad[(tipo, i)] = set(re.findall(r"[a-z]{3,}", norm(e["name"]))) - STOP_NOMBRE
        res = {}
        for (tipo, i), palabras in por_entidad.items():
            if tipo != "pj":
                continue
            otras = set().union(*(p for k, p in por_entidad.items() if k != (tipo, i)))
            res[i] = sorted(palabras - otras)
        return res

    def personas_en(self, texto):
        t = norm(texto)
        return [i for i, toks in self.tokens_pj.items() if any(menciona(t, tok) for tok in toks)]

    def npcs_en(self, texto):
        t = norm(texto)
        extra = {"voceador": ["voceador"]}
        return [i for i, n in self.npcs.items()
                if menciona(t, norm(n["name"])) or any(menciona(t, x) for x in extra.get(i, []))]

    def facciones_en(self, texto):
        t = norm(texto)
        return [i for i in self.facciones if any(menciona(t, p) for p in FAC_PALABRAS.get(i, [norm(self.facciones[i]["name"])]))]

    def minerales_en(self, texto):
        t = norm(texto)
        return [i for i, m in self.minerales.items() if any(menciona(t, p) for p in MINERAL_PALABRAS.get(i, [norm(m["name"])]))]

    def minijuegos_en(self, texto):
        t = norm(texto)
        return [i for i, m in self.minijuegos.items() if menciona(t, norm(m["name"]))]

    def recetas_en(self, texto):
        t = norm(texto)
        return [i for i, r in self.recetas.items() if menciona(t, norm(r["name"]))]

    def acto_zona(self, z):
        return z.get("act")

    def acto_mineral(self, mid):
        actos = [self.zonas[z]["act"] for z in self.minerales[mid].get("zones", {}) if z in self.zonas]
        return min(actos, key=ACTOS.index) if actos else None

    def entidades(self):
        """ID crudo -> ID de nota (para convertir en enlaces los valores que son IDs en los bloques de economía)."""
        ents = {}
        for d, pre in ((self.minijuegos, "mj-"), (self.facciones, "fac-"), (self.recetas, "rec-"), (self.minerales, "min-")):
            for i in d:
                ents[i] = pre + i
        for p in ASENT:
            ents[p] = "asent-" + p
        return ents


def _min_acto(acto):
    return ACTOS.index(acto) if acto in ACTOS else 99


def _tags(acto=None, version=None):
    tags = []
    if acto:
        tags.append("acto/%s" % acto)
    if version:
        tags.append("version/%s" % version.replace(".", "-"))
    return tags


def _linea_w(lineas, seccion, id_):
    ini = linea_de(lineas, '"%s": [' % seccion)
    return linea_de(lineas, '"id": "%s"' % id_, max(ini - 1, 0)) if ini else 0


def _fuente_w(lineas, seccion, id_):
    n = _linea_w(lineas, seccion, id_)
    return "%s:%d" % (WORLD, n) if n else WORLD


# --- generación ------------------------------------------------------------------------------------------------------------
def generar(registro, repo):
    w = cargar(repo, WORLD)
    if not w:
        registro.info.append("mundo: no hay world.json, se omite")
        return
    m = Mundo(w)
    lw = lineas_de(repo, WORLD)
    catalogo, ruta26 = leer_catalogo(repo)
    ed_por_place, ed_de_mineral, ed_de_pj, ed_de_npc, ed_de_fac, ed_de_mj, ed_de_rec = {}, {}, {}, {}, {}, {}, {}
    ed_info = {}
    for f in catalogo:
        texto = " ".join([f["nombre"], f["rol"], f["desc"]])
        es_mina = re.search(r"-mina(-|$)", f["id"]) is not None
        zona = None
        if es_mina:
            cand = [z for z, d in m.zonas.items() if d.get("place") == f["place"]]
            zona = cand[0] if len(cand) == 1 else next((z for z in cand if z.split("-")[0] in f["id"]), None)
        minerales = list(m.zonas[zona]["zone_mix"]) if zona and m.zonas[zona].get("zone_mix") else m.minerales_en(texto)
        pjs = m.personas_en(texto)
        npcs = m.npcs_en(texto)
        facs = sin_repetidos(m.facciones_en(texto) + [m.personajes[p]["faction"] for p in pjs if m.personajes[p].get("faction") in m.facciones]
                             + [m.npcs[n]["faction"] for n in npcs if m.npcs[n].get("faction") in m.facciones])
        mjs = m.minijuegos_en(f["rol"] + " " + f["desc"])
        recs = m.recetas_en(texto)
        ed_info[f["id"]] = {"zona": zona, "minerales": minerales, "pjs": pjs, "npcs": npcs, "facs": facs, "mjs": mjs, "recs": recs}
        ed_por_place.setdefault(f["place"], []).append(f["id"])
        for lista, destino in ((minerales, ed_de_mineral), (pjs, ed_de_pj), (npcs, ed_de_npc), (facs, ed_de_fac), (mjs, ed_de_mj), (recs, ed_de_rec)):
            for x in lista:
                destino.setdefault(x, []).append(f["id"])

    moc_mundo = registro.moc("moc-mundo", "Mundo", "Actos, zonas, minerales, recetas, minijuegos, mecánicas, facciones y personajes de Valdoria.",
                             intro="Datos de `studio/data/world.json` (la fuente de verdad) y el catálogo de edificaciones del documento 26. "
                                   "Cada elemento es una nota; los mapas de abajo agrupan por tipo.", orden=60)
    mocs = {
        "moc-minerales": registro.moc("moc-minerales", "Minerales", "Los diez minerales con sus zonas, recetas y cifras base.", orden=61),
        "moc-zonas": registro.moc("moc-zonas", "Zonas", "Zonas de minado y asentamientos de Valdoria.", orden=62),
        "moc-edificaciones": registro.moc("moc-edificaciones", "Edificaciones", "Catálogo de edificaciones por asentamiento (documento 26).", orden=63,
                                          auto_hijos=False),
        "moc-facciones": registro.moc("moc-facciones", "Facciones", "Las seis facciones y su gente.", orden=64),
        "moc-personajes": registro.moc("moc-personajes", "Personajes", "Los personajes con nombre y los PNJ genéricos.", orden=65),
    }
    moc_mundo.relacion("Mapas", [ref(i) for i in mocs] + [x for x in (existente(registro, "moc-economia"),) if x])
    dm = lambda *ids: [x for x in (existente(registro, i) for i in ids) if x]  # noqa: E731 - documentos que existan

    # actos ---------------------------------------------------------------------------------------------------------------
    for acto in w.get("acts", []):
        zonas = [z for z, d in m.zonas.items() if d["act"] == acto]
        mjs = [i for i, d in m.minijuegos.items() if d["act"] == acto]
        recs = [i for i, d in m.recetas.items() if d["act"] == acto]
        pjs = [i for i, d in m.personajes.items() if d.get("act") == acto]
        mecs = [i for i, d in m.mecanicas.items() if d.get("act") == acto]
        mins = [i for i in m.minerales if m.acto_mineral(i) == acto]
        nota = registro.nueva(
            "acto-" + acto, "acto", "Acto " + acto, "mundo/actos", sufijo="acto", alias=["Acto " + acto], tags=_tags(acto), arriba="moc-mundo",
            props={"acto": acto, "zonas": len(zonas), "minerales": len(mins)}, orden=ACTOS.index(acto) if acto in ACTOS else 9,
            resumen="Zonas: %s · minijuegos: %s" % (", ".join(m.zonas[z]["name"] for z in zonas) or "ninguna nueva",
                                                     ", ".join(m.minijuegos[i]["name"] for i in mjs) or "ninguno nuevo"),
            cuerpo="Lo que el mundo abre en el Acto %s según `world.json`." % acto, fuente=WORLD)
        nota.relacion("Zonas de minado", [ref("zona-" + z) for z in zonas])
        nota.relacion("Minerales que se estrenan", [ref("min-" + i) for i in mins])
        nota.relacion("Minijuegos", [ref("mj-" + i) for i in mjs])
        nota.relacion("Recetas", [ref("rec-" + i) for i in recs])
        nota.relacion("Mecánicas", [ref("mec-" + i) for i in mecs])
        nota.relacion("Personajes que entran", [ref("pj-" + i) for i in pjs])
        nota.relacion("Documentos", dm(*ACTO_DOCS.get(acto, [])))

    # minerales -------------------------------------------------------------------------------------------------------------
    recetas_de = {}
    for rid, r in m.recetas.items():
        for grupo in r.get("inputs", []):
            for mid in grupo:
                recetas_de.setdefault(mid, []).append(rid)
    for mid, d in m.minerales.items():
        acto = m.acto_mineral(mid)
        zonas = d.get("zones", {})
        ficha = [("Volatilidad", "%s (%s)" % (d.get("volatility"), d.get("volatility_num"))), ("Nivel (tier)", d.get("tier")),
                 ("Unidad", d.get("unit")), ("Energía por mena", d.get("energy")), ("Rendimiento", d.get("yield")),
                 ("Precio base (esquirlas)", d.get("base_price")), ("Sigma", d.get("sigma")), ("Tope diario de extracción", d.get("daily_cap")),
                 ("Liquidez", d.get("liquidity")), ("Tope del comprador", d.get("buyer_cap")), ("Costo de almacén", d.get("storage_pct")),
                 ("Spread", d.get("spread")), ("Prima del mercado negro", d.get("black_premium"))]
        cuerpo = ["## Ficha base", ""] + tabla(["Campo", "Valor"], [(k, valor(v)) for k, v in ficha if v is not None])
        if d.get("season"):
            cuerpo += ["", "## Estacionalidad (puntos de mercado)", ""] + tabla(["Estación", "Puntos"], [(k, valor(v)) for k, v in d["season"].items()])
        if d.get("event_sens"):
            cuerpo += ["", "## Sensibilidad a eventos", ""] + ["- **%s:** ×%s" % (k, valor(v)) for k, v in d["event_sens"].items()]
        if d.get("sectors"):
            cuerpo += ["", "## Sectores de demanda (%)", ""] + ["- **%s:** %s" % (k, valor(v)) for k, v in d["sectors"].items()]
        if zonas:
            cuerpo += ["", "## Dónde se extrae", ""] + ["- %s: %s" % (ref("zona-" + z), rol) for z, rol in zonas.items() if z in m.zonas]
        nota = registro.nueva(
            "min-" + mid, "mineral", d["name"], "mundo/minerales", sufijo="mineral", alias=[mid] if mid != d["name"] else [], arriba="moc-minerales",
            tags=_tags(acto), fuente=_fuente_w(lw, "minerals", mid),
            props={"acto": acto, "nivel": d.get("tier"), "precio_base": d.get("base_price"), "volatilidad": d.get("volatility"),
                   "zonas": [ref("zona-" + z) for z in zonas if z in m.zonas], "recetas": [ref("rec-" + r) for r in recetas_de.get(mid, [])]},
            resumen="Nivel %s · %s · %s esquirlas por %s · %d zonas" % (d.get("tier"), d.get("volatility"), d.get("base_price"), d.get("unit"), len(zonas)),
            cuerpo="\n".join(cuerpo))
        nota.relacion("Zonas", [ref("zona-" + z) for z in zonas if z in m.zonas])
        nota.relacion("Recetas", [ref("rec-" + r) for r in recetas_de.get(mid, [])])
        nota.relacion("Minijuegos", [ref("mj-" + j) for j in d.get("minigames", []) if j in m.minijuegos])
        nota.relacion("Edificaciones", [ref(e) for e in ed_de_mineral.get(mid, [])])
        nota.relacion("Se estrena en", [ref("acto-" + acto)] if acto else [])
        nota.relacion("Documentos", dm("doc-05", "doc-02", "doc-28-s03"))

    # zonas de minado y asentamientos -----------------------------------------------------------------------------------------
    zonas_de_place = {}
    for z, d in m.zonas.items():
        zonas_de_place.setdefault(d.get("place"), []).append(z)
    for z, d in m.zonas.items():
        mezcla = d.get("zone_mix", {})
        cuerpo = ["Región **%s**. %s." % (d.get("region"), "Zona profunda: %s bloques por expedición" % d.get("blocks") if d.get("deep")
                                         else "Zona normal: 1 bloque por expedición"), "", "## Mezcla de menas", ""]
        cuerpo += tabla(["Mineral", "%"], [(ref("min-" + mid), v) for mid, v in mezcla.items() if mid in m.minerales])
        if d.get("open_weekdays"):
            cuerpo += ["", "Solo abre los días %s de cada semana." % ", ".join(str(x) for x in d["open_weekdays"])]
        bocas = [e for e in ed_por_place.get(d.get("place"), []) if ed_info[e]["zona"] == z]
        nota = registro.nueva(
            "zona-" + z, "zona", d["name"], "mundo/zonas", sufijo="zona", arriba="moc-zonas", tags=_tags(d.get("act")), fuente=_fuente_w(lw, "zones", z),
            props={"acto": d.get("act"), "region": d.get("region"), "profunda": bool(d.get("deep")), "bloques": d.get("blocks"),
                   "riqueza_inicial": d.get("initial_wealth"), "asentamiento": ref("asent-" + d["place"]) if d.get("place") in ASENT else d.get("place")},
            resumen="%s · Acto %s · %s" % (d.get("region"), d.get("act"), ", ".join(m.minerales[i]["name"] for i in mezcla if i in m.minerales)),
            cuerpo="\n".join(cuerpo))
        nota.relacion("Asentamiento", [ref("asent-" + d["place"])] if d.get("place") in ASENT else [])
        nota.relacion("Boca de mina", [ref(e) for e in bocas])
        nota.relacion("Minerales", [ref("min-" + i) for i in mezcla if i in m.minerales])
        nota.relacion("Se abre en", [ref("acto-" + d["act"])] if d.get("act") else [])
        nota.relacion("Documentos", dm("doc-02", "doc-26-s01", "doc-28-s03"))
    rutas = {(r["a"], r["b"]): r["cost"] for r in w.get("economy", {}).get("travel", {}).get("routes", [])}
    for p, (titulo,) in ASENT.items():
        zs = zonas_de_place.get(p, [])
        acto = min((m.zonas[z]["act"] for z in zs), key=_min_acto) if zs else ("III" if p == "puerto-meridiano" else None)
        intro = next((e["intro"] for e in catalogo if e["place"] == p), "")
        resumen = T.primera_frase(intro)
        cuerpo = [T.convertir(intro, ruta26 or "")[0]] if intro and len(intro) > len(resumen) + 3 else []
        cuerpo += ["", "## Trayectos (esquirlas, ida o vuelta)", ""]
        cuerpo += tabla(["Destino", "Costo"], [(ref("asent-" + o), rutas.get((p, o), rutas.get((o, p)))) for o in ASENT
                                              if o != p and ((p, o) in rutas or (o, p) in rutas)])
        facs = sin_repetidos(f for e in ed_por_place.get(p, []) for f in ed_info[e]["facs"])
        regs = sin_repetidos(m.zonas[z]["region"] for z in zs)
        nota = registro.nueva(
            "asent-" + p, "asentamiento", titulo, "mundo/zonas", sufijo="asentamiento", arriba="moc-zonas", tags=_tags(acto), fuente=ruta26,
            alias=["Región " + r for r in regs] + (["Región Puerto Meridiano"] if p == "puerto-meridiano" else []),
            props={"acto": acto, "region": ", ".join(regs) or "Puerto Meridiano", "edificaciones": len(ed_por_place.get(p, []))},
            resumen=resumen or ("Asentamiento de %s" % ", ".join(regs)), cuerpo="\n".join(cuerpo))
        nota.relacion("Zonas de minado", [ref("zona-" + z) for z in zs])
        nota.relacion("Edificaciones", [ref(e) for e in ed_por_place.get(p, [])])
        nota.relacion("Facciones presentes", [ref("fac-" + f) for f in facs])
        nota.relacion("Se abre en", [ref("acto-" + acto)] if acto else [])
        nota.relacion("Documentos", dm("doc-26-s01", "doc-26-s02"))

    # edificaciones ---------------------------------------------------------------------------------------------------------
    for f in catalogo:
        info = ed_info[f["id"]]
        base = nombre_visible_ed(f["nombre"])
        asent = ASENT.get(f["place"], ("", ""))[0]
        nombre = "%s de %s" % (base, asent) if norm(base) in GENERICOS and asent else base
        conv, citas = T.convertir(f["desc"], f["ruta"])
        cuerpo = ["**Rol:** %s" % f["rol"], "", "**Qué la hace de su zona:** %s" % conv, "", "**Versión:** %s" % f["version_texto"]]
        if info["zona"]:
            cuerpo += ["", "Entrada a la zona de minado %s." % ref("zona-" + info["zona"])]
        nota = registro.nueva(
            f["id"], "edificacion", f["nombre"], "mundo/edificaciones", nombre=nombre, sufijo=asent or "edificación", arriba="moc-edificaciones",
            tags=_tags(version=f["version"]), fuente="%s:%d" % (f["ruta"], f["linea"]),
            props={"asentamiento": ref("asent-" + f["place"]) if f["place"] in ASENT else f["place"], "rol": f["rol"], "version": f["version"],
                   **({"zona": ref("zona-" + info["zona"])} if info["zona"] else {})},
            resumen=T.primera_frase(f["desc"]) or base, cuerpo="\n".join(cuerpo))
        nota.relacion("Asentamiento", [ref("asent-" + f["place"])] if f["place"] in ASENT else [])
        nota.relacion("Zona de minado", [ref("zona-" + info["zona"])] if info["zona"] else [])
        nota.relacion("Minerales", [ref("min-" + i) for i in info["minerales"]])
        nota.relacion("Facciones", [ref("fac-" + i) for i in info["facs"]])
        nota.relacion("Personajes", [ref("pj-" + i) for i in info["pjs"]])
        nota.relacion("PNJ", [ref("npc-" + i) for i in info["npcs"]])
        nota.relacion("Minijuegos", [ref("mj-" + i) for i in info["mjs"]])
        nota.relacion("Recetas", [ref("rec-" + i) for i in info["recs"]])
        nota.relacion("Tareas", [ref_suave(t, t, t) for t in citas.tareas])
        nota.relacion("Documento", dm("doc-26-s02"))
    moc_ed = registro.nota("moc-edificaciones")
    cuerpo = ["Catálogo del documento 26, sección 2: **%d edificaciones** en %d asentamientos." % (len(catalogo), len(ed_por_place))]
    for p in ASENT:
        if ed_por_place.get(p):
            cuerpo += ["", "## " + ref("asent-" + p), ""]
            cuerpo += tabla(["Edificación", "Rol", "Versión"], [(ref(e), next(x["rol"] for x in catalogo if x["id"] == e),
                                                              next(x["version"] for x in catalogo if x["id"] == e)) for e in ed_por_place[p]])
    moc_ed.cuerpo = "\n".join(cuerpo)
    moc_ed.relacion("Documento", dm("doc-26-s02"))

    # recetas, minijuegos y mecánicas ---------------------------------------------------------------------------------------
    for rid, r in m.recetas.items():
        grupos = [" o ".join(m.minerales[x]["name"] for x in g if x in m.minerales) for g in r.get("inputs", [])]
        cuerpo = ["**Ingredientes:** " + " + ".join(grupos) + ".", ""]
        compradores = r.get("buyers", [])
        if compradores:
            cuerpo.append("**Compradores:** " + ", ".join(ref("fac-" + b) for b in compradores if b in m.facciones) + ".")
        if "sells_in_store" in r:
            cuerpo.append("Se vende en la tienda: %s. Pedidos de cliente: %s. Cuenta contra el tope diario de Aetherita: %s." % (
                valor(r.get("sells_in_store")), valor(r.get("customer_orders")), valor(r.get("counts_against_aetherita_cap"))))
        if r.get("fuente"):
            cuerpo += ["", "> " + r["fuente"]]
        nota = registro.nueva(
            "rec-" + rid, "receta", r["name"], "mundo/recetas", sufijo="receta", arriba="moc-mundo", tags=_tags(r.get("act")), fuente=_fuente_w(lw, "recipes", rid),
            props={"acto": r.get("act"), "ingredientes": " + ".join(grupos), "compradores": [ref("fac-" + b) for b in compradores if b in m.facciones]},
            resumen=" + ".join(grupos), cuerpo="\n".join(cuerpo))
        nota.relacion("Minerales", [ref("min-" + x) for g in r.get("inputs", []) for x in g if x in m.minerales])
        nota.relacion("Compradores", [ref("fac-" + b) for b in compradores if b in m.facciones])
        nota.relacion("Se hace en", [ref("mec-taller")] if "taller" in m.mecanicas else [])
        nota.relacion("Edificaciones", [ref(e) for e in ed_de_rec.get(rid, [])])
        nota.relacion("Se desbloquea en", [ref("acto-" + r["act"])] if r.get("act") else [])
        nota.relacion("Documentos", dm("doc-05", "doc-28-s03"))
    herramientas = w.get("economy", {}).get("tools", {}).get("types", [])
    for jid, d in m.minijuegos.items():
        mins = [mid for mid, x in m.minerales.items() if jid in x.get("minigames", [])]
        tools = [t["id"] for t in herramientas if t.get("minigame") == jid]
        cuerpo = ["Minijuego de extracción o de tienda que se estrena en el Acto %s." % d["act"]]
        if tools:
            cuerpo.append("Herramienta que lo usa: %s." % ", ".join("`%s`" % t for t in tools))
        nota = registro.nueva(
            "mj-" + jid, "minijuego", d["name"], "mundo/minijuegos", sufijo="minijuego", arriba="moc-mundo", tags=_tags(d.get("act")),
            props={"acto": d.get("act"), "herramientas": tools}, resumen="Acto %s · %s" % (d["act"], ", ".join(m.minerales[i]["name"] for i in mins) or "tienda"),
            cuerpo="\n\n".join(cuerpo), fuente=_fuente_w(lw, "minigames", jid))
        nota.relacion("Minerales", [ref("min-" + i) for i in mins])
        nota.relacion("Edificaciones", [ref(e) for e in ed_de_mj.get(jid, [])])
        nota.relacion("Se estrena en", [ref("acto-" + d["act"])] if d.get("act") else [])
        nota.relacion("Documentos", dm("doc-09", "doc-28-s05"))
    for cid, d in m.mecanicas.items():
        docs = sin_repetidos("doc-%s" % n for mm in re.finditer(r"docs?/?\s*((?:\d{2})(?:\s*(?:y|,)\s*\d{2})*)", d.get("fuente", ""))
                             for n in re.findall(r"\d{2}", mm.group(1)))
        cuerpo = ["Mecánica del Acto %s." % d["act"]]
        if d.get("fuente"):
            cuerpo += ["", "> " + d["fuente"]]
        nota = registro.nueva(
            "mec-" + cid, "mecanica", d["name"], "mundo/mecanicas", nombre=MECANICA_NOMBRE.get(cid), sufijo="mecánica", arriba="moc-mundo",
            tags=_tags(d.get("act")), props={"acto": d.get("act")}, resumen=T.primera_frase(d.get("fuente", "")) or d["name"],
            cuerpo="\n".join(cuerpo), fuente=_fuente_w(lw, "mechanics", cid))
        nota.relacion("Necesita minerales", [ref("min-" + x) for x in d.get("needs_minerals", []) if x in m.minerales])
        nota.relacion("Se abre en", [ref("acto-" + d["act"])] if d.get("act") else [])
        if cid == "taller":
            nota.relacion("Recetas", [ref("rec-" + r) for r in m.recetas])
            if registro.existe("ed-vb-taller"):
                nota.relacion("Edificaciones", [ref("ed-vb-taller")])
                registro.nota("ed-vb-taller").relacion("Mecánica", [ref("mec-taller")])
        nota.relacion("Documentos", dm(*docs))

    # facciones, personajes y PNJ ---------------------------------------------------------------------------------------------
    for fid, d in m.facciones.items():
        miembros = [p for p, x in m.personajes.items() if x.get("faction") == fid]
        gente = [n for n, x in m.npcs.items() if x.get("faction") == fid]
        compra = [r for r, x in m.recetas.items() if fid in x.get("buyers", [])]
        subs = [f for f, x in m.facciones.items() if x.get("parent") == fid]
        cuerpo = ["Facción de Valdoria: %d personajes con nombre y %d PNJ genéricos." % (len(miembros), len(gente))]
        if d.get("parent"):
            cuerpo.append("Depende de %s." % ref("fac-" + d["parent"]))
        nota = registro.nueva(
            "fac-" + fid, "faccion", d["name"], "mundo/facciones", sufijo="facción", arriba="moc-facciones", fuente=_fuente_w(lw, "factions", fid),
            props={"personajes": len(miembros), "pnj": len(gente), **({"depende_de": ref("fac-" + d["parent"])} if d.get("parent") else {})},
            resumen="%d personajes · %d PNJ · %d edificaciones" % (len(miembros), len(gente), len(ed_de_fac.get(fid, []))), cuerpo="\n\n".join(cuerpo))
        nota.relacion("Depende de", [ref("fac-" + d["parent"])] if d.get("parent") else [])
        nota.relacion("Dependen de ella", [ref("fac-" + s) for s in subs])
        nota.relacion("Personajes", [ref("pj-" + p) for p in miembros])
        nota.relacion("PNJ", [ref("npc-" + n) for n in gente])
        nota.relacion("Edificaciones", [ref(e) for e in ed_de_fac.get(fid, [])])
        nota.relacion("Compra", [ref("rec-" + r) for r in compra])
        nota.relacion("Documentos", dm("doc-07", "doc-19"))
    for pid, d in m.personajes.items():
        nombre = PERSONAJE_NOMBRE.get(pid, d["name"])
        primeras = [x for x in m.tokens_pj.get(pid, []) if len(x) >= 3]
        alias = sin_repetidos([nombre, d["name"]] + list(d.get("aka", [])) + [x.capitalize() for x in primeras] + ["Doña Reme" if pid == "reme" else ""])
        alias = [a for a in alias if a]  # incluye el nombre visible: los hilos enlazan a los personajes por él
        fac = d.get("faction")
        cuerpo = ["Personaje del Acto %s." % d.get("act")]
        if d.get("nota"):
            cuerpo += ["", d["nota"]]
        if d.get("aka"):
            cuerpo += ["", "También aparece como: " + ", ".join("«%s»" % a for a in d["aka"]) + "."]
        nota = registro.nueva(
            "pj-" + pid, "personaje", nombre, "mundo/personajes", sufijo="personaje", alias=alias, arriba="moc-personajes", tags=_tags(d.get("act")),
            props={"acto": d.get("act"), "nombre_completo": d["name"], "faccion": ref("fac-" + fac) if fac in m.facciones else fac},
            resumen="Acto %s · %s" % (d.get("act"), m.facciones[fac]["name"] if fac in m.facciones else ("facción variable" if fac else "sin facción")),
            cuerpo="\n".join(cuerpo), fuente=_fuente_w(lw, "characters", pid))
        nota.relacion("Facción", [ref("fac-" + fac)] if fac in m.facciones else [])
        nota.relacion("Entra en", [ref("acto-" + d["act"])] if d.get("act") else [])
        nota.relacion("Edificaciones", [ref(e) for e in ed_de_pj.get(pid, [])])
        nota.relacion("Documentos", dm("doc-19", "doc-18", *PERSONAJE_DOCS.get(pid, [])))
    for nid, d in m.npcs.items():
        fac = d.get("faction")
        nota = registro.nueva(
            "npc-" + nid, "pnj", d["name"], "mundo/npc", sufijo="PNJ", arriba="moc-personajes", fuente=_fuente_w(lw, "npcs", nid),
            props={"grupo": d.get("group"), "faccion": ref("fac-" + fac) if fac in m.facciones else fac},
            resumen="%s · %s" % (d.get("group"), m.facciones[fac]["name"] if fac in m.facciones else "sin facción"),
            cuerpo="PNJ genérico del grupo «%s»." % d.get("group"))
        nota.relacion("Facción", [ref("fac-" + fac)] if fac in m.facciones else [])
        nota.relacion("Edificaciones", [ref(e) for e in ed_de_npc.get(nid, [])])
        nota.relacion("Documentos", dm("doc-12", "doc-07"))

    # mapas ---------------------------------------------------------------------------------------------------------------------
    reglas = w.get("rules", {})
    moc_min = registro.nota("moc-minerales")
    moc_min.cuerpo = "Los minerales de `world.json`: nivel, precio base y zonas."
    if reglas.get("mineral_zones_min"):
        moc_min.cuerpo += "\n\nRegla: cada mineral aparece en %s a %s zonas, salvo %s." % (
            reglas["mineral_zones_min"], reglas.get("mineral_zones_max"),
            " y ".join(ref("min-" + x) for x in reglas.get("mineral_zones_excepciones", []) if x in m.minerales))
    moc_mundo.cuerpo += "\n\n**Cifras:** %d minerales, %d zonas de minado, %d asentamientos, %d edificaciones." % (
        len(m.minerales), len(m.zonas), len(ASENT), len(catalogo))
    registro.info.append("mundo: %d actos, %d minerales, %d zonas, %d asentamientos, %d edificaciones, %d recetas, %d minijuegos, %d mecánicas, "
                         "%d facciones, %d personajes, %d PNJ" % (len(w.get("acts", [])), len(m.minerales), len(m.zonas), len(ASENT), len(catalogo),
                                                                  len(m.recetas), len(m.minijuegos), len(m.mecanicas), len(m.facciones),
                                                                  len(m.personajes), len(m.npcs)))
