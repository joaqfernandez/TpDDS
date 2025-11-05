"""Servicio especializado para gatos."""

from ...constantes import ALIMENTO_GATO
from ...patrones.strategy.plan_generico_strategy import PlanGenericoStrategy
from .animal_service import AnimalService


class GatoService(AnimalService):
    """Utiliza una estrategia generica preconfigurada."""

    def __init__(self) -> None:
        super().__init__(PlanGenericoStrategy(ALIMENTO_GATO))
