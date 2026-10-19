"""Exemplo simples de utilização da biblioteca RICH."""

import numpy as np
from rich import (
    richards_normalizada,
    derivada_richards,
    janelas_deslizantes,
)

# Criamos instantes igualmente espaçados.
tempo = np.linspace(0, 10, 11)

# Parâmetros de exemplo: q, beta, m e nu.
parametros = (1.0, 1.5, 5.0, 1.0)

print("Parâmetros utilizados:", parametros)

curva = richards_normalizada(tempo, *parametros)
derivada = derivada_richards(tempo, *parametros)

print("Tempo:", tempo)
print("Curva de Richards:", np.round(curva, 4))
print("Primeira derivada:", np.round(derivada, 4))

# Exemplo de janelas com 4 valores e avanço de 2 posições.
for numero, janela in enumerate(janelas_deslizantes(curva, tamanho=4, passo=2), start=1):
    print(f"Janela {numero}:", np.round(janela, 4))
