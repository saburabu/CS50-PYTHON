lazy import re

password = input("Password: ")

if password and isinstance(password, str):
    pattern = r"^(?=.*\d)(?=.*[A-Z])(?=.*[a-z]).{8,}$"
    
    if re.search(pattern, password):
        print("valid")
    else:
        print("invalid")
else:
    print("invalid")
