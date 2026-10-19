"""Biblioteca para modelagem com a curva de Richards."""

from .modelo import richards_normalizada, ajustar_richards
from .derivada import derivada_richards, ajustar_derivada_richards
from .janelas import janelas_deslizantes, aplicar_em_janelas

__all__ = [
    "richards_normalizada",
    "ajustar_richards",
    "derivada_richards",
    "ajustar_derivada_richards",
    "janelas_deslizantes",
    "aplicar_em_janelas",
]
