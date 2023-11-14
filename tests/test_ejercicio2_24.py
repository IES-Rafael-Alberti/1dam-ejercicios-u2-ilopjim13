import pytest
from src.P2_2.ejercicio2_24 import primosingresados


@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (2 , 1),
    (4 , 0),
    (344 , 0),
    (23 , 1),
    (44 , 0),
    (3 , 1),
    (7 , 1),
    (8 , 0),
    (11 , 1),
    (13 , 1),
    (21 , 0),
    (37 , 1),
    (97 , 1),
    (78 , 0),
    (83 , 1),
    (29 , 1),
    (99 , 0),
    (55 , 0),
    (61 , 1)
    ]
)
def test_primosingresados_params(input_n1, expected):
    assert primosingresados(input_n1, 0) == expected