import pytest
from boss import add_student, find_student, get_passed_students, InvalidScoreError

# --- Fixture ---
@pytest.fixture
def empty_students():
    """Provides a fresh empty student list for each test."""
    return []

# --- A. add_student() ---
def test_add_student_correctly_adds(empty_students):
    student = add_student(empty_students, "Alice", 75)
    assert student == {"name": "Alice", "score": 75}
    assert student in empty_students

# --- B. Boundary values ---
@pytest.mark.parametrize("score", [0, 50, 100])
def test_add_student_boundary_values(empty_students, score):
    student = add_student(empty_students, "Boundary", score)
    assert student["score"] == score
    assert student in empty_students

# --- C. Invalid scores ---
@pytest.mark.parametrize("score", [-1, 101])
def test_add_student_invalid_scores(empty_students, score):
    with pytest.raises(InvalidScoreError):
        add_student(empty_students, "Invalid", score)

# --- D. find_student() ---
def test_find_existing_student(empty_students):
    add_student(empty_students, "Bob", 60)
    found = find_student(empty_students, "Bob")
    assert found == {"name": "Bob", "score": 60}

def test_find_nonexistent_student(empty_students):
    add_student(empty_students, "Charlie", 40)
    assert find_student(empty_students, "Nonexistent") is None

# --- E. get_passed_students() ---
def test_get_passed_students():
    students = [
        {"name": "John", "score": 80},
        {"name": "Mary", "score": 45},
        {"name": "David", "score": 50},
    ]
    passed = get_passed_students(students)
    names = [s["name"] for s in passed]
    assert "John" in names
    assert "David" in names
    assert "Mary" not in names
