import pytest
from src.P2_1.ejercicio1_1 import mayoredad

@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (6, "Eres menor de edad."),
    (18, "Eres mayor de edad."),
    (3, "Eres menor de edad."),
    (86, "Eres mayor de edad."),
    (2, "Eres menor de edad."),
    (54, "Eres mayor de edad."),
    (8, "Eres menor de edad."),
    (25, "Eres mayor de edad."),
    (7, "Eres menor de edad."),
    (46, "Eres mayor de edad."),
    (-46, "Error.")
    ]
)
def test_mayoredad_params(input_n1, expected):
    assert mayoredad(input_n1) == expected