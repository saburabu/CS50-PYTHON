students = [
    {"name": "John", "score": 80},
    {"name": "Mary", "score": 45},
    {"name": "David", "score": 70},
    {"name": "johnny", "score": 50}
]

from listdict import get_passed_students as gps

def test_return():
    passed = gps(students)
    # Only John and David should be in the result
    assert {"name": "John", "score": 80} in passed
    assert {"name": "David", "score": 70} in passed
    assert {"name": "Mary", "score": 45} not in passed
    # And the length should be 2
    assert len(passed) == 3
    
def test_return_50():
    find_50 = gps(students)
    assert {"name": "johnny", "score": 50} in find_50

def test_return_empty():
    student = []
    empty = gps(student)
    assert empty == []

