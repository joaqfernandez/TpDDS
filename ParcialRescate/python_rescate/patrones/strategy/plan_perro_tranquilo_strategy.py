"""Estrategia de alimentacion para perros tranquilos."""

from ...constantes import ALIMENTO_PERRO_TRANQUILO
from ...entidades.animales.animal import Animal
from .plan_alimentacion_strategy import PlanAlimentacionStrategy


class PlanPerroTranquiloStrategy(PlanAlimentacionStrategy):
    """Entrega una racion reducida para perros con baja actividad."""

    def calcular_racion(self, animal: Animal) -> int:
        return ALIMENTO_PERRO_TRANQUILO
