"""Arte: la paleta, la política de arte provisional, las hojas de personajes, la galería de PNJ, las pruebas de estilo, la
marca y el audio previsto (studio/data/assets.json, galeria.json y palette.json).

Todo el arte actual es provisional (documento 12): cada nota lo dice en `estado`. La revisión de cada pieza
(aprobada, referencia, superada) va aparte en `revision`.
"""
import posixpath
import re

from . import texto as T
from .ayudas import cargar, existente, norm, sin_repetidos, tabla
from .mod_mundo import Mundo, WORLD
from .nucleo import ref
from .texto import slug

NOMBRE = "arte"
ASSETS, GALERIA, PALETA = "studio/data/assets.json", "studio/data/galeria.json", "studio/data/palette.json"
PREFIJO_DIR = {"prueba-de-estilo": "pe1", "prueba-de-estilo-2": "pe2", "marca": "marca"}
SECCION_DE_DIR = {"prueba-de-estilo": "Pruebas de estilo, ronda 1", "prueba-de-estilo-2": "Pruebas de estilo, ronda 2 (horizontal)", "marca": "Marca"}
REEMPLAZO = re.compile(r"[Rr]eemplazada por ([\w.-]+)\.png")


def generar(registro, repo):
    assets = cargar(repo, ASSETS)
    if not assets:
        registro.info.append("arte: no hay assets.json, se omite")
        return
    galeria = cargar(repo, GALERIA) or {}
    paleta = cargar(repo, PALETA) or {}
    w = cargar(repo, WORLD) or {}
    mundo = Mundo(w) if w else None
    defecto = assets.get("estado_por_defecto", "provisional")
    imagenes = assets.get("images", [])
    por_archivo = {i["file"]: i for i in imagenes}
    doc12, doc13 = existente(registro, "doc-12"), existente(registro, "doc-13")
    moc = registro.moc("moc-arte", "Arte", "Paleta, hojas de personajes, galería de PNJ, pruebas de estilo, marca y audio: todo provisional hasta el arte definitivo.",
                       orden=82)
    id_pieza = {}  # archivo -> ID de nota, para enlazar «reemplazada por»

    # política ---------------------------------------------------------------------------------------------------------------
    cuenta = {}
    for i in imagenes:
        cuenta[i["status"]] = cuenta.get(i["status"], 0) + 1
    cuerpo = [assets.get("source_note", ""), "", "**Estado por defecto:** %s. Las %d imágenes registradas: %s." % (
        defecto, len(imagenes), ", ".join("%d %s" % (v, k) for k, v in sorted(cuenta.items())))]
    nota = registro.nueva("arte-politica", "politica-arte", "Arte provisional y definitivo", "arte", sufijo="arte", arriba="moc-arte", fuente=ASSETS,
                          props={"estado": defecto, "imagenes": len(imagenes)}, tags=["estado/provisional"],
                          resumen="Todo el arte actual es provisional; el definitivo será pixel art con PixelLab tras la Puerta B", cuerpo="\n".join(cuerpo))
    nota.relacion("Documentos", [x for x in (doc12, doc13) if x])
    nota.relacion("Paleta", [ref("arte-paleta")] if paleta else [])

    # hojas de personajes -------------------------------------------------------------------------------------------------------
    for p in galeria.get("personajes", []):
        pid = p["id"]
        archivos = [i for i in imagenes if posixpath.dirname(i["file"]) == "assets-ref/personajes/" + pid]
        pj = "pj-" + p["personaje"]
        nombre = p.get("nombre") or (registro.nota(pj).titulo if registro.existe(pj) else pid)
        cuerpo = ["Hojas de referencia de %s: modelo, poses y expresiones. Provisionales: se rehacen en pixel art con PixelLab." % nombre, ""]
        cuerpo += tabla(["Hoja", "Revisión", "Nota"], [(i["title"], i["status"], i.get("note", "")) for i in archivos])
        cuerpo += ["", "Archivos: " + ", ".join("`%s`" % i["file"] for i in archivos)]
        nota = registro.nueva("arte-pj-" + pid, "arte-personaje", "Arte de " + nombre, "arte", sufijo="arte", arriba="moc-arte", fuente=GALERIA,
                              tags=["estado/provisional"], props={"estado": defecto, "hojas": len(archivos), "personaje": ref(pj) if registro.existe(pj) else p["personaje"]},
                              resumen="%d hojas: %s" % (len(archivos), ", ".join(sorted({posixpath.basename(i["file"]).split(".")[0] for i in archivos}))),
                              cuerpo="\n".join(cuerpo))
        nota.relacion("Personaje", [existente(registro, pj)])
        nota.relacion("Documento", [doc12] if doc12 else [])
        for i in archivos:
            id_pieza[i["file"]] = nota.id
        if registro.existe(pj) and registro.nota(pj).id == pj:
            registro.nota(pj).relacion("Arte", [ref(nota.id)])

    # galería de PNJ ------------------------------------------------------------------------------------------------------------------
    for s in galeria.get("secciones", []):
        filas, npcs = [], []
        for h in s.get("hojas", []):
            im = por_archivo.get(h["file"], {})
            filas.append((im.get("title", posixpath.basename(h["file"])), im.get("status", ""), ", ".join(existente(registro, "npc-" + n) or n for n in h.get("npcs", [])),
                          "`%s`" % h["file"]))
            npcs += h.get("npcs", [])
        cuerpo = [s.get("lead", ""), ""] + tabla(["Hoja", "Revisión", "PNJ", "Archivo"], filas)
        nota = registro.nueva("arte-gal-" + s["id"], "galeria", s["titulo"], "arte", nombre="Galería: " + s["titulo"], sufijo="arte", arriba="moc-arte",
                              fuente=GALERIA, tags=["estado/provisional"], props={"estado": defecto, "hojas": len(s.get("hojas", [])), "pnj": len(npcs)},
                              resumen="%d hojas · %d PNJ" % (len(s.get("hojas", [])), len(npcs)), cuerpo="\n".join(cuerpo))
        nota.relacion("PNJ", [existente(registro, "npc-" + n) for n in npcs])
        nota.relacion("Documento", [doc12] if doc12 else [])
        for h in s.get("hojas", []):
            id_pieza[h["file"]] = nota.id
        for n in npcs:
            if registro.existe("npc-" + n):
                registro.nota("npc-" + n).relacion("Arte", [ref(nota.id)])

    # pruebas de estilo y marca (una nota por pieza) ----------------------------------------------------------------------------------
    piezas = [i for i in imagenes if posixpath.dirname(i["file"]).rsplit("/", 1)[-1] in PREFIJO_DIR and i["file"].startswith("assets-ref/")]
    ids = {}
    for i in piezas:
        d = posixpath.dirname(i["file"]).rsplit("/", 1)[-1]
        ids[i["file"]] = "arte-%s-%s" % (PREFIJO_DIR[d], slug(posixpath.splitext(posixpath.basename(i["file"]))[0], 50))
    por_stem = {(posixpath.dirname(f), posixpath.splitext(posixpath.basename(f))[0]): f for f in ids}
    por_categoria_paleta = []
    for i in piezas:
        d = posixpath.dirname(i["file"])
        corto = d.rsplit("/", 1)[-1]
        texto = "%s %s" % (i["title"], i.get("note", ""))
        pjs = mundo.personas_en(i["title"]) if mundo and i["category"] in ("Personajes", "Escenas") else []
        if mundo and "protagonista" in norm(i["title"]) and i["category"] == "Personajes":
            pjs.append("protagonista")
        zonas = [z for z, dz in (mundo.zonas.items() if mundo else []) if norm(dz["name"]) in norm(i["title"])]
        cuerpo = ["**Archivo:** `%s` · **Categoría:** %s · **Ronda:** %s · **Revisión:** %s" % (i["file"], i["category"], i.get("round", "–"), i["status"]),
                  "", i.get("note", "")]
        m = REEMPLAZO.search(i.get("note", ""))
        sustituta = por_stem.get((d, m.group(1))) if m else None
        nota = registro.nueva(ids[i["file"]], "arte-pieza", i["title"], "arte", sufijo="arte", arriba="moc-arte", fuente=ASSETS,
                              tags=["estado/provisional"], props={"estado": defecto, "revision": i["status"], "categoria": i["category"],
                                                                 "ronda": i.get("round"), "archivo": i["file"]},
                              resumen="%s · %s · %s" % (SECCION_DE_DIR[corto], i["category"], i["status"]), cuerpo="\n".join(cuerpo))
        nota.relacion("Reemplazada por", [ref(ids[sustituta])] if sustituta else [])
        nota.relacion("Personajes", [ref("pj-" + x) for x in pjs])
        nota.relacion("Zonas", [ref("zona-" + z) for z in zonas])
        cat = i["category"]
        nota.relacion("Mapa", [existente(registro, {"Minerales": "moc-minerales", "Mapa y zonas": "moc-zonas", "Edificios": "moc-edificaciones"}.get(cat, ""))])
        if cat == "Paleta":
            por_categoria_paleta.append(nota.id)
            nota.relacion("Paleta", [ref("arte-paleta")] if paleta else [])
        nota.relacion("Documento", [doc13 if corto == "marca" and doc13 else doc12] if (doc12 or doc13) else [])
        id_pieza[i["file"]] = nota.id
    # paleta -----------------------------------------------------------------------------------------------------------------
    if paleta:
        cuerpo = ["Valores aproximados a afinar (documento 12); la paleta se bloquea al producir el arte definitivo.", "", "## Colores", ""]
        cuerpo += tabla(["Color", "Hex", "Papel", "Uso"], [(c["name"], "`%s`" % c["hex"], c.get("role", ""), c.get("use", "")) for c in paleta.get("colors", [])])
        if paleta.get("proportion"):
            cuerpo += ["", "## Proporción", ""] + ["- **%s:** %s %% (`%s`)" % (p["label"], p["pct"], p["color"]) for p in paleta["proportion"]]
        if paleta.get("rules"):
            cuerpo += ["", "## Reglas", ""] + ["- " + r for r in paleta["rules"]]
        nota = registro.nueva("arte-paleta", "paleta", "Paleta de color", "arte", sufijo="arte", arriba="moc-arte", fuente=PALETA, tags=["estado/provisional"],
                              props={"estado": "provisional", "colores": len(paleta.get("colors", []))},
                              resumen="%d colores: 80 %% neutros fríos, 15 %% tonos medios, 5 %% vinotinto" % len(paleta.get("colors", [])), cuerpo="\n".join(cuerpo))
        nota.relacion("Documentos", [x for x in (doc12, doc13) if x])
        nota.relacion("Piezas de paleta", [ref(x) for x in por_categoria_paleta])

    # audio ----------------------------------------------------------------------------------------------------------------------
    sonidos = assets.get("sounds_planned", [])
    if sonidos:
        cuerpo = ["Sonidos previstos para el juego; ninguno existe todavía.", ""] + tabla(["Sonido", "Grupo", "Estado"], [(s["name"], s["group"], s["status"]) for s in sonidos])
        nota = registro.nueva("arte-audio", "audio", "Audio previsto", "arte", sufijo="arte", arriba="moc-arte", fuente=ASSETS, tags=["estado/pendiente"],
                              props={"estado": "pendiente", "sonidos": len(sonidos)}, resumen="%d sonidos previstos, todos pendientes" % len(sonidos), cuerpo="\n".join(cuerpo))
        nota.relacion("Documento", [doc12] if doc12 else [])
    cubiertas = len(id_pieza)
    registro.info.append("arte: %d imágenes (%d piezas sueltas, %d cubiertas por hojas o galería)" % (len(imagenes), len(piezas), cubiertas - len(piezas)))
