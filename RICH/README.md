# Biblioteca RICH — Modelo de Richards

Biblioteca Python inicial para:
1. calcular a curva de Richards normalizada;
2. calcular sua primeira derivada analítica;
3. ajustar parâmetros da curva e da derivada aos dados;
4. dividir séries em janelas deslizantes e aplicar funções a cada janela.

## Fórmula implementada

A versão inicial utiliza:

`R(t) = (1 + q * exp(-beta * (t - m))) ** (-1 / nu)`

Parâmetros, nesta ordem: `q`, `beta`, `m`, `nu`.

A fórmula deve ser conferida com a equação definida pelo professor/artigo de referência antes de ser considerada a versão final do projeto.

## Instalação em ambiente de desenvolvimento

Na raiz do projeto, com o ambiente virtual ativado:

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Exemplo

```python
import numpy as np
from rich import richards_normalizada, derivada_richards, janelas_deslizantes

t = np.linspace(0, 10, 50)
parametros = (1.0, 0.8, 5.0, 1.0)

y = richards_normalizada(t, *parametros)
dy = derivada_richards(t, *parametros)
janelas = janelas_deslizantes(y, tamanho=10, passo=5)
```

## Executar os testes

Na raiz do projeto:

```bash
python -m unittest discover -s testes -v
```

## Observação sobre os ajustes

`ajustar_richards(t, y)` e `ajustar_derivada_richards(t, y_derivada)` usam
`scipy.optimize.curve_fit`. O ajuste depende da qualidade dos dados e dos
chutes iniciais dos parâmetros; para séries financeiras reais, os parâmetros
e o pré-processamento precisam ser avaliados cuidadosamente.
