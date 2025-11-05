"""Registro centralizado de servicios por tipo de animal."""

from __future__ import annotations

from typing import Dict, Type

from ...entidades.animales.animal import Animal
from ...entidades.animales.ave import Ave
from ...entidades.animales.gato import Gato
from ...entidades.animales.perro import Perro
from ...entidades.animales.reptil import Reptil
from .animal_service import AnimalService
from .ave_service import AveService
from .gato_service import GatoService
from .perro_service import PerroService
from .reptil_service import ReptilService


class AnimalServiceRegistry:
    """Resuelve dinamicamente el servicio apropiado para cada animal."""

    def __init__(self) -> None:
        self._servicios: Dict[Type[Animal], AnimalService] = {
            Perro: PerroService(),
            Gato: GatoService(),
            Ave: AveService(),
            Reptil: ReptilService(),
        }

    def obtener_servicio(self, animal: Animal) -> AnimalService:
        for tipo, servicio in self._servicios.items():
            if isinstance(animal, tipo):
                return servicio
        raise ValueError(f"No hay servicio registrado para {type(animal).__name__}")
