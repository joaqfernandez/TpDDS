"""Factory Method para crear animales segun su especie."""

from __future__ import annotations

from typing import Callable, Dict

from ...entidades.animales.ave import Ave
from ...entidades.animales.gato import Gato
from ...entidades.animales.perro import Perro
from ...entidades.animales.reptil import Reptil
from ...entidades.animales.animal import Animal


class AnimalFactory:
    """Crea instancias concretas de animales usando un registro interno."""

    _registry: Dict[str, Callable[..., Animal]] = {
        "Perro": lambda identificador, **kwargs: Perro(
            identificador, kwargs.get("raza", "Mestizo"), kwargs.get("es_activo", False)
        ),
        "Gato": lambda identificador, **kwargs: Gato(
            identificador, kwargs.get("temperamento", "Curioso")
        ),
        "Ave": lambda identificador, **kwargs: Ave(
            identificador, kwargs.get("puede_volar", True)
        ),
        "Reptil": lambda identificador, **kwargs: Reptil(
            identificador, kwargs.get("es_venenoso", False)
        ),
    }

    @classmethod
    def crear(cls, especie: str, identificador: str, **kwargs) -> Animal:
        try:
            return cls._registry[especie](identificador, **kwargs)
        except KeyError as error:
            raise ValueError(f"No existe una fabrica para la especie {especie}") from error

    @classmethod
    def registrar(cls, especie: str, constructor: Callable[..., Animal]) -> None:
        cls._registry[especie] = constructor
