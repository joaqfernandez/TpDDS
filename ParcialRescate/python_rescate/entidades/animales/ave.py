"""Entidad concreta para aves rescatadas."""

from .animal import Animal
from ...constantes import AGUA_AVE, ESPACIO_AVE


class Ave(Animal):
    """Representa un ave dentro del refugio."""

    def __init__(self, identificador: str, puede_volar: bool) -> None:
        super().__init__("Ave", identificador, AGUA_AVE, ESPACIO_AVE)
        self._puede_volar = puede_volar

    def puede_volar(self) -> bool:
        return self._puede_volar
