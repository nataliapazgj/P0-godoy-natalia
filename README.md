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
.venv\Scripts\Activate.ps1
```

Instalar las dependencias desde `requirements.txt`:

```powershell
pip install -r requirements.txt
```

> Nota: si PowerShell bloquea la activación por la política de ejecución, usar:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

## Estado actual del proyecto

- Ambiente virtual configurado con las dependencias instaladas.
- Comienzo de la entrega P0E1 del Proyecto 0.
- Aún no se reportan resultados, benchmarks ni datos del computador: se incorporarán
  solo cuando sean medidos de forma real en el equipo.
