import pytest
from src.P2_1.ejercicio1_4 import pares

@pytest.mark.parametrize(
    "input_n1,expected",
    [
    (45, "El número es impar."),
    (10, "El número es par."),
    (76, "El número es par."),
    (19, "El número es impar."),
    (146, "El número es par."),
    (34, "El número es par."),
    (3, "El número es impar."),
    (58, "El número es par.")
    ]
)
def test_pares_params(input_n1, expected):
    assert pares(input_n1) == expected