# THE signin PAGE 
def signin_bank():
    """Main account authentication entry portal router.

    Returns the validated user profile data object to main.py when a login succeeds.
    """
    while True:
        print("\n🏦 Hey, welcome to Nova Bank\nHow do you wish to signin\n\n1. Signup\n2. Login\n3. Exit App")
        choice = input("Choice: ").strip()
        
        if choice == "1":
            choose = input("Sign up by:\n1. Email\n2. Google\nChoice: ").strip()
            if choose == "1":
                from signup_auth import signin_email
                user_id = signin_email()
                if user_id:
                    return user_id  # 🎯 FIXED: Break loop, pass ID to main.py
            elif choose == "2":
                from signup_auth import signin_google
                user_id = signin_google()
                if user_id:
                    return user_id  # 🎯 FIXED: Break loop, pass ID to main.py
            else:
                print("❌ Invalid Input selection option.")
                
        elif choice == "2":
            choose = input("Login by:\n1. Email / Username Credentials\n2. Google Sign-In Verification\nChoice: ").strip()
            if choose == "1":
                from login_auth import login_email
                user_id = login_email()
                if user_id:
                    return user_id  # 🎯 FIXED: Break loop, pass ID to main.py
            elif choose == "2":
                from login_auth import login_google
                user_id = login_google()
                if user_id:
                    return user_id  # 🎯 FIXED: Break loop, pass ID to main.py
            else:
                print("❌ Invalid Input option.")
                
        elif choice == "3":
            print("Shutting down core layout logic packages. Goodbye!")
            return None
        else:
            print("❌ INVALID TRY AGAIN!")  # Start the signin process when the script is run