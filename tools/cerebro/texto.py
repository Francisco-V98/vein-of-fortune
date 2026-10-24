"""Conversión de texto Markdown del repo a texto de Obsidian con marcadores de enlace.

`convertir` cambia, fuera de los bloques de código:
  - `[texto](otro.md)` por un enlace a la nota que representa ese archivo (obligatorio: avisa si no existe);
  - un ID entre comillas invertidas (`ed-vb-tienda`, `d1.2`, `F0-90`) por un enlace, solo si algún módulo lo registra;
  - un ID de tarea suelto (F0-90) por un enlace, solo si la tarea existe.
Lo que no resuelve queda como estaba. Los enlaces externos y las imágenes no se tocan.
"""
import re

from .nucleo import ref_ruta, ref_suave, ruta_relativa

TAREA = re.compile(r"\bF\d-\d{2,3}\b")
ID_EN_CODIGO = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
FILA_BLOQUE = re.compile(r"^\s*(```|~~~)")
TOKEN = re.compile(
    r"""(?P<codigo>`[^`\n]+`)
      | (?P<imagen>!\[[^\]\n]*\]\([^)\s]+\))
      | (?P<enlace>\[(?P<txt>[^\]\n]*)\]\((?P<dest>[^)\s]+)(?:\s+"[^"]*")?\))
      | (?P<tarea>\bF\d-\d{2,3}\b)""",
    re.X,
)


class Citas:
    """Lo que el texto convertido menciona: rutas de archivos, tareas e IDs entre comillas invertidas."""

    def __init__(self):
        self.rutas = []
        self.tareas = []
        self.codigos = []

    def _anadir(self, lista, valor):
        if valor not in lista:
            lista.append(valor)


def convertir(texto, origen):
    """Convierte `texto` (Markdown del archivo `origen`, ruta relativa al repo) y devuelve (texto, Citas)."""
    citas = Citas()
    fuera, resultado = True, []
    for linea in texto.split("\n"):
        if FILA_BLOQUE.match(linea):
            fuera = not fuera
            resultado.append(linea)
        elif not fuera:
            resultado.append(linea)
        else:
            resultado.append(TOKEN.sub(lambda m: _un_token(m, origen, citas), linea))
    return "\n".join(resultado), citas


def _un_token(m, origen, citas):
    if m.group("imagen"):
        return m.group(0)
    if m.group("codigo"):
        interior = m.group("codigo")[1:-1].strip()
        if ID_EN_CODIGO.match(interior):
            citas._anadir(citas.tareas if TAREA.fullmatch(interior) else citas.codigos, interior)
            return ref_suave(interior, interior, m.group(0))
        return m.group(0)
    if m.group("enlace"):
        destino = m.group("dest")
        base = destino.split("#")[0]
        if not base.endswith(".md") or re.match(r"^[a-z][a-z0-9+.-]*:", base):
            return m.group(0)
        ruta = ruta_relativa(origen, base)
        citas._anadir(citas.rutas, ruta)
        return ref_ruta(ruta, m.group("txt") or base)
    tid = m.group("tarea")
    citas._anadir(citas.tareas, tid)
    return ref_suave(tid, tid, tid)


def primera_frase(texto, maximo=140):
    """Resumen de una línea: la primera línea de prosa, sin marcas Markdown."""
    en_bloque = False
    for linea in texto.split("\n"):
        if FILA_BLOQUE.match(linea):
            en_bloque = not en_bloque
            continue
        t = linea.strip()
        if en_bloque or not t or t[0] in "#|>-*" and not t.startswith("**") or set(t) <= set("-|: "):
            continue
        t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
        t = re.sub(r"[*_`]", "", t)
        t = re.sub(r"[✅\U0001f7e1❓⏳️]", "", t)
        t = re.sub(r"\s+", " ", t).strip()
        resto = re.sub(r"^Estado:\s*(?:cerrada|cerrado|pendiente)\.\s*", "", t)
        t = resto if len(resto) >= 20 else t
        if len(t) < 3:
            continue
        if len(t) > maximo:
            corte = t.rfind(" ", 0, maximo)
            t = t[: corte if corte > maximo // 2 else maximo].rstrip(" ,;:.") + "…"
        return t
    return ""


def slug(texto, maximo=40):
    """Identificador ASCII en minúsculas con guiones."""
    import unicodedata
    t = unicodedata.normalize("NFKD", str(texto)).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t[:maximo].strip("-") or "x"
