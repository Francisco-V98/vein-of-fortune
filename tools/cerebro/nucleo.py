"""Núcleo del cerebro del proyecto: registro de notas, resolución de enlaces y escritura del vault de Obsidian.

Los módulos (mod_*.py) no escriben archivos ni conocen nombres de archivo: registran notas con IDs estables
(`Registro.nueva`) y se enlazan entre sí con marcadores (`ref`, `ref_suave`). Al final, `construir` resuelve los
marcadores contra la tabla de IDs, avisa de los que no resuelven y devuelve el texto de cada archivo; `escribir`
lo deja en disco sin tocar nunca `mis-notas/` ni `.obsidian/`.

Solo biblioteca estándar.
"""
import json
import pathlib
import posixpath
import re
import shutil

DIR_GENERADO = "generado"
DIR_MOC = "MOC"
DIRS_PROPIOS = (DIR_GENERADO, DIR_MOC)  # el script borra y reescribe estas carpetas enteras
DIRS_DEL_AUTOR = ("mis-notas",)  # el script no las toca nunca
ID_INICIO = "inicio"
NOMBRE_INICIO = "00 Inicio"

PROHIBIDOS = set('#^[]|:/\\?*"<>')
MARCAS = re.compile("[✅\U0001f7e1❓⏳️]")
ID_VALIDO = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")

# Marcadores de enlace, resueltos al final:
#   ⟦id|texto⟧            enlace obligatorio: si no resuelve, avisa y deja «texto»
#   ⟦~id|texto|respaldo⟧  enlace opcional: si no resuelve, deja «respaldo» sin avisar
#   ⟦@ruta|texto⟧         enlace a un archivo del repo (se busca en `Registro.rutas`)
MARCADOR = re.compile(r"⟦(?P<suave>~)?(?P<id>[^|⟦⟧]+)(?:\|(?P<a>[^|⟦⟧]*))?(?:\|(?P<b>[^⟦⟧]*))?⟧")


def _plano(texto):
    return re.sub(r"[⟦⟧|\[\]\r\n]+", " ", str(texto)).strip()


def ref(id_, texto=None):
    """Marcador de enlace obligatorio a la nota `id_` (con texto visible opcional)."""
    return "⟦%s|%s⟧" % (id_, _plano(texto)) if texto else "⟦%s⟧" % id_


def ref_suave(id_, visible, respaldo):
    """Enlace opcional: si `id_` no existe, queda `respaldo` tal cual y no hay aviso."""
    return "⟦~%s|%s|%s⟧" % (id_, _plano(visible), str(respaldo).replace("⟦", "").replace("⟧", ""))


def ref_ruta(ruta, texto=None):
    """Enlace a un archivo del repo (p. ej. `studio/docs/27-guion.md`), resuelto con `Registro.asociar_ruta`."""
    return "⟦@%s|%s⟧" % (ruta, _plano(texto or ""))


def nombre_seguro(texto, maximo=80):
    """Nombre de archivo legible: sin marcas de limpieza ni caracteres que Obsidian no admite en enlaces."""
    t = MARCAS.sub("", str(texto)).replace("·", " ")
    t = re.sub(r"\s*[:/]\s*", " - ", t)
    t = "".join(c for c in t if c not in PROHIBIDOS and ord(c) >= 32)
    t = re.sub(r"\s+", " ", t).strip(" .-")
    if len(t) > maximo:
        corte = t.rfind(" ", 0, maximo)
        t = t[: corte if corte > maximo // 2 else maximo].rstrip(" .,;-")
    return t


def yaml_valor(v):
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, (list, tuple)):
        return "[" + ", ".join(yaml_valor(x) for x in v) + "]"
    return json.dumps(str(v), ensure_ascii=False)


class Nota:
    """Una nota del vault. `cuerpo` y `relaciones` pueden llevar marcadores de enlace."""

    def __init__(self, id, tipo, titulo, ruta_carpeta, nombre, props, resumen, cuerpo, arriba, alias, tags, fuente, orden):
        self.id = id
        self.tipo = tipo
        self.titulo = titulo
        self.carpeta = ruta_carpeta
        self.nombre = nombre
        self.props = props
        self.resumen = resumen
        self.cuerpo = cuerpo
        self.arriba = arriba
        self.alias = list(alias)
        self.tags = list(tags)
        self.fuente = fuente
        self.orden = orden
        self.relaciones = []  # [(etiqueta, [marcadores])]
        self.auto_hijos = tipo == "moc"  # los MOC listan solos las notas cuyo `arriba` son ellos
        self.extra = ""  # texto que añade `construir` tras el cuerpo (lista de contenido de los MOC)
        self.enlaces = []  # IDs a los que apunta (se rellena al construir)

    @property
    def archivo(self):
        return "%s/%s.md" % (self.carpeta, self.nombre) if self.carpeta else self.nombre + ".md"

    def relacion(self, etiqueta, items):
        """Añade una línea «Etiqueta: enlaces» a la sección Relaciones (ignora listas vacías)."""
        items = [i for i in items if i]
        if items:
            self.relaciones.append((etiqueta, items))

    def previo(self):
        """Texto de la nota con los marcadores todavía sin resolver."""
        fm = [("id", self.id), ("tipo", self.tipo), ("title", self.titulo), ("aliases", [self.id] + self.alias)]
        fm += list(self.props.items())
        if self.arriba:
            fm.append(("arriba", ref(self.arriba)))
        if self.tags:
            fm.append(("tags", self.tags))
        if self.fuente:
            fm.append(("fuente", self.fuente))
        fm.append(("generado", True))
        out = ["---"] + ["%s: %s" % (k, yaml_valor(v)) for k, v in fm] + ["---", "", "# " + self.titulo, ""]
        if self.resumen:
            out += ["> " + self.resumen, ""]
        for texto in (self.cuerpo, self.extra):
            if texto.strip():
                out += [texto.strip("\n"), ""]
        if self.relaciones:
            out += ["## Relaciones", ""]
            for etiqueta, items in self.relaciones:
                if len(items) <= 6:
                    out.append("- **%s:** %s" % (etiqueta, ", ".join(items)))
                else:
                    out.append("- **%s:**" % etiqueta)
                    out += ["  - " + i for i in items]
            out.append("")
        if self.fuente:
            out += ["## Fuente", "", "`%s`" % self.fuente, ""]
        return "\n".join(out)


class Registro:
    """Tabla de notas del vault. Las IDs son estables; los nombres de archivo se derivan y no se repiten."""

    def __init__(self, opciones=None):
        self.notas = {}
        self.orden_alta = []
        self.nombres = {NOMBRE_INICIO.casefold(): ID_INICIO}  # nombre en minúsculas -> id (el de Inicio está reservado)
        self.alias_ids = {}  # alias -> id (también resuelven enlaces)
        self.rutas = {}  # ruta del repo -> id
        self.avisos = []
        self.info = []
        self.opciones = dict(opciones or {})

    # --- alta de notas -------------------------------------------------------------------------------------------
    def nueva(self, id, tipo, titulo, carpeta, *, nombre=None, sufijo=None, props=None, resumen="", cuerpo="", arriba=None,
              alias=(), tags=(), fuente=None, orden=None):
        """Registra una nota. `carpeta` es relativa a `generado/` (los MOC van a `MOC/`). El nombre de archivo sale de
        `nombre` (o `titulo`), se limpia, y si ya existe se desambigua con `sufijo` (o el tipo) y, si hace falta, un número."""
        if not ID_VALIDO.match(str(id)):
            raise ValueError("ID de nota inválido: %r" % (id,))
        if id in self.notas or id in self.alias_ids:
            raise ValueError("ID de nota repetido: %s" % id)
        base = nombre_seguro(nombre or titulo) or str(id)
        final = self._nombre_unico(base, sufijo or tipo)
        ruta = self._carpeta(tipo, carpeta)
        reservados = {"id", "tipo", "title", "aliases", "arriba", "tags", "fuente", "generado"}
        props = dict(props or {})
        if reservados & set(props):
            raise ValueError("%s: propiedades reservadas: %s" % (id, sorted(reservados & set(props))))
        nota = Nota(id, tipo, titulo, ruta, final, props, resumen, cuerpo, arriba, alias, tags, fuente, orden)
        self.notas[id] = nota
        self.orden_alta.append(id)
        self.nombres[final.casefold()] = id
        for a in nota.alias:
            if a in self.notas or a in self.alias_ids:
                self.avisos.append("%s: el alias %s ya es una ID o un alias de otra nota" % (id, a))
            else:
                self.alias_ids[a] = id
        return nota

    def moc(self, id, titulo, resumen, intro="", orden=50, auto_hijos=True):
        """Mapa de contenido (carpeta `MOC/`): lista solo las notas cuyo `arriba` es su ID."""
        nota = self.nueva(id, "moc", titulo, "", nombre="MOC " + titulo, resumen=resumen, cuerpo=intro, arriba=ID_INICIO, orden=orden)
        nota.auto_hijos = auto_hijos
        return nota

    def asociar_ruta(self, ruta, id):
        """Dice qué nota representa un archivo del repo, para convertir enlaces `[x](archivo.md)`."""
        self.rutas[ruta] = id

    def _carpeta(self, tipo, carpeta):
        if tipo == "moc":
            return DIR_MOC
        partes = [p for p in str(carpeta).replace("\\", "/").split("/") if p]
        if any(p in ("..", ".") or p.startswith(".") for p in partes) or (partes and partes[0] in DIRS_DEL_AUTOR):
            raise ValueError("carpeta no permitida: %r" % (carpeta,))
        return "/".join([DIR_GENERADO] + partes)

    def _nombre_unico(self, base, sufijo):
        if base.casefold() not in self.nombres:
            return base
        con_sufijo = "%s (%s)" % (base, nombre_seguro(sufijo, 30)) if sufijo else base
        candidato, n = con_sufijo, 2
        while candidato.casefold() in self.nombres:
            candidato = "%s %d" % (con_sufijo, n)
            n += 1
        return candidato

    # --- consultas -----------------------------------------------------------------------------------------------
    def existe(self, id):
        return id in self.notas or id in self.alias_ids

    def nota(self, id):
        return self.notas.get(self.alias_ids.get(id, id))

    def hijos(self, id):
        return [self.notas[i] for i in self.orden_alta if self.notas[i].arriba == id]

    def por_tipo(self, tipo):
        return [self.notas[i] for i in self.orden_alta if self.notas[i].tipo == tipo]

    def conteo(self):
        cuenta = {}
        for n in self.notas.values():
            cuenta[n.tipo] = cuenta.get(n.tipo, 0) + 1
        return cuenta

    def aviso(self, msg):
        self.avisos.append(msg)

    def resolver_id(self, id):
        if id.startswith("@"):
            return self.rutas.get(id[1:].split("#")[0])
        return self.alias_ids.get(id, id) if self.existe(id) else None

    def indice_referencias(self):
        """Índice de quién enlaza a quién, mirando los marcadores (antes de resolver). Se construye con las notas que
        existen en ese momento, pero se puede consultar por el ID de una nota que aún no existía: `indice.a(id)`."""
        crudo = {}
        for origen in self.orden_alta:
            for m in MARCADOR.finditer(self.notas[origen].previo()):
                lista = crudo.setdefault(m.group("id"), [])
                if origen not in lista:
                    lista.append(origen)
        return Indice(self, crudo)

    # --- resolución ----------------------------------------------------------------------------------------------
    def _resolver(self, texto, origen, sin_resolver):
        salientes = []

        def un_enlace(m, en_tabla):
            destino = self.resolver_id(m.group("id"))
            a, b = m.group("a"), m.group("b")
            if destino is None:
                if m.group("suave"):
                    return b if b is not None else (a or m.group("id"))
                sin_resolver.setdefault((origen.id, m.group("id")), None)
                return a or m.group("id").lstrip("@")
            if destino not in salientes:
                salientes.append(destino)
            nombre = self.notas[destino].nombre
            visible = a if a else None
            if visible and visible != nombre:
                return "[[%s%s%s]]" % (nombre, "\\|" if en_tabla else "|", visible)
            return "[[%s]]" % nombre

        lineas = []
        for linea in texto.split("\n"):
            en_tabla = linea.lstrip().startswith("|")
            lineas.append(MARCADOR.sub(lambda m: un_enlace(m, en_tabla), linea))
        return "\n".join(lineas), salientes

    def construir(self):
        """Completa MOC e Inicio, resuelve los enlaces y devuelve {ruta relativa: texto}. Rellena `avisos`."""
        self._inicio()
        for nota in list(self.notas.values()):
            if nota.auto_hijos:
                self._listar_hijos(nota)
        archivos, sin_resolver = {}, {}
        for id in self.orden_alta:
            nota = self.notas[id]
            texto, nota.enlaces = self._resolver(nota.previo(), nota, sin_resolver)
            if nota.archivo in archivos:
                raise ValueError("dos notas con el mismo archivo: %s" % nota.archivo)
            archivos[nota.archivo] = texto + ("" if texto.endswith("\n") else "\n")
        for (origen, destino) in sin_resolver:
            self.avisos.append("enlace sin resolver en %s: %s" % (self.notas[origen].nombre, destino))
        entrantes = set()
        for nota in self.notas.values():
            entrantes.update(d for d in nota.enlaces if d != nota.id)
        for id in self.orden_alta:
            nota = self.notas[id]
            if id not in entrantes and not [d for d in nota.enlaces if d != id]:
                self.avisos.append("nota huérfana (sin enlaces): %s" % nota.nombre)
        return archivos

    def _listar_hijos(self, nota):
        grupos = {}
        for hijo in self.hijos(nota.id):
            grupos.setdefault(hijo.tipo, []).append(hijo)
        nota.extra = ""
        if not grupos:
            return
        lineas = ["## Contenido", ""]
        for tipo, hijos in grupos.items():
            if len(grupos) > 1:
                lineas += ["### " + tipo.capitalize(), ""]
            if any(h.orden is not None for h in hijos):
                hijos = sorted(hijos, key=lambda h: h.orden if h.orden is not None else 0)
            lineas += ["- " + ref(h.id) + (" — " + h.resumen if h.resumen else "") for h in hijos] + [""]
        nota.extra = "\n".join(lineas)

    def _inicio(self):
        if ID_INICIO in self.notas:
            return
        self.nombres.pop(NOMBRE_INICIO.casefold(), None)
        mapas = sorted(self.por_tipo("moc"), key=lambda n: (n.orden if n.orden is not None else 50))
        cuenta = {t: c for t, c in self.conteo().items() if t != "moc"}
        cuerpo = [
            "Este vault se **genera** desde el repositorio (`python3 studio/hub/build.py`). Los documentos y los datos del repo "
            "son la fuente de verdad: aquí solo se leen y se navegan. Todo lo que cuelga de `generado/` y `MOC/` se borra y se "
            "reescribe en cada pasada; tus notas van en `mis-notas/`, que nunca se toca.",
            "",
            "## Mapas",
            "",
        ]
        cuerpo += ["- %s — %s" % (ref(m.id), m.resumen) for m in mapas]
        cuerpo += ["", "## Cifras", "", "| Tipo | Notas |", "|---|---|"]
        cuerpo += ["| %s | %d |" % (t, c) for t, c in sorted(cuenta.items())]
        cuerpo += ["", "## Cómo moverse", "",
                   "- Abre el **Graph View**: cada nota es un nodo; los colores salen de `.obsidian/graph.json`.",
                   "- En el panel de marcadores hay vistas guardadas del grafo (por ejemplo, sin el backlog de F1 a F6).",
                   "- Las tareas llevan las etiquetas `#estado/…`, `#prio/…` y `#fase/…` para filtrar."]
        nota = self.nueva(ID_INICIO, "inicio", "Veta de Fortuna: cerebro del proyecto", "", nombre=NOMBRE_INICIO,
                          resumen="Punto de entrada del vault generado.", cuerpo="\n".join(cuerpo), orden=0)
        nota.carpeta = ""  # en la raíz del vault
        nota.auto_hijos = False


class Indice:
    """Resultado de `Registro.indice_referencias()`."""

    def __init__(self, registro, crudo):
        self.registro = registro
        self.crudo = crudo

    def a(self, id):
        """IDs de las notas que enlazan a `id` (por su ID o por cualquiera de sus alias), en orden de alta."""
        nota = self.registro.nota(id)
        claves = {id} | (set(nota.alias) | {nota.id} if nota else set())
        origenes = {o for c in claves for o in self.crudo.get(c, [])} - {nota.id if nota else id}
        return [o for o in self.registro.orden_alta if o in origenes]


# --- escritura del vault ----------------------------------------------------------------------------------------------

def _es_generado(ruta):
    try:
        with open(ruta, "rb") as f:
            cabecera = f.read(4000).decode("utf-8", "ignore")
    except OSError:
        return False
    return cabecera.startswith("---") and re.search(r"^generado:\s*true\s*$", cabecera.split("\n---", 1)[0], re.M) is not None


def _comprobar_ruta(rel):
    partes = pathlib.PurePosixPath(rel).parts
    if not partes or pathlib.PurePosixPath(rel).is_absolute() or ".." in partes:
        raise ValueError("ruta fuera del vault: %s" % rel)
    if partes[0] in DIRS_DEL_AUTOR or partes[0].startswith("."):
        raise ValueError("el cerebro no escribe en %s" % partes[0])
    if len(partes) == 1 and partes[0] != NOMBRE_INICIO + ".md":
        raise ValueError("solo la nota de inicio puede ir en la raíz: %s" % rel)
    if len(partes) > 1 and partes[0] not in DIRS_PROPIOS:
        raise ValueError("carpeta no generada: %s" % rel)


def escribir(vault, archivos):
    """Deja en `vault` exactamente `archivos` ({ruta relativa: texto}) dentro de `generado/`, `MOC/` y la raíz.

    Borra los archivos sobrantes de `generado/` y `MOC/` y los `.md` con `generado: true`. No toca `mis-notas/`
    ni las carpetas ocultas (`.obsidian/`). Escribe solo lo que cambia. Devuelve (escritos, sin_cambio, borrados)."""
    vault = pathlib.Path(vault)
    for rel in archivos:
        _comprobar_ruta(rel)
    vault.mkdir(parents=True, exist_ok=True)
    objetivo = {pathlib.PurePosixPath(r).as_posix() for r in archivos}
    borrados = 0
    for raiz, dirs, nombres in _recorrer(vault):
        propio = pathlib.Path(raiz).relative_to(vault).parts[:1] in [(d,) for d in DIRS_PROPIOS]
        for n in nombres:
            ruta = pathlib.Path(raiz) / n
            rel = ruta.relative_to(vault).as_posix()
            if rel in objetivo or ruta.is_symlink():
                continue
            if propio or (n.endswith(".md") and _es_generado(ruta)):
                ruta.unlink()
                borrados += 1
    for d in DIRS_PROPIOS:  # carpetas vacías de las propias
        base = vault / d
        if base.is_dir() and not base.is_symlink():
            for sub in sorted((p for p in base.rglob("*") if p.is_dir() and not p.is_symlink()), key=lambda p: -len(p.parts)):
                if not any(sub.iterdir()):
                    sub.rmdir()
    escritos = sin_cambio = 0
    for rel, texto in sorted(archivos.items()):
        ruta = vault / rel
        ruta.parent.mkdir(parents=True, exist_ok=True)
        if ruta.is_file() and ruta.read_text(encoding="utf-8") == texto:
            sin_cambio += 1
            continue
        _escribir_texto(ruta, texto)
        escritos += 1
    return escritos, sin_cambio, borrados


def _escribir_texto(ruta, texto):
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def _recorrer(vault):
    """os.walk sin entrar en carpetas ocultas, en `mis-notas/` ni en enlaces simbólicos."""
    import os
    for raiz, dirs, nombres in os.walk(vault, followlinks=False):
        rel = pathlib.Path(raiz).relative_to(vault)
        if not rel.parts:
            dirs[:] = [d for d in dirs if not d.startswith(".") and d not in DIRS_DEL_AUTOR]
        dirs[:] = sorted(d for d in dirs if not (pathlib.Path(raiz) / d).is_symlink())
        yield raiz, dirs, sorted(nombres)


README_MIS_NOTAS = """# Mis notas

Esta carpeta es **tuya**. El generador del cerebro (`python3 studio/hub/build.py`) no la lee ni la borra nunca.

- Crea aquí tus notas y enlázalas a las generadas con `[[Nombre de la nota]]` o por su ID (por ejemplo `[[F0-90]]`, `[[doc-27]]`).
- Las notas de `generado/` y `MOC/` se reescriben en cada pasada: no las edites, tus cambios se perderían.
- Si renombras algo en el repo, los enlaces por ID siguen funcionando; los que usan el nombre visible pueden romperse.
"""


def preparar_vault(vault, plantilla):
    """Crea `mis-notas/` (vacía, con su README) y copia la plantilla `.obsidian/` solo en lo que falte."""
    vault = pathlib.Path(vault)
    mis = vault / DIRS_DEL_AUTOR[0]
    mis.mkdir(parents=True, exist_ok=True)
    readme = mis / "README.md"
    if not readme.exists():
        _escribir_texto(readme, README_MIS_NOTAS)
    plantilla = pathlib.Path(plantilla) if plantilla else None
    if plantilla and plantilla.is_dir():
        for origen in sorted(plantilla.rglob("*")):
            if origen.is_file():
                destino = vault / ".obsidian" / origen.relative_to(plantilla)
                if not destino.exists():
                    destino.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(origen, destino)


def ruta_relativa(origen, destino):
    """Ruta POSIX normalizada de `destino` visto desde la carpeta del archivo `origen` (ambos relativos al repo)."""
    return posixpath.normpath(posixpath.join(posixpath.dirname(origen), destino))
