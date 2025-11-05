"""Servicios para generar y controlar tareas."""

from __future__ import annotations

from datetime import date
from typing import Dict

from ...entidades.personal.herramienta import Herramienta
from ...entidades.personal.tarea import Tarea


class TareaService:
    """Permite crear tareas y asignar herramientas certificadas."""

    def __init__(self) -> None:
        self._tareas: Dict[str, Tarea] = {}

    def crear_tarea(self, identificador: str, descripcion: str, fecha: date, prioridad: int) -> Tarea:
        tarea = Tarea(prioridad, identificador, descripcion, fecha)
        self._tareas[identificador] = tarea
        return tarea

    def asignar_herramienta(self, identificador: str, herramienta: Herramienta) -> None:
        tarea = self._tareas.get(identificador)
        if not tarea:
            raise ValueError(f"La tarea {identificador} no existe")
        tarea.asignar_herramienta(herramienta)

    def listar(self) -> Dict[str, Tarea]:
        return dict(self._tareas)
