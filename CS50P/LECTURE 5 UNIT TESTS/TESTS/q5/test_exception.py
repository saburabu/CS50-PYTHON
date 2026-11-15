import pytest
from exceptions import calculate_average as ca

def test_average():
    ave = ca([10, 20, 30])
    assert ave == 20

def tests_single():
    ave = ca([50])
    assert ave == 50

def test_empty():
    with pytest.raises(ValueError):
        ca([])