import numpy as np


def mimatmul(A, B):
    if A.ndim != 2 or B.ndim != 2:
        raise ValueError("Ambas matrices deben ser de dos dimensiones")
    if A.shape[1] != B.shape[0]:
        raise ValueError(
            "Dimensiones incompatibles: A debe ser (n, k) y B debe ser (k, m)"
        )

    resultado = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                resultado[i, j] += A[i, k] * B[k, j]
    return resultado
