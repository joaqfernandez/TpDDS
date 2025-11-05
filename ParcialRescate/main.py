"""Demostracion CLI del sistema de gestion de rescate animal."""

from __future__ import annotations

import time
from datetime import date

from python_rescate.entidades.personal.herramienta import Herramienta
from python_rescate.entidades.personal.voluntario import Voluntario
from python_rescate.monitoreo.control_salud import ControlOcupacion, ControlSalud
from python_rescate.monitoreo.sensores import SensorOcupacion, SensorSalud
from python_rescate.servicios.animales.animal_service_registry import AnimalServiceRegistry
from python_rescate.servicios.instalaciones.refugio_service import RefugioService
from python_rescate.servicios.instalaciones.registro_rescate_service import RegistroRescateService
from python_rescate.servicios.negocio.refugio_negocio_service import RefugioNegocioService
from python_rescate.servicios.personal.tarea_service import TareaService
from python_rescate.servicios.personal.voluntario_service import VoluntarioService


class ConsolaAccion:
    """Implementa la accion correctiva escribiendo en consola."""

    def ejecutar(self, mensaje: str) -> None:
        print(mensaje)


def ejecutar_demo() -> None:
    print("========== SISTEMA PYTHON RESCATE ==========")

    refugio_service = RefugioService()
    registro_service = RegistroRescateService(directorio="data")
    negocio_service = RefugioNegocioService(registro_service, AnimalServiceRegistry())

    refugio = refugio_service.crear_refugio("Huellitas", "Av. Siempre Viva 742")
    zona_perros = refugio_service.crear_zona_basica(refugio, "Caninos")
    zona_gatos = refugio_service.crear_zona_basica(refugio, "Felinos")

    print(f"Refugio creado: {refugio.get_nombre()} - {refugio.get_domicilio()}")
    print("Zonas disponibles:", [zona.get_zona().get_nombre() for zona in [zona_perros, zona_gatos]])

    animales = negocio_service.crear_animales(
        [
            {"especie": "Perro", "identificador": "DOG-001", "raza": "Labrador", "es_activo": True},
            {"especie": "Perro", "identificador": "DOG-002", "raza": "Mestizo", "es_activo": False},
            {"especie": "Gato", "identificador": "CAT-001", "temperamento": "Curioso"},
        ]
    )

    negocio_service.admitir_animales(zona_perros, animales[:2])
    negocio_service.admitir_animales(zona_gatos, animales[2:])

    consumo_caninos = negocio_service.alimentar_zona(zona_perros)
    print("Consumo de alimento en zona Caninos:", consumo_caninos)

    tarea_service = TareaService()
    voluntario_service = VoluntarioService()

    voluntario = Voluntario("VOL-01", "Ana Perez", apto_medico=True)
    voluntario_service.registrar(voluntario)

    tarea = tarea_service.crear_tarea("TAR-001", "Limpieza de caniles", date.today(), prioridad=1)
    tarea_service.asignar_herramienta("TAR-001", Herramienta("H-01", "Guantes", "Higiene-2025"))
    voluntario_service.asignar_tarea("VOL-01", tarea)

    accion = ConsolaAccion()
    control_salud = ControlSalud(accion)
    control_ocupacion = ControlOcupacion(accion)

    sensor_salud = SensorSalud()
    sensor_ocupacion = SensorOcupacion()
    sensor_salud.subscribe(control_salud)
    sensor_ocupacion.subscribe(control_ocupacion)

    print("Iniciando sensores por 5 segundos...")
    sensor_salud.iniciar()
    sensor_ocupacion.iniciar()
    time.sleep(5)
    sensor_salud.detener()
    sensor_ocupacion.detener()

    registro = negocio_service.generar_registro_rescate(
        refugio,
        responsable="Coordinador General",
        descripcion="Operativo semanal de admisiones",
    )
    print(registro.mostrar_resumen())


if __name__ == "__main__":
    ejecutar_demo()
