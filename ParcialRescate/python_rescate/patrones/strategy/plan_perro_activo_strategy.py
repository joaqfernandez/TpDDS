"""Estrategia de alimentacion para perros activos."""

from ...constantes import ALIMENTO_PERRO_ACTIVO
from ...entidades.animales.animal import Animal
from .plan_alimentacion_strategy import PlanAlimentacionStrategy


class PlanPerroActivoStrategy(PlanAlimentacionStrategy):
    """Entrega una mayor racion para perros con alto gasto energetico."""

    def calcular_racion(self, animal: Animal) -> int:
        return ALIMENTO_PERRO_ACTIVO
