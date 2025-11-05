"""Servicio especializado para reptiles."""

from ...constantes import ALIMENTO_REPTIL
from ...patrones.strategy.plan_generico_strategy import PlanGenericoStrategy
from .animal_service import AnimalService


class ReptilService(AnimalService):
    """Aplica la estrategia generica para reptiles."""

    def __init__(self) -> None:
        super().__init__(PlanGenericoStrategy(ALIMENTO_REPTIL))
