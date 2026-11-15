import json
import requests
from user_tools import create_user, find_user, show_users

USERS_FILE = "users.json"

def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)

def load_users():
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def option_show(users):
    show_users(users)

def option_get():
    url = "https://reqres.in/api/users"
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    data = response.json()
    print("Response type:", type(data))
    print("Keys:", data.keys())
    # Inspect structure
    if "data" in data:
        for user in data["data"]:
            print(f"API User: {user['first_name']} {user['last_name']} - {user['email']}")

def option_post(users):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    email = input("Enter email: ")
    new_user = create_user(name, age, email)
    users.append(new_user)

    url = "https://reqres.in/api/users"
    response = requests.post(url, json=new_user, timeout=15)
    response.raise_for_status()
    data = response.json()
    new_user["api_response"] = data
    save_users(users)

def option_put(users):
    name = input("Enter the name of the user to replace: ")
    user = find_user(name, users)
    if not user:
        print("User not found.")
        return

    new_name = input("Enter new name: ")
    new_age = int(input("Enter new age: "))
    new_email = input("Enter new email: ")
    replacement = create_user(new_name, new_age, new_email)

    url = "https://reqres.in/api/users/2"
    response = requests.put(url, json=replacement, timeout=15)
    response.raise_for_status()
    data = response.json()
    user.update(replacement)
    user["api_update"] = data
    save_users(users)

def option_patch(users):
    name = input("Enter the name of the user to update: ")
    user = find_user(name, users)
    if not user:
        print("User not found.")
        return

    print("1. Change email\n2. Change age")
    choice = input("Choose option: ")
    if choice == "1":
        new_email = input("Enter new email: ")
        update = {"email": new_email}
    elif choice == "2":
        new_age = int(input("Enter new age: "))
        update = {"age": new_age}
    else:
        print("Invalid choice.")
        return

    url = "https://reqres.in/api/users/2"
    response = requests.patch(url, json=update, timeout=15)
    response.raise_for_status()
    data = response.json()
    user.update(update)
    user["api_update"] = data
    save_users(users)

def main():
    users = [
        {"name": "Sabur", "age": 17, "email": "sabur@example.com"},
        {"name": "John", "age": 18, "email": "john@example.com"},
        {"name": "Mary", "age": 19, "email": "mary@example.com"}
    ]
    save_users(users)
    users = load_users()

    while True:
        print("\n===== USER MANAGER =====")
        print("1. Show local users")
        print("2. Get users from API")
        print("3. Add user")
        print("4. Replace user")
        print("5. Update part of user")
        print("6. Exit")

        choice = input("Choose option: ")
        if choice == "1":
            option_show(users)
        elif choice == "2":
            option_get()
        elif choice == "3":
            option_post(users)
        elif choice == "4":
            option_put(users)
        elif choice == "5":
            option_patch(users)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
