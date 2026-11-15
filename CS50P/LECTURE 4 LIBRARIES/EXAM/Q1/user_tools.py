def create_user(name, age, email):
    return {
        "name": name,
        "age": age,
        "email": email
    }

def find_user(name, users):
    if not isinstance(name, str):
        return None
    for user in users:
        if user.get("name") == name:
            return user
    return None

def show_users(users):
    for user in users:
        print(f"Name: {user['name']}, Age: {user['age']}, Email: {user['email']}")
