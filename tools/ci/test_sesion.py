import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import sesion  # noqa: E402


class TestSesion(unittest.TestCase):
    def test_numeracion_correlativa_y_titulo(self):
        with tempfile.TemporaryDirectory() as d:
            ruta = Path(d) / "sesiones.json"
            a = sesion.nueva("F0-25 Flujo de pantallas", ruta, "2026-10-24")
            b = sesion.nueva("F0-24   Storyboard", ruta, "2026-10-25")
            self.assertEqual((a["n"], b["n"]), (1, 2))
            self.assertEqual(sesion.titulo(b), "S-02 · F0-24 Storyboard")
            self.assertEqual(sesion.siguiente(sesion.cargar(ruta)), 3)

    def test_tema_vacio_falla(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                sesion.nueva("   ", Path(d) / "s.json")

    def test_registro_real_es_correlativo(self):
        numeros = [s["n"] for s in sesion.cargar()["sesiones"]]
        self.assertEqual(numeros, list(range(1, len(numeros) + 1)))
        self.assertTrue(all(s["tema"].strip() for s in sesion.cargar()["sesiones"]))


if __name__ == "__main__":
    unittest.main()
