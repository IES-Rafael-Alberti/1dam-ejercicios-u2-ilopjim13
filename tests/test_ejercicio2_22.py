import pytest
from src.P2_2.ejercicio2_22 import digitospares

@pytest.mark.parametrize(
    "input_n1, expected",
    [
    ("23", "1 1"),
    ("534", "1 2"),
    ("64232", "4 1"),
    ("76", "1 1"),
    ("55", "0 2"),
    ("53", "0 2"),
    ("11", "0 2"),
    ("-3", "Error."),
    ("4", "1 0"),
    ("-6", "Error."),
    ("44", "2 0"),
    ("90", "0 1"),
    ("70", "0 1"),
    ("60", "1 0"),
    ("-425", "Error."),
    ("45", "1 1"),
    ("20", "1 0"),
    ("89", "1 1"),
    ("15", "0 2")
    ]
)
def test_digitospares_params(input_n1, expected):
    assert digitospares(input_n1) == expected