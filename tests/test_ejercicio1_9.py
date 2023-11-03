import pytest
from src.P2_1.ejercicio1_9 import entrada

@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (2, "La entrada es gratis"),
    (10,"Debe pagar 5€ por la entrada."),
    (6, "Debe pagar 5€ por la entrada."),
    (19, "Debe pagar 10€ por la entrada."),
    (56, "Debe pagar 10€ por la entrada."),
    (20,"Debe pagar 10€ por la entrada."),
    (4, "Debe pagar 5€ por la entrada."),
    (0, "Error"),
    (-30, "Error"),
    (-5, "Error"),
    (30, "Debe pagar 10€ por la entrada.")
    ]
)
def test_entrada_params(input_n1,  expected):
    assert entrada(input_n1,) == expected