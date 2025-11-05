"""Entidad concreta para perros rescatados."""

from .animal import Animal
from ...constantes import AGUA_PERRO, ESPACIO_PERRO


class Perro(Animal):
    """Representa un perro dentro del refugio."""

    def __init__(self, identificador: str, raza: str, es_activo: bool) -> None:
        super().__init__("Perro", identificador, AGUA_PERRO, ESPACIO_PERRO)
        self._raza = raza
        self._es_activo = es_activo

    def get_raza(self) -> str:
        return self._raza

    def es_activo(self) -> bool:
        return self._es_activo
