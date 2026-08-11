import numpy as np
import pytest

from src.mimatmul import mimatmul


def test_resultado_conocido():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    esperado = np.array([[19, 22], [43, 50]])
    np.testing.assert_array_equal(mimatmul(A, B), esperado)


def test_dimensiones_incompatibles():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[1, 2], [3, 4]])
    with pytest.raises(ValueError):
        mimatmul(A, B)


def test_matrices_cuadradas_3x3():
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    esperado = np.array([[30, 24, 18], [84, 69, 54], [138, 114, 90]])
    np.testing.assert_array_equal(mimatmul(A, B), esperado)


def test_matrices_rectangulares():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    esperado = np.array([[38, 44, 50, 56], [83, 98, 113, 128]])
    np.testing.assert_array_equal(mimatmul(A, B), esperado)


def test_comparacion_con_numpy():
    A = np.array([[2.0, -1.0], [0.5, 3.0], [4.0, 1.5]])
    B = np.array([[1.0, 0.0, -2.0], [3.0, 1.0, 0.5]])
    np.testing.assert_allclose(mimatmul(A, B), A @ B)
