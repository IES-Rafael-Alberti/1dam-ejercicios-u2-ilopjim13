import pytest
from src.P2_1.ejercicio1_6 import curso

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
    ("maria", "mujer", "Estas en el grupo B."),
    ("manuela", "hombre", "Estas en el grupo B."),
    ("nico", "hombre", "Estas en el grupo A."),
    ("sara", "mujer", "Estas en el grupo B."),
    ("alba", "mujer", "Estas en el grupo A."),
    ("jose", "hombre", "Estas en el grupo B."),
    ("elias", "mujer", "Estas en el grupo A."),
    ("fran", "mujer", "Estas en el grupo A."),
    ("cesar", "mujer", "Estas en el grupo A."),
    ("emilia", "mujer", "Estas en el grupo A."),
    ("paco", "hombre", "Estas en el grupo A.")
    ]
)
def test_curso_params(input_n1, input_n2, expected):
    assert curso(input_n1, input_n2) == expected