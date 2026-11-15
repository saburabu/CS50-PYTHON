class InvalidScoreError(Exception):
    pass


def add_student(students, name, score):
    if score < 0 or score > 100:
        raise InvalidScoreError

    student = {
        "name": name,
        "score": score
    }

    students.append(student)

    return student


def find_student(students, name):
    for student in students:
        if student["name"] == name:
            return student

    return None


def get_passed_students(students):
    return [
        student for student in students
        if student["score"] >= 50
    ]