"""Sensores simulados para monitorear el refugio."""

from __future__ import annotations

import random
import threading
import time
from typing import Callable, Optional

from ..constantes import (
    INTERVALO_SENSOR_OCUPACION,
    INTERVALO_SENSOR_SALUD,
    OCUPACION_MAXIMA,
    SALUD_MAXIMA,
    SALUD_MINIMA,
)
from ..patrones.observer.observable import Observable


class SensorBase(Observable[float]):
    """Sensor generico que publica lecturas periodicas en un hilo aparte."""

    def __init__(self, intervalo: Callable[[], float]) -> None:
        super().__init__()
        self._intervalo = intervalo
        self._activo = False
        self._thread: Optional[threading.Thread] = None

    def iniciar(self) -> None:
        if self._activo:
            return
        self._activo = True
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def detener(self) -> None:
        self._activo = False
        if self._thread:
            self._thread.join(timeout=0.1)

    def _loop(self) -> None:
        while self._activo:
            lectura = self._leer()
            self.notify(lectura)
            time.sleep(self._intervalo())

    def _leer(self) -> float:
        raise NotImplementedError


class SensorSalud(SensorBase):
    """Genera lecturas aleatorias de salud promedio."""

    def __init__(self) -> None:
        super().__init__(INTERVALO_SENSOR_SALUD)

    def _leer(self) -> float:
        return random.uniform(SALUD_MINIMA, SALUD_MAXIMA)


class SensorOcupacion(SensorBase):
    """Simula la ocupacion relativa de las instalaciones."""

    def __init__(self) -> None:
        super().__init__(INTERVALO_SENSOR_OCUPACION)

    def _leer(self) -> float:
        return random.uniform(0.0, OCUPACION_MAXIMA)
