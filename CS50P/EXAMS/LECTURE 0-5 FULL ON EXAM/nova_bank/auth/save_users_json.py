import requests, json

from auth import signin_bank as sb

file_path = r"c:\Users\USER\Documents\VS CODE\CS50 CLASS\EXAMS\LECTURE 0-5 FULL ON EXAM\nova_bank\active_user.json"
def extract_info(user_id):
    try:
        url = f"https://6ac4b98154a61668c5f62368.mockapi.io/api/saburabu/mini_banking/accounts/{user_id}"
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
                print(f"❌ Failed to fetch user profile. Status Code: {response.status_code}")
                return None
    except requests.exceptions.RequestException as e:
        print(f"🔌 Connection drop while fetching user dictionary: {e}")
        return None

    
def save_json():
    user_id = sb()
    
    if not user_id:
        print("❌ USER NOT FOUND OR LOGIN CANCELLED!")
        return None

    user = extract_info(user_id)

    with open("user.json", "w") as file:
        json.dump(user, file, indent=4)
if __name__ == "__main__":
    save_json()