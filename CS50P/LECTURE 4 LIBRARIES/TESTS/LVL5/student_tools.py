def create_students(name, age, skills, score):
    return {
        "name": name,
        "age": age,
        "skills": skills,
        "score": score
    }


def filter_passed(student):
    return "PASSED" if student["score"] >= 50 else "FAILED"


def find_student(name, students):
    for student in students:
        if student["name"].strip().lower() == name.strip().lower():
            return student
    return None