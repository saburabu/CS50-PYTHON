import os
import random
import sys
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import requests

# Global container to capture the authorization code from the server callback loop
auth_code = None

class OAuthCallbackHandler(BaseHTTPRequestHandler):
    """Temporary local micro-server to intercept Google's successful redirect token code."""
    def do_GET(self):
        global auth_code
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        
        # Extract the success query string parameter out of the incoming browser URL path
        query_components = parse_qs(urlparse(self.path).query)
        if "code" in query_components:
            auth_code = query_components["code"][0]
            self.wfile.write(b"<h1>Authentication Successful!</h1><p>You can close this browser tab and check your Python VS Code terminal.</p>")
        else:
            self.wfile.write(b"<h1>Authentication Failed</h1>")

    def log_message(self, format, *args):
        return  # Suppress internal terminal tracking text logs to keep output clean

def authenticate_with_google():
    """Manually constructs the exact browser auth path matching your custom keys configuration."""
    global auth_code
    auth_code = None
    
    # 🎯 YOUR EXACT KEYS DICTIONARY - ZERO ALTERATIONS
    client_config = {"web":{"client_id":"720126107908-r8sd92s9ft28saadtl7848a39obsnaq2.apps.googleusercontent.com","project_id":"minibanking-py","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"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","redirect_uris":["http://localhost:8080/"],"javascript_origins":["http://localhost:8080"]}}
    
    web_keys = client_config["web"]
    
    # Safely extract the pure string URL out of the redirect_uris array list
    redirect_uri_str = web_keys["redirect_uris"][0]
    
    # Manually compile a clean authorization URL string with completely standard profile flags
    auth_url = (
        f"{web_keys['auth_uri']}?"
        f"client_id={web_keys['client_id']}&"
        f"redirect_uri={redirect_uri_str}&"
        f"response_type=code&"
        f"scope=openid%20email%20profile&"
        f"prompt=select_account"
    )
    
    print("\n🌐 Opening a fresh, clean browser login tab...")
    webbrowser.open(auth_url)
    
    # Fire up a quick local port listener to catch the return callback payload
    server = HTTPServer(("localhost", 8080), OAuthCallbackHandler)
    while auth_code is None:
        server.handle_request()
    server.server_close()
    
    print("⏳ Verifying access credentials with Google auth servers...")
    
    # Swap the temporary authorization code token for an identity token profile dictionary
    token_payload = {
        "code": auth_code,
        "client_id": web_keys["client_id"],
        "client_secret": web_keys["client_secret"],
        "redirect_uri": redirect_uri_str,
        "grant_type": "authorization_code"
    }
    
    try:
        from google.oauth2 import id_token
        from google.auth.transport import requests as google_requests
        
        token_res = requests.post(web_keys["token_uri"], data=token_payload)
        if token_res.status_code != 200:
            print(f"❌ Token exchange failed. Status: {token_res.status_code}")
            return None
            
        tokens = token_res.json()
        id_token_str = tokens.get("id_token")
        
        # Verify the cryptographic signature validation checks
        info = id_token.verify_oauth2_token(
            id_token_str, 
            google_requests.Request(), 
            web_keys["client_id"]
        )

        print("✅ Google Authentication Completed Successfully!")
        return {
            "full_name": info.get("name"),
            "email": info.get("email"),
            "password": None,
            "user_name": info.get("name"), 
            "google_id": info.get("sub"), # Keeps identification signature safe
            "account_number": random.randint(1000000000, 9999999999), 
            "account_balance": random.randint(10000, 150000) 
        }
    except Exception as e:
        print(f"❌ Error extracting user metadata details: {e}")
        return None
    

def auth_email(email, password, full_name, user_name):
    url = "https://6ac4b98154a61668c5f62368.mockapi.io/api/saburabu/mini_banking/accounts"
    
    # ----------------------------------------------------
    # PHASE 1: Validate Email Structure & Uniqueness
    # ----------------------------------------------------
    if "@" in email and "." in email.split("@")[-1]:
        print("✅ Email format verified")
    else:
        print("❌ Invalid email format.")
        return None

    try:
        email_response = requests.get(url, timeout=15, params={"email": email})
        
        if email_response.status_code == 200:
            email_data = email_response.json()
            if isinstance(email_data, list) and len(email_data) > 0:
                print(f"❌ Email '{email}' already exists. Please try a different one.")
                return None  # 🎯 FIXED: Rejection check added
        elif email_response.status_code == 404:
            print(f"✅ Email '{email}' is perfect and available!")
        else:
            print(f"❌ Server issue during email validation (Status: {email_response.status_code}). Aborting.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"🔌 Connection drop during email uniqueness validation: {e}")
        return None

    # ----------------------------------------------------
    # PHASE 2: Validate Username Uniqueness
    # ----------------------------------------------------
    try:
        username_response = requests.get(url, timeout=15, params={"user_name": user_name})
        
        if username_response.status_code == 200:
            username_data = username_response.json()
            if isinstance(username_data, list) and len(username_data) > 0:
                print(f"❌ Username '{user_name}' already exists. Please try a different one.")
                return None
        elif username_response.status_code == 404:
            print(f"✅ Username '{user_name}' is perfect and available!")
        else:
            print(f"❌ Server issue during username validation (Status: {username_response.status_code}). Aborting.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"🔌 Connection drop during username uniqueness validation: {e}")
        return None

    # ----------------------------------------------------
    # PHASE 3: Validate Password Length
    # ----------------------------------------------------
    if len(password) >= 8:
        print("✅ Desired password length attained")
    else:
        print("❌ Invalid password. It must be 8 characters or longer.")
        return None  # 🎯 FIXED: Rejection check added

    # ----------------------------------------------------
    # PHASE 4: Pack and Return Validated Dictionary
    # ----------------------------------------------------
    return {
        "email": email,
        "password": password,
        "user_name": user_name,      # Spelled to match your database schema key
        "full_name": full_name,      # Spelled to match your database schema key
        "account_number": random.randint(1000000000, 9999999999), 
        "account_balance": random.randint(10000, 150000) 
    }
    

def faker_login(searcher, password):
    """
    Queries MockAPI database to locate and verify user credentials.
    
    Returns:
        str: The authenticated user's ID string if successful.
        None: Explicitly returned for any validation failure, wrong password, or connection drop.
    """
    url = "https://6ac4b98154a61668c5f62368.mockapi.io/api/saburabu/mini_banking/accounts"
    
    # ----------------------------------------------------
    # PHASE 1: Determine Query Parameter
    # ----------------------------------------------------
    # Auto-detect if user typed an email or a username based on the '@' symbol
    if "@" in searcher:
        query = {"email": searcher.lower().strip()}
    else:
        query = {"user_name": searcher.strip()}

    # ----------------------------------------------------
    # PHASE 2: Database Communication & Guard Clauses
    # ----------------------------------------------------
    try:
        response = requests.get(url, params=query, timeout=10)
        
        # Guard Clause: Check if the API server failed to respond normally
        if response.status_code != 200:
            print(f"❌ Server connection issue. Error Status: {response.status_code}")
            return None

        accounts_list = response.json()
        
        # Guard Clause: Check if MockAPI returned an empty array or an unexpected data type
        if not isinstance(accounts_list, list) or len(accounts_list) == 0:
            print("❌ Invalid username/email or password configuration combination.")
            return None

        # ----------------------------------------------------
        # PHASE 3: Credential Verification
        # ----------------------------------------------------
        account = accounts_list[0]
        
        # Guard Clause: Check if the password doesn't match the database record
        if account.get("password") != password:
            print("❌ Invalid username/email or password configuration combination.")
            return None

        # ----------------------------------------------------
        # PHASE 4: Successful Validation
        # ----------------------------------------------------
        print(f"\n✅ Login Successful! Welcome back, {account.get('full_name')}!")
        
            
    except requests.exceptions.Timeout:
        print("🔌 Connection Timeout: The banking server took too long to respond.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"🔌 Critical Connection Drop: {e}")
        return None
    else:
        return account.get("id")
