import pytest
from src.P2_2.ejercicio2_18 import sumadigitospositivos

@pytest.mark.parametrize(
    "input_n1, expected",
    [
    ("45", 9),
    ("23", 5),
    ("24", 6),
    ("2456", 17),
    ("1111", 4),
    ("0", 0),
    ("12", 3),
    ("67", 13),
    (-3, "Error."),
    ("20", 2),
    ("24", 6),
    ("44", 8),
    ("22", 4),
    ("11", 2),
    ("88", 16),
    ("77", 14),
    ("22484", 20),
    ("8888", 32),
    ("908", 17),
    ("222222", 12)
    ]
)
def test_sumadigitospositivos_params(input_n1, expected):
    assert sumadigitospositivos(input_n1) == expected