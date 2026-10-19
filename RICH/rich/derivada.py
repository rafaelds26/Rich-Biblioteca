"""Primeira derivada da curva de Richards e ajuste aos dados de derivada."""

import numpy as np
from scipy.optimize import curve_fit
from .modelo import richards_normalizada


def derivada_richards(t, q, beta, m, nu):
    """
    Calcula a primeira derivada analítica da curva de Richards.

    Para R(t) = (1 + q exp(-beta(t-m)))^(-1/nu), temos:
    R'(t) = (beta*q/nu) * exp(-beta(t-m))
            * (1 + q*exp(-beta(t-m)))^(-1/nu - 1)

    A derivada depende dos mesmos parâmetros (q, beta, m, nu).
    """
    t = np.asarray(t, dtype=float)

    if q <= 0:
        raise ValueError("O parâmetro q deve ser maior que zero.")
    if nu <= 0:
        raise ValueError("O parâmetro nu deve ser maior que zero.")

    expoente = np.clip(-beta * (t - m), -700, 700)
    e = np.exp(expoente)
    base = 1.0 + q * e
    return (beta * q / nu) * e * base ** (-1.0 / nu - 1.0)


def ajustar_derivada_richards(t, y_derivada, p0=None, bounds=None, maxfev=20000):
    """
    Ajusta a curva da primeira derivada aos valores observados.

    Retorna (parametros, covariancia), com parâmetros na ordem
    (q, beta, m, nu).
    """
    t = np.asarray(t, dtype=float)
    y_derivada = np.asarray(y_derivada, dtype=float)

    if t.ndim != 1 or y_derivada.ndim != 1:
        raise ValueError("t e y_derivada devem ser vetores unidimensionais.")
    if len(t) != len(y_derivada):
        raise ValueError("t e y_derivada devem ter o mesmo número de elementos.")
    if len(t) < 4:
        raise ValueError("São necessários pelo menos 4 pontos para ajustar 4 parâmetros.")
    if not np.all(np.isfinite(t)) or not np.all(np.isfinite(y_derivada)):
        raise ValueError("Os dados não podem conter NaN ou infinito.")

    if p0 is None:
        p0 = (1.0, 1.0, float(np.median(t)), 1.0)
    if bounds is None:
        bounds = ([1e-8, -np.inf, -np.inf, 1e-8],
                  [np.inf, np.inf, np.inf, np.inf])

    parametros, covariancia = curve_fit(
        derivada_richards,
        t,
        y_derivada,
        p0=p0,
        bounds=bounds,
        maxfev=maxfev,
    )
    return parametros, covariancia
