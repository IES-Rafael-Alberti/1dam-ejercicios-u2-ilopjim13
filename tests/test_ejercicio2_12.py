import pytest
from src.P2_2.ejercicio2_12 import letra

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
    ("hola", "a", 1),
    ("agua", "a", 2),
    ("teclado", "e", 1),
    ("ordenador", "o", 2),
    ("monitor", "i", 1),
    ("sala", "i", 0),
    ("maraca", "a", 3),
    ("retrete", "e", 3),
    ("comida", "i", 1),
    ("moto", "o", 2),
    ("clase", "e", 1),
    ("pala", "e", 0),
    ("aula", "u", 1),
    ("cuarto", "u", 1),
    ("calor", "a", 1),
    ("funcion", "o", 1),
    ("wifi", "i", 2),
    ("csgo", "o", 1),
    ("vscode", "e", 1),
    ("musica", "i", 1)
    ]
)
def test_letra_params(input_n1,input_n2, expected):
    assert letra(input_n1,input_n2) == expected