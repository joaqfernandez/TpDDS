"""Servicio para administrar veterinarios."""

from __future__ import annotations

from typing import Dict

from ...entidades.personal.veterinario import Veterinario


class VeterinarioService:
    """Mantiene un registro de los veterinarios disponibles."""

    def __init__(self) -> None:
        self._veterinarios: Dict[str, Veterinario] = {}

    def registrar(self, veterinario: Veterinario) -> None:
        veterinario.validar()
        self._veterinarios[veterinario.matricula] = veterinario

    def listar(self) -> Dict[str, Veterinario]:
        return dict(self._veterinarios)
