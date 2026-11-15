
import json
import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url, timeout=10)
response.raise_for_status
print(response)

data = response.json()
stu_l = []
for info in data:
        stu_d = {
            "name": info['name'],
            "email": info['email'],
            "city": info['address']['city']
        }

        stu_l.append(stu_d)

for stu in stu_l:
        print(f"Name: {stu['name']}\nEmail: {stu['email']}\nCity: {stu['city']}")

with open("users.json", "w") as file:
    json.dump(stu_l, file, indent=4)

with open("users.json", "r") as file:
       json.load(file)

biz = []
print("PEOPLE WITH \"biz\" IN THEIR EMAIL")
for info_1 in data:
       if "biz" in info_1['email']:
            biz.append(info_1)
            print(f"Name: {info_1['name']}\nEmail: {info_1['email']}")