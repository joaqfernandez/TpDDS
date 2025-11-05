"""Servicio especializado para aves."""

from ...constantes import ALIMENTO_AVE
from ...patrones.strategy.plan_generico_strategy import PlanGenericoStrategy
from .animal_service import AnimalService


class AveService(AnimalService):
    """Implementa la logica especifica para aves."""

    def __init__(self) -> None:
        super().__init__(PlanGenericoStrategy(ALIMENTO_AVE))
