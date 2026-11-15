import requests
import json

# 1. Collect user
name = input("Name: ").strip().title()
age = int(input("Age: "))
email = input("Email: ").strip().lower()

user = {
    "name": name,
    "email": email,
    "age": age
}

# 2. Save to JSON
with open("user.json", "w") as file:
    json.dump(user, file, indent=4)

# 3. Load back
with open("user.json", "r") as file:
    my_json = json.load(file)

# 4. Ask for update
print("What do you want to change?")
new_email = input("NEW EMAIL: ").strip().lower()

update = {"NEW EMAIL": new_email}

# 5. Send PATCH request
url = "https://reqres.in/api/users/2"
response = requests.patch(url, json=update, timeout=15)
print(f"STATUS: {response.status_code}")
response.raise_for_status()

# 6. Get response
data = response.json()

# 7. Build updated user dictionary
updated_user = {
    "name": user["name"],
    "email": user["email"],
    "age": user["age"],
    "api_update": data   # attach API response
}


with open("update_result.json", "w") as file:
    json.dump(updated_user, file, indent=4)

with open("update_result.json", file) as file:
    my_json_1 = json.load(file)

print(my_json)
