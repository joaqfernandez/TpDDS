"""Excepcion para indicar que no hay espacio suficiente en una zona del refugio."""


class CapacidadInsuficienteException(Exception):
    """Se produce cuando se intenta alojar mas animales de los permitidos."""

    def __init__(self, mensaje: str = "La zona no dispone de capacidad suficiente") -> None:
        super().__init__(mensaje)
