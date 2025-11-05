"""Excepcion para indicar falta de recursos esenciales en el refugio."""


class RecursoInsuficienteException(Exception):
    """Se produce cuando no hay agua o alimento suficiente para los animales."""

    def __init__(self, recurso: str) -> None:
        super().__init__(f"No hay suficiente {recurso} para completar la operacion")
