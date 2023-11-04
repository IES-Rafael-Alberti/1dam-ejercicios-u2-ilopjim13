import pytest
from src.P2_2.ejercicio2_11 import deletrear

@pytest.mark.parametrize(
    "input_n1,expected",
    [
    ("hola", "aloh"),
    ("agua", "auga"),
    ("teclado", "odalcet"),
    ("ordenador", "rodanedro"),
    ("monitor", "rotinom"),
    ("comida", "adimoc"),
    ("clase", "esalc"),
    ("aula", "alua"),
    ("cuarto", "otrauc"),
    ("calor", "rolac"),
    ("funcion", "noicnuf"),
    ("wifi", "ifiw"),
    ("csgo", "ogsc"),
    ("vscode", "edocsv"),
    ("musica", "acisum")
    ]
)
def test_deletrear_params(input_n1, expected):
    assert deletrear(input_n1) == expected