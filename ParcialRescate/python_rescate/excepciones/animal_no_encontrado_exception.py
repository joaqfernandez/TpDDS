"""Excepcion cuando se intenta operar con un animal que no esta registrado."""


class AnimalNoEncontradoException(Exception):
    """Se lanza cuando un animal no esta presente en la zona consultada."""

    def __init__(self, identificador: str) -> None:
        super().__init__(f"No se encontro al animal con identificador '{identificador}'")
