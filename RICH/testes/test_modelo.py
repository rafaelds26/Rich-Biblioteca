import unittest
import numpy as np
from rich.modelo import richards_normalizada, ajustar_richards


class TestModeloRichards(unittest.TestCase):
    def test_valores_entre_zero_e_um(self):
        t = np.linspace(-5, 5, 30)
        y = richards_normalizada(t, 1.0, 1.0, 0.0, 1.0)
        self.assertTrue(np.all(y >= 0))
        self.assertTrue(np.all(y <= 1))

    def test_ajuste_recupera_parametros_aproximados(self):
        t = np.linspace(-5, 5, 100)
        esperado = (1.2, 0.8, 0.5, 1.1)
        y = richards_normalizada(t, *esperado)
        parametros, _ = ajustar_richards(t, y, p0=(1.0, 0.7, 0.0, 1.0))
        y_estimado = richards_normalizada(t, *parametros)
        self.assertTrue(np.allclose(y, y_estimado, atol=1e-5))

    def test_rejeita_nu_invalido(self):
        with self.assertRaises(ValueError):
            richards_normalizada([0, 1], 1, 1, 0, 0)


if __name__ == "__main__":
    unittest.main()
