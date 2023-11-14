import pytest
from src.P2_2.ejercicio2_10 import primos

@pytest.mark.parametrize(
    "input_n1,expected",
    [
    (2, "Es primo"),
    (53, "Es primo"),
    (10, "No es primo"),
    (4, "No es primo"),
    (659, "Es primo"),
    (-45, "Error."),
    (8, "No es primo"),
    (3, "Es primo"),
    (-5, "Error."),
    (7, "Es primo"),
    (101, "Es primo"),
    (13, "Es primo"),
    (19, "Es primo"),
    (0, "Error."),
    (2, "Es primo")
    ]
)
def test_primos_params(input_n1, expected):
    assert primos(input_n1) == expected