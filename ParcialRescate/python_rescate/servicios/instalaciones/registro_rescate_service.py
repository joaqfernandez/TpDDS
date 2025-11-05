"""Servicio para gestionar la persistencia de registros de rescate."""

from __future__ import annotations

import pickle
from pathlib import Path
from typing import Optional

from ...entidades.instalaciones.registro_rescate import RegistroRescate


class RegistroRescateService:
    """Permite guardar y recuperar registros de rescate desde disco."""

    def __init__(self, directorio: str = "data") -> None:
        self._directorio = Path(directorio)
        self._directorio.mkdir(parents=True, exist_ok=True)

    def guardar(self, registro: RegistroRescate) -> Path:
        ruta = self._directorio / f"{registro.identificador}.dat"
        with ruta.open("wb") as archivo:
            pickle.dump(registro, archivo)
        return ruta

    def cargar(self, identificador: str) -> Optional[RegistroRescate]:
        ruta = self._directorio / f"{identificador}.dat"
        if not ruta.exists():
            return None
        with ruta.open("rb") as archivo:
            return pickle.load(archivo)
