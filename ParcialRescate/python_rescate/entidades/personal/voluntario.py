"""Representacion de un voluntario dentro del refugio."""

from dataclasses import dataclass, field
from typing import List

from .tarea import Tarea


@dataclass
class Voluntario:
    """Modelo de voluntario con su informacion basica."""

    identificador: str
    nombre: str
    apto_medico: bool
    tareas: List[Tarea] = field(default_factory=list)

    def asignar_tarea(self, tarea: Tarea) -> None:
        if not self.apto_medico:
            raise ValueError("El voluntario no posee apto medico vigente")
        self.tareas.append(tarea)

    def completar_tarea(self, identificador_tarea: str) -> None:
        for tarea in self.tareas:
            if tarea.identificador == identificador_tarea:
                tarea.marcar_completada()
                return
        raise ValueError(f"No se encontro la tarea {identificador_tarea}")
