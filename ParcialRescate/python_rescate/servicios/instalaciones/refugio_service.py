"""Servicios de alto nivel para administrar el refugio."""

from __future__ import annotations

from typing import Dict

from ...constantes import CAPACIDAD_REFUGIO_DEFECTO
from ...entidades.instalaciones.refugio import Refugio
from ...entidades.instalaciones.zona import Zona
from ...patrones.singleton.refugio_registry import RefugioRegistry
from .zona_service import ZonaService


class RefugioService:
    """Coordina operaciones sobre el refugio y sus zonas."""

    def __init__(self, registry: RefugioRegistry | None = None) -> None:
        self._registry = registry or RefugioRegistry()

    def crear_refugio(self, nombre: str, domicilio: str) -> Refugio:
        refugio = Refugio(nombre, domicilio)
        self._registry.registrar(refugio)
        return refugio

    def crear_zona_basica(self, refugio: Refugio, nombre: str) -> ZonaService:
        zona = Zona(nombre, CAPACIDAD_REFUGIO_DEFECTO(), {"agua": 80, "alimento": 60})
        refugio.agregar_zona(zona)
        return ZonaService(zona)

    def registrar_zona(self, refugio: Refugio, zona: Zona) -> ZonaService:
        refugio.agregar_zona(zona)
        return ZonaService(zona)

    def resumen_recursos(self, refugio: Refugio) -> Dict[str, int]:
        return {
            "agua": refugio.get_agua_disponible(),
            "alimento": refugio.get_alimento_disponible(),
            "zonas": len(refugio.get_zonas()),
        }
