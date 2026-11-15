import requests
import json

lists = []
city = str(input("CITY: ")).strip().title()
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url, timeout=15)
response.raise_for_status()
print(response)

data = response.json()

for info in data:
    if info['address']['city'] == city:
        user_dict = {
            "name": info['name'],
            "username": info['username'],
            "email": info['email'],
            "city": info['address']['city'],
            "company": info["company"]["name"]
        }
        lists.append(user_dict)

if lists:
    print(lists)
else:
    print("No users found in that city.")

for ans in lists:
    print(f"Name: {ans['name']}\nUsername: {ans['username']}\nEmail: {ans['email']}\nCity: {ans['city']}\nCompany: {ans['company']}")

with open("city.json", "w") as file:
    json.dump(lists, file, indent=4)