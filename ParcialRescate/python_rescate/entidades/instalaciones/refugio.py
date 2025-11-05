"""Entidad principal que agrupa las zonas del refugio."""

from typing import Dict, List

from ...constantes import AGUA_REFUGIO_INICIAL, ALIMENTO_REFUGIO_INICIAL
from .zona import Zona


class Refugio:
    """Representa la infraestructura del refugio animal."""

    def __init__(self, nombre: str, domicilio: str) -> None:
        self._nombre = nombre
        self._domicilio = domicilio
        self._zonas: Dict[str, Zona] = {}
        self._agua_disponible = AGUA_REFUGIO_INICIAL()
        self._alimento_disponible = ALIMENTO_REFUGIO_INICIAL()

    def agregar_zona(self, zona: Zona) -> None:
        if zona.get_nombre() in self._zonas:
            raise ValueError("Ya existe una zona con ese nombre")
        self._zonas[zona.get_nombre()] = zona

    def obtener_zona(self, nombre: str) -> Zona:
        try:
            return self._zonas[nombre]
        except KeyError as error:
            raise ValueError(f"La zona {nombre} no existe") from error

    def get_zonas(self) -> List[Zona]:
        return list(self._zonas.values())

    def get_agua_disponible(self) -> int:
        return self._agua_disponible

    def get_alimento_disponible(self) -> int:
        return self._alimento_disponible

    def ajustar_agua(self, delta: int) -> None:
        self._agua_disponible += delta
        if self._agua_disponible < 0:
            raise ValueError("El agua disponible no puede ser negativa")

    def ajustar_alimento(self, delta: int) -> None:
        self._alimento_disponible += delta
        if self._alimento_disponible < 0:
            raise ValueError("El alimento disponible no puede ser negativo")

    def get_nombre(self) -> str:
        return self._nombre

    def get_domicilio(self) -> str:
        return self._domicilio
