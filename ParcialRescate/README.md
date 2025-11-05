# Sistema de Gestion de Rescate Animal

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

Plataforma educativa que reproduce la arquitectura y los patrones del proyecto original, adaptados al dominio de los refugios de animales rescatados.

---

## Tabla de Contenidos

- [Contexto del Dominio](#contexto-del-dominio)
- [Caracteristicas Principales](#caracteristicas-principales)
- [Arquitectura del Sistema](#arquitectura-del-sistema)
- [Patrones de Diseno Implementados](#patrones-de-diseno-implementados)
- [Requisitos del Sistema](#requisitos-del-sistema)
- [Instalacion](#instalacion)
- [Uso del Sistema](#uso-del-sistema)
- [Exportacion para Descarga](#exportacion-para-descarga)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Modulos del Sistema](#modulos-del-sistema)
- [Documentacion Tecnica](#documentacion-tecnica)
- [Testing y Validacion](#testing-y-validacion)
- [Contribucion](#contribucion)
- [Licencia](#licencia)

---

## Contexto del Dominio

### Problema que Resuelve

El sistema **PythonRescate** aborda la coordinacion integral de refugios para animales rescatados.

1. **Gestion de Ingresos y Alojamiento**
   - Alta de animales de distintas especies
   - Control de capacidad y recursos por zona del refugio
   - Registro de historiales medicos

2. **Monitoreo de Condiciones**
   - Sensores simulados de salud y ocupacion
   - Alertas automaticas mediante Observer
   - Reaccion inmediata con acciones correctivas

3. **Gestion de Personal Voluntario**
   - Control de apto medico
   - Asignacion de tareas con prioridades
   - Herramientas certificadas por tarea

4. **Operativos de Rescate**
   - Planificacion y transferencia de animales entre zonas
   - Generacion de registros oficiales persistidos en disco
   - Reportes de recursos disponibles

5. **Trazabilidad y Auditoria**
   - Persistencia de registros con Pickle
   - Registro global de refugios via Singleton
   - Historial de monitoreo centralizado

### Actores del Sistema

- **Coordinador del Refugio**: Administra recursos y personal
- **Voluntario**: Ejecuta tareas y atiende animales
- **Veterinario**: Supervisa salud y tratamientos
- **Sistema de Monitoreo**: Publica eventos de salud y ocupacion
- **Auditor**: Consulta registros de rescate almacenados

### Flujo de Operaciones Tipico

```
1. REGISTRO --> Se crea el refugio y sus zonas
2. ADMISION --> Se admiten animales creados por la factory
3. MONITOREO --> Sensores publican lecturas de salud y ocupacion
4. REACCION --> Observadores generan alertas correctivas
5. CUIDADO --> Servicios alimentan e hidratan a cada animal
6. PERSONAL --> Voluntarios ejecutan tareas priorizadas
7. RESCATE --> Se generan registros oficiales persistidos
```

---

## Caracteristicas Principales

### Funcionalidades del Sistema

#### 1. Gestion de Animales

- **Creacion dinamica** de Perros, Gatos, Aves y Reptiles via Factory
- **Estrategias de alimentacion** configurables segun especie y actividad
- **Historial medico** por animal con registros de controles

#### 2. Monitoreo Inteligente

- **Sensores en tiempo real** (Observer generico)
- **Control de salud** y **control de ocupacion**
- **Acciones correctivas** desencadenadas automaticamente

#### 3. Gestion de Personal

- **Voluntarios con apto medico** obligatorio
- **Tareas priorizadas** con herramientas certificadas
- **Registro de veterinarios** habilitados

#### 4. Gestion de Refugios y Zonas

- **Refugio** con recursos globales (agua y alimento)
- **Zonas** configurables con capacidad y recursos propios
- **Transferencia de animales** entre zonas con validaciones

#### 5. Operaciones de Negocio

- **Admisiones masivas** y alimentacion centralizada
- **Generacion de registros de rescate** persistibles
- **Resumenes de recursos** para auditoria

#### 6. Persistencia de Datos

- **Serializacion con Pickle** de registros oficiales
- **Directorio configurable** para archivos
- **Validaciones** ante recursos insuficientes

---

## Arquitectura del Sistema

### Principios Arquitectonicos

- **SRP**: Entidades enfocadas en datos, servicios en logica
- **OCP**: Nuevas especies se agregan registrando estrategias
- **LSP**: Todos los animales derivan de `Animal`
- **ISP**: Estrategias y observadores con interfaces especificas
- **DIP**: Servicios dependen de abstracciones (Strategy, Observer)

### Separacion de Capas

```
+-------------------------------+
|        PRESENTACION           |
|  main.py - Demostracion CLI   |
+-------------------------------+
             |
             v
+-------------------------------+
|      SERVICIOS DE NEGOCIO     |
|  RefugioNegocioService        |
+-------------------------------+
             |
             v
+-------------------------------+
|      SERVICIOS DE DOMINIO     |
|  ZonaService, AnimalServices  |
+-------------------------------+
             |
             v
+-------------------------------+
|           ENTIDADES           |
|  Animal, Zona, Voluntario     |
+-------------------------------+
             |
             v
+-------------------------------+
|      PATRONES / UTILIDADES    |
|  Factory, Strategy, Observer  |
+-------------------------------+
```

### Inyeccion de Dependencias

Se realiza manualmente pasando instancias de servicios y estrategias en los constructores.

---

## Patrones de Diseno Implementados

1. **Factory Method**: `AnimalFactory`
2. **Strategy**: `PlanAlimentacionStrategy` y derivados
3. **Observer**: Sensores y controles de monitoreo
4. **Singleton**: `RefugioRegistry`
5. **Template Method**: Aplicado en `AnimalService` para alimentacion/hidratacion

Cada patron replica el enfoque del proyecto original pero adaptado al dominio animal.

---

## Requisitos del Sistema

- Python 3.13+
- Sistema operativo con soporte para hilos

---

## Instalacion

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt  # No requerido para la demo basica
```

---

## Uso del Sistema

```bash
python main.py
```

El script principal ejecuta un flujo completo de admision, monitoreo y generacion de registros.

---

## Exportacion para Descarga

Para generar un unico archivo ZIP listo para entregar o compartir:

```bash
python descargar_proyecto.py --salida ParcialRescate.zip
```

El script empaqueta todo el directorio del parcial excluyendo carpetas temporales.

---

## Estructura del Proyecto

```
ParcialRescate/
├── data/
├── main.py
├── buscar_paquete.py
├── README.md
├── USER_STORIES.md
├── RUBRICA_AUTOMATIZADA.md
├── RUBRICA_EVALUACION.md
└── python_rescate/
    ├── entidades/
    ├── servicios/
    ├── patrones/
    ├── monitoreo/
    └── excepciones/
```

---

## Modulos del Sistema

- `entidades.animales`: Modelos de animales y seguimiento medico
- `entidades.personal`: Voluntarios, veterinarios y tareas
- `entidades.instalaciones`: Refugio, zonas y registros
- `servicios`: Capa de logica aplicada y orquestacion
- `patrones`: Implementaciones reutilizables
- `monitoreo`: Sensores y observadores

---

## Documentacion Tecnica

- [Historias de Usuario](USER_STORIES.md)
- [Rubrica de Evaluacion](RUBRICA_EVALUACION.md)
- [Rubrica Automatizada](RUBRICA_AUTOMATIZADA.md)

---

## Testing y Validacion

- Pruebas manuales mediante ejecucion de `main.py`
- Validacion de patrones mediante revisiones de codigo

---

## Contribucion

1. Fork del repositorio
2. Crear rama de feature
3. Seguir el estandar PEP8
4. Enviar Pull Request con descripcion detallada

---

## Licencia

Proyecto educativo liberado bajo licencia MIT.
