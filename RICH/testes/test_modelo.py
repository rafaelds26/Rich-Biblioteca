import unittest
import numpy as np

from rich.modelo import richards_normalizada, ajustar_richards


class TestModeloRichards(unittest.TestCase):

    def test_valores_entre_zero_e_um(self):
        t = np.linspace(-5, 5, 30)

        y = richards_normalizada(
            t,
            q=1.0,
            beta=1.0,
            m=0.0,
            nu=1.0
        )

        self.assertTrue(np.all(np.isfinite(y)))
        self.assertTrue(np.all(y >= 0))
        self.assertTrue(np.all(y <= 1))

    def test_ajuste_produz_curva_proxima_dos_dados(self):
        t = np.linspace(-5, 5, 100)

        parametros_originais = (1.2, 0.8, 0.5, 1.1)

        y = richards_normalizada(t, *parametros_originais)

        parametros_estimados, _ = ajustar_richards(
            t,
            y,
            p0=(1.0, 0.7, 0.0, 1.0)
        )

        y_estimado = richards_normalizada(
            t,
            *parametros_estimados
        )

        np.testing.assert_allclose(
            y_estimado,
            y,
            atol=1e-5,
            rtol=1e-5
        )

    def test_recupera_parametros_originais(self):
        t = np.linspace(-5, 5, 100)

        parametros_originais = np.array(
            [1.2, 0.8, 0.5, 1.1]
        )

        y = richards_normalizada(
            t,
            *parametros_originais
        )

        parametros_estimados, _ = ajustar_richards(
            t,
            y,
            p0=(1.0, 0.7, 0.0, 1.0)
        )

        np.testing.assert_allclose(
            parametros_estimados,
            parametros_originais,
            atol=1e-3,
            rtol=1e-3
        )

    def test_rejeita_q_zero(self):
        with self.assertRaises(ValueError):
            richards_normalizada([0, 1], 0, 1, 0, 1)

    def test_rejeita_q_negativo(self):
        with self.assertRaises(ValueError):
            richards_normalizada([0, 1], -1, 1, 0, 1)

    def test_rejeita_nu_zero(self):
        with self.assertRaises(ValueError):
            richards_normalizada([0, 1], 1, 1, 0, 0)

    def test_rejeita_nu_negativo(self):
        with self.assertRaises(ValueError):
            richards_normalizada([0, 1], 1, 1, 0, -1)

    def test_ajuste_rejeita_vetores_com_tamanhos_diferentes(self):
        with self.assertRaises(ValueError):
            ajustar_richards(
                t=[0, 1, 2, 3],
                y=[0.1, 0.2, 0.3]
            )

    def test_ajuste_rejeita_dados_nao_finitos(self):
        with self.assertRaises(ValueError):
            ajustar_richards(
                t=[0, 1, 2, np.nan],
                y=[0.1, 0.2, 0.3, 0.4]
            )


if __name__ == "__main__":
    unittest.main()