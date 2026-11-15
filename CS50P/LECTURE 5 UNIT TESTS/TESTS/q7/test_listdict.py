from listdict import find_student as FS
students = [
    {"name": "John", "score": 80},
    {"name": "Mary", "score": 90},
    {"name": "David", "score": 65}
]

def test_john():
    student = FS(students, "John")
    assert student == {"name": "John", "score": 80}

def test_mary():
    student = FS(students, "Mary")
    assert student == {"name": "Mary", "score": 90}

def test_bob():
    student = FS(students, "Bob")
    assert student == None