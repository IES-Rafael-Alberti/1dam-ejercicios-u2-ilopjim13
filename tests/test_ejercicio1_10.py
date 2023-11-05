import pytest
from src.P2_1.ejercicio1_10 import pizzas
from src.P2_1.ejercicio1_10 import ingredientesveganos
from src.P2_1.ejercicio1_10 import ingredientesnoveganos

@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (1, "Estos son los ingredientes vegetarianos: Pimiento y Tofu."),
    (2,"Estos son los ingredientes no vegetarianos: Peperoni, Jamón y Salmón."),
    (6, "Error."),
    (19, "Error."),
    (-6, "Error."),
    (0, "Error."),
    (4, "Error."),
    (-30, "Error."),
    (-5, "Error."),
    (30, "Error.")
    ]
)
def test_pizzas_params(input_n1,  expected):
    assert pizzas(input_n1,) == expected


@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (1, "Su pizza elegida es la vegetariana con pimiento como ingrediente."),
    (2, "Su pizza elegida es la vegetariana con tofu como ingrediente."),
    (6, "Error."),
    (19, "Error."),
    (-6, "Error."),
    (0, "Error."),
    (4, "Error."),
    (-30, "Error."),
    (-5, "Error."),
    (30, "Error.")
    ]
)
def test_ingredientesveganos_params(input_n1,  expected):
    assert ingredientesveganos(input_n1,) == expected


@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (1, "Su pizza elegida es la no vegetariana con peperoni como ingrediente."),
    (2, "Su pizza elegida es la no vegetariana con jamón como ingrediente."),
    (3, "Su pizza elegida es la no vegetariana con salmón como ingrediente."),
    (19, "Error."),
    (-6, "Error."),
    (0, "Error."),
    (4, "Error."),
    (-30, "Error."),
    (-5, "Error."),
    (30, "Error.")
    ]
)
def test_ingredientesnoveganos_params(input_n1,  expected):
    assert ingredientesnoveganos(input_n1,) == expected