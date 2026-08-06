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
