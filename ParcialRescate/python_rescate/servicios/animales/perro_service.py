"""Servicio especializado para perros."""

from ...entidades.animales.perro import Perro
from ...patrones.strategy.plan_perro_activo_strategy import PlanPerroActivoStrategy
from ...patrones.strategy.plan_perro_tranquilo_strategy import PlanPerroTranquiloStrategy
from .animal_service import AnimalService


class PerroService(AnimalService):
    """Selecciona dinamicamente la estrategia segun el nivel de actividad."""

    def __init__(self) -> None:
        super().__init__(PlanPerroTranquiloStrategy())
        self._estrategia_activo = PlanPerroActivoStrategy()

    def alimentar(self, animal: Perro, zona_service):  # type: ignore[override]
        estrategia = self._estrategia_activo if animal.es_activo() else self._estrategia
        self._estrategia = estrategia
        return super().alimentar(animal, zona_service)
