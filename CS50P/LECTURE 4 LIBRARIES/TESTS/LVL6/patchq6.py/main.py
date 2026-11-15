import json
import requests
from user_tools import create_student as cs, find_user as fu

def main():
    url = "https://reqres.in/api/users/2"
    users = []
    
    # Collect user data
    for i in range(1):
        print(f"USER {i + 1} DETAILS:")
        name = input("Name: ").strip().title()
        age = int(input("Age: "))
        email = input("Email: ").strip().lower()
        score = float(input("Score: "))

        user = cs(name, age, email, score)
        users.append(user)

    # Save users to file
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

    # Ask which user to update
    print("\nWhich user would you like to change?")
    name_1 = input("Name: ").strip().title()

    user_fu = fu(name_1, users)
    if not user_fu:
        print("Name doesn't exist")
        return

    print("What do you want to change?\n1. email\n2. score")
    choice = input("Choose: ")

    if choice == "1":
        new_email = input("New Email: ").strip().lower()
        update = {"email": new_email}
        user_fu["email"] = new_email
    elif choice == "2":
        new_score = float(input("New Score: "))
        update = {"score": new_score}
        user_fu["score"] = new_score
    else:
        print("Invalid choice")
        return

    # Send update to API
    response = requests.patch(url, json=update, timeout=15)
    print(f"STATUS: {response.status_code}")
    response.raise_for_status()
    data = response.json()

    # Show updated person
    print("\nUpdated User Data:")
    print(json.dumps(user_fu, indent=4))

    # Save only updated person + API info
    updated_data = {
        "Updated User": user_fu,
        "api_info": data
    }

    with open("updated_users.json", "w") as file:
        json.dump(updated_data, file, indent=4)

if __name__ == "__main__":
    main()
