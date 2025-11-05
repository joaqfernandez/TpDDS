"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate
Fecha de generacion: 2025-11-05 00:23:32
Total de archivos integrados: 55
Total de directorios procesados: 17
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. constantes.py
#
# DIRECTORIO: entidades
#   3. __init__.py
#
# DIRECTORIO: entidades/animales
#   4. __init__.py
#   5. animal.py
#   6. ave.py
#   7. gato.py
#   8. perro.py
#   9. reptil.py
#
# DIRECTORIO: entidades/instalaciones
#   10. __init__.py
#   11. refugio.py
#   12. registro_rescate.py
#   13. zona.py
#
# DIRECTORIO: entidades/personal
#   14. __init__.py
#   15. herramienta.py
#   16. tarea.py
#   17. veterinario.py
#   18. voluntario.py
#
# DIRECTORIO: excepciones
#   19. __init__.py
#   20. animal_no_encontrado_exception.py
#   21. capacidad_insuficiente_exception.py
#   22. recurso_insuficiente_exception.py
#
# DIRECTORIO: monitoreo
#   23. __init__.py
#   24. control_salud.py
#   25. sensores.py
#
# DIRECTORIO: patrones
#   26. __init__.py
#
# DIRECTORIO: patrones/factory
#   27. __init__.py
#   28. animal_factory.py
#
# DIRECTORIO: patrones/observer
#   29. __init__.py
#   30. observable.py
#
# DIRECTORIO: patrones/singleton
#   31. __init__.py
#   32. refugio_registry.py
#
# DIRECTORIO: patrones/strategy
#   33. __init__.py
#   34. plan_alimentacion_strategy.py
#   35. plan_generico_strategy.py
#   36. plan_perro_activo_strategy.py
#   37. plan_perro_tranquilo_strategy.py
#
# DIRECTORIO: servicios
#   38. __init__.py
#
# DIRECTORIO: servicios/animales
#   39. __init__.py
#   40. animal_service.py
#   41. animal_service_registry.py
#   42. ave_service.py
#   43. gato_service.py
#   44. perro_service.py
#   45. reptil_service.py
#
# DIRECTORIO: servicios/instalaciones
#   46. __init__.py
#   47. refugio_service.py
#   48. registro_rescate_service.py
#   49. zona_service.py
#
# DIRECTORIO: servicios/negocio
#   50. __init__.py
#   51. refugio_negocio_service.py
#
# DIRECTORIO: servicios/personal
#   52. __init__.py
#   53. tarea_service.py
#   54. veterinario_service.py
#   55. voluntario_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/55: __init__.py
# Directorio: .
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/__init__.py
# ==============================================================================

"""Paquete principal del sistema de gestion de rescate animal."""

__all__ = [
    "constantes",
]


# ==============================================================================
# ARCHIVO 2/55: constantes.py
# Directorio: .
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/constantes.py
# ==============================================================================

"""Constantes globales para el sistema de gestion de rescate animal."""

# Capacidad y recursos basicos
def CAPACIDAD_REFUGIO_DEFECTO() -> int:
    """Capacidad de plazas del refugio por defecto."""
    return 40


def AGUA_REFUGIO_INICIAL() -> int:
    """Cantidad de litros de agua que se almacenan inicialmente en el refugio."""
    return 250


def ALIMENTO_REFUGIO_INICIAL() -> int:
    """Cantidad de raciones disponibles al iniciar el refugio."""
    return 180


# Parametros de animales
AGUA_PERRO = 4
AGUA_GATO = 3
AGUA_AVE = 1
AGUA_REPTIL = 2

ESPACIO_PERRO = 3.5
ESPACIO_GATO = 2.0
ESPACIO_AVE = 1.0
ESPACIO_REPTIL = 1.5


# Estrategias de alimentacion basadas en nivel de actividad
ALIMENTO_PERRO_ACTIVO = 3
ALIMENTO_PERRO_TRANQUILO = 2
ALIMENTO_GATO = 2
ALIMENTO_AVE = 1
ALIMENTO_REPTIL = 1


# Sensores y monitoreo
def INTERVALO_SENSOR_SALUD() -> float:
    """Intervalo en segundos para lecturas del sensor de salud."""
    return 2.5


def INTERVALO_SENSOR_OCUPACION() -> float:
    """Intervalo en segundos para lecturas del sensor de ocupacion."""
    return 3.5


SALUD_MINIMA = 0
SALUD_MAXIMA = 100
OCUPACION_MAXIMA = 1.0



################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 3/55: __init__.py
# Directorio: entidades
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/entidades/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades/animales
################################################################################

# ==============================================================================
# ARCHIVO 4/55: __init__.py
# Directorio: entidades/animales
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/entidades/animales/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 5/55: animal.py
# Directorio: entidades/animales
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/entidades/animales/animal.py
# ==============================================================================

"""Entidades base para animales alojados en el refugio."""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import List


@dataclass
class SeguimientoMedico:
    """Registro basico de controles veterinarios."""

    descripcion: str
    responsable: str


class Animal(ABC):
    """Modelo abstracto para cualquier animal que ingresa al refugio."""

    def __init__(self, especie: str, identificador: str, agua: int, espacio: float) -> None:
        if agua <= 0:
            raise ValueError("El agua inicial debe ser positiva")
        if espacio <= 0:
            raise ValueError("El espacio requerido debe ser positivo")

        self._especie = especie
        self._identificador = identificador
        self._agua = agua
        self._espacio = espacio
        self._salud = 100
        self._historial_medico: List[SeguimientoMedico] = []

    def registrar_control(self, descripcion: str, responsable: str) -> None:
        """Guarda un seguimiento medico en el historial del animal."""

        self._historial_medico.append(SeguimientoMedico(descripcion, responsable))

    def consumir_agua(self, litros: int) -> None:
        """Reduce la reserva de agua disponible para el animal."""

        if litros < 0:
            raise ValueError("El consumo de agua no puede ser negativo")
        self._agua = max(0, self._agua - litros)

    def recibir_agua(self, litros: int) -> None:
        """Incrementa la reserva de agua disponible."""

        if litros <= 0:
            raise ValueError("Los litros deben ser positivos")
        self._agua += litros

    def actualizar_salud(self, delta: int) -> None:
        """Modifica la salud del animal respetando los limites aceptados."""

        nueva_salud = min(100, max(0, self._salud + delta))
        self._salud = nueva_salud

    # Getters basicos
    def get_especie(self) -> str:
        return self._especie

    def get_identificador(self) -> str:
        return self._identificador

    def get_agua(self) -> int:
        return self._agua

    def get_espacio(self) -> float:
        return self._espacio

    def get_salud(self) -> int:
        return self._salud

    def get_historial_medico(self) -> List[SeguimientoMedico]:
        return list(self._historial_medico)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(id={self._identificador}, especie={self._especie}, "
            f"agua={self._agua}, espacio={self._espacio}, salud={self._salud})"
        )


# ==============================================================================
# ARCHIVO 6/55: ave.py
# Directorio: entidades/animales
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/entidades/animales/ave.py
# ==============================================================================

"""Entidad concreta para aves rescatadas."""

from .animal import Animal
from ...constantes import AGUA_AVE, ESPACIO_AVE


class Ave(Animal):
    """Representa un ave dentro del refugio."""

    def __init__(self, identificador: str, puede_volar: bool) -> None:
        super().__init__("Ave", identificador, AGUA_AVE, ESPACIO_AVE)
        self._puede_volar = puede_volar

    def puede_volar(self) -> bool:
        return self._puede_volar


# ==============================================================================
# ARCHIVO 7/55: gato.py
# Directorio: entidades/animales
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/entidades/animales/gato.py
# ==============================================================================

"""Entidad concreta para gatos rescatados."""

from .animal import Animal
from ...constantes import AGUA_GATO, ESPACIO_GATO


class Gato(Animal):
    """Representa un gato dentro del refugio."""

    def __init__(self, identificador: str, temperamento: str) -> None:
        super().__init__("Gato", identificador, AGUA_GATO, ESPACIO_GATO)
        self._temperamento = temperamento

    def get_temperamento(self) -> str:
        return self._temperamento


# ==============================================================================
# ARCHIVO 8/55: perro.py
# Directorio: entidades/animales
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/entidades/animales/perro.py
# ==============================================================================

"""Entidad concreta para perros rescatados."""

from .animal import Animal
from ...constantes import AGUA_PERRO, ESPACIO_PERRO


class Perro(Animal):
    """Representa un perro dentro del refugio."""

    def __init__(self, identificador: str, raza: str, es_activo: bool) -> None:
        super().__init__("Perro", identificador, AGUA_PERRO, ESPACIO_PERRO)
        self._raza = raza
        self._es_activo = es_activo

    def get_raza(self) -> str:
        return self._raza

    def es_activo(self) -> bool:
        return self._es_activo


# ==============================================================================
# ARCHIVO 9/55: reptil.py
# Directorio: entidades/animales
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/entidades/animales/reptil.py
# ==============================================================================

"""Entidad concreta para reptiles rescatados."""

from .animal import Animal
from ...constantes import AGUA_REPTIL, ESPACIO_REPTIL


class Reptil(Animal):
    """Representa un reptil dentro del refugio."""

    def __init__(self, identificador: str, es_venenoso: bool) -> None:
        super().__init__("Reptil", identificador, AGUA_REPTIL, ESPACIO_REPTIL)
        self._es_venenoso = es_venenoso

    def es_venenoso(self) -> bool:
        return self._es_venenoso



################################################################################
# DIRECTORIO: entidades/instalaciones
################################################################################

# ==============================================================================
# ARCHIVO 10/55: __init__.py
# Directorio: entidades/instalaciones
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/entidades/instalaciones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 11/55: refugio.py
# Directorio: entidades/instalaciones
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/entidades/instalaciones/refugio.py
# ==============================================================================

"""Entidad principal que agrupa las zonas del refugio."""

from typing import Dict, List

from ...constantes import AGUA_REFUGIO_INICIAL, ALIMENTO_REFUGIO_INICIAL
from .zona import Zona


class Refugio:
    """Representa la infraestructura del refugio animal."""

    def __init__(self, nombre: str, domicilio: str) -> None:
        self._nombre = nombre
        self._domicilio = domicilio
        self._zonas: Dict[str, Zona] = {}
        self._agua_disponible = AGUA_REFUGIO_INICIAL()
        self._alimento_disponible = ALIMENTO_REFUGIO_INICIAL()

    def agregar_zona(self, zona: Zona) -> None:
        if zona.get_nombre() in self._zonas:
            raise ValueError("Ya existe una zona con ese nombre")
        self._zonas[zona.get_nombre()] = zona

    def obtener_zona(self, nombre: str) -> Zona:
        try:
            return self._zonas[nombre]
        except KeyError as error:
            raise ValueError(f"La zona {nombre} no existe") from error

    def get_zonas(self) -> List[Zona]:
        return list(self._zonas.values())

    def get_agua_disponible(self) -> int:
        return self._agua_disponible

    def get_alimento_disponible(self) -> int:
        return self._alimento_disponible

    def ajustar_agua(self, delta: int) -> None:
        self._agua_disponible += delta
        if self._agua_disponible < 0:
            raise ValueError("El agua disponible no puede ser negativa")

    def ajustar_alimento(self, delta: int) -> None:
        self._alimento_disponible += delta
        if self._alimento_disponible < 0:
            raise ValueError("El alimento disponible no puede ser negativo")

    def get_nombre(self) -> str:
        return self._nombre

    def get_domicilio(self) -> str:
        return self._domicilio


# ==============================================================================
# ARCHIVO 12/55: registro_rescate.py
# Directorio: entidades/instalaciones
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/entidades/instalaciones/registro_rescate.py
# ==============================================================================

"""Registro integral de un operativo de rescate."""

from dataclasses import dataclass
from datetime import datetime

from .refugio import Refugio


@dataclass
class RegistroRescate:
    """Documento que vincula un refugio con un operativo de rescate."""

    identificador: str
    refugio: Refugio
    fecha: datetime
    responsable: str
    cantidad_animales: int
    descripcion: str

    def mostrar_resumen(self) -> str:
        return (
            f"REGISTRO DE RESCATE\n"
            f"===================\n"
            f"ID Operativo: {self.identificador}\n"
            f"Refugio: {self.refugio.get_nombre()}\n"
            f"Fecha: {self.fecha:%Y-%m-%d %H:%M}\n"
            f"Responsable: {self.responsable}\n"
            f"Animales Trasladados: {self.cantidad_animales}\n"
            f"Descripcion: {self.descripcion}\n"
        )


# ==============================================================================
# ARCHIVO 13/55: zona.py
# Directorio: entidades/instalaciones
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/entidades/instalaciones/zona.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 14/55: __init__.py
# Directorio: entidades/personal
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/entidades/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 15/55: herramienta.py
# Directorio: entidades/personal
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/entidades/personal/herramienta.py
# ==============================================================================

"""Herramientas utilizadas por el personal del refugio."""

from dataclasses import dataclass


@dataclass
class Herramienta:
    """Herramienta certificada para tareas de rescate."""

    identificador: str
    nombre: str
    certificado: str

    def validar(self) -> None:
        if not self.identificador:
            raise ValueError("El identificador de la herramienta es obligatorio")
        if not self.certificado:
            raise ValueError("La herramienta debe tener un certificado vigente")


# ==============================================================================
# ARCHIVO 16/55: tarea.py
# Directorio: entidades/personal
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/entidades/personal/tarea.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 17/55: veterinario.py
# Directorio: entidades/personal
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/entidades/personal/veterinario.py
# ==============================================================================

"""Entidad para los veterinarios del refugio."""

from dataclasses import dataclass


@dataclass
class Veterinario:
    """Veterinario habilitado para supervisar la salud de los animales."""

    matricula: str
    nombre: str
    especialidad: str

    def validar(self) -> None:
        if not self.matricula:
            raise ValueError("La matricula profesional es obligatoria")


# ==============================================================================
# ARCHIVO 18/55: voluntario.py
# Directorio: entidades/personal
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/entidades/personal/voluntario.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 19/55: __init__.py
# Directorio: excepciones
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/excepciones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 20/55: animal_no_encontrado_exception.py
# Directorio: excepciones
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/excepciones/animal_no_encontrado_exception.py
# ==============================================================================

"""Excepcion cuando se intenta operar con un animal que no esta registrado."""


class AnimalNoEncontradoException(Exception):
    """Se lanza cuando un animal no esta presente en la zona consultada."""

    def __init__(self, identificador: str) -> None:
        super().__init__(f"No se encontro al animal con identificador '{identificador}'")


# ==============================================================================
# ARCHIVO 21/55: capacidad_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/excepciones/capacidad_insuficiente_exception.py
# ==============================================================================

"""Excepcion para indicar que no hay espacio suficiente en una zona del refugio."""


class CapacidadInsuficienteException(Exception):
    """Se produce cuando se intenta alojar mas animales de los permitidos."""

    def __init__(self, mensaje: str = "La zona no dispone de capacidad suficiente") -> None:
        super().__init__(mensaje)


# ==============================================================================
# ARCHIVO 22/55: recurso_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/excepciones/recurso_insuficiente_exception.py
# ==============================================================================

"""Excepcion para indicar falta de recursos esenciales en el refugio."""


class RecursoInsuficienteException(Exception):
    """Se produce cuando no hay agua o alimento suficiente para los animales."""

    def __init__(self, recurso: str) -> None:
        super().__init__(f"No hay suficiente {recurso} para completar la operacion")



################################################################################
# DIRECTORIO: monitoreo
################################################################################

# ==============================================================================
# ARCHIVO 23/55: __init__.py
# Directorio: monitoreo
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/monitoreo/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 24/55: control_salud.py
# Directorio: monitoreo
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/monitoreo/control_salud.py
# ==============================================================================

"""Control centralizado que reacciona a los sensores del refugio."""

from __future__ import annotations

from typing import Protocol

from ..constantes import OCUPACION_MAXIMA
from ..patrones.observer.observable import Observer


class AccionCorrectiva(Protocol):
    """Interfaz para ejecutar acciones correctivas."""

    def ejecutar(self, mensaje: str) -> None:
        """Ejecuta la accion con el mensaje indicado."""


class ControlSalud(Observer[float]):
    """Observador que registra las lecturas de salud."""

    def __init__(self, accion_correctiva: AccionCorrectiva) -> None:
        self._accion_correctiva = accion_correctiva

    def update(self, value: float) -> None:
        if value < 60:
            self._accion_correctiva.ejecutar(
                f"[ALERTA] Salud promedio baja detectada: {value:.2f}"
            )


class ControlOcupacion(Observer[float]):
    """Observador que supervisa el nivel de ocupacion."""

    def __init__(self, accion_correctiva: AccionCorrectiva) -> None:
        self._accion_correctiva = accion_correctiva

    def update(self, value: float) -> None:
        if value > OCUPACION_MAXIMA * 0.8:
            self._accion_correctiva.ejecutar(
                f"[ALERTA] Ocupacion al {value * 100:.0f}%: reorganizar zonas"
            )


# ==============================================================================
# ARCHIVO 25/55: sensores.py
# Directorio: monitoreo
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/monitoreo/sensores.py
# ==============================================================================

"""Sensores simulados para monitorear el refugio."""

from __future__ import annotations

import random
import threading
import time
from typing import Callable, Optional

from ..constantes import (
    INTERVALO_SENSOR_OCUPACION,
    INTERVALO_SENSOR_SALUD,
    OCUPACION_MAXIMA,
    SALUD_MAXIMA,
    SALUD_MINIMA,
)
from ..patrones.observer.observable import Observable


class SensorBase(Observable[float]):
    """Sensor generico que publica lecturas periodicas en un hilo aparte."""

    def __init__(self, intervalo: Callable[[], float]) -> None:
        super().__init__()
        self._intervalo = intervalo
        self._activo = False
        self._thread: Optional[threading.Thread] = None

    def iniciar(self) -> None:
        if self._activo:
            return
        self._activo = True
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def detener(self) -> None:
        self._activo = False
        if self._thread:
            self._thread.join(timeout=0.1)

    def _loop(self) -> None:
        while self._activo:
            lectura = self._leer()
            self.notify(lectura)
            time.sleep(self._intervalo())

    def _leer(self) -> float:
        raise NotImplementedError


class SensorSalud(SensorBase):
    """Genera lecturas aleatorias de salud promedio."""

    def __init__(self) -> None:
        super().__init__(INTERVALO_SENSOR_SALUD)

    def _leer(self) -> float:
        return random.uniform(SALUD_MINIMA, SALUD_MAXIMA)


class SensorOcupacion(SensorBase):
    """Simula la ocupacion relativa de las instalaciones."""

    def __init__(self) -> None:
        super().__init__(INTERVALO_SENSOR_OCUPACION)

    def _leer(self) -> float:
        return random.uniform(0.0, OCUPACION_MAXIMA)



################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 26/55: __init__.py
# Directorio: patrones
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/patrones/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 27/55: __init__.py
# Directorio: patrones/factory
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/patrones/factory/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 28/55: animal_factory.py
# Directorio: patrones/factory
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/patrones/factory/animal_factory.py
# ==============================================================================

"""Factory Method para crear animales segun su especie."""

from __future__ import annotations

from typing import Callable, Dict

from ...entidades.animales.ave import Ave
from ...entidades.animales.gato import Gato
from ...entidades.animales.perro import Perro
from ...entidades.animales.reptil import Reptil
from ...entidades.animales.animal import Animal


class AnimalFactory:
    """Crea instancias concretas de animales usando un registro interno."""

    _registry: Dict[str, Callable[..., Animal]] = {
        "Perro": lambda identificador, **kwargs: Perro(
            identificador, kwargs.get("raza", "Mestizo"), kwargs.get("es_activo", False)
        ),
        "Gato": lambda identificador, **kwargs: Gato(
            identificador, kwargs.get("temperamento", "Curioso")
        ),
        "Ave": lambda identificador, **kwargs: Ave(
            identificador, kwargs.get("puede_volar", True)
        ),
        "Reptil": lambda identificador, **kwargs: Reptil(
            identificador, kwargs.get("es_venenoso", False)
        ),
    }

    @classmethod
    def crear(cls, especie: str, identificador: str, **kwargs) -> Animal:
        try:
            return cls._registry[especie](identificador, **kwargs)
        except KeyError as error:
            raise ValueError(f"No existe una fabrica para la especie {especie}") from error

    @classmethod
    def registrar(cls, especie: str, constructor: Callable[..., Animal]) -> None:
        cls._registry[especie] = constructor



################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 29/55: __init__.py
# Directorio: patrones/observer
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/patrones/observer/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 30/55: observable.py
# Directorio: patrones/observer
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/patrones/observer/observable.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 31/55: __init__.py
# Directorio: patrones/singleton
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/patrones/singleton/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 32/55: refugio_registry.py
# Directorio: patrones/singleton
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/patrones/singleton/refugio_registry.py
# ==============================================================================

"""Singleton que mantiene un registro global de refugios."""

from __future__ import annotations

from threading import Lock
from typing import Dict

from ...entidades.instalaciones.refugio import Refugio


class RefugioRegistry:
    """Permite registrar y recuperar refugios desde cualquier parte del sistema."""

    _instance: "RefugioRegistry | None" = None
    _lock = Lock()

    def __new__(cls) -> "RefugioRegistry":
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._refugios = {}
        return cls._instance

    def registrar(self, refugio: Refugio) -> None:
        self._refugios[refugio.get_nombre()] = refugio

    def obtener(self, nombre: str) -> Refugio:
        try:
            return self._refugios[nombre]
        except KeyError as error:
            raise ValueError(f"El refugio {nombre} no esta registrado") from error

    def listar(self) -> Dict[str, Refugio]:
        return dict(self._refugios)



################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 33/55: __init__.py
# Directorio: patrones/strategy
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/patrones/strategy/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 34/55: plan_alimentacion_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/patrones/strategy/plan_alimentacion_strategy.py
# ==============================================================================

"""Estrategia para definir el plan de alimentacion de un animal."""

from __future__ import annotations

from abc import ABC, abstractmethod

from ...entidades.animales.animal import Animal


class PlanAlimentacionStrategy(ABC):
    """Define el contrato para calcular raciones de alimento por animal."""

    @abstractmethod
    def calcular_racion(self, animal: Animal) -> int:
        """Devuelve la cantidad de raciones a entregar a un animal."""



# ==============================================================================
# ARCHIVO 35/55: plan_generico_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/patrones/strategy/plan_generico_strategy.py
# ==============================================================================

"""Estrategia generica configurable para alimentacion."""

from ...entidades.animales.animal import Animal
from .plan_alimentacion_strategy import PlanAlimentacionStrategy


class PlanGenericoStrategy(PlanAlimentacionStrategy):
    """Calcula raciones utilizando un valor fijo configurado."""

    def __init__(self, racion: int) -> None:
        if racion <= 0:
            raise ValueError("La racion debe ser positiva")
        self._racion = racion

    def calcular_racion(self, animal: Animal) -> int:
        return self._racion


# ==============================================================================
# ARCHIVO 36/55: plan_perro_activo_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/patrones/strategy/plan_perro_activo_strategy.py
# ==============================================================================

"""Estrategia de alimentacion para perros activos."""

from ...constantes import ALIMENTO_PERRO_ACTIVO
from ...entidades.animales.animal import Animal
from .plan_alimentacion_strategy import PlanAlimentacionStrategy


class PlanPerroActivoStrategy(PlanAlimentacionStrategy):
    """Entrega una mayor racion para perros con alto gasto energetico."""

    def calcular_racion(self, animal: Animal) -> int:
        return ALIMENTO_PERRO_ACTIVO


# ==============================================================================
# ARCHIVO 37/55: plan_perro_tranquilo_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/patrones/strategy/plan_perro_tranquilo_strategy.py
# ==============================================================================

"""Estrategia de alimentacion para perros tranquilos."""

from ...constantes import ALIMENTO_PERRO_TRANQUILO
from ...entidades.animales.animal import Animal
from .plan_alimentacion_strategy import PlanAlimentacionStrategy


class PlanPerroTranquiloStrategy(PlanAlimentacionStrategy):
    """Entrega una racion reducida para perros con baja actividad."""

    def calcular_racion(self, animal: Animal) -> int:
        return ALIMENTO_PERRO_TRANQUILO



################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 38/55: __init__.py
# Directorio: servicios
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/servicios/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios/animales
################################################################################

# ==============================================================================
# ARCHIVO 39/55: __init__.py
# Directorio: servicios/animales
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/servicios/animales/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 40/55: animal_service.py
# Directorio: servicios/animales
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/servicios/animales/animal_service.py
# ==============================================================================

"""Servicios comunes para el manejo de animales."""

from __future__ import annotations

from ..instalaciones.zona_service import ZonaService
from ...entidades.animales.animal import Animal
from ...patrones.strategy.plan_alimentacion_strategy import PlanAlimentacionStrategy


class AnimalService:
    """Servicio base que utiliza estrategias de alimentacion."""

    def __init__(self, estrategia: PlanAlimentacionStrategy) -> None:
        self._estrategia = estrategia

    def alimentar(self, animal: Animal, zona_service: ZonaService) -> int:
        racion = self._estrategia.calcular_racion(animal)
        zona_service.consumir_recurso("alimento", racion)
        return racion

    def hidratar(self, animal: Animal, zona_service: ZonaService) -> int:
        zona_service.consumir_recurso("agua", 1)
        animal.recibir_agua(1)
        return 1


# ==============================================================================
# ARCHIVO 41/55: animal_service_registry.py
# Directorio: servicios/animales
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/servicios/animales/animal_service_registry.py
# ==============================================================================

"""Registro centralizado de servicios por tipo de animal."""

from __future__ import annotations

from typing import Dict, Type

from ...entidades.animales.animal import Animal
from ...entidades.animales.ave import Ave
from ...entidades.animales.gato import Gato
from ...entidades.animales.perro import Perro
from ...entidades.animales.reptil import Reptil
from .animal_service import AnimalService
from .ave_service import AveService
from .gato_service import GatoService
from .perro_service import PerroService
from .reptil_service import ReptilService


class AnimalServiceRegistry:
    """Resuelve dinamicamente el servicio apropiado para cada animal."""

    def __init__(self) -> None:
        self._servicios: Dict[Type[Animal], AnimalService] = {
            Perro: PerroService(),
            Gato: GatoService(),
            Ave: AveService(),
            Reptil: ReptilService(),
        }

    def obtener_servicio(self, animal: Animal) -> AnimalService:
        for tipo, servicio in self._servicios.items():
            if isinstance(animal, tipo):
                return servicio
        raise ValueError(f"No hay servicio registrado para {type(animal).__name__}")


# ==============================================================================
# ARCHIVO 42/55: ave_service.py
# Directorio: servicios/animales
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/servicios/animales/ave_service.py
# ==============================================================================

"""Servicio especializado para aves."""

from ...constantes import ALIMENTO_AVE
from ...patrones.strategy.plan_generico_strategy import PlanGenericoStrategy
from .animal_service import AnimalService


class AveService(AnimalService):
    """Implementa la logica especifica para aves."""

    def __init__(self) -> None:
        super().__init__(PlanGenericoStrategy(ALIMENTO_AVE))


# ==============================================================================
# ARCHIVO 43/55: gato_service.py
# Directorio: servicios/animales
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/servicios/animales/gato_service.py
# ==============================================================================

"""Servicio especializado para gatos."""

from ...constantes import ALIMENTO_GATO
from ...patrones.strategy.plan_generico_strategy import PlanGenericoStrategy
from .animal_service import AnimalService


class GatoService(AnimalService):
    """Utiliza una estrategia generica preconfigurada."""

    def __init__(self) -> None:
        super().__init__(PlanGenericoStrategy(ALIMENTO_GATO))


# ==============================================================================
# ARCHIVO 44/55: perro_service.py
# Directorio: servicios/animales
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/servicios/animales/perro_service.py
# ==============================================================================

"""Servicio especializado para perros."""

from ...entidades.animales.perro import Perro
from ...patrones.strategy.plan_perro_activo_strategy import PlanPerroActivoStrategy
from ...patrones.strategy.plan_perro_tranquilo_strategy import PlanPerroTranquiloStrategy
from .animal_service import AnimalService


class PerroService(AnimalService):
    """Selecciona dinamicamente la estrategia segun el nivel de actividad."""

    def __init__(self) -> None:
        super().__init__(PlanPerroTranquiloStrategy())
        self._estrategia_activo = PlanPerroActivoStrategy()

    def alimentar(self, animal: Perro, zona_service):  # type: ignore[override]
        estrategia = self._estrategia_activo if animal.es_activo() else self._estrategia
        self._estrategia = estrategia
        return super().alimentar(animal, zona_service)


# ==============================================================================
# ARCHIVO 45/55: reptil_service.py
# Directorio: servicios/animales
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/servicios/animales/reptil_service.py
# ==============================================================================

"""Servicio especializado para reptiles."""

from ...constantes import ALIMENTO_REPTIL
from ...patrones.strategy.plan_generico_strategy import PlanGenericoStrategy
from .animal_service import AnimalService


class ReptilService(AnimalService):
    """Aplica la estrategia generica para reptiles."""

    def __init__(self) -> None:
        super().__init__(PlanGenericoStrategy(ALIMENTO_REPTIL))



################################################################################
# DIRECTORIO: servicios/instalaciones
################################################################################

# ==============================================================================
# ARCHIVO 46/55: __init__.py
# Directorio: servicios/instalaciones
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/servicios/instalaciones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 47/55: refugio_service.py
# Directorio: servicios/instalaciones
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/servicios/instalaciones/refugio_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 48/55: registro_rescate_service.py
# Directorio: servicios/instalaciones
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/servicios/instalaciones/registro_rescate_service.py
# ==============================================================================

"""Servicio para gestionar la persistencia de registros de rescate."""

from __future__ import annotations

import pickle
from pathlib import Path
from typing import Optional

from ...entidades.instalaciones.registro_rescate import RegistroRescate


class RegistroRescateService:
    """Permite guardar y recuperar registros de rescate desde disco."""

    def __init__(self, directorio: str = "data") -> None:
        self._directorio = Path(directorio)
        self._directorio.mkdir(parents=True, exist_ok=True)

    def guardar(self, registro: RegistroRescate) -> Path:
        ruta = self._directorio / f"{registro.identificador}.dat"
        with ruta.open("wb") as archivo:
            pickle.dump(registro, archivo)
        return ruta

    def cargar(self, identificador: str) -> Optional[RegistroRescate]:
        ruta = self._directorio / f"{identificador}.dat"
        if not ruta.exists():
            return None
        with ruta.open("rb") as archivo:
            return pickle.load(archivo)


# ==============================================================================
# ARCHIVO 49/55: zona_service.py
# Directorio: servicios/instalaciones
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/servicios/instalaciones/zona_service.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 50/55: __init__.py
# Directorio: servicios/negocio
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/servicios/negocio/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 51/55: refugio_negocio_service.py
# Directorio: servicios/negocio
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/servicios/negocio/refugio_negocio_service.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: servicios/personal
################################################################################

# ==============================================================================
# ARCHIVO 52/55: __init__.py
# Directorio: servicios/personal
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/servicios/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 53/55: tarea_service.py
# Directorio: servicios/personal
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/servicios/personal/tarea_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 54/55: veterinario_service.py
# Directorio: servicios/personal
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/servicios/personal/veterinario_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 55/55: voluntario_service.py
# Directorio: servicios/personal
# Ruta completa: /Users/joaquinfernandez/Documents/Facultad/Diseño de sistemas/ParcialRescate/python_rescate/servicios/personal/voluntario_service.py
# ==============================================================================

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



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 55
# Generado: 2025-11-05 00:23:32
################################################################################
