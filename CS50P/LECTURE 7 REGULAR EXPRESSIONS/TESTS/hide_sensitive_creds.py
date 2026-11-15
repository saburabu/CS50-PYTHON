lazy import re

text = """
My phone is 08012345678.
My second number is 07098765432.
Call me if necessary.
"""

if text and isinstance(text, str) and len(text) > 1:
    pattern = r"\d+"

    if numbers := re.sub(pattern, "************", text):
        print(numbers)
    else:
        print("An error had occured check user input")