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

    def test_bloque_con_varias_tareas_en_el_titulo(self):
        with tempfile.TemporaryDirectory() as d:
            ruta = Path(d) / "sesiones.json"
            a = sesion.nueva("Vistas del hub (F0-74, F0-75)", ruta, "2026-10-26")
            self.assertEqual(sesion.titulo(a), "S-01 · Vistas del hub (F0-74, F0-75)")

    def test_tema_vacio_falla(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                sesion.nueva("   ", Path(d) / "s.json")

    def test_resumen_conserva_y_no_repite(self):
        with tempfile.TemporaryDirectory() as d:
            ruta = Path(d) / "sesiones.json"
            sesion.nueva("F0-25 Flujo", ruta, "2026-10-24")
            sesion.resumen(1, "Hizo el flujo", ["F0-25"], ["66"], ["30"], ["Menús D"], ruta)
            s = sesion.resumen(1, None, ["F0-25", "F2-41"], [], [], [], ruta)
            self.assertEqual(s["tareas"], ["F0-25", "F2-41"])
            self.assertEqual(s["resumen"], "Hizo el flujo")
            self.assertEqual(s["decisiones"], ["Menús D"])
            with self.assertRaises(ValueError):
                sesion.resumen(9, "x", ruta=ruta)

    def test_buscar_y_markdown(self):
        with tempfile.TemporaryDirectory() as d:
            ruta = Path(d) / "sesiones.json"
            sesion.nueva("A", ruta, "2026-10-24")
            sesion.nueva("B", ruta, "2026-10-25")
            sesion.resumen(2, "Storyboard | imágenes", ["F0-24"], ["70"], [], [], ruta)
            datos = sesion.cargar(ruta)
            self.assertEqual([s["n"] for s in sesion.buscar(datos, "f0-24")], [2])
            self.assertEqual([s["n"] for s in sesion.buscar(datos, "#70")], [2])
            md = sesion.markdown(datos)
            self.assertIn("| S-02 · B | 2026-10-25 | F0-24 | #70 | Storyboard / imágenes |", md)
            self.assertIn("| S-01 · A | 2026-10-24 | — | — | — |", md)

    def test_errores_claros_en_la_linea_de_comandos(self):
        self.assertEqual(sesion.ejecutar(["sesion.py", "ver", "9999"]), 1)
        self.assertEqual(sesion.ejecutar(["sesion.py", "ver", "abc"]), 1)
        self.assertEqual(sesion.ejecutar(["sesion.py", "resumen", "9999", "x"]), 1)

    def test_registro_real_es_correlativo(self):
        numeros = [s["n"] for s in sesion.cargar()["sesiones"]]
        self.assertEqual(numeros, list(range(1, len(numeros) + 1)))
        self.assertTrue(all(s["tema"].strip() for s in sesion.cargar()["sesiones"]))


if __name__ == "__main__":
    unittest.main()
