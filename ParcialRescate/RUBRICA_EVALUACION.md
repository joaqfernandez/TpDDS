# Rubrica de Evaluacion - PythonRescate

## 1. Arquitectura (30 pts)

| Criterio | Descripcion | Puntos |
|----------|-------------|--------|
| Separacion de capas | Entidades, servicios y patrones separados | 10 |
| Principios SOLID | Respeto por SRP, OCP e ISP | 10 |
| Inyeccion de dependencias | Servicios reciben dependencias por constructor | 10 |

## 2. Patrones de Diseno (25 pts)

| Criterio | Descripcion | Puntos |
|----------|-------------|--------|
| Factory Method | Uso de `AnimalFactory` con registro dinamico | 8 |
| Strategy | Estrategias de alimentacion por especie | 8 |
| Observer | Sensores y controles implementados con generics | 5 |
| Singleton | `RefugioRegistry` compartido en todo el sistema | 4 |

## 3. Dominio y Negocio (20 pts)

| Criterio | Descripcion | Puntos |
|----------|-------------|--------|
| Modelado de entidades | Animales, zonas y personal con validaciones | 10 |
| Servicios de negocio | `RefugioNegocioService` orquesta operaciones | 10 |

## 4. Persistencia y Datos (10 pts)

| Criterio | Descripcion | Puntos |
|----------|-------------|--------|
| Persistencia | Pickle para registros de rescate | 5 |
| Integridad | Manejo de recursos insuficientes | 5 |

## 5. Documentacion y Codigo (15 pts)

| Criterio | Descripcion | Puntos |
|----------|-------------|--------|
| Documentacion | README y historias completas | 5 |
| Estilo | Cumplimiento PEP8 y nombres descriptivos | 5 |
| Demostracion | `main.py` recorre flujo completo | 5 |

**Total**: 100 puntos
