# Historias de Usuario - Sistema de Gestion de Rescate Animal

**Proyecto**: PythonRescate  
**Version**: 1.0.0  
**Fecha**: Octubre 2025  
**Metodologia**: User Story Mapping

---

## Indice

1. [Epic 1: Gestion de Refugios y Zonas](#epic-1-gestion-de-refugios-y-zonas)
2. [Epic 2: Gestion de Animales](#epic-2-gestion-de-animales)
3. [Epic 3: Monitoreo y Alertas](#epic-3-monitoreo-y-alertas)
4. [Epic 4: Gestion de Personal](#epic-4-gestion-de-personal)
5. [Epic 5: Operativos de Rescate](#epic-5-operativos-de-rescate)
6. [Historias Tecnicas (Patrones de Diseno)](#historias-tecnicas-patrones-de-diseno)

---

## Epic 1: Gestion de Refugios y Zonas

### US-001: Registrar Refugio

**Como** coordinador general  
**Quiero** registrar un nuevo refugio con sus datos basicos  
**Para** centralizar la administracion de recursos

#### Criterios de Aceptacion

- [x] Debe permitir definir nombre y domicilio del refugio
- [x] Al registrarse se guarda en `RefugioRegistry`
- [x] Se inicializan recursos globales de agua y alimento

#### Detalles Tecnicos

- **Clase**: `Refugio` (`python_rescate/entidades/instalaciones/refugio.py`)
- **Servicio**: `RefugioService` (`python_rescate/servicios/instalaciones/refugio_service.py`)

```python
from python_rescate.servicios.instalaciones.refugio_service import RefugioService

refugio_service = RefugioService()
refugio = refugio_service.crear_refugio(
    nombre="Huellitas", domicilio="Av. Siempre Viva 742"
)
```

---

### US-002: Crear Zona de Alojamiento

**Como** coordinador de refugio  
**Quiero** crear zonas internas con recursos asociados  
**Para** alojar animales de forma ordenada

#### Criterios de Aceptacion

- [x] La zona define capacidad maxima y recursos iniciales
- [x] Se valida que la capacidad sea positiva
- [x] Debe permitir alojar y retirar animales

#### Detalles Tecnicos

- **Clase**: `Zona` (`python_rescate/entidades/instalaciones/zona.py`)
- **Servicio**: `ZonaService` (`python_rescate/servicios/instalaciones/zona_service.py`)

---

## Epic 2: Gestion de Animales

### US-003: Ingresar Animal Rescatado

**Como** voluntario de admision  
**Quiero** ingresar animales mediante una factory  
**Para** asegurar instanciacion estandarizada

#### Criterios de Aceptacion

- [x] Se crean animales via `AnimalFactory`
- [x] Se asigna identificador unico por especie
- [x] Se valida agua y espacio inicial positivo
- [x] La zona debe tener capacidad disponible

```python
animales = negocio_service.crear_animales([
    {"especie": "Perro", "identificador": "DOG-001", "raza": "Labrador", "es_activo": True},
    {"especie": "Gato", "identificador": "CAT-002", "temperamento": "Sereno"},
])
negocio_service.admitir_animales(zona_service, animales)
```

---

### US-004: Alimentar Animales por Estrategia

**Como** cuidador  
**Quiero** alimentar animales segun estrategias  
**Para** respetar requerimientos nutricionales

#### Criterios de Aceptacion

- [x] Cada especie tiene una estrategia de alimentacion
- [x] Perros activos consumen mas raciones
- [x] Se descuenta el recurso alimento de la zona
- [x] Si no hay recurso suficiente se lanza `RecursoInsuficienteException`

---

## Epic 3: Monitoreo y Alertas

### US-005: Recibir Alertas de Salud

**Como** veterinario de guardia  
**Quiero** recibir alertas cuando la salud promedio baje  
**Para** actuar de inmediato

#### Criterios de Aceptacion

- [x] Sensor de salud publica valores entre 0 y 100
- [x] ControlSalud dispara alerta si la lectura es menor a 60
- [x] Las alertas ejecutan una accion correctiva configurada

#### Detalles Tecnicos

- **Sensor**: `SensorSalud` (`python_rescate/monitoreo/sensores.py`)
- **Observer**: `ControlSalud` (`python_rescate/monitoreo/control_salud.py`)

---

### US-006: Controlar Ocupacion

**Como** coordinador logistico  
**Quiero** recibir notificaciones de ocupacion alta  
**Para** redistribuir animales entre zonas

#### Criterios de Aceptacion

- [x] Sensor de ocupacion retorna valores de 0.0 a 1.0
- [x] ControlOcupacion alerta si supera 80%
- [x] La accion correctiva detalla el porcentaje ocupacional

---

## Epic 4: Gestion de Personal

### US-007: Registrar Voluntario

**Como** coordinador de voluntarios  
**Quiero** registrar voluntarios con apto medico  
**Para** asignar tareas de cuidado

#### Criterios de Aceptacion

- [x] Se almacena identificador, nombre y apto medico
- [x] Si no tiene apto medico, no puede recibir tareas
- [x] Permite marcar tareas como completadas

---

### US-008: Planificar Tareas

**Como** responsable operativo  
**Quiero** crear tareas con prioridad y herramientas  
**Para** organizar el trabajo diario

#### Criterios de Aceptacion

- [x] Las tareas incluyen prioridad, descripcion y fecha
- [x] Se pueden asignar multiples herramientas certificadas
- [x] Se listan ordenadas por prioridad

---

## Epic 5: Operativos de Rescate

### US-009: Generar Registro Oficial

**Como** auditor municipal  
**Quiero** generar un registro completo del operativo  
**Para** guardar trazabilidad de cada rescate

#### Criterios de Aceptacion

- [x] Se calcula la cantidad total de animales alojados
- [x] Se persiste en disco dentro de `data/`
- [x] Se puede recuperar posteriormente con `RegistroRescateService`

---

### US-010: Transferir Animales Entre Zonas

**Como** coordinador logistico  
**Quiero** transferir animales entre zonas  
**Para** balancear recursos y capacidades

#### Criterios de Aceptacion

- [x] Se retiran animales del origen y se alojan en destino
- [x] Se valida capacidad en la zona destino
- [x] El proceso es atomico: si falla se detiene la transferencia

---

## Historias Tecnicas (Patrones de Diseno)

### US-T01: Registrar Nuevas Especies

**Como** desarrollador  
**Quiero** agregar nuevas especies sin modificar codigo existente  
**Para** mantener el sistema abierto a extension

- [x] Registrar constructor en `AnimalFactory`
- [x] Implementar servicio especifico si requiere estrategia propia
- [x] Agregarlo al `AnimalServiceRegistry`

### US-T02: Persistir Registros

**Como** desarrollador  
**Quiero** reutilizar la infraestructura de Pickle  
**Para** almacenar registros de rescate sin esfuerzo adicional

- [x] Utilizar `RegistroRescateService`
- [x] Definir ruta personalizada opcional
- [x] Manejar ausencia de archivos devolviendo `None`
