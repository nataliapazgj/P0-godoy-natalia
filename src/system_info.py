import json
import platform
from pathlib import Path

import numpy as np
import psutil


def obtener_dato(funcion):
    try:
        return funcion()
    except Exception:
        return "No disponible"


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
