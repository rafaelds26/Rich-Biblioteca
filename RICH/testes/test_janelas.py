import unittest
import numpy as np
from rich.janelas import janelas_deslizantes, aplicar_em_janelas


class TestJanelas(unittest.TestCase):
    def test_janelas_com_passo_um(self):
        resultado = janelas_deslizantes([1, 2, 3, 4], tamanho=3)
        self.assertEqual(len(resultado), 2)
        self.assertTrue(np.array_equal(resultado[0], [1, 2, 3]))
        self.assertTrue(np.array_equal(resultado[1], [2, 3, 4]))

    def test_aplicar_funcao_em_janelas(self):
        resultado = aplicar_em_janelas([1, 2, 3, 4], np.mean, tamanho=2)
        self.assertEqual(resultado, [1.5, 2.5, 3.5])


if __name__ == "__main__":
    unittest.main()
