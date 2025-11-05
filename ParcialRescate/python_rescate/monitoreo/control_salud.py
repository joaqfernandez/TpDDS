"""Control centralizado que reacciona a los sensores del refugio."""

from __future__ import annotations

from typing import Protocol

from ..constantes import OCUPACION_MAXIMA
from ..patrones.observer.observable import Observer


class AccionCorrectiva(Protocol):
    """Interfaz para ejecutar acciones correctivas."""

    def ejecutar(self, mensaje: str) -> None:
        """Ejecuta la accion con el mensaje indicado."""


class ControlSalud(Observer[float]):
    """Observador que registra las lecturas de salud."""

    def __init__(self, accion_correctiva: AccionCorrectiva) -> None:
        self._accion_correctiva = accion_correctiva

    def update(self, value: float) -> None:
        if value < 60:
            self._accion_correctiva.ejecutar(
                f"[ALERTA] Salud promedio baja detectada: {value:.2f}"
            )


class ControlOcupacion(Observer[float]):
    """Observador que supervisa el nivel de ocupacion."""

    def __init__(self, accion_correctiva: AccionCorrectiva) -> None:
        self._accion_correctiva = accion_correctiva

    def update(self, value: float) -> None:
        if value > OCUPACION_MAXIMA * 0.8:
            self._accion_correctiva.ejecutar(
                f"[ALERTA] Ocupacion al {value * 100:.0f}%: reorganizar zonas"
            )
