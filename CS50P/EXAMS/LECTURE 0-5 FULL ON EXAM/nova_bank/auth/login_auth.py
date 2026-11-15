from auth_tools import authenticate_with_google, faker_login
import requests

def login_email():
    """Captures manual terminal credentials and passes verification values to backend parsing rules."""
    searcher = str(input("Login with Email or username: ")).strip()
    password = str(input("Password: ")).strip()

    # Passes the data down to faker_login, which returns the user account ID string
    user_id = faker_login(searcher, password)
    if user_id:
        return user_id


def login_google():
    """Authenticates through Google Secure Sign-In, verifies registration status on MockAPI,

    and returns the existing customer user ID to shut down the authentication loops.
    """
    # 1. Run the browser handshake. It returns the verified user data object payload dictionary
    google_profile = authenticate_with_google()
    
    if not google_profile:
        print("❌ Google Sign-In operation was cancelled.")
        return None

    # Extract their verified primary email address tracking token
    email_to_search = google_profile.get("email")
    url = "https://6ac4b98154a61668c5f62368.mockapi.io/api/saburabu/mini_banking/accounts"
    
    print("⏳ Querying bank account records to verify profile registration...")
    
    try:
        # 2. Search MockAPI database for a pre-existing row matching this email
        response = requests.get(url, params={"email": email_to_search}, timeout=10)
        
        if response.status_code == 200:
            accounts = response.json()
            
            # 3. If a match is found, extract the record and terminate the login sequence blocks cleanly
            if isinstance(accounts, list) and len(accounts) > 0:
                user_account = accounts[0]
                print(f"\n✅ Login Successful! Welcome back, {user_account['full_name']}!")
                
                # Hand this ID up to oauth.py so the master application welcome gate snaps shut!
                return user_account['id']
            else:
                print("\n❌ No banking registration records found matching this Google account.")
                print("💡 Please select 'Option 1: Signup' from the main menu to open an account first.")
                return None
        else:
            print(f"❌ Server connection mapping fault. Error Status: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"🔌 Connection drop during verification sequence: {e}")
        return None
