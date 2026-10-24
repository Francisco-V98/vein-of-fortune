"""Glosario ES/EN del documento 18 (sección 6): una nota por término.

Cada fila de las tablas 6.1 a 6.12 es un término con su español, su inglés (si ya está decidido), su estado y su nota de uso, y
enlaza a la sección del glosario de la biblia, a los documentos que cita y, si existe, a la nota del mundo que lo representa
(mineral, zona, facción, personaje…). Un término repetido en dos tablas (por ejemplo «Aetherita» en 6.2 y 6.3) es una sola nota.
"""
import re

from . import narr_fuentes as F
from . import texto as T
from .nucleo import ref, ref_suave

NOMBRE = "glosario"
DOC_18 = "studio/docs/18-biblia-narrativa.md"
SECCION_GLOSARIO = "doc-18-s06"
PENDIENTE = re.compile(r"⏳\s*(F\d-\d{2,3})")
CAPITULO = re.compile(r"^###\s+(6\.\d+)\s+(.*)$")
CARPETAS_DEL_MUNDO = ("generado/mundo", "generado/economia")


def _limpio(t):
    return re.sub(r"\s+", " ", re.sub(r"[*_]", "", t)).strip()


def _termino(espanol):
    """Término sin el número de zona («1 · Galerías del Hollín» -> «Galerías del Hollín»)."""
    return re.sub(r"^\d\s*·\s*", "", _limpio(espanol))


def _nombre_de_archivo(nombre):
    """«A · B · C» (varios términos en una fila) se lee «A, B y C» en el nombre del archivo."""
    partes = [p.strip() for p in nombre.split("·") if p.strip()]
    return nombre if len(partes) < 2 else ", ".join(partes[:-1]) + " y " + partes[-1]


def _filas(texto):
    """[(línea, capítulo, español, inglés, estado, uso)] de las tablas de las secciones 6.1 a 6.12."""
    lineas = texto.split("\n")
    desde = next((i for i, l in enumerate(lineas) if l.startswith("## 6 ·")), None)
    if desde is None:
        return []
    hasta = next((i for i in range(desde + 1, len(lineas)) if lineas[i].startswith("## ")), len(lineas))
    capitulo, filas = "6", []
    capitulos = {}
    for i in range(desde, hasta):
        m = CAPITULO.match(lineas[i])
        if m:
            capitulos[i] = m.group(1) + " " + m.group(2).strip()
    for n, cab, c in F.tablas(lineas, desde, hasta):
        if cab[:2] != ["Español", "English"] or len(c) != 4:
            continue
        capitulo = next((capitulos[i] for i in sorted(capitulos, reverse=True) if i < n), capitulo)
        filas.append((n, capitulo, c[0], c[1], c[2], c[3]))
    return filas


def _nota_del_mundo(registro, termino):
    """ID de la nota del mundo cuyo título o alias coincide con el término, si existe."""
    clave = termino.casefold()
    for nota in registro.notas.values():
        if nota.carpeta.startswith(CARPETAS_DEL_MUNDO) and (nota.titulo.casefold() == clave or clave in (a.casefold() for a in nota.alias)):
            return nota.id
    return None


def generar(registro, repo):
    ruta = repo / DOC_18
    if not ruta.is_file():
        registro.info.append("glosario: sin documento 18")
        return
    registro.moc("moc-glosario", "Glosario", "Cómo se dice cada cosa en español y en inglés (documento 18, sección 6).", orden=90, auto_hijos=False)
    terminos, ids_usados, por_capitulo = {}, set(), {}
    for linea, capitulo, espanol, ingles, estado, uso in _filas(ruta.read_text(encoding="utf-8")):
        nombre = _termino(espanol)
        clave = nombre.casefold()
        ingles_txt = _limpio(ingles)
        sin_ingles = ingles_txt.startswith("sin traducir")
        if clave in terminos:  # el mismo término en otra tabla: se anota en la nota que ya existe
            nota, datos = terminos[clave]
            datos["tambien"].append((capitulo, ingles_txt, _limpio(uso)))
            continue
        base = "term-" + T.slug(nombre, 48)
        tid, k = base, 2
        while tid in ids_usados:
            tid, k = "%s-%d" % (base, k), k + 1
        ids_usados.add(tid)
        pendiente = bool(PENDIENTE.search(estado + " " + ingles))
        conv_uso, _ = T.convertir(_limpio(uso), DOC_18)
        props = {"espanol": nombre, "capitulo": capitulo, "estado_glosario": "ingles-pendiente" if pendiente else "decidido"}
        if not sin_ingles:
            props["ingles"] = ingles_txt
        cuerpo = ["- **Español:** " + nombre, "- **English:** " + ("sin traducir todavía, el inglés lo propone el localizador" if sin_ingles else ingles_txt),
                  "- **Estado:** " + _limpio(estado), "", "## Nota de uso", "", conv_uso]
        nota = registro.nueva(
            tid, "termino", nombre, "glosario", nombre=_nombre_de_archivo(nombre), sufijo="término", props=props, tags=["estado/pendiente" if pendiente else "estado/hecho"],
            resumen=("%s" % ingles_txt if not sin_ingles else "inglés pendiente") + (" (inglés pendiente)" if pendiente and not sin_ingles else ""),
            cuerpo="\n".join(cuerpo), arriba="moc-glosario", fuente="%s:%d" % (DOC_18, linea))
        nota.relacion("Biblia", [ref(SECCION_GLOSARIO, "18 §6 Glosario ES/EN")] if registro.existe(SECCION_GLOSARIO) else [])
        nota.relacion("En el mundo", [ref(m)] if (m := _nota_del_mundo(registro, nombre)) else [])
        tareas = [t for t in dict.fromkeys(PENDIENTE.findall(estado + " " + ingles + " " + uso)) if registro.existe(t)]
        nota.relacion("Pendiente", [ref(t) for t in tareas])
        terminos[clave] = (nota, {"tambien": []})
        por_capitulo.setdefault(capitulo, []).append(nota)
    for nota, datos in terminos.values():
        if datos["tambien"]:
            extra = ["", "", "## También en", ""] + ["- **%s:** %s. %s" % (c, i, u) for c, i, u in datos["tambien"]]
            nota.cuerpo += "\n".join(extra)
            nota.props["tambien_en"] = [c for c, _, _ in datos["tambien"]]
    cuerpo = ["%d términos del glosario oficial. **Cada término se usa igual en todo el proyecto**: interfaz, diálogos, prensa, tienda y arte." % len(terminos),
              "", "Fuente: %s." % (ref(SECCION_GLOSARIO, "18 §6 Glosario ES/EN") if registro.existe(SECCION_GLOSARIO) else "documento 18, sección 6"), ""]
    for capitulo, notas in por_capitulo.items():
        cuerpo += ["## " + capitulo, ""] + ["- %s — %s" % (ref(n.id), n.resumen) for n in notas] + [""]
    registro.nota("moc-glosario").cuerpo = "\n".join(cuerpo)
    registro.info.append("glosario: %d términos en %d tablas" % (len(terminos), len(por_capitulo)))
