def get_passed_students(students):
    return [
        student for student in students
        if student["score"] >= 50
    ]