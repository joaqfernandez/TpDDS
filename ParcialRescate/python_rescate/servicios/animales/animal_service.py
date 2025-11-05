"""Servicios comunes para el manejo de animales."""

from __future__ import annotations

from ..instalaciones.zona_service import ZonaService
from ...entidades.animales.animal import Animal
from ...patrones.strategy.plan_alimentacion_strategy import PlanAlimentacionStrategy


class AnimalService:
    """Servicio base que utiliza estrategias de alimentacion."""

    def __init__(self, estrategia: PlanAlimentacionStrategy) -> None:
        self._estrategia = estrategia

    def alimentar(self, animal: Animal, zona_service: ZonaService) -> int:
        racion = self._estrategia.calcular_racion(animal)
        zona_service.consumir_recurso("alimento", racion)
        return racion

    def hidratar(self, animal: Animal, zona_service: ZonaService) -> int:
        zona_service.consumir_recurso("agua", 1)
        animal.recibir_agua(1)
        return 1
