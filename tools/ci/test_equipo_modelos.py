"""Pruebas de la política de modelos del equipo: validación en el build y sincronizador de agentes. Ejecutar:
    python3 -m unittest discover -s tools/ci -p "test_equipo*.py" -v
Usan fixtures en una carpeta temporal: no tocan .claude/agents ni equipo.json reales.
"""
import contextlib
import importlib.util
import io
import json
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]


def load_module(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


hub = load_module("hub_build_equipo", "studio/hub/build.py")
sync = load_module("sincronizar_agentes_test", "tools/equipo/sincronizar_agentes.py")

POLITICA = {"modelos": ["haiku", "sonnet", "opus", "fable"],
            "esfuerzos": ["low", "medium", "high", "xhigh", "max"], "fable_requiere_autorizacion": True}
AGENTE = """---
name: demo
description: Agente de prueba.
tools: Read, Grep
model: haiku
---

Eres el agente de prueba.

## Decidir ahora o aplazar

%s

Texto propio del rol.
""" % sync._BASE


def equipo(modelo="sonnet", esfuerzo="high", politica=True):
    data = {"roles": [{"id": "demo", "agente": "demo", "modelo": modelo, "esfuerzo": esfuerzo},
                      {"id": "autor", "agente": None}]}
    if politica:
        data["politica_modelos"] = POLITICA
    return data


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tmp.name)
        (self.root / "studio/data").mkdir(parents=True)
        (self.root / ".claude/agents").mkdir(parents=True)
        self.md = self.root / ".claude/agents/demo.md"
        self.md.write_text(AGENTE, encoding="utf-8")
        self.addCleanup(self.tmp.cleanup)

    def escribir_equipo(self, **kw):
        (self.root / "studio/data/equipo.json").write_text(json.dumps(equipo(**kw)), encoding="utf-8")

    def sincronizar(self, *extra):
        with contextlib.redirect_stdout(io.StringIO()):
            return sync.main(["--raiz", str(self.root)] + list(extra))

    def avisos(self, data):
        hub.warnings.clear()
        with contextlib.redirect_stdout(io.StringIO()):
            hub.check_modelos_equipo(data, self.root / ".claude/agents")
        return list(hub.warnings)


class SincronizadorTests(Base):
    def test_sincroniza_frontmatter_y_bloque(self):
        self.escribir_equipo()
        self.assertEqual(self.sincronizar(), 0)
        texto = self.md.read_text(encoding="utf-8")
        front, _ = sync.partir_frontmatter(texto)
        self.assertEqual(sync.valor_front(front, "model"), "sonnet")
        self.assertEqual(sync.valor_front(front, "effort"), "high")
        self.assertEqual(sync.valor_front(front, "tools"), "Read, Grep")
        self.assertIn(sync.BLOQUE_MARCADO, texto)
        self.assertNotIn("Decidir ahora o aplazar", texto)
        self.assertIn("Texto propio del rol.", texto)

    def test_idempotente(self):
        self.escribir_equipo()
        self.sincronizar()
        primero = self.md.read_text(encoding="utf-8")
        self.sincronizar()
        self.assertEqual(self.md.read_text(encoding="utf-8"), primero)
        self.assertEqual(self.sincronizar("--comprobar"), 0)

    def test_comprobar_no_escribe_y_falla(self):
        self.escribir_equipo()
        self.assertEqual(self.sincronizar("--comprobar"), 1)
        self.assertEqual(self.md.read_text(encoding="utf-8"), AGENTE)

    def test_actualiza_un_bloque_existente(self):
        self.escribir_equipo()
        self.sincronizar()
        viejo = self.md.read_text(encoding="utf-8").replace("Lee lo mínimo", "Texto viejo")
        self.md.write_text(viejo, encoding="utf-8")
        self.assertEqual(self.sincronizar("--comprobar"), 1)
        self.sincronizar()
        self.assertEqual(self.sincronizar("--comprobar"), 0)


class ValidacionBuildTests(Base):
    def sincronizado(self):
        self.escribir_equipo()
        self.sincronizar()

    def test_caso_bueno(self):
        self.sincronizado()
        self.assertEqual(self.avisos(equipo()), [])

    def test_modelo_invalido(self):
        self.sincronizado()
        self.assertTrue(any("modelo inválido" in a for a in self.avisos(equipo(modelo="gpt"))))

    def test_esfuerzo_invalido(self):
        self.sincronizado()
        self.assertTrue(any("esfuerzo inválido" in a for a in self.avisos(equipo(esfuerzo="ultra"))))

    def test_falta_politica(self):
        self.sincronizado()
        self.assertTrue(any("politica_modelos" in a for a in self.avisos(equipo(politica=False))))

    def test_frontmatter_desincronizado(self):
        self.sincronizado()
        avisos = self.avisos(equipo(modelo="opus", esfuerzo="max"))
        self.assertTrue(any("model es sonnet" in a for a in avisos))
        self.assertTrue(any("effort es high" in a for a in avisos))

    def test_bloque_comun_ausente(self):
        self.sincronizado()
        self.md.write_text(self.md.read_text(encoding="utf-8").replace(sync.INICIO, ""), encoding="utf-8")
        self.assertTrue(any("bloque común" in a for a in self.avisos(equipo())))

    def test_datos_reales_sincronizados(self):
        hub.warnings.clear()
        with contextlib.redirect_stdout(io.StringIO()):
            hub.check_modelos_equipo(json.loads((ROOT / "studio/data/equipo.json").read_text(encoding="utf-8")),
                                     ROOT / ".claude/agents")
        self.assertEqual(list(hub.warnings), [])


if __name__ == "__main__":
    unittest.main()
