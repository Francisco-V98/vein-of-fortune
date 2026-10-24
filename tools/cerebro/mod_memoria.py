"""Memoria del proyecto (la carpeta `memory/` de Claude Code para este repo, fuera del repositorio).

Si la carpeta no existe (CI, otra máquina), el módulo se omite sin avisos. Una nota por archivo de memoria, con su descripción,
y enlaces a los documentos, ADR y tareas que menciona. Ruta: opción `memoria` del registro, variable de entorno
`CEREBRO_MEMORIA` o `~/.claude/projects/<ruta del repo con guiones>/memory/`.
"""
import os
import pathlib
import re

from . import texto as T
from .nucleo import ref

NOMBRE = "memoria"
DOC_RE = re.compile(r"(?i)\b(?:docs?|documentos?|documents?)[ /.]*(?:studio/docs/)?(\d{2})\b")
ADR_RE = re.compile(r"\bADR-?(\d{4})\b")
WIKI_RE = re.compile(r"\[\[([^\]|#]+)\]\]")


def ruta_memoria(registro, repo):
    explicita = registro.opciones.get("memoria") or os.environ.get("CEREBRO_MEMORIA")
    if explicita:
        return pathlib.Path(explicita)
    clave = re.sub(r"[^A-Za-z0-9]", "-", str(repo))
    return pathlib.Path.home() / ".claude" / "projects" / clave / "memory"


def leer(ruta):
    """(campos del encabezado, cuerpo). El encabezado se lee sin dependencias: solo claves de primer nivel."""
    texto = ruta.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", texto, re.S)
    if not m:
        return {}, texto
    campos = {}
    for linea in m.group(1).split("\n"):
        k, sep, v = linea.partition(":")
        if sep and k.strip() and not linea.startswith((" ", "\t")):
            campos[k.strip()] = v.strip().strip('"')
    tipo = re.search(r"^\s+type:\s*(\S+)", m.group(1), re.M)
    if tipo:
        campos["memoria_tipo"] = tipo.group(1)
    return campos, m.group(2)


def titulo_de(slug):
    t = slug.replace("-", " ").replace("_", " ").strip()
    return t[:1].upper() + t[1:]


def generar(registro, repo):
    carpeta = ruta_memoria(registro, repo)
    archivos = sorted(p for p in carpeta.glob("*.md") if p.name != "MEMORY.md") if carpeta.is_dir() else []
    if not archivos:
        registro.info.append("memoria: no hay carpeta de memoria, se omite")
        return
    moc = registro.moc("moc-memoria", "Memoria", "Lo que el proyecto recuerda entre sesiones: decisiones del autor, estilo y herramientas.", orden=40)
    ids = {p.stem: "mem-" + T.slug(p.stem, 60) for p in archivos}
    for p in archivos:
        campos, cuerpo = leer(p)
        mid = ids[p.stem]
        texto = cuerpo.strip("\n")
        texto = WIKI_RE.sub(lambda m: ref(ids[m.group(1).strip()]) if m.group(1).strip() in ids else m.group(1), texto)
        texto, citas = T.convertir(texto, "memoria/%s" % p.name)
        docs = []
        for n in DOC_RE.findall(cuerpo):
            if registro.existe("doc-" + n) and "doc-" + n not in docs:
                docs.append("doc-" + n)
        for n in ADR_RE.findall(cuerpo):
            if registro.existe("adr-" + n) and "adr-" + n not in docs:
                docs.append("adr-" + n)
        props = {"nombre": campos.get("name", p.stem)}
        if campos.get("memoria_tipo"):
            props["memoria_tipo"] = campos["memoria_tipo"]
        nota = registro.nueva(mid, "memoria", titulo_de(campos.get("name", p.stem)), "memoria", props=props, arriba="moc-memoria",
                              resumen=campos.get("description", "").replace("\\\"", "\"")[:200], cuerpo=texto)
        nota.relacion("Documentos", [ref(d) for d in docs])
        nota.relacion("Tareas", [ref(t) for t in citas.tareas if registro.existe(t)])
    registro.info.append("memoria: %d notas" % len(archivos))
    moc.props["notas"] = len(archivos)
