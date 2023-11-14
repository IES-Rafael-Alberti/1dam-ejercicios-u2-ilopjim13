import pytest
from src.P2_1.ejercicio1_2 import pasar

@pytest.mark.parametrize(
    "input_n1, expected",
    [
    ("contraseña", "La contraseña es correcta."),
    ("Contraseña", "La contraseña es incorrecta"),
    ("cOntraseña", "La contraseña es incorrecta"),
    ("contraseñA", "La contraseña es incorrecta"),
    ("coNtraseña", "La contraseña es incorrecta"),
    ("cOntraseña", "La contraseña es incorrecta"),
    ("conTraseña", "La contraseña es incorrecta"),
    ("contRaseña", "La contraseña es incorrecta"),
    ("contraSeña", "La contraseña es incorrecta"),
    ("aguacate", "La contraseña es incorrecta")
    ]
)
def test_pasar_params(input_n1, expected):
    assert pasar(input_n1) == expected