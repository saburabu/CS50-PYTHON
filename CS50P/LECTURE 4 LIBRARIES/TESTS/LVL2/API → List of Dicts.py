def apis():
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

apis()