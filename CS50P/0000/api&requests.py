import requests
import json

print("Number from 1 to 10")
number = int(input("Enter USERID: "))
while True:
    try:
        url = f"https://jsonplaceholder.typicode.com/users/{number}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print(response)

        data = response.json()

        print(f"Name: {data['name']},\nUserName: {data['username']},\nEmail: {data['email']},\nPhoneNumber: {data['phone']},\nWebsite: {data['website']}")
        print(f"City: {data['address']['city']},\nStreet: {data['address']['street']}")

    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.HTTPError as e:
        print("HTTP error:", e)
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
    except Exception as e:
        print("Unexpected error:", e)
    else:
        break


username = str(input("Enter a username to search for: ")).strip().title()
url_1 = "https://jsonplaceholder.typicode.com/users"
params = {"username": username}
while True:
    try:
        response_1 = requests.get(url_1, timeout=15, params=params)
        response_1.raise_for_status()
        data_1 = response_1.json()

        if data_1:
            for user in data_1:
                print(f"Name: {user['name']}, Email: {user['email']}")
        else:
            print("No user found with that username.")

    except requests.exceptions.RequestException as e:
        print("Error searching for user:", e)
    except Exception as e:
        print("Unexpected error:", e)
    else:
        break


name = str(input("Name: ")).strip().title()
username_1 = str(input("Username: ")).strip()
email = str(input("Email: ")).strip()

data_2 = {
    "name": name,
    "username": username_1,
    "email": email
}
url = "https://jsonplaceholder.typicode.com/users"
while True:
    try:
        response_2 = requests.post(url, timeout=15, json=data_2)
        print("Status Code:", response_2.status_code)
        response_2.raise_for_status()
        data_2 = response_2.json()

        print("Created user:")
        print(f"Name: {data_2['name']}")
        print(f"Username: {data_2['username']}")
        print(f"Email: {data_2['email']}")

    except requests.exceptions.RequestException as e:
        print("Error creating user:", e)
    except Exception as e:
        print("Unexpected error:", e)
    else:
        break
