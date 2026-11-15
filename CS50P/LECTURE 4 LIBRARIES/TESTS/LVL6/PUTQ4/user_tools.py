def create_user(name, age, email):
    return {
        "name": name,
        "age": age,
        "email": email
    }

def find_user(email, users):
    email = email.strip().lower()
    for user in users:
        if user["email"].lower() == email:
            return user
    return None

