"""Herramientas para generar un paquete descargable del proyecto.

Este script empaqueta todo el directorio ``ParcialRescate`` en un archivo
ZIP, excluyendo carpetas temporales como ``__pycache__`` o ``.venv``. La
intencion es facilitar la entrega del parcial en plataformas que solo
permiten la subida de un unico archivo.

Uso basico::

    python descargar_proyecto.py --salida ParcialRescate.zip

"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Iterable
from zipfile import ZIP_DEFLATED, ZipFile


EXCLUSIONES = {"__pycache__", ".git", ".venv", "venv", ".mypy_cache"}


def iterar_archivos(base: Path) -> Iterable[Path]:
    """Itera sobre todos los archivos a empaquetar.

    Args:
        base: Directorio raiz del proyecto a comprimir.

    Yields:
        Rutas absolutas de cada archivo a incluir en el ZIP.
    """

    for ruta in base.rglob("*"):
        if not ruta.is_file():
            continue

        partes = set(ruta.relative_to(base).parts)
        if partes & EXCLUSIONES:
            continue

        yield ruta


def crear_zip(origen: Path, destino: Path) -> Path:
    """Crea un archivo ZIP con el contenido del directorio ``origen``.

    Args:
        origen: Directorio a comprimir.
        destino: Ruta (archivo) donde guardar el ZIP.

    Returns:
        Ruta final del archivo ZIP creado.
    """

    destino.parent.mkdir(parents=True, exist_ok=True)

    with ZipFile(destino, "w", compression=ZIP_DEFLATED) as archivo_zip:
        for archivo in iterar_archivos(origen):
            archivo_zip.write(archivo, arcname=archivo.relative_to(origen))

    return destino


def parsear_argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Genera un paquete descargable del proyecto ParcialRescate",
    )
    parser.add_argument(
        "--salida",
        type=Path,
        default=Path("ParcialRescate.zip"),
        help="Ruta del archivo ZIP resultante (por defecto ParcialRescate.zip)",
    )
    parser.add_argument(
        "--origen",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="Directorio a comprimir (por defecto el directorio del script)",
    )
    return parser.parse_args()


def main() -> None:
    argumentos = parsear_argumentos()
    origen = argumentos.origen.resolve()
    destino = argumentos.salida.resolve()

    if not origen.exists() or not origen.is_dir():
        raise FileNotFoundError(f"Directorio origen inexistente: {origen}")

    zip_creado = crear_zip(origen, destino)
    print(f"Archivo generado: {zip_creado}")
    tamanio = os.path.getsize(zip_creado)
    print(f"Tamaño aproximado: {tamanio / 1024:.2f} KiB")


if __name__ == "__main__":
    main()
