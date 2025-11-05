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
