"""Entidad concreta para gatos rescatados."""

from .animal import Animal
from ...constantes import AGUA_GATO, ESPACIO_GATO


class Gato(Animal):
    """Representa un gato dentro del refugio."""

    def __init__(self, identificador: str, temperamento: str) -> None:
        super().__init__("Gato", identificador, AGUA_GATO, ESPACIO_GATO)
        self._temperamento = temperamento

    def get_temperamento(self) -> str:
        return self._temperamento
