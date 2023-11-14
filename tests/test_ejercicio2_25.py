import pytest
from src.P2_2.ejercicio2_25 import separador

@pytest.mark.parametrize(
    "input_n1, expected",
    [
    ("hola que tal", "La palabra mas larga es 'hola' de 4 palabras"),
    ("no se que poner", "La palabra mas larga es 'poner' de 5 palabras"),
    ("palabras para probar", "La palabra mas larga es 'palabras' de 8 palabras"),
    ("me pica la mano", "La palabra mas larga es 'pica' de 4 palabras"),
    ("son las 6 de la mañana ayuda", "La palabra mas larga es 'mañana' de 6 palabras"),
    ("me encantan las pruebas unitarias", "La palabra mas larga es 'unitarias' de 9 palabras"),
    ("ola hola bola", "La palabra mas larga es 'hola' de 4 palabras"),
    ("aguacates en salsa", "La palabra mas larga es 'aguacates' de 9 palabras"),
    ("tengo hambre", "La palabra mas larga es 'hambre' de 6 palabras"),
    ("hace frio en la calle", "La palabra mas larga es 'calle' de 5 palabras"),
    ("a no ser", "La palabra mas larga es 'ser' de 3 palabras"),
    ("estoy cansado", "La palabra mas larga es 'cansado' de 7 palabras"),
    ("me quedan solo dos pruebas mas", "La palabra mas larga es 'pruebas' de 7 palabras"),
    ("ya mismo termino ahhhh", "La palabra mas larga es 'termino' de 7 palabras"),
    ("tomateconlimon es mejor que espinacasconacelgas", "La palabra mas larga es 'espinacasconacelgas' de 19 palabras"),
    ("ah oh uh", "La palabra mas larga es 'ah' de 2 palabras"),
    ("me aburro", "La palabra mas larga es 'aburro' de 6 palabras"),
    ("no ce que mas poner xd", "La palabra mas larga es 'poner' de 5 palabras"),
    ("esta es la ultima vamooos", "La palabra mas larga es 'vamooos' de 7 palabras")
    ]
)
def test_separador_params(input_n1, expected):
    assert separador(input_n1) == expected