import pytest
from src.P2_1.ejercicio1_3 import division

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
    (2, 4, 0.5),
    (10, 5, 2 ),
    (6, 3, 2 ),
    (19, 4, 4.75 ),
    (567, 78, 7.269230769230769),
    (20, 2 , 10),
    (90, 2, 45 ),
    (107,11, 9.727272727272727)
    ]
)
def test_division_params(input_n1, input_n2, expected):
    assert division(input_n1, input_n2) == expected