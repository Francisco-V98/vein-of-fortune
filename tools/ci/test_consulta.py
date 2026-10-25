import contextlib
import io
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import consulta  # noqa: E402

MD = "# Título\n\n## A\ntexto A\n### A1\nsub\n```\n# no es encabezado\n```\n## B\ntexto B ✅\n"


def ejecutar(*argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        rc = consulta.main(list(argv))
    return rc, out.getvalue(), err.getvalue()


class TestConsulta(unittest.TestCase):
    def test_limpieza_coincide_con_el_build(self):
        docs, total = consulta.cargar_docs()
        rc, out, _ = ejecutar("limpieza", "--max", "500")
        self.assertEqual(rc, 0)
        fila = [l for l in out.splitlines() if l.startswith("TOTAL")][0].split()
        self.assertEqual([int(x) for x in fila[1:5]], [total["ok"], total["prop"], total["open"], total["wait"]])
        self.assertEqual(sum(d["counts"]["ok"] for d in docs), total["ok"])

    def test_limpieza_de_un_documento_por_prefijo(self):
        rc, out, _ = ejecutar("limpieza", "23")
        self.assertEqual(rc, 0)
        self.assertEqual(len(out.splitlines()), 2)

    def test_abiertos_coinciden_con_analyze_docs(self):
        docs, _ = consulta.cargar_docs()
        esperado = sum(len(d["clean"]["items"]) for d in docs)
        rc, out, _ = ejecutar("abiertos", "--max", "100000")
        self.assertEqual(rc, 0)
        self.assertEqual(len(out.splitlines()), esperado)
        self.assertRegex(out.splitlines()[0], r"^studio/docs/.+\.md:\d+ ")

    def test_abiertos_filtra_por_tipo(self):
        rc, out, _ = ejecutar("abiertos", "--tipo", "prop", "--max", "100000")
        self.assertEqual(rc, 0)
        self.assertTrue(all("🟡" in l for l in out.splitlines() if l.startswith("studio/")))

    def test_indice_y_seccion_ignoran_codigo(self):
        hs = consulta.encabezados(MD)
        self.assertEqual([(n, lv) for n, lv, _ in hs], [(1, 1), (3, 2), (5, 3), (10, 2)])
        sec = consulta.seccion_de(MD, "a")
        self.assertEqual(sec[0].split(None, 1)[1], "## A")
        self.assertEqual(len(sec), 7)  # líneas 3 a 9, antes de «## B»
        self.assertIn("texto B", consulta.seccion_de(MD, "B")[-1])
        with self.assertRaises(consulta.Error):
            consulta.seccion_de(MD, "inexistente")

    def test_seccion_con_documento_real(self):
        rc, out, _ = ejecutar("seccion", "23", "Reglas del árbol")
        self.assertEqual(rc, 0)
        self.assertIn("Reglas del árbol", out)

    def test_ficha_entre_10_y_20_lineas(self):
        for ref in ("23", "F0-75"):
            rc, out, _ = ejecutar("ficha", ref, "--max", "100")
            self.assertEqual(rc, 0)
            self.assertTrue(10 <= len(out.splitlines()) <= 20, (ref, len(out.splitlines())))

    def test_tarea_inexistente_da_error(self):
        rc, out, err = ejecutar("tarea", "F9-99")
        self.assertEqual((rc, out), (1, ""))
        self.assertIn("No existe la tarea", err)

    def test_tareas_con_filtros(self):
        rc, out, _ = ejecutar("tareas", "--estado", "done", "--fase", "F0", "--max", "100000")
        self.assertEqual(rc, 0)
        self.assertTrue(all(l.startswith("F0-") and "· done ·" in l for l in out.splitlines()))

    def test_mundo_ruta_valida_e_invalida(self):
        rc, out, _ = ejecutar("mundo")
        self.assertEqual(rc, 0)
        self.assertIn("economy:", out)
        rc, out, _ = ejecutar("mundo", "rules")
        self.assertEqual(rc, 0)
        rc, out, err = ejecutar("mundo", "rules.noexiste")
        self.assertEqual((rc, out), (1, ""))
        self.assertIn("Claves vecinas", err)

    def test_sin_argumentos_muestra_ayuda(self):
        rc, out, _ = ejecutar()
        self.assertEqual(rc, 0)
        self.assertIn("consulta.py limpieza", out)

    def test_documento_inexistente(self):
        rc, _, err = ejecutar("indice", "99")
        self.assertEqual(rc, 1)
        self.assertIn("No existe el documento", err)


class TestRobustez(unittest.TestCase):
    def test_seccion_vacia_falla(self):
        with self.assertRaises(consulta.Error):
            consulta.seccion_de("# A\ntexto", "  ")

    def test_max_invalido(self):
        rc, _, err = ejecutar("--max", "0", "limpieza")
        self.assertEqual(rc, 1)
        self.assertIn("--max", err)

    def test_prefijo_numerico_no_ambiguo(self):
        docs, _ = consulta.cargar_docs()
        self.assertTrue(consulta.buscar_doc(docs, "2")["id"].startswith("02-"))


if __name__ == "__main__":
    unittest.main()
