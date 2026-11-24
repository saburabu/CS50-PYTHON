class InvalidAgeError(Exception):
    """Custom exception for invalid ages."""
    pass

def check_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("YOUR AGE IS INVALID")

try:
    age = int(input("Age: "))
    check_age(age)
except InvalidAgeError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Invalid input: {e}")
else:
    print(f"Valid age entered: {age}")
