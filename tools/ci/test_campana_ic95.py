"""ic95 con valores infinitos (F0-96): Python 3.11 lanzaba AttributeError en statistics.pstdev."""
import math
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))

from sim import campana  # noqa: E402

S = {"estadistica": {"z95": 1.96}}


class TestIc95(unittest.TestCase):
    def test_valor_infinito_no_lanza_error(self):
        ic = campana.ic95([1.0, 2.0, float("inf")], S)
        self.assertEqual(ic[0], ic[1])
        self.assertTrue(math.isinf(ic[0]))

    def test_valores_finitos_igual_que_antes(self):
        ic = campana.ic95([1.0, 2.0, 3.0], S)
        self.assertLess(ic[0], 2.0)
        self.assertGreater(ic[1], 2.0)


if __name__ == "__main__":
    unittest.main()
