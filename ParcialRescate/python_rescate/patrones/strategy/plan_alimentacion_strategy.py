"""Estrategia para definir el plan de alimentacion de un animal."""

from __future__ import annotations

from abc import ABC, abstractmethod

from ...entidades.animales.animal import Animal


class PlanAlimentacionStrategy(ABC):
    """Define el contrato para calcular raciones de alimento por animal."""

    @abstractmethod
    def calcular_racion(self, animal: Animal) -> int:
        """Devuelve la cantidad de raciones a entregar a un animal."""

