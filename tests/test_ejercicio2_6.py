import pytest
from src.P2_2.ejercicio2_6 import triangulo

@pytest.mark.parametrize(
    "input_n1,expected",
    [
    (2, "**"),
    (5, "*****"),
    (10, "**********"),
    (4, "****"),
    (6, "******"),
    (-45, "Error."),
    (8, "********"),
    (3, "***"),
    (-5, "Error."),
    (7, "*******"),
    (11, "***********"),
    (13, "*************"),
    (15, "***************"),
    (0, "Error."),
    (1, "*")
    ]
)
def test_triangulo_params(input_n1, expected):
    assert triangulo(input_n1) == expected