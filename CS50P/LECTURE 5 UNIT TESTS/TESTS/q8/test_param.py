import pytest
from param import multiply as M

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (5, 4, 20),
        (10, 0, 0),
        (-2, 5, -10),
        (7, 7, 49)
    ]
)

def test_multiply(a, b, expected):
    assert M(a, b) == expected
    