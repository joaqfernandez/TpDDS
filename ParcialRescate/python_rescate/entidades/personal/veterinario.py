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
