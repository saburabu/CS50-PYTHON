import pytest
from fix import calculate_total as CT

@pytest.fixture
def student():
    return {
    "name": "Sabur",
    "score": 80,
    "bonus": 10
}

def test_name(student):
    assert student['name'] == "Sabur"
    
def test_calc(student):
    assert CT(student) == 90

