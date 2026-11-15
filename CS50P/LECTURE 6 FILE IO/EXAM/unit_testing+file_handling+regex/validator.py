lazy import re
class EmailError(Exception):
    pass
class PhoneNumberError(Exception):
    pass
class NameError(Exception):
    pass
class AgeError(Exception):
    pass

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if validated_email := re.fullmatch(pattern, email):
        return validated_email
    else:
        raise EmailError("Invalid email format")

def validate_phone_number(phone_number):
    pattern = r'^\+?\d{1,3}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,3}[-.\s]?\d{7,10}$'
    if validated_phone := re.fullmatch(pattern, phone_number):
        return validated_phone
    else:
        raise PhoneNumberError("Invalid phone number format")

def validate_name(name):
    pattern = r'^[A-Za-z]\s+[A-Za-z]\s+(?:[A-Za-z])?$'
    if validated_name := re.fullmatch(pattern, name):
        return validated_name
    else:
        raise NameError("Invalid name format")

def validate_age(age):
    if isinstance(age, int) and 18 <= age <= 100:
        return age
    else:
        raise AgeError("Invalid age. Age must be an integer between 18 and 100.")

def format_to_international(phone_number: str, default_country_code: str = "234") -> str:
    """
    Cleans and formats a phone number into standard international format (+CountryCodeNumber).
    Defaults to Nigeria (+234) if no country code is detected.
    """
    # Step 1: Strip out all non-digit characters except an optional leading '+'
    cleaned = re.sub(r'(?<!^)\+|[^\d+]', '', phone_number.strip())
    
    pattern = r'^(?:\+(\d{1,3}))?0*(\d{7,10})$'
    match = re.match(pattern, cleaned)
    
    if not match:
        raise ValueError("Invalid phone number format")
        
    country_code, national_number = match.groups()
    # If no explicit country code was provided, apply the default
    final_cc = country_code if country_code else default_country_code
    
    return f"+{final_cc}{national_number}"
