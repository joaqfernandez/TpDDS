"""Tareas asignadas al personal del refugio."""

from dataclasses import dataclass, field
from datetime import date
from typing import List

from .herramienta import Herramienta


@dataclass(order=True)
class Tarea:
    """Tarea programada para realizar en el refugio."""

    prioridad: int
    identificador: str = field(compare=False)
    descripcion: str = field(compare=False)
    fecha_programada: date = field(compare=False)
    completada: bool = field(default=False, compare=False)
    herramientas: List[Herramienta] = field(default_factory=list, compare=False)

    def marcar_completada(self) -> None:
        self.completada = True

    def asignar_herramienta(self, herramienta: Herramienta) -> None:
        herramienta.validar()
        self.herramientas.append(herramienta)
