"""Pruebas del cálculo de limpieza y conexiones del hub. Ejecutar:
    python3 -m unittest discover -s tools/ci -v
"""
import importlib.util
import pathlib
import unittest

BUILD = pathlib.Path(__file__).resolve().parents[2] / "studio" / "hub" / "build.py"
spec = importlib.util.spec_from_file_location("hub_build", BUILD)
hub = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hub)

TASKS = {"F0-10": "backlog", "F0-11": "done"}


def run(md, doc_id="00-prueba"):
    hub.warnings.clear()
    docs = [{"id": doc_id, "title": "t", "group": "g", "md": md, "counts": {}}]
    total = hub.analyze_docs(docs, TASKS)
    return docs[0], total


class Limpieza(unittest.TestCase):
    def test_porcentaje(self):
        doc, total = run("## A ✅\nuno ✅\ndos 🟡\ntres ❓\n")
        self.assertEqual(doc["counts"], {"ok": 2, "prop": 1, "open": 1})
        self.assertEqual(doc["clean"]["pct"], 50)
        self.assertEqual(total["pct"], 50)

    def test_sin_marcas_no_aplica(self):
        doc, _ = run("solo texto\n")
        self.assertIsNone(doc["clean"]["pct"])

    def test_el_codigo_no_cuenta(self):
        doc, _ = run("✅ uno\n```\n🟡 ❓ ejemplo\n```\nuso `🟡` en línea\n")
        self.assertEqual(doc["counts"], {"ok": 1, "prop": 0, "open": 0})

    def test_diferido_no_resta(self):
        doc, _ = run("✅ uno\n⏳ F0-10 depende del prototipo\n")
        self.assertEqual(doc["clean"]["pct"], 100)
        self.assertEqual(doc["clean"]["wait"], 1)
        self.assertEqual(doc["clean"]["problems"], [])

    def test_diferido_exige_tarea_valida(self):
        doc, _ = run("⏳ sin tarea\n⏳ F9-99 inexistente\n")
        self.assertEqual(len(doc["clean"]["problems"]), 3)  # sin tarea, inexistente y cita de tarea inexistente

    def test_diferido_de_tarea_terminada_debe_resolverse(self):
        doc, _ = run("⏳ F0-11 ya terminada\n")
        self.assertTrue(any("terminada" in p for p in doc["clean"]["problems"]))

    def test_enlace_roto_y_tarea_inexistente(self):
        doc, _ = run("[x](no-existe.md) y F0-77\n")
        problems = doc["clean"]["problems"]
        self.assertTrue(any("enlace roto" in p for p in problems))
        self.assertTrue(any("F0-77" in p for p in problems))

    def test_enlace_valido(self):
        doc, _ = run("[visión](00-vision.md)\n")
        self.assertEqual(doc["clean"]["problems"], [])


if __name__ == "__main__":
    unittest.main()
