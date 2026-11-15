import time
import random
import requests
import json
from faker import Faker

BASE_URL = "https://6ac4b98154a61668c5f62368.mockapi.io/api/saburabu/mini_banking" 
fake = Faker()

def generate_fake_customers(count=30):
    """Generates fake customers, uploads them, and returns the successful profiles list."""
    print(f"\n--- Generating and Uploading {count} Fake Customers ---")
    
    # 1. Create an empty list to store successfully created accounts
    uploaded_users = []
    for i in range(count):
        customer_data = {
            "full_name": fake.name(),
            "email": fake.email(),
            "user_name": fake.user_name(),
            "password": fake.password() if hasattr(fake, 'password') else fake.word(),
            "account_number": int(random.randint(1000000000, 9999999999)), 
            "account_balance": int(random.randint(10000, 1500000000)) 
        }
        try:
            response = requests.post(f"{BASE_URL}/accounts", json=customer_data)
            if response.status_code == 201:
                created = response.json()
                
                if isinstance(created, list):
                    created = created[0]
                
                if "full_name" in created:
                    print(f"[{i+1}/{count}] ✅ Saved Online: {created['full_name']} (ID: {created['id']}) - Balance: ₦{float(created['account_balance']):,}")
                    
                    # 2. Append the successful account payload to our tracking list
                    uploaded_users.append(created)
                else:
                    print(f"[{i+1}/{count}] ⚠️ Server accepted payload, but keys dropped.")
            else:
                print(f"❌ Failed to communicate with endpoint. Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Network error at user index {i+1}: {e}")   
        time.sleep(0.1)

    # 3. CRUCIAL: Return the full list to whoever called the function!
    return uploaded_users


def save_fake_users():
    file_path = r"c:/Users/USER/Documents/VS CODE/CS50 CLASS/EXAMS/LECTURE 0-5 FULL ON EXAM/minibankingsystem/the_api/api_users.json"
    
    # Now 'users' will receive the populated 'uploaded_users' list instead of None
    users = generate_fake_customers(30)
    
    with open(file_path, "w") as file:
        json.dump(users, file, indent=4)
    print(f"\n💾 Successfully saved all user profiles locally to: {file_path}")
    
if __name__ == "__main__":
    save_fake_users()