"""Entidades base para animales alojados en el refugio."""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import List


@dataclass
class SeguimientoMedico:
    """Registro basico de controles veterinarios."""

    descripcion: str
    responsable: str


class Animal(ABC):
    """Modelo abstracto para cualquier animal que ingresa al refugio."""

    def __init__(self, especie: str, identificador: str, agua: int, espacio: float) -> None:
        if agua <= 0:
            raise ValueError("El agua inicial debe ser positiva")
        if espacio <= 0:
            raise ValueError("El espacio requerido debe ser positivo")

        self._especie = especie
        self._identificador = identificador
        self._agua = agua
        self._espacio = espacio
        self._salud = 100
        self._historial_medico: List[SeguimientoMedico] = []

    def registrar_control(self, descripcion: str, responsable: str) -> None:
        """Guarda un seguimiento medico en el historial del animal."""

        self._historial_medico.append(SeguimientoMedico(descripcion, responsable))

    def consumir_agua(self, litros: int) -> None:
        """Reduce la reserva de agua disponible para el animal."""

        if litros < 0:
            raise ValueError("El consumo de agua no puede ser negativo")
        self._agua = max(0, self._agua - litros)

    def recibir_agua(self, litros: int) -> None:
        """Incrementa la reserva de agua disponible."""

        if litros <= 0:
            raise ValueError("Los litros deben ser positivos")
        self._agua += litros

    def actualizar_salud(self, delta: int) -> None:
        """Modifica la salud del animal respetando los limites aceptados."""

        nueva_salud = min(100, max(0, self._salud + delta))
        self._salud = nueva_salud

    # Getters basicos
    def get_especie(self) -> str:
        return self._especie

    def get_identificador(self) -> str:
        return self._identificador

    def get_agua(self) -> int:
        return self._agua

    def get_espacio(self) -> float:
        return self._espacio

    def get_salud(self) -> int:
        return self._salud

    def get_historial_medico(self) -> List[SeguimientoMedico]:
        return list(self._historial_medico)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(id={self._identificador}, especie={self._especie}, "
            f"agua={self._agua}, espacio={self._espacio}, salud={self._salud})"
        )
