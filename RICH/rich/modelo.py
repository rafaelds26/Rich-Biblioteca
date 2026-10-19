"""Modelo normalizado de Richards e ajuste de parâmetros."""

import numpy as np
from scipy.optimize import curve_fit


def richards_normalizada(t, q, beta, m, nu):
    """
    Calcula a curva de Richards normalizada.

    Fórmula adotada:
        R(t) = (1 + q * exp(-beta * (t - m))) ** (-1 / nu)

    Parâmetros
    ----------
    t : array-like
        Instantes ou posições temporais.
    q : float
        Parâmetro de deslocamento/forma, deve ser positivo.
    beta : float
        Parâmetro associado à taxa de crescimento.
    m : float
        Parâmetro de deslocamento no eixo do tempo.
    nu : float
        Parâmetro de forma, deve ser positivo.

    Retorna
    -------
    numpy.ndarray ou numpy.float64
        Valores da curva. Para q > 0 e nu > 0, os valores ficam entre
        0 e 1, salvo pequenos efeitos numéricos.
    """
    t = np.asarray(t, dtype=float)

    if q <= 0:
        raise ValueError("O parâmetro q deve ser maior que zero.")
    if nu <= 0:
        raise ValueError("O parâmetro nu deve ser maior que zero.")

    expoente = np.clip(-beta * (t - m), -700, 700)
    return (1.0 + q * np.exp(expoente)) ** (-1.0 / nu)


def ajustar_richards(t, y, p0=None, bounds=None, maxfev=20000):
    """
    Ajusta os parâmetros da curva de Richards aos dados observados.

    Retorna (parametros, covariancia), como scipy.optimize.curve_fit.
    A ordem dos parâmetros é (q, beta, m, nu).
    """
    t = np.asarray(t, dtype=float)
    y = np.asarray(y, dtype=float)

    if t.ndim != 1 or y.ndim != 1:
        raise ValueError("t e y devem ser vetores unidimensionais.")
    if len(t) != len(y):
        raise ValueError("t e y devem ter o mesmo número de elementos.")
    if len(t) < 4:
        raise ValueError("São necessários pelo menos 4 pontos para ajustar 4 parâmetros.")
    if not np.all(np.isfinite(t)) or not np.all(np.isfinite(y)):
        raise ValueError("t e y não podem conter NaN ou infinito.")

    if p0 is None:
        p0 = (1.0, 1.0, float(np.median(t)), 1.0)
    if bounds is None:
        bounds = ([1e-8, -np.inf, -np.inf, 1e-8],
                  [np.inf, np.inf, np.inf, np.inf])

    parametros, covariancia = curve_fit(
        richards_normalizada,
        t,
        y,
        p0=p0,
        bounds=bounds,
        maxfev=maxfev,
    )
    return parametros, covariancia
