"""Estrategia generica configurable para alimentacion."""

from ...entidades.animales.animal import Animal
from .plan_alimentacion_strategy import PlanAlimentacionStrategy


class PlanGenericoStrategy(PlanAlimentacionStrategy):
    """Calcula raciones utilizando un valor fijo configurado."""

    def __init__(self, racion: int) -> None:
        if racion <= 0:
            raise ValueError("La racion debe ser positiva")
        self._racion = racion

    def calcular_racion(self, animal: Animal) -> int:
        return self._racion
