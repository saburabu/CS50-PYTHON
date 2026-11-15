import sys
import json
import requests

name = sys.argv[1].strip().title()
email = sys.argv[2].strip()
age = int(sys.argv[3])

user = {
    "name": name,
    "email": email,
    "age": age
}
with open("user.json", "w") as file:
    json.dump(user, file, indent=4)
with open("user.json", "r") as file:
    users = json.load(file)

url = "https://reqres.in/api/users/2"
response = requests.put(url, timeout=15, json=users)
print(f"STATUS: {response.status_code}")
response.raise_for_status()

data = response.json()

users_with_response = {
    "users": users,
    "api_response": data
}
print(json.dumps(users_with_response, indent=4))

with open("put_result.json", "w") as file:
    json.dump(users_with_response, file, indent=4)