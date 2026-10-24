"""Documentos 00 a 28 y registros de decisiones de arquitectura (ADR).

Por documento: una nota índice (limpieza y puntos abiertos como propiedades, lista de secciones, documentos que enlaza y que
lo citan, puntos abiertos) y una nota por sección «##» con las «###» dentro, enlace al documento y a la sección anterior y
siguiente. Los enlaces entre documentos, los IDs de tarea y los IDs entre comillas invertidas pasan a enlaces del vault.
"""
import re

from . import texto as T
from .nucleo import ref

NOMBRE = "documentos"
MARCA_RE = {"ok": "✅", "prop": "\U0001f7e1", "open": "❓", "espera": "⏳"}
TAREA_ESPERA = re.compile(r"⏳\s*(F\d-\d{2,3})")
NUMERO_SECCION = re.compile(r"^(\d+)\s*(?:·|\.|\))\s*(.*)$")
TITULO_DOC = re.compile(r"^(?:ADR-)?(\d+)\s*·\s*(.*)$")


def contar(texto):
    """Marcas de limpieza y líneas con puntos abiertos, con el mismo criterio que build.py (sin código ni ejemplos)."""
    c = {"ok": 0, "prop": 0, "open": 0, "espera": 0}
    items, en_bloque = [], False
    for n, linea in enumerate(texto.split("\n"), start=1):
        if T.FILA_BLOQUE.match(linea):
            en_bloque = not en_bloque
            continue
        if en_bloque:
            continue
        s = re.sub(r"`[^`]*`", "", linea)
        for clave, marca in MARCA_RE.items():
            c[clave] += s.count(marca)
        if any(MARCA_RE[k] in s for k in ("prop", "open", "espera")):
            t = re.sub(r"[*_`]", "", s).strip(" |-•")
            t = re.sub(r"\s+", " ", t)
            items.append((n, t[:200], MARCA_RE["prop"] in s or MARCA_RE["open"] in s))
    return c, items


def limpieza(c):
    decididos = c["ok"] + c["prop"] + c["open"]
    return round(100 * c["ok"] / decididos) if decididos else None


def partir(texto):
    """(titulo, preámbulo, [(titulo_seccion, línea, cuerpo)]) cortando por «## » fuera de bloques de código."""
    lineas = texto.split("\n")
    titulo, en_bloque = "", False
    marcas = []
    for i, linea in enumerate(lineas):
        if T.FILA_BLOQUE.match(linea):
            en_bloque = not en_bloque
        elif not en_bloque:
            if linea.startswith("# ") and not titulo:
                titulo = linea[2:].strip()
                marcas.append(("h1", i))
            elif linea.startswith("## "):
                marcas.append(("h2", i))
    primero = next((i for k, i in marcas if k == "h2"), len(lineas))
    h1 = next((i for k, i in marcas if k == "h1"), -1)
    preambulo = "\n".join(lineas[h1 + 1: primero]).strip("\n")
    secciones = []
    cortes = [i for k, i in marcas if k == "h2"] + [len(lineas)]
    for a, b in zip(cortes, cortes[1:]):
        secciones.append((lineas[a][3:].strip(), a + 1, "\n".join(lineas[a + 1: b]).strip("\n")))
    return titulo, preambulo, secciones


def _estado(abiertos, espera, limpio):
    return "con-abiertos" if abiertos else "con-aplazados" if espera else limpio


def _nombre_doc(titulo, prefijo):
    m = TITULO_DOC.match(titulo)
    resto = m.group(2) if m else titulo
    return "%s %s" % (prefijo, resto)


def _datos_seccion(titulo, prefijo, ids_usados):
    """(id, nombre, número) de una sección según su encabezado."""
    limpio = re.sub(r"\s+", " ", re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", titulo)).strip()  # «de [19](19-x.md) a»: queda «de 19 a»
    m = NUMERO_SECCION.match(limpio)
    if m:
        numero, resto = int(m.group(1)), m.group(2)
        resto = " - ".join(p.strip() for p in resto.split("·") if p.strip())
        sid = "%s-s%02d" % (prefijo[0], numero)
        nombre = "%s §%d %s" % (prefijo[1], numero, resto)
    else:
        numero = None
        sid = "%s-%s" % (prefijo[0], T.slug(limpio))
        nombre = "%s §%s" % (prefijo[1], limpio)
    base, n = sid, 2
    while sid in ids_usados:
        sid = "%s-%d" % (base, n)
        n += 1
    ids_usados.add(sid)
    return sid, nombre, numero


def _importar(registro, repo, ruta, id_doc, prefijo_nombre, tipo, carpeta_doc, arriba, rutas_a_ids):
    rel = ruta.relative_to(repo).as_posix()
    texto = ruta.read_text(encoding="utf-8")
    titulo, preambulo, secciones = partir(texto)
    conteo, _ = contar(texto)
    rutas_a_ids[rel] = id_doc
    registro.asociar_ruta(rel, id_doc)
    usados, notas_sec, fichas = set(), [], []
    lin_titulo = next((i for i, l in enumerate(texto.split("\n"), 1) if l.startswith("# ")), 1)
    for titulo_sec, linea, cuerpo in secciones:
        sid, nombre, _ = _datos_seccion(titulo_sec, (id_doc, prefijo_nombre), usados)
        c, items = contar(cuerpo)
        conv, citas = T.convertir(cuerpo, rel)
        espera = sorted(set(TAREA_ESPERA.findall(cuerpo)))
        props = {"documento": ref(id_doc), "limpieza": limpieza(c), "abiertos": c["prop"] + c["open"], "espera": c["espera"]}
        if props["limpieza"] is None:
            del props["limpieza"]
        if espera:
            props["aplazado_a"] = [ref(t) for t in espera]
        props["estado"] = _estado(props["abiertos"], c["espera"], "limpia")
        nota = registro.nueva(
            sid, "seccion", titulo_sec, "secciones", nombre=nombre, props=props, resumen=T.primera_frase(cuerpo),
            cuerpo=conv, arriba=id_doc, fuente="%s:%d" % (rel, linea))
        notas_sec.append(nota)
        fichas.append({"nota": nota, "items": items, "citas": citas, "linea": linea, "espera": espera})
    for i, nota in enumerate(notas_sec):
        ant = notas_sec[i - 1] if i else None
        sig = notas_sec[i + 1] if i + 1 < len(notas_sec) else None
        if ant:
            nota.props["anterior"] = ref(ant.id)
        if sig:
            nota.props["siguiente"] = ref(sig.id)
        nav = ["← " + ref(ant.id) if ant else "", ref(id_doc, "↑ " + (prefijo_nombre)), (ref(sig.id) + " →") if sig else ""]
        nota.cuerpo = " · ".join(p for p in nav if p) + "\n\n" + nota.cuerpo
    conv_pre, citas_pre = T.convertir(preambulo, rel)
    props = {"limpieza": limpieza(conteo), "ok": conteo["ok"], "propuestas": conteo["prop"], "abiertos": conteo["prop"] + conteo["open"],
             "espera": conteo["espera"], "secciones": len(notas_sec)}
    if props["limpieza"] is None:
        del props["limpieza"]
    estado = _estado(props["abiertos"], conteo["espera"], "limpio")
    if tipo == "adr":
        m = re.search(r"\*\*Estado:\*\*\s*([^·\n]*)", preambulo)
        f = re.search(r"\*\*Fecha:\*\*\s*(\d{4}-\d{2}-\d{2})", preambulo)
        if m:
            estado = re.sub(r"[✅\U0001f7e1❓⏳️*]", "", m.group(1)).strip()
        if f:
            props["fecha"] = f.group(1)
    props = {"estado": estado, **props}
    resumen = "Limpieza %s %% · %d abiertos · %d secciones" % (props.get("limpieza", "n/d"), props["abiertos"], len(notas_sec))
    cuerpo = [conv_pre, "", "## Secciones", ""] if conv_pre.strip() else ["## Secciones", ""]
    cuerpo += ["%d. %s%s" % (i, ref(s.id), " — " + s.resumen if s.resumen else "") for i, s in enumerate(notas_sec, 1)]
    abiertos, aplazados = [], []
    for ficha in fichas:
        for n, t, abierto in ficha["items"]:
            if abierto:
                abiertos.append("- %s (línea %d): %s" % (ref(ficha["nota"].id), ficha["linea"] + n, t.replace("|", "/")))
        for tid in ficha["espera"]:
            if tid not in aplazados:
                aplazados.append(tid)
    if abiertos:
        cuerpo += ["", "## Puntos abiertos", ""] + abiertos
    doc = registro.nueva(
        id_doc, tipo, titulo, carpeta_doc, nombre=_nombre_doc(titulo, prefijo_nombre), props=props, resumen=resumen,
        cuerpo="\n".join(cuerpo), arriba=arriba, fuente="%s:%d" % (rel, lin_titulo))
    doc.relacion("Aplazados a", [ref(t) for t in sorted(aplazados)])
    citados = []
    for c in [citas_pre] + [f["citas"] for f in fichas]:
        for r in c.rutas:
            if r != rel and r not in citados:
                citados.append(r)
    return doc, citados


def generar(registro, repo):
    docs_dir = repo / "studio" / "docs"
    archivos = sorted(docs_dir.glob("[0-9][0-9]-*.md"))
    adrs = sorted((docs_dir / "adr").glob("[0-9][0-9][0-9][0-9]-*.md")) if (docs_dir / "adr").is_dir() else []
    moc_d = registro.moc("moc-documentos", "Documentos", "Los documentos de diseño 00 a 28 con su limpieza.", orden=10, auto_hijos=False)
    moc_a = registro.moc("moc-adr", "ADR", "Registros de decisiones de arquitectura.", orden=11)
    rutas_a_ids, creados, citas_por_doc = {}, [], {}
    for ruta in archivos:
        pref = ruta.stem[:2]
        doc, citados = _importar(registro, repo, ruta, "doc-" + pref, pref, "documento", "docs", "moc-documentos", rutas_a_ids)
        creados.append(doc)
        citas_por_doc[doc.id] = citados
    for ruta in adrs:
        num = ruta.stem[:4]
        doc, citados = _importar(registro, repo, ruta, "adr-" + num, "ADR-" + num, "adr", "adr", "moc-adr", rutas_a_ids)
        creados.append(doc)
        citas_por_doc[doc.id] = citados
    entrantes = {}
    for origen, citados in citas_por_doc.items():
        destinos = [rutas_a_ids[r] for r in citados if r in rutas_a_ids]
        for d in destinos:
            entrantes.setdefault(d, []).append(origen)
        registro.nota(origen).relacion("Enlaza a", [ref(d) for d in destinos])
    for d, origenes in entrantes.items():
        registro.nota(d).relacion("Citado por", [ref(o) for o in origenes])
    filas = ["| Documento | Limpieza | Abiertos | Esperan |", "|---|---|---|---|"]
    total = {"ok": 0, "prop": 0, "open": 0}
    for d in (x for x in creados if x.tipo == "documento"):
        p = d.props
        filas.append("| %s | %s | %d | %d |" % (ref(d.id), "%s %%" % p["limpieza"] if "limpieza" in p else "n/d", p["abiertos"], p["espera"]))
        total["ok"] += p["ok"]
        total["prop"] += p["propuestas"]
        total["open"] += p["abiertos"] - p["propuestas"]
    decididos = sum(total.values())
    pct = round(100 * total["ok"] / decididos) if decididos else 0
    moc_d.cuerpo = "Limpieza total del diseño: **%d %%** (✅ %d · 🟡 %d · ❓ %d).\n\n%s" % (pct, total["ok"], total["prop"], total["open"], "\n".join(filas))
    moc_d.props["limpieza_total"] = pct
    registro.info.append("documentos: %d documentos, %d ADR, %d secciones" % (
        sum(1 for d in creados if d.tipo == "documento"), sum(1 for d in creados if d.tipo == "adr"), len(registro.por_tipo("seccion"))))
