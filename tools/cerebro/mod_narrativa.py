"""Narrativa: decisiones y opciones, banderas y medidores, cuellos, cintas, hilos, escenas del Acto I, piezas del epílogo y carriles.

Fuentes: `studio/data/decisions.json`, `hilos.json` y `story.json`; la tabla maestra de escenas del documento 27 (sección 21), las
54 piezas del documento 25, los títulos de las cintas del 23 y las edificaciones del 26. Los personajes y las edificaciones los crea
la parte del mundo (`pj-<id>`, `npc-<id>`, `ed-…`): aquí se enlazan con `ref_suave`, así que el módulo funciona aunque no estén.
"""
import json
import re

from . import narr_fuentes as F
from . import texto as T
from .nucleo import ref, ref_suave

NOMBRE = "narrativa"
DOC_23, DOC_25, DOC_26, DOC_27 = (
    "studio/docs/23-arbol-de-decisiones.md", "studio/docs/25-finales-y-epilogos.md",
    "studio/docs/26-zonas-y-edificios.md", "studio/docs/27-guion-del-acto-i.md")
ACTOS = ["I", "II", "III", "IV"]
NIVELES = {"grande": "grande", "mediana": "mediana", "pequena": "pequeña"}
TEMAS_PIEZA = {  # prefijo -> (tema, nota del tema si existe)
    "H": ("Cabecera", None), "RE": ("Reme", "pj-reme"), "ES": ("Esteban", "pj-esteban"), "CA": ("Casilda", "pj-casilda"),
    "QU": ("Quiroga", "pj-quiroga"), "LU": ("Lucía", "pj-lucia"), "TE": ("Teo", "pj-teo"), "DU": ("Montenegro", "pj-montenegro"),
    "UN": ("Unión", "fac-union"), "FC": ("Facciones", None), "MU": ("Mundo", None), "ME": ("Mercado", None), "FM": ("Familia", None)}
NOMBRES_MEDIDOR = {"union": "Unión", "lucia": "Lucía", "esteban": "Esteban", "teo": "Teo"}


def _leer(repo, ruta):
    p = repo / ruta
    return p.read_text(encoding="utf-8") if p.is_file() else ""


def _json(repo, ruta):
    return json.loads(_leer(repo, ruta)) if (repo / ruta).is_file() else {}


def _linea(lineas, patron, desde=0):
    """Número de línea (1-based) de la primera línea desde `desde` (0-based) que casa con `patron`; 1 si no hay."""
    for i in range(desde, len(lineas)):
        if re.search(patron, lineas[i]):
            return i + 1
    return 1


def _celda(t):
    return re.sub(r"\s+", " ", str(t)).replace("|", "/").strip()


def _acto_id(acto):
    """Nota de la historia de un acto (la nota `acto-<N>` es del mundo y la crea la otra parte)."""
    return "historia-" + acto


def _suave_o_texto(registro, id_, texto):
    """Enlace obligatorio si la nota existe; si no, el texto plano (para IDs sacados de texto libre)."""
    return ref(id_, texto) if registro.existe(id_) else texto


class Narrativa:
    def __init__(self, registro, repo):
        self.r = registro
        self.repo = repo
        self.world = _json(repo, "studio/data/world.json")
        self.nombres, self.ids_mundo = {}, {}
        for p in self.world.get("characters", []):
            self.ids_mundo[p["id"]] = "pj-" + p["id"]
            for nombre in [p["name"]] + list(p.get("aka", [])):
                self.nombres[nombre] = "pj-" + p["id"]
        for n in self.world.get("npcs", []):
            self.ids_mundo[n["id"]] = "npc-" + n["id"]
        self.doc27, self.doc25 = _leer(repo, DOC_27), _leer(repo, DOC_25)
        self.hilos_de_nodo, self.hilos_de_cinta, self.hilos_de_pieza = {}, {}, {}
        self.escenas_de_hilo, self.escenas_de_cinta = {}, {}
        self.escenas_de_nodo, self.piezas_de_bandera = {}, {}
        self.nodos_de_acto, self.hilos_de_acto = {}, {}
        self.escenas, self.piezas, self.cintas, self.hilos = [], [], [], []

    # --- enlaces a lo que crea la parte del mundo -------------------------------------------------------------------
    def pj(self, nombre):
        nid = self.nombres.get(nombre)
        return ref_suave(nid, "", nombre) if nid else nombre

    def personaje_de_mundo(self, id_mundo):
        nid = self.ids_mundo.get(id_mundo)
        return ref_suave(nid, "", id_mundo) if nid else id_mundo

    @staticmethod
    def edificacion(ed):
        return ref_suave(ed, "", "`%s`" % ed)

    def doc(self, id_, texto=None):
        return _suave_o_texto(self.r, id_, texto or id_)

    # --- decisiones, banderas y cuellos ----------------------------------------------------------------------------
    def decisiones(self):
        ruta = "studio/data/decisions.json"
        datos = _json(self.repo, ruta)
        lineas = _leer(self.repo, ruta).split("\n")
        botones = F.botones_acto1(self.doc27)
        fijan, leen, cuello_de = {}, {}, {}
        for n in datos["nodes"]:
            for o in n["opciones"]:
                for f in o["fija"]:
                    fijan.setdefault(f, []).append("%s.%s" % (n["id"], o["id"]))
            for f in n["lee"]:
                leen.setdefault(f, []).append(n["id"])
        for c in datos["cuellos"]:
            for nid in c["recibe"]:
                cuello_de.setdefault(nid, []).append(c["id"])
        for f in datos["flags"]:
            self._bandera(f, fijan.get(f["id"], []), leen.get(f["id"], []), "%s:%d" % (ruta, _linea(lineas, r'"id":\s*"%s"' % re.escape(f["id"]))))
        for n in datos["nodes"]:
            self._nodo(n, cuello_de.get(n["id"], []), botones, lineas, ruta)
        for c in datos["cuellos"]:
            nota = self.r.nueva(
                c["id"], "cuello", c["titulo"], "narrativa/decisiones", sufijo="cuello", tags=["acto/" + c["acto"]],
                props={"acto": c["acto"], "recibe": [ref(n) for n in c["recibe"]]},
                resumen="Cuello de botella del Acto %s: reúne %d decisiones." % (c["acto"], len(c["recibe"])),
                cuerpo="Todas las ramas del Acto %s pasan por aquí: sea cual sea lo que hayas elegido, la historia vuelve a ser la misma." % c["acto"],
                arriba="moc-decisiones", fuente="%s:%d" % (ruta, _linea(lineas, r'"id":\s*"%s"' % re.escape(c["id"]))))
            nota.relacion("Reúne", [ref(n) for n in c["recibe"]])
            nota.relacion("Acto", [ref(_acto_id(c["acto"]))])
        self.datos_decisiones = datos
        return datos

    def _bandera(self, f, fijadas_por, leidas_por, fuente):
        medidor = f["tipo"] == "medidor"
        clave = f["id"][2:]
        nombre = "Medidor %s" % NOMBRES_MEDIDOR.get(clave, clave.replace("-", " ")) if medidor else "Bandera %s" % clave.replace("-", " ")
        nota = self.r.nueva(
            f["id"], "medidor" if medidor else "bandera", nombre, "narrativa/banderas", sufijo=f["tipo"],
            props={"clase": f["tipo"], "personajes": [self.pj(p) for p in f.get("personajes", [])],
                   "fijada_por": [ref(o) for o in fijadas_por], "leida_por": [ref(n) for n in leidas_por]},
            resumen=f["descripcion"], arriba="moc-decisiones", fuente=fuente)
        nota.relacion("Mueve" if medidor else "La fija", [ref(o) for o in fijadas_por])
        nota.relacion("La leen", [ref(n) for n in leidas_por])
        nota.relacion("Personajes", [self.pj(p) for p in f.get("personajes", [])])

    def _nodo(self, n, cuellos, botones, lineas, ruta):
        nid = n["id"]
        linea_nodo = _linea(lineas, r'"id":\s*"%s"' % re.escape(nid))
        opciones = ["%s.%s" % (nid, o["id"]) for o in n["opciones"]]
        fija = []
        for o in n["opciones"]:
            fija += [f for f in o["fija"] if f not in fija]
        filas = ["| Opción | Qué haces | Fija |", "|---|---|---|"]
        filas += ["| %s | %s | %s |" % (ref(oid), _celda(o["texto"]), ", ".join(ref(f) for f in o["fija"])) for oid, o in zip(opciones, n["opciones"])]
        cuerpo = ["**Se dispara:** " + n["dispara"], "", "## Opciones", ""] + filas
        nota = self.r.nueva(
            nid, "nodo", n["titulo"], "narrativa/decisiones", sufijo="decisión", tags=["acto/" + n["acto"]],
            props={"acto": n["acto"], "nivel": NIVELES.get(n["nivel"], n["nivel"]), "estado": n["estado"], "opciones": len(opciones),
                   "fija": [ref(f) for f in fija], "lee": [ref(f) for f in n["lee"]]},
            resumen="Acto %s · decisión %s · %d opciones" % (n["acto"], NIVELES.get(n["nivel"], n["nivel"]), len(opciones)),
            cuerpo="\n".join(cuerpo), arriba="moc-decisiones", fuente="%s:%d" % (ruta, linea_nodo))
        nota.relacion("Opciones", [ref(o) for o in opciones])
        nota.relacion("Fija o mueve", [ref(f) for f in fija])
        nota.relacion("Lee", [ref(f) for f in n["lee"]])
        nota.relacion("Cuello de botella", [ref(c) for c in cuellos])
        nota.relacion("Acto", [ref(_acto_id(n["acto"]))])
        self.nodos_de_acto.setdefault(n["acto"], []).append(nid)
        corto = re.sub(r"\s+", " ", n["titulo"])[:50].rstrip(" ,;:.")
        desde = linea_nodo - 1
        for k, (oid, o) in enumerate(zip(opciones, n["opciones"]), start=1):
            texto_boton = botones.get((nid, o["id"]))
            cuerpo = ["## Efectos", ""]
            for etiqueta, clave in (("Mundo", "mundo"), ("Mercado", "mercado"), ("Personajes", "personajes")):
                if o.get(clave) and o[clave] != "—":
                    cuerpo.append("- **%s:** %s" % (etiqueta, o[clave]))
            if texto_boton:
                cuerpo += ["", "**Botón:** «%s»" % texto_boton]
            props = {"decision": ref(nid), "opcion": o["id"], "fija": [ref(f) for f in o["fija"]]}
            if texto_boton:
                props["boton"] = texto_boton
            linea_opcion = _linea(lineas, r'"id":\s*"%s"' % re.escape(o["id"]), desde)
            desde = linea_opcion
            opcion = self.r.nueva(
                oid, "opcion", o["texto"], "narrativa/opciones", nombre="%s - %s" % (corto, o["id"]), alias=["%s.b%d" % (nid, k)], props=props,
                tags=["acto/" + n["acto"]], resumen=o["texto"], cuerpo="\n".join(cuerpo), arriba=nid, fuente="%s:%d" % (ruta, linea_opcion))
            opcion.relacion("Decisión", [ref(nid)])
            opcion.relacion("Fija o mueve", [ref(f) for f in o["fija"]])

    # --- cintas ---------------------------------------------------------------------------------------------------
    def cintas_de_anselmo(self, datos):
        ruta = "studio/data/decisions.json"
        lineas = _leer(self.repo, ruta).split("\n")
        titulos = F.titulos_cintas(_leer(self.repo, DOC_23))
        sitios = F.edificaciones_de_cintas(_leer(self.repo, DOC_26))
        for c in datos["cintas"]:
            n = c["n"]
            titulo = titulos.get(n)
            nombre = "Cinta %d - %s" % (n, titulo) if titulo else "Cinta %d" % n
            eds = sitios.get(n, [])
            nota = self.r.nueva(
                "cinta-%d" % n, "cinta", nombre, "narrativa/cintas", props={"n": n, "acto": c["acto"], "lugar": c["lugar"], "estado": c["estado"]},
                tags=["acto/" + c["acto"]], resumen="Se recoge en el Acto %s: %s" % (c["acto"], c["lugar"]),
                cuerpo="**Dónde la dejó Anselmo:** %s\n\nSe recoge en el Acto %s y solo se oye en el Acto IV, con el reproductor." % (c["lugar"], c["acto"]),
                arriba="moc-cintas", fuente="%s:%d" % (ruta, _linea(lineas, r'"n":\s*%d\b' % n)))
            nota.relacion("Lugar", [self.edificacion(e) for e in eds])
            nota.relacion("Acto", [ref(_acto_id(c["acto"]))])
            docs = [self.doc("doc-23-s07", "23 §7 Las ocho cintas"), self.doc("doc-21-s07", "21 §7 Las ocho cintas")]
            nota.relacion("Documentos", docs + ([self.doc("doc-27-s14", "27 §14 La cinta 1")] if n == 1 else []))
            self.cintas.append(nota)

    # --- escenas del Acto I ---------------------------------------------------------------------------------------
    def escenas_acto_i(self):
        datos, orden = F.escenas_acto1(self.doc27)
        previa = None
        for clave in orden:
            d = datos[clave]
            if "titulo" not in d:
                continue
            dia = int(clave[1])
            conv = lambda t: T.convertir(_celda(t), DOC_27)[0]  # noqa: E731
            lugares = F.EDIFICACION.findall(d["lugar"])
            personajes = [self.personaje_de_mundo(p) for p in F.codigos(d["personajes"])]
            nodos = [n for n in F.codigos(d.get("decision", "")) if n.startswith("n-")]
            hilos = [h for h in F.codigos(d.get("hilos", "")) if h.startswith("h-")]
            cintas = [n for n in F.numeros_de_cintas(d.get("sombra", ""))]
            tareas = list(dict.fromkeys(F.TAREA.findall(d.get("responsable", ""))))
            peso = d["peso"] if d["peso"].isdigit() else "por asignar (F3-16)"
            props = {"dia": dia, "bloque": d["bloque"], "peso": int(peso) if peso.isdigit() else peso,
                     "lugar": [self.edificacion(e) for e in lugares] or ("calle" if "calle" in d["lugar"] else _celda(d["lugar"])),
                     "personajes": personajes, "cajas": int(d["cajas"]), "ayudas": int(d["ayudas"]), "cartas": int(d["cartas"]), "textos": int(d["total"]),
                     "decision": [ref(n) for n in nodos] or "ninguna", "hilos": [ref(h) for h in hilos], "cinta": [ref("cinta-%d" % n) for n in cintas]}
            if previa:
                props["anterior"] = ref("esc-" + previa)
            cuerpo = ["- **Día %d · %s.** Lugar: %s. Personajes: %s." % (dia, d["bloque"].lower(), ", ".join(self.edificacion(e) for e in lugares) or conv(d["lugar"]),
                                                                  ", ".join(personajes)),
                      "- **Textos:** %s cajas, %s ayudas e interfaz, %s cartas y avisos (%s en total)." % (d["cajas"], d["ayudas"], d["cartas"], d["total"]),
                      "- **Peso:** %s." % (d["peso"] if d["peso"].isdigit() else "lo asigna " + conv(d["peso"])),
                      "- **Disparador:** " + conv(d.get("disparador", "")),
                      "- **Cola:** " + conv(d.get("cola", "")),
                      "- **Mecánica que enseña:** " + conv(d.get("mecanica", "")),
                      "- **Decisión:** " + conv(d.get("decision", "")),
                      "- **Hilos que siembra:** " + conv(d.get("hilos", "")),
                      "- **Sombra de Anselmo:** " + conv(d.get("sombra", "")),
                      "- **Props y pantalla:** " + conv(d.get("props", "")),
                      "- **Ramas:** " + conv(d.get("ramas", "")),
                      "- **Responsable del texto:** " + conv(d.get("responsable", "")),
                      "", "## Reparto de textos (orientativo)", "",
                      "- **Cajas:** " + conv(d.get("reparto", "")), "- **Ayudas e interfaz:** " + conv(d.get("reparto_ayudas", "")),
                      "- **Cartas y avisos:** " + conv(d.get("reparto_cartas", ""))]
            nota = self.r.nueva(
                "esc-" + clave, "escena", d["titulo"], "narrativa/escenas", nombre="%s %s" % (clave, d["titulo"]), alias=[clave], props=props,
                tags=["acto/I"], resumen="Día %d, %s: %s" % (dia, d["bloque"].lower(), d["titulo"]), cuerpo="\n".join(cuerpo),
                arriba="moc-escenas", fuente="%s:%d" % (DOC_27, d["linea"]))
            nota.relacion("Día", [self.doc("doc-27-s%02d" % (3 + dia), "27 §%d Día %d" % (3 + dia, dia)), self.doc("doc-27-s21", "27 §21 Esquema de escenas")])
            nota.relacion("Lugar", [self.edificacion(e) for e in lugares])
            nota.relacion("Personajes", personajes)
            nota.relacion("Decisión", [ref(n) for n in nodos])
            nota.relacion("Hilos que siembra", [ref(h) for h in hilos])
            nota.relacion("Cinta", [ref("cinta-%d" % n) for n in cintas])
            nota.relacion("Responsables", [self.doc(t, t) for t in tareas])
            for h in hilos:
                self.escenas_de_hilo.setdefault(h, []).append(nota.id)
            for n in nodos:
                self.escenas_de_nodo.setdefault(n, []).append(nota.id)
            for n in cintas:
                self.escenas_de_cinta.setdefault(n, []).append(nota.id)
            if previa:
                self.r.nota("esc-" + previa).props["siguiente"] = ref(nota.id)
            previa = clave
            self.escenas.append(nota)

    # --- piezas del epílogo -----------------------------------------------------------------------------------------
    def piezas_epilogo(self):
        piezas = F.piezas_epilogo(self.doc25)
        for p in piezas:
            codigo = p["codigo"]
            prefijo = codigo.split("-")[0]
            tema, nota_tema = TEMAS_PIEZA[prefijo]
            lee = [c for c in F.codigos(p["lee"])]
            banderas = [c for c in lee if c.startswith(("f-", "m-"))]
            estados = [c for c in lee if c.startswith("e-")]
            conv = lambda t: T.convertir(t.replace("<br>", "\n"), DOC_25)[0]  # noqa: E731
            cuerpo = ["- **Cuándo:** %s" % conv(p["cuando"]), "- **Lee:** %s" % (conv(p["lee"]) if lee else "—"), "- **Medio:** %s" % p["medio"],
                      "", "## Ejemplo (guía)", "", "> " + conv(p["ejemplo"]), "",
                      "Los textos de las tablas son ejemplos de voz, no los textos finales (los escribe %s)." % ref("F4-212")]
            props = {"codigo": codigo, "tema": tema, "medio": p["medio"], "cuando": _celda(p["cuando"]),
                     "lee": [ref(b) if self.r.existe(b) else b for b in banderas] + estados}
            seccion = "doc-25-s04" if prefijo == "H" else "doc-25-s05"
            nota = self.r.nueva(
                "ep-" + codigo, "pieza", "%s %s" % (codigo, _celda(re.sub(r"[*`]", "", p["cuando"]))), "narrativa/epilogos", alias=[codigo], props=props,
                tags=["acto/IV"], resumen="%s · %s: %s" % (tema, p["medio"], _celda(re.sub(r"[*`]", "", p["cuando"]))), cuerpo="\n".join(cuerpo),
                arriba="moc-finales", fuente="%s:%d" % (DOC_25, p["linea"]))
            if nota_tema:
                nota.relacion("Tema", [ref_suave(nota_tema, "", tema)])
            nota.relacion("Banderas que lee", [ref(b) for b in banderas if self.r.existe(b)])
            nota.relacion("Estados que lee", [ref("doc-25-s08", "25 §8 Estado legible")] if estados else [])
            nota.relacion("Documento", [self.doc(seccion, "25 §%s" % seccion[-2:].lstrip("0"))])
            for b in banderas:
                self.piezas_de_bandera.setdefault(b, []).append(nota.id)
            self.piezas.append(nota)
        for b, ids in self.piezas_de_bandera.items():
            if self.r.existe(b):
                self.r.nota(b).relacion("La leen las piezas del epílogo", [ref(i) for i in ids])
        return piezas

    # --- hilos -----------------------------------------------------------------------------------------------------
    def hilos_narrativos(self):
        ruta = "studio/data/hilos.json"
        datos = _json(self.repo, ruta)
        lineas = _leer(self.repo, ruta).split("\n")
        for h in datos["hilos"]:
            hid = h["id"]
            vistos = {"siembra": F.refs_vacias(), "resuelve": F.refs_vacias()}
            cuerpo = ["## Qué cambia", "", h["cambia"], ""]
            for clave, titulo in (("siembra", "Dónde se siembra"), ("resuelve", "Dónde se resuelve")):
                cuerpo += ["## " + titulo, ""]
                if not h[clave]:
                    cuerpo += ["Nada: el hilo %s." % ("se deja abierto" if clave == "resuelve" else "ya existe"), ""]
                for item in h[clave]:
                    refs = F.extraer_refs(item["ref"], self.r)
                    for k, v in refs.items():
                        vistos[clave][k] += [x for x in v if x not in vistos[clave][k]]
                    cuerpo.append("- **Acto %s.** %s _(%s)_" % (item["acto"], item["donde"], item["ref"]))
                cuerpo.append("")
            if h.get("motivo"):
                cuerpo += ["## Motivo del estado", "", h["motivo"], ""]
            todo = F.refs_vacias()
            for v in vistos.values():
                for k, ids in v.items():
                    todo[k] += [x for x in ids if x not in todo[k]]
            personajes = [self.pj(p) for p in h["personajes"]]
            props = {"tipo_hilo": h["tipo"], "estado": h["estado"], "personajes": personajes,
                     "siembra": sorted({s["acto"] for s in h["siembra"]}), "resuelve": sorted({s["acto"] for s in h["resuelve"]})}
            nota = self.r.nueva(
                hid, "hilo", h["titulo"], "narrativa/hilos", props=props, tags=["estado/hecho" if h["estado"] == "resuelto" else "estado/pendiente"],
                resumen="%s (%s): %s" % (h["tipo"].capitalize(), h["estado"], h["cambia"]), cuerpo="\n".join(cuerpo), arriba="moc-hilos",
                fuente="%s:%d" % (ruta, _linea(lineas, r'"id":\s*"%s"' % re.escape(hid))))
            nota.relacion("Personajes", personajes)
            escenas = list(dict.fromkeys(self.escenas_de_hilo.get(hid, []) + todo["escenas"]))
            self.escenas_de_hilo[hid] = escenas
            nota.relacion("Escenas", [ref(e) for e in escenas])
            nota.relacion("Decisiones", [ref(n) for n in todo["nodos"]])
            nota.relacion("Banderas y medidores", [ref(b) for b in todo["banderas"]])
            nota.relacion("Cuellos", [ref(c) for c in todo["cuellos"]])
            nota.relacion("Cintas", [ref(c) for c in todo["cintas"]])
            nota.relacion("Piezas del epílogo", [ref(p) for p in todo["piezas"]])
            nota.relacion("Edificaciones", [self.edificacion(e) for e in todo["edificaciones"]])
            nota.relacion("Documentos", [ref(d) for d in todo["docs"]])
            nota.relacion("Tareas", [ref(t) for t in todo["tareas"]])
            if todo["desconocidos"]:
                self.r.aviso("hilo %s: ID narrativo desconocido en «ref»: %s" % (hid, ", ".join(todo["desconocidos"])))
            for n in todo["nodos"]:
                self.hilos_de_nodo.setdefault(n, []).append(hid)
            for c in todo["cintas"]:
                self.hilos_de_cinta.setdefault(c, []).append(hid)
            for p in todo["piezas"]:
                self.hilos_de_pieza.setdefault(p, []).append(hid)
            for a in sorted({s["acto"] for s in h["siembra"] + h["resuelve"]}):
                self.hilos_de_acto.setdefault(a, []).append(hid)
            self.hilos.append(nota)
        return datos

    def enlaces_inversos(self):
        for nid, hilos in self.hilos_de_nodo.items():
            self.r.nota(nid).relacion("Hilos que lo citan", [ref(h) for h in hilos])
        for nid, escenas in self.escenas_de_nodo.items():
            self.r.nota(nid).relacion("Escenas", [ref(e) for e in escenas])
        for n, escenas in self.escenas_de_cinta.items():
            self.r.nota("cinta-%d" % n).relacion("Escena donde se encuentra", [ref(e) for e in escenas])
        for cid, hilos in self.hilos_de_cinta.items():
            self.r.nota(cid).relacion("Hilos", [ref(h) for h in hilos])
        for escena in self.escenas:
            citados = [h for h, escenas in self.escenas_de_hilo.items() if escena.id in escenas and ref(h) not in escena.props["hilos"]]
            escena.relacion("Hilos que la citan", [ref(h) for h in citados])
        for pid, hilos in self.hilos_de_pieza.items():
            self.r.nota(pid).relacion("Hilos que cierra o deja abiertos", [ref(h) for h in hilos])

    # --- carriles y actos -----------------------------------------------------------------------------------------
    def carriles_y_actos(self):
        story = _json(self.repo, "studio/data/story.json")
        ruta = "studio/data/story.json"
        lineas = _leer(self.repo, ruta).split("\n")
        carriles = []
        for lane in story.get("lanes", []):
            cuerpo = []
            for i, celdas in enumerate(lane["cells"]):
                if celdas:
                    cuerpo += ["## Acto %s" % ACTOS[i], ""] + ["- " + c for c in celdas] + [""]
            nota = self.r.nueva(
                "carril-" + lane["id"], "carril", "Carril %s" % lane["label"], "narrativa/carriles", sufijo="carril",
                props={"etiqueta": lane["label"], "glifo": lane.get("glyph", ""), "elementos": sum(len(c) for c in lane["cells"])},
                resumen="Fila «%s» de la línea de historia, acto por acto." % lane["label"], cuerpo="\n".join(cuerpo), arriba="moc-narrativa",
                fuente="%s:%d" % (ruta, _linea(lineas, r'"id":\s*"%s"' % re.escape(lane["id"]))))
            nota.relacion("Actos", [ref(_acto_id(a)) for a, c in zip(ACTOS, lane["cells"]) if c])
            carriles.append(nota)
        for i, a in enumerate(story.get("acts", [])):
            aid = _acto_id(a["n"])
            cuerpo = ["**Lugar:** %s · **Duración:** %s" % (a["place"], a["time"]), "", "**Al terminar:** " + a["closes"], ""]
            for lane in story.get("lanes", []):
                celdas = lane["cells"][i] if i < len(lane["cells"]) else []
                if celdas:
                    cuerpo += ["## " + lane["label"], ""] + ["- " + c for c in celdas] + [""]
            nota = self.r.nueva(
                aid, "historia", "Acto %s - %s" % (a["n"], a["title"]), "narrativa/actos", sufijo="historia",
                props={"acto": a["n"], "lugar": a["place"], "duracion": a["time"], "color": a.get("color", "")}, tags=["acto/" + a["n"]],
                resumen=a["closes"], cuerpo="\n".join(cuerpo), arriba="moc-narrativa",
                fuente="%s:%d" % (ruta, _linea(lineas, r'"n":\s*"%s"' % a["n"])))
            nota.relacion("Lo que abre el mundo", [ref_suave("acto-" + a["n"], "", "Acto " + a["n"])])
            nota.relacion("Tareas del acto", [self.doc(t, t) for t in a.get("tasks", [])])
            nota.relacion("Decisiones", [ref(n) for n in self.nodos_de_acto.get(a["n"], [])])
            nota.relacion("Hilos que toca", [ref(h) for h in self.hilos_de_acto.get(a["n"], [])])
            nota.relacion("Cintas", [ref(c.id) for c in self.cintas if c.props["acto"] == a["n"]])
            if a["n"] == "I":
                nota.relacion("Escenas", [ref(e.id) for e in self.escenas])
            nota.relacion("Carriles", [ref(c.id) for c, l in zip(carriles, story["lanes"]) if i < len(l["cells"]) and l["cells"][i]])
            if self.r.existe("acto-" + a["n"]):  # la nota del mundo enlaza de vuelta a la historia del acto
                self.r.nota("acto-" + a["n"]).relacion("Historia del acto", [ref(aid)])
        return story


def _mocs(n, story):
    """Cuerpo de los mapas de contenido. Los nodos listan solos a sus hijos; aquí van las tablas y las explicaciones."""
    r = n.r
    r.nota("moc-narrativa").cuerpo = "\n".join([
        "Historia, decisiones, hilos, escenas y finales de Veta de Fortuna. Todo sale de `studio/data/` y de los documentos 18 a 27.", "",
        "## Mapas", "",
        "- %s: los %d nodos del árbol, sus opciones, las banderas y los medidores, y los cuellos de botella." % (ref("moc-decisiones"), len(r.por_tipo("nodo"))),
        "- %s: los %d hilos (pistas, promesas, secretos y conflictos) con dónde se siembran y se resuelven." % (ref("moc-hilos"), len(n.hilos)),
        "- %s: las %d escenas del Acto I (guion del documento 27)." % (ref("moc-escenas"), len(n.escenas)),
        "- %s: la cabecera, las tarjetas y el acta (documento 25), %d piezas." % (ref("moc-finales"), len(n.piezas)),
        "- %s: las ocho cintas de Anselmo." % ref("moc-cintas"), "",
        "## Documentos de la historia", "",
        "- " + ", ".join(n.doc("doc-%s" % d) for d in ("08", "17", "18", "19", "21", "22", "23", "24", "25", "27")), "",
        "## Después del Acto IV", "", story.get("after", ""), ""])
    r.nota("moc-decisiones").cuerpo = "\n".join(
        ["## Por acto", "", "| Acto | Decisiones |", "|---|---|"] +
        ["| %s | %s |" % (a, ", ".join(ref(x) for x in n.nodos_de_acto.get(a, []))) for a in ACTOS] +
        ["", "Cada decisión tiene sus opciones como notas propias (`n-…​.b1` es la primera) y una o varias banderas o medidores que fija. "
         "Los cuellos de botella reúnen las ramas para que cualquier camino llegue al mismo punto."])
    filas = ["| Hilo | Siembra | Se resuelve | Estado |", "|---|---|---|---|"]
    cuerpo = ["%d hilos: %s." % (len(n.hilos), ", ".join("%d %s" % (sum(1 for h in n.hilos if h.props["tipo_hilo"] == t), t) for t in ("pista", "promesa", "secreto", "conflicto"))), ""]
    for tipo in ("pista", "promesa", "secreto", "conflicto"):
        cuerpo += ["## " + tipo.capitalize() + "s", ""] + filas
        for h in (x for x in n.hilos if x.props["tipo_hilo"] == tipo):
            cuerpo.append("| %s | %s | %s | %s |" % (ref(h.id), ", ".join(h.props["siembra"]) or "—", ", ".join(h.props["resuelve"]) or "abierto", h.props["estado"]))
        cuerpo.append("")
    r.nota("moc-hilos").cuerpo = "\n".join(cuerpo)
    filas = ["| Escena | Título | Bloque | Decisión | Cinta |", "|---|---|---|---|---|"]
    por_dia = {}
    for e in n.escenas:
        por_dia.setdefault(e.props["dia"], []).append(e)
    cuerpo = ["Las 28 escenas del Acto I, en los siete días del guion (documento 27, sección 21). Cada una enlaza a su día, sus hilos y su lugar.", ""]
    for dia, escenas in por_dia.items():
        cuerpo += ["## Día %d" % dia, ""] + filas
        for e in escenas:
            decision = e.props["decision"]
            cuerpo.append("| %s | %s | %s | %s | %s |" % (ref(e.id), e.titulo, e.props["bloque"], ", ".join(decision) if isinstance(decision, list) else decision,
                                                         ", ".join(e.props["cinta"]) or "—"))
        cuerpo.append("")
    r.nota("moc-escenas").cuerpo = "\n".join(cuerpo)
    cuerpo = ["Cómo se cierra el Acto IV: la cabecera, las tarjetas por piezas y, al final, el acta de calibración (no es una pieza). "
              "Son %d piezas y unas 17 por partida." % len(n.piezas), "",
              "- Documento: %s · %s · %s · %s · %s" % (n.doc("doc-25-s03", "25 §3 El acta"), n.doc("doc-25-s04", "25 §4 La cabecera"), n.doc("doc-25-s05", "25 §5 Las piezas"),
                                                    n.doc("doc-25-s06", "25 §6 Cobertura"), n.doc("doc-25-s07", "25 §7 Hilos abiertos")),
              "- Salidas: revelar, callar o vender (a Casilda, al Consorcio o al Ministerio). Decide %s." % ref("n-iv-aetherita"), ""]
    caminos = F.caminos_prueba(n.doc25)
    if caminos:
        cuerpo += ["## Ocho caminos de prueba", "", "| Camino | Salida | Piezas |", "|---|---|---|"]
        for numero, salida, _, codigos in caminos:
            cuerpo.append("| %d | %s | %s |" % (numero, salida, " ".join(ref("ep-" + c, c) for c in codigos if r.existe("ep-" + c))))
        cuerpo.append("")
    cuerpo += ["## Hilos que siguen abiertos", "", "- " + ", ".join(ref(h.id) for h in n.hilos if h.props["estado"] == "abierto")]
    r.nota("moc-finales").cuerpo = "\n".join(cuerpo)
    r.nota("moc-cintas").cuerpo = "\n".join(
        ["Las ocho cintas que Anselmo escondió. Se recogen a lo largo de la historia (1 en el I, 2 en el II, 3 a 5 en el III y 6 a 8 en el IV) y se oyen en el Acto IV.", "",
         "| Cinta | Acto | Dónde |", "|---|---|---|"] +
        ["| %s | %s | %s |" % (ref(c.id), c.props["acto"], _celda(c.props["lugar"])) for c in n.cintas])


def generar(registro, repo):
    if not (repo / "studio" / "data" / "decisions.json").is_file():
        registro.info.append("narrativa: sin studio/data/decisions.json, se omite")
        return
    n = Narrativa(registro, repo)
    registro.moc("moc-narrativa", "Narrativa", "Historia, decisiones, hilos, escenas, finales y cintas.", orden=70)
    registro.moc("moc-decisiones", "Decisiones", "Árbol de decisiones: nodos, opciones, banderas y medidores.", orden=71, auto_hijos=True)
    registro.moc("moc-hilos", "Hilos", "Pistas, promesas, secretos y conflictos de la historia.", orden=72, auto_hijos=False)
    registro.moc("moc-escenas", "Escenas", "Las 28 escenas del Acto I.", orden=73, auto_hijos=False)
    registro.moc("moc-finales", "Finales", "Cabecera, tarjetas y acta del epílogo.", orden=74)
    registro.moc("moc-cintas", "Cintas", "Las ocho cintas de Anselmo.", orden=75, auto_hijos=False)
    datos = n.decisiones()
    n.cintas_de_anselmo(datos)
    n.escenas_acto_i()
    n.piezas_epilogo()
    n.hilos_narrativos()
    n.enlaces_inversos()
    story = n.carriles_y_actos()
    _mocs(n, story)
    registro.info.append("narrativa: %d nodos, %d opciones, %d banderas y medidores, %d hilos, %d escenas, %d piezas, %d cintas" % (
        len(registro.por_tipo("nodo")), len(registro.por_tipo("opcion")), len(registro.por_tipo("bandera")) + len(registro.por_tipo("medidor")),
        len(n.hilos), len(n.escenas), len(n.piezas), len(n.cintas)))
