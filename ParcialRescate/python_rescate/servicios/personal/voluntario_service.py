"""Servicios para el manejo de voluntarios."""

from __future__ import annotations

from typing import Dict

from ...entidades.personal.tarea import Tarea
from ...entidades.personal.voluntario import Voluntario


class VoluntarioService:
    """Gestiona el ciclo de vida de los voluntarios."""

    def __init__(self) -> None:
        self._voluntarios: Dict[str, Voluntario] = {}

    def registrar(self, voluntario: Voluntario) -> None:
        self._voluntarios[voluntario.identificador] = voluntario

    def asignar_tarea(self, identificador: str, tarea: Tarea) -> None:
        voluntario = self._voluntarios.get(identificador)
        if not voluntario:
            raise ValueError(f"El voluntario {identificador} no existe")
        voluntario.asignar_tarea(tarea)

    def obtener(self, identificador: str) -> Voluntario:
        try:
            return self._voluntarios[identificador]
        except KeyError as error:
            raise ValueError(f"El voluntario {identificador} no existe") from error

    def listar(self) -> Dict[str, Voluntario]:
        return dict(self._voluntarios)
