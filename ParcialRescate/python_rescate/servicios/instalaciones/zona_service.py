"""Servicios para administrar zonas del refugio."""

from __future__ import annotations

from typing import Dict

from ...entidades.animales.animal import Animal
from ...entidades.instalaciones.zona import Zona
from ...excepciones.capacidad_insuficiente_exception import CapacidadInsuficienteException
from ...excepciones.recurso_insuficiente_exception import RecursoInsuficienteException


class ZonaService:
    """Gestiona el ciclo de vida de los animales dentro de una zona."""

    def __init__(self, zona: Zona) -> None:
        self._zona = zona

    def alojar(self, animal: Animal) -> None:
        try:
            self._zona.agregar_animal(animal)
        except ValueError as error:
            raise CapacidadInsuficienteException(str(error)) from error

    def retirar(self, identificador: str) -> Animal:
        return self._zona.quitar_animal(identificador)

    def animales(self) -> Dict[str, Animal]:
        return {animal.get_identificador(): animal for animal in self._zona.get_animales()}

    def consumir_recurso(self, recurso: str, cantidad: int) -> None:
        recursos = self._zona.get_recursos()
        if recursos.get(recurso, 0) < cantidad:
            raise RecursoInsuficienteException(recurso)
        self._zona.ajustar_recurso(recurso, -cantidad)

    def reponer_recurso(self, recurso: str, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self._zona.ajustar_recurso(recurso, cantidad)

    def get_zona(self) -> Zona:
        return self._zona
