"""Registro integral de un operativo de rescate."""

from dataclasses import dataclass
from datetime import datetime

from .refugio import Refugio


@dataclass
class RegistroRescate:
    """Documento que vincula un refugio con un operativo de rescate."""

    identificador: str
    refugio: Refugio
    fecha: datetime
    responsable: str
    cantidad_animales: int
    descripcion: str

    def mostrar_resumen(self) -> str:
        return (
            f"REGISTRO DE RESCATE\n"
            f"===================\n"
            f"ID Operativo: {self.identificador}\n"
            f"Refugio: {self.refugio.get_nombre()}\n"
            f"Fecha: {self.fecha:%Y-%m-%d %H:%M}\n"
            f"Responsable: {self.responsable}\n"
            f"Animales Trasladados: {self.cantidad_animales}\n"
            f"Descripcion: {self.descripcion}\n"
        )
