def create_student(name, age, email, score):
    return {
        "name": name,
        "age": age,
        "email": email,
        "score": score
    }

def find_user(name_1, users):
    name_1 = name_1.strip().title()
    for user in users:
        if user['name'].strip().title() == name_1:
            return user
    return None

