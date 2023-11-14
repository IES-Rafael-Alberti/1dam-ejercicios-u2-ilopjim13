import pytest
from src.P2_2.ejercicio2_17 import sumadigitos

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
    ("90", 9),
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
def test_sumadigitos_params(input_n1, expected):
    assert sumadigitos(input_n1) == expected