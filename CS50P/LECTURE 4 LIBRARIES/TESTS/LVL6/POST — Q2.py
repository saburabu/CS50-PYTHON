import json
import sys
import requests

users = []
# Each user has 3 arguments: name, email, age
# Skip sys.argv[0] (the script name)
args = sys.argv[1:]

for i in range(0, len(args), 3):
    name = args[i].strip().title()
    email = args[i + 1].strip()
    age = int(args[i + 2])
    users.append({"name": name, "email": email, "age": age})
if len(args) % 3 != 0:
    print("Error: Arguments must come in groups of 3 (name, email, age).")
    sys.exit(1)
    
with open("users.json", "w") as file:
    json.dump(users, file, indent=4)

with open("users.json", "r") as file:
    us = json.load(file)

url = "https://reqres.in/api/users"
response = requests.post(url, timeout=15, json=users)
if response.status_code in (200, 201):
    print("SUCCESSFULLY ADDED")
else:
    print("UNSUCCESSFUL TRY AGAIN")
response.raise_for_status()
data = response.json()
users_with_response = {
    "users": users,
    "api_response": data
}
print(json.dumps(users_with_response, indent=4))

with open("users.json", "w") as file:
    json.dump(users_with_response, file, indent=4)

with open("users.json", "r") as file:
    us = json.load(file)

print(us)