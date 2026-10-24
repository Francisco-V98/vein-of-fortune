"""Ayudas compartidas por los módulos de datos (mundo, economía, QA, simulador, arte).

Leer JSON del repo, localizar líneas, normalizar texto para buscar menciones, convertir referencias «28 §7.2» a IDs de
sección y volcar estructuras JSON como listas legibles con enlaces.
"""
import json
import re
import unicodedata

from .nucleo import ref

ACTOS = ["I", "II", "III", "IV"]
REF_DOC = re.compile(r"^(\d{2})(?:\s*§\s*(\d+)(?:\.\d+)?)?$")


def cargar(repo, ruta):
    """JSON del repo (ruta relativa) o None si no existe."""
    p = repo / ruta
    if not p.is_file():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def lineas_de(repo, ruta):
    p = repo / ruta
    return p.read_text(encoding="utf-8").split("\n") if p.is_file() else []


def linea_de(lineas, patron, desde=0):
    """Número de línea (desde 1) de la primera que contiene `patron` a partir de `desde`; 0 si no está."""
    for i in range(desde, len(lineas)):
        if patron in lineas[i]:
            return i + 1
    return 0


def norm(texto):
    """Minúsculas sin acentos ni marcas Markdown, para buscar menciones."""
    t = unicodedata.normalize("NFKD", str(texto))
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    return re.sub(r"[*_`]", "", t)


def menciona(texto_norm, palabra):
    """¿Aparece `palabra` (ya normalizada) como palabra completa? Admite plural simple en la última palabra."""
    return re.search(r"\b" + re.escape(palabra) + r"(?:e?s)?\b", texto_norm) is not None


def id_doc(destino):
    """«28 §7.2» -> «doc-28-s07»; «27» -> «doc-27»; otra cosa -> None."""
    m = REF_DOC.match(str(destino).strip())
    if not m:
        return None
    return "doc-%s-s%02d" % (m.group(1), int(m.group(2))) if m.group(2) else "doc-%s" % m.group(1)


def existente(registro, id_):
    """El marcador de enlace a `id_` si la nota existe, o None (para listas opcionales)."""
    return ref(id_) if registro.existe(id_) else None


def ref_doc(registro, destino):
    i = id_doc(destino)
    return existente(registro, i) if i else None


def sin_repetidos(items):
    vistos, out = set(), []
    for x in items:
        if x and x not in vistos:
            vistos.add(x)
            out.append(x)
    return out


def etiqueta_acto(acto):
    return "acto/%s" % acto if acto else None


# --- volcado de estructuras JSON -----------------------------------------------------------------------------------
def _escalar(v):
    return v is None or isinstance(v, (str, int, float, bool))


def valor(v, entidades=None):
    """Texto de un valor JSON; las cadenas que son IDs conocidos (`entidades`: ID crudo -> ID de nota) pasan a enlace."""
    if v is None:
        return "–"
    if isinstance(v, bool):
        return "sí" if v else "no"
    if isinstance(v, float) and v.is_integer() and abs(v) < 1e15:
        return str(int(v))
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, str):
        if entidades and v in entidades:
            return ref(entidades[v])
        return re.sub(r"\s*\n\s*", " ", v).replace("|", "/")
    if isinstance(v, (list, tuple)):
        return ", ".join(valor(x, entidades) for x in v)
    if isinstance(v, dict):
        return "; ".join("%s: %s" % (k, valor(x, entidades)) for k, x in v.items())
    return str(v)


def lineas(datos, entidades=None, nivel=0):
    """Una estructura JSON como lista de viñetas anidadas (`clave: valor`)."""
    sangria = "  " * nivel
    out = []
    for k, v in datos.items():
        if _escalar(v) or (isinstance(v, list) and all(_escalar(x) or isinstance(x, list) for x in v)):
            out.append("%s- **%s:** %s" % (sangria, k, valor(v, entidades)))
        elif isinstance(v, dict):
            out.append("%s- **%s:**" % (sangria, k))
            out += lineas(v, entidades, nivel + 1)
        else:  # lista de diccionarios u otras mezclas
            out.append("%s- **%s:**" % (sangria, k))
            out += ["%s  - %s" % (sangria, valor(x, entidades)) for x in v]
    return out


def celda(c):
    t = str(c).replace("\n", " ")
    return t if "⟦" in t else t.replace("|", "/")


def tabla(cabecera, filas):
    """Tabla Markdown (las barras de los enlaces se escapan solas al resolverlos; las del texto plano se sustituyen)."""
    out = ["| " + " | ".join(cabecera) + " |", "|" + "---|" * len(cabecera)]
    out += ["| " + " | ".join(celda(c) for c in f) + " |" for f in filas]
    return out
