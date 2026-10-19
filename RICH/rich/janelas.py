"""Funções para criar e processar janelas deslizantes."""

import numpy as np


def janelas_deslizantes(dados, tamanho, passo=1):
    """
    Gera janelas consecutivas de um vetor ou sequência.

    Parâmetros
    ----------
    dados : sequência ou array-like
        Série que será dividida.
    tamanho : int
        Número de elementos por janela.
    passo : int
        Distância entre o início de uma janela e a próxima.

    Retorna
    -------
    list
        Lista de arrays, um para cada janela.
    """
    dados = np.asarray(dados)

    if dados.ndim != 1:
        raise ValueError("dados deve ser uma sequência unidimensional.")
    if not isinstance(tamanho, int) or tamanho <= 0:
        raise ValueError("tamanho deve ser um inteiro positivo.")
    if not isinstance(passo, int) or passo <= 0:
        raise ValueError("passo deve ser um inteiro positivo.")
    if tamanho > len(dados):
        return []

    return [
        dados[inicio:inicio + tamanho]
        for inicio in range(0, len(dados) - tamanho + 1, passo)
    ]


def aplicar_em_janelas(dados, funcao, tamanho, passo=1):
    """
    Aplica uma função a cada janela e retorna os resultados.

    A função recebida deve aceitar um array como único argumento.
    """
    janelas = janelas_deslizantes(dados, tamanho, passo)
    return [funcao(janela) for janela in janelas]
