"""Lectura de las fuentes de la narrativa (parte de F0-90): tablas Markdown de los documentos y referencias de `hilos.json`.

Sirve a `mod_narrativa`: saca de los documentos 23, 25, 26 y 27 las filas que los datos JSON no tienen (escenas del Acto I,
piezas del epílogo, títulos de las cintas, botones de las decisiones) y analiza el texto libre `ref` de cada siembra y
resolución de un hilo para convertirlo en enlaces (secciones de documentos, nodos, banderas, cuellos, cintas, escenas,
tareas, piezas del epílogo y edificaciones).
"""
import re

SEPARADOR = re.compile(r"^\|[\s:|-]+\|\s*$")
CODIGO = re.compile(r"`([^`\n]+)`")
TAREA = re.compile(r"\bF\d-\d{2,3}\b")
ESCENA = re.compile(r"\bd(\d)\.(\d)\b")
PIEZA = re.compile(r"\b(H|RE|ES|CA|QU|LU|TE|DU|UN|FC|MU|ME|FM)-(\d\d)\b")
RANGO_PIEZAS = re.compile(r"\b(H|RE|ES|CA|QU|LU|TE|DU|UN|FC|MU|ME|FM)-(\d\d)\s+a\s+(?:\1-)?(\d\d)\b")
ID_NARRATIVO = re.compile(r"\b[nfmc]-[a-z0-9]+(?:-[a-z0-9]+)*\b")
EDIFICACION = re.compile(r"\bed-[a-z0-9]+(?:-[a-z0-9]+)*\b")
CINTAS = re.compile(r"\bcintas?\s+(\d(?:\s*(?:,|y|e)\s*\d)*)", re.I)
SEGMENTO_DOC = re.compile(r"^\s*doc\s+(\d{2})\b(.*)$", re.I)


def celdas(linea):
    """Celdas de una fila de tabla Markdown, sin los bordes."""
    return [c.strip() for c in linea.strip().strip("|").split("|")]


def tablas(lineas, desde=0, hasta=None):
    """Genera (número de línea 1-based, cabecera, celdas) de cada fila de datos de las tablas de `lineas[desde:hasta]`."""
    hasta = len(lineas) if hasta is None else hasta
    cabecera = None
    for i in range(desde, hasta):
        s = lineas[i].strip()
        if not s.startswith("|"):
            cabecera = None
            continue
        if SEPARADOR.match(s):
            continue
        if i + 1 < len(lineas) and SEPARADOR.match(lineas[i + 1].strip()):
            cabecera = celdas(s)
            continue
        if cabecera is not None:
            yield i + 1, cabecera, celdas(s)


def sin_codigo(celda):
    """Quita las comillas invertidas de una celda («`d1.1`» -> «d1.1»)."""
    return celda.replace("`", "").strip()


def codigos(celda):
    """Textos entre comillas invertidas de una celda."""
    return [c.strip() for c in CODIGO.findall(celda)]


def seccion_de(lineas, patron_inicio):
    """Rango (desde, hasta) de índices de la sección «##» cuyo encabezado empieza por `patron_inicio`."""
    desde = next((i for i, l in enumerate(lineas) if l.startswith("## ") and re.match(patron_inicio, l[3:])), None)
    if desde is None:
        return 0, 0
    hasta = next((i for i in range(desde + 1, len(lineas)) if lineas[i].startswith("## ")), len(lineas))
    return desde, hasta


def escenas_acto1(texto):
    """{escena: campos} y orden de las 28 escenas de la sección 21 del documento 27 (tablas 21.2 a 21.5)."""
    lineas = texto.split("\n")
    desde, hasta = seccion_de(lineas, r"21\s*·")
    datos, orden = {}, []
    for n, cab, c in tablas(lineas, desde, hasta):
        m = re.fullmatch(r"`(d\d\.\d)`", c[0])
        if not m or len(c) != len(cab):
            continue
        clave = m.group(1)
        d = datos.setdefault(clave, {"linea": n})
        if clave not in orden:
            orden.append(clave)
        if cab[1] == "Título":
            d.update(titulo=c[1], bloque=c[2], peso=c[3], lugar=c[4], personajes=c[5], cajas=c[6], ayudas=c[7], cartas=c[8], total=c[9], linea=n)
        elif cab[1].startswith("Disparador"):
            d.update(disparador=c[1], cola=c[2], mecanica=c[3], decision=c[4])
        elif cab[1].startswith("Hilos"):
            d.update(hilos=c[1], sombra=c[2], props=c[3], ramas=c[4], responsable=c[5])
        elif cab[1].startswith("Cajas"):
            d.update(reparto=c[1], reparto_ayudas=c[2], reparto_cartas=c[3])
    return datos, orden


def botones_acto1(texto):
    """{(nodo, opción): texto del botón} de la tabla 21.8 del documento 27."""
    out = {}
    for _, cab, c in tablas(texto.split("\n")):
        if cab[0] == "Botón" and len(c) >= 3:
            m = re.fullmatch(r"`(n-[a-z0-9-]+)\.b\d`", c[0])
            if m:
                out[(m.group(1), sin_codigo(c[1]))] = c[2].strip("«» ")
    return out


def piezas_epilogo(texto):
    """Lista de piezas del documento 25 (cabeceras de la sección 4 y piezas de la 5), en orden de aparición."""
    piezas = []
    for n, cab, c in tablas(texto.split("\n")):
        if len(c) == 5 and cab[0] == "ID" and re.fullmatch(r"(?:H|RE|ES|CA|QU|LU|TE|DU|UN|FC|MU|ME|FM)-\d\d", c[0]):
            piezas.append({"codigo": c[0], "cuando": c[1], "lee": c[2], "medio": c[3], "ejemplo": c[4], "linea": n})
    return piezas


def codigos_de_piezas(texto):
    """Códigos de pieza del epílogo que aparecen en un texto."""
    return [m.group(1) + "-" + m.group(2) for m in PIEZA.finditer(texto)]


def caminos_prueba(texto):
    """[(número, salida, estado, piezas)] de la tabla «Ocho caminos de prueba» (documento 25, 6.4)."""
    out = []
    for _, cab, c in tablas(texto.split("\n")):
        if cab[0] == "Camino" and len(c) == len(cab) and c[0].isdigit():
            out.append((int(c[0]), c[1], c[2], codigos_de_piezas(c[-1])))
    return out


def titulos_cintas(texto):
    """{número: título} de la tabla «Las ocho cintas» del documento 23."""
    out = {}
    for _, cab, c in tablas(texto.split("\n")):
        if cab[0] == "#" and len(c) >= 2 and c[0].isdigit():
            out[int(c[0])] = c[1]
    return out


def edificaciones_de_cintas(texto):
    """{número de cinta: [id de edificación]} según la tabla de edificaciones del documento 26."""
    out = {}
    for _, cab, c in tablas(texto.split("\n")):
        m = re.fullmatch(r"`(ed-[a-z0-9-]+)`", c[0]) if c else None
        if not m:
            continue
        for texto_celda in c[1:]:
            for grupo in CINTAS.findall(texto_celda):
                for n in re.findall(r"\d", grupo):
                    lista = out.setdefault(int(n), [])
                    if m.group(1) not in lista:
                        lista.append(m.group(1))
    return out


def numeros_de_cintas(texto):
    """Números de cinta que menciona un texto («cinta 1», «cintas 6 y 7», «cintas 1, 2 y 3»)."""
    vistos = []
    for grupo in CINTAS.findall(texto):
        for n in re.findall(r"\d", grupo):
            if int(n) not in vistos:
                vistos.append(int(n))
    return vistos


def expandir_piezas(texto):
    """Códigos de pieza de un texto, con los rangos («LU-01 a LU-04») desplegados."""
    out = []

    def poner(c):
        if c not in out:
            out.append(c)

    for m in RANGO_PIEZAS.finditer(texto):
        for k in range(int(m.group(2)), int(m.group(3)) + 1):
            poner("%s-%02d" % (m.group(1), k))
    for c in codigos_de_piezas(texto):
        poner(c)
    return out


def _sin_marcas(t):
    return re.sub(r"[✅\U0001f7e1❓⏳️*`]", "", t).casefold()


def _seccion_por_titulo(registro, doc, claves):
    """Primera sección del documento cuyo título contiene alguna de las `claves`."""
    claves = [k.casefold() for k in claves if k]
    for s in registro.hijos(doc):
        if s.tipo == "seccion":
            titulo = _sin_marcas(s.titulo)
            if any(k in titulo for k in claves):
                return s.id
    return None


def documentos_de(texto, registro):
    """IDs de documento y de sección que cita un texto de `ref` («doc 21 §5 y §11», «doc 18 Anexo», «doc 19 ficha de Reme»)."""
    ids = []

    def poner(i):
        if i and registro.existe(i) and i not in ids:
            ids.append(i)

    for segmento in texto.split("·"):
        m = SEGMENTO_DOC.match(segmento)
        if not m:
            continue
        doc, resto = "doc-" + m.group(1), m.group(2)
        secciones = [int(n) for n in re.findall(r"§\s*(\d+)", resto)]
        if not secciones:
            sin_parentesis = re.sub(r"\([^)]*\)", "", resto)
            secciones = [int(n) for n in re.findall(r"(?<![\w.])(\d+)\.\d+\b", sin_parentesis)]
        encontradas = [n for n in secciones if registro.existe("%s-s%02d" % (doc, n))]
        for n in encontradas:
            poner("%s-s%02d" % (doc, n))
        claves = re.findall(r"«([^»]+)»", resto)
        if re.search(r"\bAnexo\b", resto):
            claves.append("Anexo")
        claves += [a or b for a, b in re.findall(r"ficha de (\w+)|\b(Protagonista|Anselmo)\b", resto)]
        titulada = [x for x in (_seccion_por_titulo(registro, doc, [k]) for k in claves) if x]
        for x in titulada:
            poner(x)
        if not encontradas and not titulada:
            poner(doc)
    return ids


def refs_vacias():
    return {"docs": [], "nodos": [], "banderas": [], "cuellos": [], "cintas": [], "escenas": [], "tareas": [], "piezas": [],
            "edificaciones": [], "desconocidos": []}


def extraer_refs(texto, registro):
    """Enlaces que contiene un texto libre de `ref` (hilos.json). Devuelve un dict de listas de IDs, solo con las que existen
    (las edificaciones, que crea otra parte, se devuelven siempre) y la lista de IDs con aspecto narrativo que no se conocen."""
    out = refs_vacias()

    def poner(clave, valor):
        if valor not in out[clave]:
            out[clave].append(valor)

    out["docs"] = documentos_de(texto, registro)
    for t in ID_NARRATIVO.findall(EDIFICACION.sub(" ", texto)):
        nota = registro.nota(t)
        if nota is None:
            poner("desconocidos", t)
        elif t.startswith("n-"):
            poner("nodos", nota.id)
        elif t.startswith("c-"):
            poner("cuellos", nota.id)
        else:
            poner("banderas", nota.id)
    for n in numeros_de_cintas(texto):
        if registro.existe("cinta-%d" % n):
            poner("cintas", "cinta-%d" % n)
    for a, b in ESCENA.findall(texto):
        if registro.existe("esc-d%s.%s" % (a, b)):
            poner("escenas", "esc-d%s.%s" % (a, b))
    for t in TAREA.findall(texto):
        if registro.existe(t):
            poner("tareas", t)
    for c in expandir_piezas(texto):
        if registro.existe("ep-" + c):
            poner("piezas", "ep-" + c)
    for e in EDIFICACION.findall(texto):
        poner("edificaciones", e)
    return out
