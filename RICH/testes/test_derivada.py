import unittest
import numpy as np
from rich.derivada import derivada_richards
from rich.modelo import richards_normalizada


class TestDerivadaRichards(unittest.TestCase):
    def test_derivada_confere_com_diferenca_numerica(self):
        t = np.linspace(-2, 2, 1000)
        parametros = (1.1, 0.7, 0.2, 1.3)
        y = richards_normalizada(t, *parametros)
        numerica = np.gradient(y, t)
        analitica = derivada_richards(t, *parametros)
        self.assertTrue(np.allclose(analitica[2:-2], numerica[2:-2], atol=2e-4))


if __name__ == "__main__":
    unittest.main()
