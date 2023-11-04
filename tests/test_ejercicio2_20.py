import pytest
from src.P2_2.ejercicio2_20 import coincide

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
    ("hola", "a", 4),
    ("agua", "a", 1),
    ("teclado", "e", 2),
    ("ordenador", "o", 1),
    ("monitor", "i", 4),
    ("sala", "i", "No existe coincidencias en esta posicion 'sala'"),
    ("maraca", "a", 2),
    ("retrete", "e", 2),
    ("comida", "i", 4),
    ("moto", "o", 2),
    ("clase", "e", 5),
    ("pala", "e", "No existe coincidencias en esta posicion 'pala'"),
    ("aula", "u", 2),
    ("cuarto", "u", 2),
    ("calor", "a", 2),
    ("funcion", "o", 6),
    ("wifi", "i", 2),
    ("csgo", "o", 4),
    ("vscode", "e", 6),
    ("musica", "i", 4)
    ]
)
def test_coincide_params(input_n1, input_n2, expected):
    assert coincide(input_n1, input_n2) == expected