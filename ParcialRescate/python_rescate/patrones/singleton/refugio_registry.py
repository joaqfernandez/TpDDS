"""Singleton que mantiene un registro global de refugios."""

from __future__ import annotations

from threading import Lock
from typing import Dict

from ...entidades.instalaciones.refugio import Refugio


class RefugioRegistry:
    """Permite registrar y recuperar refugios desde cualquier parte del sistema."""

    _instance: "RefugioRegistry | None" = None
    _lock = Lock()

    def __new__(cls) -> "RefugioRegistry":
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._refugios = {}
        return cls._instance

    def registrar(self, refugio: Refugio) -> None:
        self._refugios[refugio.get_nombre()] = refugio

    def obtener(self, nombre: str) -> Refugio:
        try:
            return self._refugios[nombre]
        except KeyError as error:
            raise ValueError(f"El refugio {nombre} no esta registrado") from error

    def listar(self) -> Dict[str, Refugio]:
        return dict(self._refugios)
