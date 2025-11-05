"""Servicios de negocio que orquestan operaciones complejas del refugio."""

from __future__ import annotations

from datetime import datetime
from typing import Dict, Iterable, List

from ...entidades.animales.animal import Animal
from ...entidades.instalaciones.refugio import Refugio
from ...entidades.instalaciones.registro_rescate import RegistroRescate
from ...patrones.factory.animal_factory import AnimalFactory
from ..animales.animal_service_registry import AnimalServiceRegistry
from ..instalaciones.registro_rescate_service import RegistroRescateService
from ..instalaciones.zona_service import ZonaService


class RefugioNegocioService:
    """Coordina la admision de animales y las operaciones de rescate."""

    def __init__(
        self,
        registro_service: RegistroRescateService,
        animal_registry: AnimalServiceRegistry | None = None,
    ) -> None:
        self._registro_service = registro_service
        self._animal_registry = animal_registry or AnimalServiceRegistry()

    def admitir_animales(self, zona_service: ZonaService, animales: Iterable[Animal]) -> None:
        for animal in animales:
            zona_service.alojar(animal)

    def crear_animales(self, especificaciones: List[Dict]) -> List[Animal]:
        animales: List[Animal] = []
        for especificacion in especificaciones:
            datos = dict(especificacion)
            especie = datos.pop("especie")
            identificador = datos.pop("identificador")
            animales.append(AnimalFactory.crear(especie, identificador, **datos))
        return animales

    def alimentar_zona(self, zona_service: ZonaService) -> Dict[str, int]:
        consumo: Dict[str, int] = {}
        for animal in zona_service.get_zona().get_animales():
            servicio = self._animal_registry.obtener_servicio(animal)
            racion = servicio.alimentar(animal, zona_service)
            consumo[animal.get_identificador()] = racion
        return consumo

    def generar_registro_rescate(
        self,
        refugio: Refugio,
        responsable: str,
        descripcion: str,
    ) -> RegistroRescate:
        total_animales = sum(len(zona.get_animales()) for zona in refugio.get_zonas())
        registro = RegistroRescate(
            identificador=f"RES-{datetime.now():%Y%m%d%H%M%S}",
            refugio=refugio,
            fecha=datetime.now(),
            responsable=responsable,
            cantidad_animales=total_animales,
            descripcion=descripcion,
        )
        self._registro_service.guardar(registro)
        return registro

    def transferir_animales(
        self,
        origen: ZonaService,
        destino: ZonaService,
        identificadores: Iterable[str],
    ) -> None:
        for identificador in identificadores:
            animal = origen.retirar(identificador)
            destino.alojar(animal)
