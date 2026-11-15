import json
import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url, timeout=10)
response.raise_for_status
print(response)

lists = []
data = response.json()

for info in data:
    if info['address']['city'].startswith("S"):

        dicts = {
            "name": info['name'],
            "city": info['address']['city'],
            "company": info["company"]["name"]
        }

        lists.append(dicts)

for ans in lists:
    print(f"Name: {ans['name']}\nCompany: {ans['company']}\nADDRESS: {ans['city']}")

# just to store user data in json
with open("typi.json", "w") as file:
    json.dump(lists, file, indent=4)