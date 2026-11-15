import json
import requests
from user_tools import create_user, find_user

def main():
    users = []

    # 1. Ask for 5 users
    for i in range(5):
        print(f"\nEnter details for user {i+1}:")
        name = input("Name: ").strip().title()
        age = int(input("Age: ").strip())
        email = input("Email: ").strip().lower()

        user_dict = create_user(name, age, email)
        users.append(user_dict)

    # 4. Save them to users.json
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

    # 5. Load them back
    with open("users.json", "r") as file:
        users = json.load(file)

    # 6. Ask which user to update
    target_email = input("\nEnter the email of the user to update: ").strip().lower()

    # 7. Find that user
    user = find_user(target_email, users)
    if not user:
        print("User not found.")
        return

    # 8. Ask for new details
    new_name = input("New name: ").strip().title()
    new_age = int(input("New age: ").strip())
    new_email = input("New email: ").strip().lower()

    updated_user = create_user(new_name, new_age, new_email)

    # 10. Send PUT request
    url = "https://reqres.in/api/users/2"
    response = requests.put(url, json=updated_user, timeout=15)

    # 11. Convert response to dict
    api_response = response.json()

    # 12. Add it to the selected user
    user["api_update"] = api_response

    # 13. Save back to users.json
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

    # 14. Load again
    with open("users.json", "r") as file:
        final_data = json.load(file)

    # 15. Print final data
    print("\nFinal data:")
    print(json.dumps(final_data, indent=4))

if __name__ == "__main__":
    main()
