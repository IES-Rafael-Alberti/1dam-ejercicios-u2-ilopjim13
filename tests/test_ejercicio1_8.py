import pytest
from src.P2_1.ejercicio1_8 import puntuacion

@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (0.0, "El nivel de rendimiento es inaceptable por lo que la cantidad recibida será de 0 euros."),
    (0.1, "Puntuación errónea"),
    (0.2, "Puntuación errónea"),
    (0.3, "Puntuación errónea"),
    (0.4, "El nivel es aceptable por lo que la cantidad recibida será de 960€."),
    (0.5, "Puntuación errónea"),
    (0.6, "El nivel es meritorio por lo que la cantidad recibida será de 1440€."),
    (0.7, "El nivel es meritorio por lo que la cantidad recibida será de 1680€."),
    (0.8, "El nivel es meritorio por lo que la cantidad recibida será de 1920€."),
    (0.9, "El nivel es meritorio por lo que la cantidad recibida será de 2160€."),
    (1, "El nivel es meritorio por lo que la cantidad recibida será de 2400€."),
    (2, "El nivel es meritorio por lo que la cantidad recibida será de 4800€.")
    ]
)
def test_puntuacion_params(input_n1, expected):
    assert puntuacion(input_n1) == expected