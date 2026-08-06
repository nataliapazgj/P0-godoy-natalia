# P0-godoy-natalia

Proyecto 0 de la materia. El propósito general del Proyecto 0 es poner en práctica el
trabajo con repositorios, ambientes virtuales de Python, automatización de tareas y
análisis de datos del computador (CPU, memoria, disco) sobre un equipo real.

## Entorno

- Sistema operativo: Windows
- Versión de Python: 3.11.13

## Configuración del ambiente virtual

Crear el ambiente virtual (desde la raíz del repositorio, en PowerShell):

```powershell
python -m venv .venv
```

Activar el ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias desde `requirements.txt`:

```powershell
pip install -r requirements.txt
```

> Nota: si PowerShell bloquea la activación por la política de ejecución, usar:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

## Ejecución

Generar la información del computador en `data/system_info.json`:

```powershell
python src/system_info.py
```

Ejecutar las pruebas:

```powershell
python -m pytest
```

## Estado actual del proyecto

- Ambiente virtual configurado con las dependencias instaladas.
- Implementado `src/system_info.py`, que obtiene datos reales del computador y los
  guarda en `data/system_info.json`.
- Generado `data/system_info.json` con datos reales del computador.
- Implementado `src/mimatmul.py` (multiplicación de matrices con ciclos explícitos).
- Existen dos pruebas iniciales en `tests/test_mimatmul.py`, ambas aprobadas.
