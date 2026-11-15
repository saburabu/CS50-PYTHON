def create_student(name, age, skills, score):
    student = {
        "name": name,
        "age": age,
        "skills": skills,
        "score": score
    }

    return student


def passed(student):
    if student["score"] >= 50:
        return True
    else:
        return False