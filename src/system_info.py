import json
import platform
import subprocess
from pathlib import Path

import numpy as np
import psutil


def obtener_dato(funcion):
    try:
        valor = funcion()
        if valor is None or valor == "":
            return "No disponible"
        return valor
    except Exception:
        return "No disponible"


def obtener_modelo_gpu():
    resultado = subprocess.run(
        [
            "powershell",
            "-NoProfile",
            "-Command",
            "(Get-CimInstance Win32_VideoController).Name",
        ],
        capture_output=True,
        text=True,
        timeout=10,
    )
    nombre = resultado.stdout.strip()
    if not nombre:
        raise ValueError("No se encontro modelo de GPU")
    return nombre


def obtener_info_sistema():
    return {
        "sistema_operativo": obtener_dato(lambda: f"{platform.system()} {platform.release()}"),
        "arquitectura": obtener_dato(platform.machine),
        "version_python": obtener_dato(platform.python_version),
        "version_numpy": obtener_dato(lambda: np.__version__),
        "modelo_procesador": obtener_dato(platform.processor),
        "nucleos_fisicos": obtener_dato(lambda: psutil.cpu_count(logical=False)),
        "procesadores_logicos": obtener_dato(lambda: psutil.cpu_count(logical=True)),
        "memoria_ram_total": obtener_dato(lambda: psutil.virtual_memory().total),
        "memoria_ram_disponible": obtener_dato(lambda: psutil.virtual_memory().available),
        "modelo_gpu": obtener_dato(obtener_modelo_gpu),
        "disco_total": obtener_dato(lambda: psutil.disk_usage("/").total),
        "disco_disponible": obtener_dato(lambda: psutil.disk_usage("/").free),
    }


def main():
    info = obtener_info_sistema()
    carpeta_datos = Path(__file__).resolve().parent.parent / "data"
    carpeta_datos.mkdir(exist_ok=True)
    archivo_salida = carpeta_datos / "system_info.json"
    with open(archivo_salida, "w", encoding="utf-8") as archivo:
        json.dump(info, archivo, indent=2, ensure_ascii=False)
        archivo.write("\n")


if __name__ == "__main__":
    main()
