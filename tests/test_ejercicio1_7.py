import pytest
from src.P2_1.ejercicio1_7 import impositivo

@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (6254, "Le corresponde un impositivo del 5%"),
    (10526, "Le corresponde un impositivo del 15%"),
    (602345, "Le corresponde un impositivo del 45%"),
    (29344, "Le corresponde un impositivo del 20%"),
    (567, "Le corresponde un impositivo del 5%"),
    (0, "Error"),
    (-90256, "Error"),
    (35070, "Le corresponde un impositivo del 30%"),
    (-785,"Error"),
    (26567, "Le corresponde un impositivo del 20%"),
    (10778, "Le corresponde un impositivo del 15%")
    ]
)
def test_impositivo_params(input_n1, expected):
    assert impositivo(input_n1) == expected