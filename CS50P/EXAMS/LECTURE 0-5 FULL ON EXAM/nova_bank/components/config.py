import hashlib
import sys

AUTH_HASH = "88ebd1325a19f0a8b2422828c2bcc5962f81d41aa6d7b6da41fcb6fdcc6d1ca4"


# 2. Raw values are kept here safely as private placeholders
_FLW_ClIENT_ID = "e2292aaa-35a4-4d8b-8e1d-b38f742a2263"
_FLW_CLIENT_SECRET = "Kr8MtR7YElVBRrdj3LjKC0yawRwkAx7qFQIOnE3hfRTUA9V4ydNdBPZm6F9MAZR5b61eoSsV21Sawmx79Djnkl"
_FLW_ENCRYPTION_KEY = "fcUkbdnNu6DyC4Pc+3I48+No/x6mEj92VzBKTv1tTaY="

def get_flutterwave_credentials():
    """Forces password validation in the terminal before releasing your API keys."""
    print("\n🔒 SYSTEM AUTHENTICATION REQUIRED")
    input_password = input("Enter configuration authorization password: ").strip()

    
    # Hash what the user typed to see if it matches our footprint
    input_hash = hashlib.sha256(input_password.encode()).hexdigest()
    
    if input_hash == AUTH_HASH:
        print("✅ Access Granted. Loading keys...")
        return _FLW_CLIENT_SECRET, _FLW_ENCRYPTION_KEY
    else:
        print("❌ ACCESS DENIED: Incorrect authorization password!")
        sys.exit("Execution halted due to security violation.") # Kill the app instantly

