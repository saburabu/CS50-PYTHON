import pytest
from customexcept import InvalidScoreError, check_score as cs

def test_positive():
    assert cs(50) == 50
    assert cs(100) == 100

def test_zero():
    assert cs(0) == 0

def test_invalid():
    with pytest.raises(InvalidScoreError):
        cs(-1)
        cs(101)