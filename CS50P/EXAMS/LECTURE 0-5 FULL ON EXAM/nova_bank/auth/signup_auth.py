from auth_tools import auth_email, authenticate_with_google
import json
import requests

class InvalidNameError(Exception):
    pass

class InvalidCredentialsError(Exception):
    pass

url = "https://6ac4b98154a61668c5f62368.mockapi.io/api/saburabu/mini_banking/accounts"

def InvalidName(first_name, last_name, middle_name):
    if len(first_name) == 0 or len(last_name) == 0:
        raise InvalidNameError("❌ Name is invalid. First and Last name cannot be empty! TRY AGAIN!")
    if middle_name and len(middle_name) <= 1:
        raise InvalidNameError("❌ Invalid Middle Name. Must be longer than 1 character! TRY AGAIN!")

def InvalidCRED(email, password, username):
    if len(email) == 0 or len(password) == 0 or len(username) == 0:
        raise InvalidCredentialsError("Your credentials are invalid")

def signin_email():
    while True:
        try:
            first_name = input("Firstname: ").strip().title()
            last_name = input("Lastname: ").strip().title()
            middle_name = input("Middlename (Or tap ENTER to skip): ").strip().title()
            InvalidName(first_name, last_name, middle_name)
        except InvalidNameError as a:
            print(a)
        else:
            full_name = f"{first_name} {middle_name} {last_name}" if middle_name else f"{first_name} {last_name}"
            print(f"✅ Registered Name: {full_name}")
            break

    while True:
        try:
            email = input("Email: ").strip().lower()
            user_name = input("Desired username: ").strip()
            password = input("Password: ").strip()
            InvalidCRED(email, password, user_name)
        except InvalidCredentialsError as b:
            print(b)
        else:
            break

    user = auth_email(email, password, full_name, user_name)
    if not user:
        return None
    
    try:
        response = requests.post(url, json=user, timeout=15)
        if response.status_code == 201:
            created_user = response.json()
            print(f"🎉 {created_user['full_name']} successfully added to the server database!")
            return created_user["id"]  # 🎯 FIXED: Bubble up the new ID
        else:
            print(f"❌ Signup failed (status {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"🔌 Error connecting to database: {e}")
    return None

def signin_google():
    user = authenticate_with_google()
    if not user:
        return None

    try:
        response = requests.post(url, json=user, timeout=15)
        if response.status_code == 201:
            created_user = response.json()
            print(f"🎉 {created_user['full_name']} successfully added to the server database!")
            return created_user["id"]  # 🎯 FIXED: Bubble up the new ID
    except requests.exceptions.RequestException as e:
        print(f"🔌 Error connecting to database: {e}")
    return None
