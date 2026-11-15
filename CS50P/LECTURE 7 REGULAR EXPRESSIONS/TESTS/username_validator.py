lazy import re
import sys

user_name = (sys.argv[1]) # if we wanted to strip of whitespaces immediately it will have been easier to do .strip()

if validator := re.search(r"^\w+{4,12}$", user_name):
    print("valid")
else:
    print("invalid")