import json
import requests

# 1. Configuration (Updated with your brand new project ID)
PROJECT_ID = "nova-8db80"
COLLECTION = "users"
BASE_URL = f"https://googleapis.com/{PROJECT_ID}/databases/(default)/documents/{COLLECTION}"

# 2. Body Payload 
jsons = {
    "fields": {
        "name": {"stringValue": "alice"},
        "age": {"integerValue": "20"},
        "grade": {"doubleValue": "35.5"},
        "tall": {"booleanValue": True},
    }
}

try:
    print("Sending request to Firestore...")
    response = requests.post(BASE_URL, timeout=15, json=jsons)

    # Firestore returns a 200 OK status code on successful creation via POST
    if response.status_code == 201:
        print("SUCCESSFUL WE ARE DOMINATING 🚀🚀🚀")
        print(json.dumps(response.json(), indent=2))
    else:
        print("OMO GU SORRY OO!!!!!!! ❌")
        print(f"Status Code: {response.status_code}")
        print(f"Error Details: {response.text}")
        
except Exception as e:
    print(f"Connection failed: {e}")
