"""Pruebas del verificador de commits. Ejecutar:
    python3 -m unittest discover -s tools/ci -v
"""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import check_commits as cc  # noqa: E402


class AsuntosValidos(unittest.TestCase):
    def test_formatos_correctos(self):
        for s in [
            "feat(market): F2-04 modelo de precio",
            "fix(extraction): F2-12 desgaste de la herramienta",
            "docs: F0-31 documentos de arquitectura",
            "chore(ci): F0-34 flujo de integración continua",
            "refactor(shop)!: F3-05 separa los contratos",
            "studio(roadmap): F0-30 backlog desglosado",
        ]:
            self.assertEqual(cc.check_subject(s), [], s)

    def test_merge_y_revert_se_aceptan(self):
        self.assertEqual(cc.check_subject("Merge branch 'main' into feat/x"), [])
        self.assertEqual(cc.check_subject('Revert "feat(market): algo"'), [])


class AsuntosInvalidos(unittest.TestCase):
    def test_sin_tipo(self):
        self.assertTrue(cc.check_subject("Actualiza cosas"))

    def test_tipo_desconocido(self):
        self.assertTrue(cc.check_subject("feature(market): algo"))

    def test_sin_descripcion(self):
        self.assertTrue(cc.check_subject("feat(market):"))

    def test_mayusculas_en_el_ambito(self):
        self.assertTrue(cc.check_subject("feat(Market): algo"))

    def test_termina_en_punto(self):
        self.assertTrue(any("punto" in p for p in cc.check_subject("docs: algo.")))

    def test_demasiado_largo(self):
        self.assertTrue(any("máximo" in p for p in cc.check_subject("docs: " + "x" * 120)))


class DeteccionDeTareas(unittest.TestCase):
    def test_reconoce_ids(self):
        self.assertTrue(cc.TASK_RE.search("feat(market): F2-04 algo"))
        self.assertTrue(cc.TASK_RE.search("feat(story): F4-123 algo"))
        self.assertFalse(cc.TASK_RE.search("feat(market): algo"))


if __name__ == "__main__":
    unittest.main()
