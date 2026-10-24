"""Pruebas del cerebro del proyecto (F0-90): tools/cerebro, el vault de Obsidian generado en studio/cerebro.

Un repo de prueba mínimo (documentos, ADR, roadmap, equipo y memoria) comprueba el núcleo y los generadores; una pasada
sobre el repo real comprueba que no hay enlaces sin resolver, huérfanos ni nombres inválidos. Ejecutar:
    python3 -m unittest discover -s tools/ci -p "test_cerebro.py" -v
"""
import json
import pathlib
import re
import sys
import tempfile
import types
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from cerebro import generar, nucleo, texto  # noqa: E402

PROHIBIDOS = set('#^[]|:/\\?*"<>')
LINK = re.compile(r"\[\[([^\]|\\]+)(?:\\?\|[^\]]*)?\]\]")

DOC_00 = """# 00 · Visión de prueba ✅

Intro con enlace a [01](01-segundo.md) y a la tarea F0-01.

## Concepto ✅

Texto con `ed-vb-tienda`, `no-existe-aun` y un ejemplo `a | b`. Ver [ADR](adr/0001-uno.md). Tarea F0-02 y F9-99.

### Detalle

Una ### dentro.

## 2 · Pilares: «uno» / dos ✅

Algo 🟡 por decidir y otro punto ❓ abierto, aplazado ⏳ F0-02.

```
Esto no se convierte: [01](01-segundo.md) F0-01 `ed-vb-tienda`
```
"""
DOC_01 = """# 01 · Segundo

## Único

Vuelve a [00](00-vision.md#concepto).
"""
ADR_1 = """# ADR-0001 · Uno

**Estado:** ✅ Aceptada · **Fecha:** 2026-10-11

## Decisión

Se hace. Ver [00](../00-vision.md).
"""
ROADMAP = {
    "meta": {"targets": ["MVP"]},
    "phases": [
        {"id": "F0", "name": "Diseño", "target": "MVP", "goal": "Todo en papel.", "milestones": [
            {"id": "F0.1", "name": "Primero", "tasks": [
                {"id": "F0-01", "title": "Visión: pilares / alcance", "est": 2, "status": "done", "desc": "Documento 00 y ADR-0001.", "done_when": "Hecho.", "prio": "P0"},
                {"id": "F0-02", "title": "Segunda", "est": 1, "status": "doing", "desc": "Sigue de F0-01 ([01](01-segundo.md)).", "prio": "P1"},
            ]}]},
        {"id": "F1", "name": "Base", "target": "MVP", "goal": "", "milestones": [
            {"id": "F1.1", "name": "Motor", "tasks": [
                {"id": "F1-01", "title": "Futura", "est": 1, "status": "backlog", "desc": "", "prio": "P2"}]}]},
    ],
}
TAREA_02 = {"id": "F0-02", "history": [{"at": "2026-10-20", "from": "backlog", "to": "doing", "by": "claude", "note": "Empieza"}], "comments": [], "evidence": [],
            "pipeline": {"especialista": "narrador", "etapas": [
                {"etapa": "analisis", "estado": "hecha", "at": "2026-10-20", "por": "analista", "nota": "Con | barra"},
                {"etapa": "produccion", "estado": "activa", "por": "narrador"}],
                "traspasos": [{"de": "coordinador", "a": "analista", "que": "Encargo", "at": "2026-10-20"}]}}
EQUIPO = {
    "version": 1, "nota": "Equipo de prueba.", "reglas": ["Una regla."], "estados_etapa": ["pendiente", "activa", "hecha"],
    "deptos": [{"id": "dir", "nombre": "Dirección"}],
    "etapas": [{"id": "analisis", "nombre": "Análisis", "rol": "analista", "glifo": "A", "que": "Analizar."},
               {"id": "produccion", "nombre": "Producción", "rol": "especialista", "glifo": "P", "que": "Producir."}],
    "roles": [{"id": "coordinador", "nombre": "Coordinador", "tipo": "principal", "agente": None, "depto": "dir", "desde": "F0", "hace": "Reparte.", "entrega": "Cierre"},
              {"id": "analista", "nombre": "Analista", "tipo": "agente", "agente": "analista", "depto": "dir", "desde": "F0", "hace": "Analiza."},
              {"id": "narrador", "nombre": "Narrador", "tipo": "agente", "agente": "narrador", "especialista": True, "depto": "dir", "desde": "F0", "hace": "Escribe."}],
}
AGENTE = "---\nname: analista\ndescription: Analiza.\ntools: Read, Grep\nmodel: sonnet\n---\nCuerpo.\n"
MEMORIA = "---\nname: nota-uno\ndescription: \"Una memoria\"\nmetadata:\n  type: project\n---\nMira doc 00 y F0-01. Ver [[nota-dos]].\n"


def escribir(ruta, texto_):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(texto_, encoding="utf-8")


def repo_de_prueba(base):
    docs = base / "studio" / "docs"
    escribir(docs / "00-vision.md", DOC_00)
    escribir(docs / "01-segundo.md", DOC_01)
    escribir(docs / "adr" / "0001-uno.md", ADR_1)
    datos = base / "studio" / "data"
    escribir(datos / "roadmap.json", json.dumps(ROADMAP, indent=2, ensure_ascii=False))
    escribir(datos / "tasks" / "F0-02.json", json.dumps(TAREA_02, ensure_ascii=False))
    escribir(datos / "equipo.json", json.dumps(EQUIPO, ensure_ascii=False))
    escribir(base / ".claude" / "agents" / "analista.md", AGENTE)
    mem = base / "memoria-prueba"
    escribir(mem / "MEMORY.md", "- [x](nota-uno.md)\n")
    escribir(mem / "nota-uno.md", MEMORIA)
    escribir(mem / "nota-dos.md", "---\nname: nota-dos\ndescription: Otra\n---\nTexto.\n")
    return base


def vault_en(base, repo, **kw):
    destino = base / "vault"
    res = generar.generar_vault(repo, destino, opciones={"memoria": str(repo / "memoria-prueba")}, **kw)
    return destino, res


def notas(destino):
    return {p.relative_to(destino).as_posix(): p.read_text(encoding="utf-8") for p in destino.rglob("*.md")
            if p.relative_to(destino).parts[0] in ("generado", "MOC") or p.parent == destino}


def comprobar_vault(caso, destino):
    """Nombres válidos y únicos, enlaces que resuelven y ninguna nota sin enlaces. Devuelve {nombre: texto}."""
    por_nombre, enlaces = {}, {}
    for rel, txt in notas(destino).items():
        nombre = pathlib.PurePosixPath(rel).stem
        caso.assertFalse(PROHIBIDOS & set(nombre), "nombre con caracteres prohibidos: %s" % nombre)
        caso.assertNotIn(nombre.casefold(), por_nombre, "nombre repetido: %s" % nombre)
        por_nombre[nombre.casefold()] = txt
        enlaces[nombre.casefold()] = {m.casefold() for m in LINK.findall(txt)}
    for origen, destinos in enlaces.items():
        for d in destinos:
            caso.assertIn(d, por_nombre, "enlace sin destino en %s: %s" % (origen, d))
    con_entrada = {d for ds in enlaces.values() for d in ds}
    for origen, destinos in enlaces.items():
        caso.assertTrue(destinos - {origen} or origen in con_entrada, "nota huérfana: %s" % origen)
    return por_nombre


class NucleoTest(unittest.TestCase):
    def test_nombre_seguro_quita_caracteres_y_marcas(self):
        n = nucleo.nombre_seguro('4 · Día 1: "La llave" [x] #a ^b | c ? * < > \\ / ✅')
        self.assertFalse(PROHIBIDOS & set(n), n)
        self.assertNotIn("✅", n)
        self.assertEqual(n, n.strip())

    def test_nombre_seguro_corta_largos_en_palabra(self):
        n = nucleo.nombre_seguro("palabra " * 30, 40)
        self.assertLessEqual(len(n), 40)
        self.assertTrue(n.endswith("palabra"))

    def test_nombres_unicos_con_sufijo_de_tipo(self):
        r = nucleo.Registro()
        a = r.nueva("min-taller", "mecanica", "Taller", "mundo", sufijo="mecánica")
        b = r.nueva("ed-vb-taller", "edificacion", "Taller", "mundo", sufijo="edificación")
        c = r.nueva("otro-taller", "edificacion", "Taller", "mundo", sufijo="edificación")
        d = r.nueva("taller-4", "x", "TALLER", "mundo")
        self.assertEqual(a.nombre, "Taller")
        self.assertEqual(b.nombre, "Taller (edificación)")
        self.assertEqual(c.nombre, "Taller (edificación) 2")
        self.assertNotIn(d.nombre.casefold(), [a.nombre.casefold(), b.nombre.casefold(), c.nombre.casefold()])

    def test_ids_repetidos_o_invalidos_fallan(self):
        r = nucleo.Registro()
        r.nueva("a", "t", "A", "x")
        with self.assertRaises(ValueError):
            r.nueva("a", "t", "Otra", "x")
        with self.assertRaises(ValueError):
            r.nueva("con espacio", "t", "B", "x")
        with self.assertRaises(ValueError):
            r.nueva("b", "t", "B", "../fuera")
        with self.assertRaises(ValueError):
            r.nueva("c", "t", "C", "mis-notas")

    def test_resolucion_de_ids_alias_y_enlaces_opcionales(self):
        r = nucleo.Registro()
        r.nueva("esc-d1.1", "escena", "La llave", "narrativa", alias=["d1.1"], arriba="inicio")
        r.nueva("x", "t", "X", "x", arriba="inicio", cuerpo="\n".join([
            "Por id " + nucleo.ref("esc-d1.1"), "Por alias " + nucleo.ref("d1.1", "d1.1"),
            "Opcional " + nucleo.ref_suave("nada", "nada", "`nada`"), "Obligatorio " + nucleo.ref("falta", "visible"),
            "| tabla | " + nucleo.ref("esc-d1.1", "alias") + " |"]))
        archivos = r.construir()
        txt = archivos["generado/x/X.md"]
        self.assertIn("Por id [[La llave]]", txt)
        self.assertIn("Por alias [[La llave|d1.1]]", txt)
        self.assertIn("Opcional `nada`", txt)
        self.assertIn("Obligatorio visible", txt)
        self.assertIn("[[La llave\\|alias]]", txt)  # en tablas la barra se escapa
        sin_resolver = [a for a in r.avisos if a.startswith("enlace sin resolver")]
        self.assertEqual(len(sin_resolver), 1)
        self.assertIn("falta", sin_resolver[0])

    def test_conversion_de_texto(self):
        out, citas = texto.convertir(
            "Ver [01](01-x.md) y [web](https://a.b/c.md), `ed-vb-tienda`, `a | b`, F0-01.\n```\n[01](01-x.md) F0-01\n```", "studio/docs/00-y.md")
        self.assertIn(nucleo.ref_ruta("studio/docs/01-x.md", "01"), out)
        self.assertIn("(https://a.b/c.md)", out)
        self.assertIn("`a | b`", out)
        self.assertIn(nucleo.ref_suave("ed-vb-tienda", "ed-vb-tienda", "`ed-vb-tienda`"), out)
        self.assertIn("```\n[01](01-x.md) F0-01\n```", out)
        self.assertEqual((citas.rutas, citas.tareas, citas.codigos), (["studio/docs/01-x.md"], ["F0-01"], ["ed-vb-tienda"]))


class VaultTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.base = pathlib.Path(cls.tmp.name)
        cls.repo = repo_de_prueba(cls.base)
        cls.destino, cls.res = vault_en(cls.base, cls.repo)
        cls.por_nombre = {n.stem.casefold(): n.read_text(encoding="utf-8") for n in cls.destino.rglob("*.md")
                          if n.relative_to(cls.destino).parts[0] in ("generado", "MOC") or n.parent == cls.destino}

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def nota(self, nombre):
        return self.por_nombre[nombre.casefold()]

    def test_nombres_validos_y_unicos_sin_huerfanos(self):
        comprobar_vault(self, self.destino)

    def test_sin_avisos_y_conteos(self):
        self.assertEqual(self.res.avisos, [])  # F9-99 no existe, pero es un enlace opcional: no avisa
        c = self.res.conteo
        self.assertEqual((c["documento"], c["adr"], c["seccion"], c["tarea"], c["fase"], c["hito"], c["rol"], c["etapa"], c["memoria"]),
                         (2, 1, 4, 3, 2, 2, 3, 2, 2))

    def test_documento_indice_con_propiedades(self):
        txt = self.nota("00 Visión de prueba")
        self.assertIn('id: "doc-00"', txt)
        self.assertRegex(txt, r"limpieza: \d+")
        self.assertIn("abiertos: 2", txt)
        self.assertIn("espera: 1", txt)
        self.assertIn("[[00 §Concepto]]", txt)
        self.assertIn("[[00 §2 Pilares - «uno» - dos]]", txt)

    def test_secciones_con_navegacion_y_subtitulos(self):
        txt = self.nota("00 §Concepto")
        self.assertIn('id: "doc-00-concepto"', txt)
        self.assertIn('siguiente: "[[00 §2 Pilares - «uno» - dos]]"', txt)
        self.assertNotIn("anterior:", txt)
        self.assertIn("### Detalle", txt)
        self.assertIn("[[ADR-0001 Uno|ADR]]", txt)
        self.assertIn("[[F0-02 Segunda|F0-02]]", txt)
        self.assertIn("F9-99", txt)
        self.assertNotIn("[[F9-99", txt)
        self.assertIn("`no-existe-aun`", txt)
        self.assertIn("`a | b`", txt)

    def test_codigo_no_se_convierte(self):
        txt = self.nota("00 §2 Pilares - «uno» - dos")
        self.assertIn("```\nEsto no se convierte: [01](01-segundo.md) F0-01 `ed-vb-tienda`\n```", txt)
        self.assertIn('id: "doc-00-s02"', txt)
        self.assertIn('aplazado_a: ["[[F0-02 Segunda]]"]', txt)

    def test_enlaces_entre_documentos_y_adr(self):
        self.assertIn("[[01 Segundo|01]]", self.nota("00 Visión de prueba"))
        self.assertIn("[[00 Visión de prueba|00]]", self.nota("01 §Único"))
        self.assertIn("[[00 Visión de prueba|00]]", self.nota("ADR-0001 §Decisión"))
        self.assertIn("**Enlaza a:**", self.nota("00 Visión de prueba"))
        self.assertIn("**Citado por:**", self.nota("01 Segundo"))
        self.assertIn('estado: "Aceptada"', self.nota("ADR-0001 Uno"))

    def test_tareas_con_etapas_traspasos_y_documentos(self):
        txt = self.nota("F0-02 Segunda")
        self.assertIn('hito: "[[F0.1 Primero]]"', txt)
        self.assertIn('status: "doing"', txt)
        self.assertIn('"analisis: hecha"', txt)
        self.assertIn("estado/en-curso", txt)
        self.assertIn("[[Coordinador]] → [[Analista]]", txt)
        self.assertIn("Con / barra", txt)
        self.assertIn("[[00 §Concepto]]", txt)  # la sección que la cita
        t1 = self.nota("F0-01 Visión - pilares - alcance")
        self.assertIn('docs: ["[[00 Visión de prueba]]", "[[ADR-0001 Uno]]"', t1)
        self.assertIn("estado/hecho", t1)
        t3 = self.nota("F1-01 Futura")
        self.assertIn("backlog/futuro", t3)
        self.assertNotIn("backlog/futuro", self.nota("F0-02 Segunda"))

    def test_roadmap_equipo_y_memoria(self):
        self.assertIn("[[F0.1 Primero]]", self.nota("F0 Diseño"))
        self.assertIn('modelo: "sonnet"', self.nota("Analista"))
        self.assertIn('esfuerzo: "heredado"', self.nota("Analista"))
        self.assertIn("[[F0-02 Segunda]]", self.nota("Analista"))
        self.assertIn("[[Analista]]", self.nota("Etapa Análisis"))
        mem = self.nota("Nota uno")
        self.assertIn("[[Nota dos]]", mem)
        self.assertIn("[[00 Visión de prueba]]", mem)
        self.assertIn("[[F0-01 Visión - pilares - alcance|F0-01]]", mem)

    def test_inicio_y_mis_notas(self):
        self.assertIn("[[MOC Documentos]]", self.nota("00 Inicio"))
        self.assertTrue((self.destino / "mis-notas" / "README.md").is_file())
        self.assertTrue((self.destino / ".obsidian" / "graph.json").is_file())

    def test_plantilla_obsidian_es_json_valido_y_cubre_tipos(self):
        for archivo in (generar.PLANTILLA).glob("*.json"):
            json.loads(archivo.read_text(encoding="utf-8"))
        graph = json.loads((generar.PLANTILLA / "graph.json").read_text(encoding="utf-8"))
        consultas = " ".join(g["query"] for g in graph["colorGroups"])
        for etiqueta in ("estado/hecho", "estado/en-curso", "estado/pendiente", "generado/docs", "generado/adr", "generado/equipo", "MOC"):
            self.assertIn(etiqueta, consultas)
        marcadores = json.loads((generar.PLANTILLA / "bookmarks.json").read_text(encoding="utf-8"))
        self.assertTrue(any("backlog/futuro" in b["options"]["search"] for b in marcadores["items"]))


class EscrituraTest(unittest.TestCase):
    def test_idempotente_y_sin_tocar_lo_del_autor(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = pathlib.Path(tmp)
            repo = repo_de_prueba(base)
            destino = base / "vault"
            escribir(destino / "mis-notas" / "mi-nota.md", "---\ngenerado: true\n---\nmía\n")
            escribir(destino / "mis-notas" / "README.md", "mi readme")
            escribir(destino / ".obsidian" / "graph.json", '{"mio": true}')
            escribir(destino / ".obsidian" / "workspace.json", "{}")
            escribir(destino / "Mi nota suelta.md", "# mía, sin la marca\n")
            escribir(destino / "generado" / "viejo" / "Sobrante.md", "x")
            escribir(destino / "MOC" / "MOC Viejo.md", "x")
            escribir(destino / "Raíz vieja.md", "---\nid: \"x\"\ngenerado: true\n---\n")
            _, r1 = vault_en(base, repo)
            self.assertGreater(r1.escritos, 0)
            self.assertGreaterEqual(r1.borrados, 3)
            self.assertFalse((destino / "generado" / "viejo").exists())
            self.assertFalse((destino / "MOC" / "MOC Viejo.md").exists())
            self.assertFalse((destino / "Raíz vieja.md").exists())
            self.assertEqual((destino / "mis-notas" / "mi-nota.md").read_text(encoding="utf-8"), "---\ngenerado: true\n---\nmía\n")
            self.assertEqual((destino / "mis-notas" / "README.md").read_text(encoding="utf-8"), "mi readme")
            self.assertEqual((destino / ".obsidian" / "graph.json").read_text(encoding="utf-8"), '{"mio": true}')
            self.assertTrue((destino / ".obsidian" / "workspace.json").is_file())
            self.assertTrue((destino / "Mi nota suelta.md").is_file())
            self.assertTrue((destino / ".obsidian" / "app.json").is_file())  # lo que faltaba sí se copia
            antes = {p.relative_to(destino).as_posix(): p.read_bytes() for p in destino.rglob("*") if p.is_file()}
            _, r2 = vault_en(base, repo)
            despues = {p.relative_to(destino).as_posix(): p.read_bytes() for p in destino.rglob("*") if p.is_file()}
            self.assertEqual(antes, despues)
            self.assertEqual((r2.escritos, r2.borrados), (0, 0))

    def test_no_escribe_fuera_de_las_carpetas_propias(self):
        with tempfile.TemporaryDirectory() as tmp:
            for rel in ("mis-notas/x.md", ".obsidian/x.md", "otra/x.md", "../x.md", "x.md"):
                with self.assertRaises(ValueError, msg=rel):
                    nucleo.escribir(pathlib.Path(tmp) / "v", {rel: "x"})

    def test_sin_memoria_se_omite_sin_avisos(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = pathlib.Path(tmp)
            repo = repo_de_prueba(base)
            res = generar.generar_vault(repo, base / "vault", opciones={"memoria": str(base / "no-existe")})
            self.assertEqual(res.avisos, [])
            self.assertNotIn("memoria", res.conteo)
            self.assertFalse((base / "vault" / "MOC" / "MOC Memoria.md").exists())


class InterfazDeModulosTest(unittest.TestCase):
    def test_un_modulo_nuevo_se_integra_y_uno_roto_solo_avisa(self):
        def bueno(registro, repo):
            registro.moc("moc-mundo", "Mundo", "Entidades del mundo.", orden=60)
            registro.nueva("min-carbon", "mineral", "Carbón", "mundo/minerales", arriba="moc-mundo", alias=["carbon-id"],
                           props={"zonas": [nucleo.ref("doc-00")]})

        def roto(registro, repo):
            raise RuntimeError("datos incompletos")

        with tempfile.TemporaryDirectory() as tmp:
            base = pathlib.Path(tmp)
            repo = repo_de_prueba(base)
            modulos = ["documentos", "tareas", "equipo", types.SimpleNamespace(generar=bueno, __name__="bueno"), types.SimpleNamespace(generar=roto, __name__="roto")]
            res = generar.generar_vault(repo, base / "vault", modulos=modulos)
            self.assertEqual(len(res.avisos), 1)
            self.assertIn("datos incompletos", res.avisos[0])
            vault = base / "vault"
            self.assertIn("[[Carbón]]", (vault / "MOC" / "MOC Mundo.md").read_text(encoding="utf-8"))
            self.assertIn("[[MOC Mundo]]", (vault / "00 Inicio.md").read_text(encoding="utf-8"))
            self.assertTrue((vault / "generado" / "mundo" / "minerales" / "Carbón.md").is_file())


class RepoRealTest(unittest.TestCase):
    """Una pasada completa sobre el repo real, en un directorio temporal."""

    def test_vault_del_repo_sin_avisos_ni_huerfanos(self):
        with tempfile.TemporaryDirectory() as tmp:
            destino = pathlib.Path(tmp) / "vault"
            res = generar.generar_vault(ROOT, destino, opciones={"memoria": str(pathlib.Path(tmp) / "sin-memoria")})
            self.assertEqual(res.avisos, [])
            roadmap = json.loads((ROOT / "studio" / "data" / "roadmap.json").read_text(encoding="utf-8"))
            tareas = sum(len(m["tasks"]) for p in roadmap["phases"] for m in p["milestones"])
            self.assertEqual(res.conteo["tarea"], tareas)
            self.assertEqual(res.conteo["documento"], len(list((ROOT / "studio" / "docs").glob("[0-9][0-9]-*.md"))))
            self.assertEqual(res.conteo["rol"], 21)
            self.assertEqual(res.conteo["etapa"], 7)
            self.assertLess(res.segundos, 30)
            comprobar_vault(self, destino)


if __name__ == "__main__":
    unittest.main()
