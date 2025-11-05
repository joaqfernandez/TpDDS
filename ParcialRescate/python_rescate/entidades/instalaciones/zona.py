"""Representa un area dentro del refugio donde se alojan animales."""

from __future__ import annotations

from typing import Dict, List, Type

from ..animales.animal import Animal


class Zona:
    """Zona de alojamiento para un conjunto de animales."""

    def __init__(self, nombre: str, capacidad: int, recursos: Dict[str, int]) -> None:
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser positiva")
        self._nombre = nombre
        self._capacidad = capacidad
        self._recursos = recursos
        self._animales: List[Animal] = []

    def agregar_animal(self, animal: Animal) -> None:
        if len(self._animales) >= self._capacidad:
            raise ValueError("No hay mas espacio en la zona")
        self._animales.append(animal)

    def quitar_animal(self, identificador: str) -> Animal:
        for idx, animal in enumerate(self._animales):
            if animal.get_identificador() == identificador:
                return self._animales.pop(idx)
        raise ValueError(f"Animal {identificador} no encontrado en la zona {self._nombre}")

    def animales_por_tipo(self, tipo: Type[Animal]) -> List[Animal]:
        return [animal for animal in self._animales if isinstance(animal, tipo)]

    def get_animales(self) -> List[Animal]:
        return list(self._animales)

    def get_capacidad_disponible(self) -> int:
        return self._capacidad - len(self._animales)

    def get_nombre(self) -> str:
        return self._nombre

    def get_recursos(self) -> Dict[str, int]:
        return dict(self._recursos)

    def ajustar_recurso(self, clave: str, delta: int) -> None:
        self._recursos[clave] = self._recursos.get(clave, 0) + delta

    def __repr__(self) -> str:
        return f"Zona(nombre={self._nombre}, capacidad={self._capacidad}, animales={len(self._animales)})"
