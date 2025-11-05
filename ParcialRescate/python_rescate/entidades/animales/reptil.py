"""Entidad concreta para reptiles rescatados."""

from .animal import Animal
from ...constantes import AGUA_REPTIL, ESPACIO_REPTIL


class Reptil(Animal):
    """Representa un reptil dentro del refugio."""

    def __init__(self, identificador: str, es_venenoso: bool) -> None:
        super().__init__("Reptil", identificador, AGUA_REPTIL, ESPACIO_REPTIL)
        self._es_venenoso = es_venenoso

    def es_venenoso(self) -> bool:
        return self._es_venenoso
