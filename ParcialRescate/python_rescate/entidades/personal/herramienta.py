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
