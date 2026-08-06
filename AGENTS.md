# AGENTS.md

Instrucciones permanentes para trabajar en este repositorio con OpenCode (u otros
agentes de IA).

## Reglas generales

- Mantener el código sencillo y fácil de explicar. Evitar soluciones excesivamente
  complejas o difíciles de justificar.
- No inventar mediciones del computador (CPU, memoria, disco, benchmarks). Los datos
  solo deben obtenerse midiendo de forma real en el equipo.
- Conservar los datos originales: no sobrescribir ni perder los datos obtenidos.
- Ejecutar `pytest` después de modificar código para verificar que todo siga pasando.
- No crear matrices tan grandes que puedan agotar la memoria del equipo.
- No subir credenciales, archivos `.env` ni el ambiente virtual (`.venv`).
- No ejecutar comandos destructivos de Git como `git reset --hard`.
- No hacer `git commit` ni `git push` sin autorización explícita.
- Mostrar los cambios al usuario (por ejemplo con `git diff`) antes de que los confirme.

## Comandos de verificación

- Ejecutar todos los tests:

  ```powershell
  .venv\Scripts\python.exe -m pytest
  ```

- Ver los cambios sin confirmar:

  ```powershell
  git status
  git diff
  ```

## Estructura del repositorio

- `README.md`: descripción y guía del proyecto.
- `requirements.txt`: dependencias de Python.
- `src/`: scripts de Python del proyecto.
- `data/`: datos generados (resultados de mediciones).
- `tests/`: pruebas automatizadas (pytest).
