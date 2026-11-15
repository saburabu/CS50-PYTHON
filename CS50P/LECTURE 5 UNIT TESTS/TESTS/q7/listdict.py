def find_student(students, name):
    for student in students:
        if student["name"] == name:
            return student

    return None