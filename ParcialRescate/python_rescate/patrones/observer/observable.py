"""Implementacion generica del patron Observer."""

from __future__ import annotations

from typing import Generic, List, Protocol, TypeVar

T = TypeVar("T")


class Observer(Protocol[T]):
    """Interfaz que deben implementar los observadores."""

    def update(self, value: T) -> None:
        """Recibe actualizaciones del observable."""


class Observable(Generic[T]):
    """Componente observable que notifica a sus observadores."""

    def __init__(self) -> None:
        self._observers: List[Observer[T]] = []

    def subscribe(self, observer: Observer[T]) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer[T]) -> None:
        self._observers.remove(observer)

    def notify(self, value: T) -> None:
        for observer in list(self._observers):
            observer.update(value)
