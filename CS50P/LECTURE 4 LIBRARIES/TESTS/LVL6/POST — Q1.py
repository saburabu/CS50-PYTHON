import sys
import requests
import json

use = []
for i in range(1):
    name = sys.argv[1].strip().title()
    email = sys.argv[2].strip()
    a = sys.argv[3]
    age = int(a)
    user = {
    "name": name,
    "email": email,
    "age": age
    }
    use.append(user)

url = "https://reqres.in/api/users"
response = requests.post(url, timeout=10, json=use)
print(f"RESPONSE: {response.status_code}")
response.raise_for_status()

data = response.json()
users = []
for dat in data:
    user_data = {
        "name": dat["name"],
        "email": dat["email"],
        "age": dat["age"]
    }
    users.append(user_data)

with open("users.json", "w") as file:
    json.dump(users, file, indent=4)

with open("users.json", "r") as file:
    us = json.load(file)

print(us)