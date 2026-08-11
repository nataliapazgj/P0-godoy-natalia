import csv
import sys
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.mimatmul import mimatmul

TAMANOS = [25, 50, 75, 100]
REPETICIONES = 3


def crear_matrices(tamano, rng):
    return rng.random((tamano, tamano), dtype=np.float64), rng.random(
        (tamano, tamano), dtype=np.float64
    )


def medir(funcion, matrices):
    tiempos = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        funcion(matrices[0], matrices[1])
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return tiempos


def main():
    rng = np.random.default_rng(42)
    filas = []
    tiempos_mimatmul = {}
    tiempos_numpy = {}

    for tamano in TAMANOS:
        matrices = crear_matrices(tamano, rng)

        medir(mimatmul, matrices)
        medir(lambda a, b: a @ b, matrices)

        for metodo, funcion, destino in (
            ("mimatmul", mimatmul, tiempos_mimatmul),
            ("numpy", lambda a, b: a @ b, tiempos_numpy),
        ):
            tiempos = medir(funcion, matrices)
            destino[tamano] = tiempos
            for repeticion, tiempo in enumerate(tiempos, start=1):
                filas.append(
                    {
                        "metodo": metodo,
                        "tamano": tamano,
                        "repeticion": repeticion,
                        "tiempo": tiempo,
                    }
                )

    raiz = Path(__file__).resolve().parent.parent
    carpeta_datos = raiz / "data"
    carpeta_datos.mkdir(exist_ok=True)
    archivo_csv = carpeta_datos / "benchmark_results.csv"
    with open(archivo_csv, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(
            archivo, fieldnames=["metodo", "tamano", "repeticion", "tiempo"]
        )
        escritor.writeheader()
        escritor.writerows(filas)

    carpeta_figuras = raiz / "figures"
    carpeta_figuras.mkdir(exist_ok=True)

    for metodo, datos, estilo in (
        ("mimatmul", tiempos_mimatmul, "-o"),
        ("numpy", tiempos_numpy, "-s"),
    ):
        promedios = [sum(datos[t]) / len(datos[t]) for t in TAMANOS]
        plt.plot(TAMANOS, promedios, estilo, label=metodo)

    plt.xlabel("Tamaño de matriz")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Benchmark: mimatmul vs NumPy")
    plt.legend()
    plt.savefig(carpeta_figuras / "benchmark.png")


if __name__ == "__main__":
    main()
