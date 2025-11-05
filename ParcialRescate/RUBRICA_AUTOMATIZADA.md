# Rubrica Automatizada - PythonRescate

## Checklist CI/CD

- [ ] `python -m compileall` sobre `python_rescate/`
- [ ] `pytest` (cuando existan pruebas)
- [ ] `flake8` para estilo PEP8
- [ ] `mypy` para chequeo de tipos opcional
- [ ] Generacion de `integrador.py` via `buscar_paquete.py`

## Validaciones Clave

1. **Factory Method**
   - `AnimalFactory.crear("Perro", ...)` retorna instancia `Perro`
   - Permite registrar nuevas especies con `AnimalFactory.registrar`

2. **Strategy**
   - `PerroService` selecciona estrategia segun actividad
   - `GatoService` utiliza estrategia generica parametrizada

3. **Observer**
   - `SensorSalud` y `SensorOcupacion` extienden `SensorBase`
   - `ControlSalud` y `ControlOcupacion` implementan `Observer`

4. **Singleton**
   - `RefugioRegistry` garantiza unica instancia compartida

5. **Persistencia**
   - `RegistroRescateService.guardar` crea archivo `.dat`
   - `RegistroRescateService.cargar` devuelve `None` si no existe

## Escenarios Automatizables

- Crear refugio y zona basica, admitir 3 animales, alimentar y persistir registro
- Simular lectura de sensores y verificar ejecucion de acciones correctivas
- Transferir animales entre zonas y validar capacidad resultante
