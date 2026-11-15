import re

message = """
Contact John: 08012345678
Contact Mary: 07098765432
Contact Peter: 08123456789
"""

if type(message) == str:
    if phone_numbers := re.findall(r"\d+", message):
        print(phone_numbers)