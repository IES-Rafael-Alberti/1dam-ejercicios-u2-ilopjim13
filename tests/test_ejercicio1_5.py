import pytest
from src.P2_1.ejercicio1_5 import tributar

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
    (56, 378, "No puedes tributar."),
    (10, 10000, "No puedes tributar."),
    (16, 30500, "Puedes tributar."),
    (67, 402, "No puedes tributar."),
    (36, 10000, "Puedes tributar."),
    (24, 24215 , "Puedes tributar."),
    (82, 290, "No puedes tributar."),
    (44, 110, "No puedes tributar."),
    (-29, 11000, "Error."),
    (15, 10493, "No puedes tributar."),
    (59, -78934, "Error.")
    ]
)
def test_tributar_params(input_n1, input_n2, expected):
    assert tributar(input_n1, input_n2) == expected