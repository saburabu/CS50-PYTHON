import re

def extract_numbers(raw_text):
    # Match EXACTLY an 11-digit number first, otherwise fall back to any other digit sequence
    # This prevents an 11-digit number from bleeding into both lists
    phone_pattern = r"\b\d{11}\b"
    general_pattern = r"\b\d+\b"
    
    all_phones = re.findall(phone_pattern, raw_text)

    remaining_text = re.sub(phone_pattern, "", raw_text)
    all_numbers = re.findall(general_pattern, remaining_text)
    
    if all_phones:
        print("Phone numbers: ", all_phones)
    if all_numbers:
        print("Numbers: ", all_numbers)
        
    return all_numbers, all_phones


def extract_emails(raw_text):
    emails_found = []
    

    pattern = r"\b[\w\.-]+@[\w\.-]+\.(?:com|org)\b"
    
    for match in re.finditer(pattern, raw_text, re.IGNORECASE):
        emails_found.append(match.group(0))
            
    if emails_found:
        print("\n📧 Emails found:")
        print("\n".join(emails_found))
    else:
        print("\n📧 No valid emails found.")


def capslock(raw_text):
    # Match any word starting with an uppercase letter
    pattern = r"\b[A-Z]\w*"
    matches = re.findall(pattern, raw_text)
    
    if matches:
        print("\n🔠 Words starting with capital letters found:")
        print(", ".join(matches))
    else:
        print("\n🔠 No uppercase starting words found.")


def replace_numbers(raw_text):
    replaced_phone_no = re.sub(r"\b\d{11}\b", "***********", raw_text)
    replaced_numbers = re.sub(r"\b\d+\b", "[NUMBERS]", raw_text)

    print("\n🔢 Text after replacing phone numbers with asterisks:")
    print(replaced_phone_no)
    print("\n🔢 Text after replacing numbers with [NUMBERS]:")
    print(replaced_numbers)


def search(raw_text, search_term):
    pattern = re.escape(search_term)
    matches = re.findall(pattern, raw_text, re.IGNORECASE)

    if matches:
        if len(matches) > 1:
            print(f"\n🔍 The term '{search_term}' was found {len(matches)} times.")
        else:
            print(f"\n🔍 The term '{search_term}' was found once.")
    else:
        print(f"\n🔍 The term '{search_term}' was not found.")

def main():
    raw_text = input("GIVE ME ANY SHIT FROM PHONE NUMBERS TO EMAILS OR ANYTHING REALLY\nNOTE EMAILS CAN ONLY SUPPORT 2 DOMAINS NOTHING MORE: ")

    while True:
        print("\n--- Run a command ---")
        print("1. Extract all numbers")
        print("2. Extract all email addresses")
        print("3. Find all words beginning with a capital letter")
        print("4. Replace all numbers with [NUMBER]")
        print("5. Search for a specific word or phrase")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        match choice:
            case "1":
                extract_numbers(raw_text)
            case "2":
                extract_emails(raw_text)
            case "3":
                capslock(raw_text)
            case "4":
                replace_numbers(raw_text)
            case "5":
                search_term = input("Enter the word or phrase to search for: ").strip()
                search(raw_text, search_term)
            case "6":
                print("Exiting the program.")
                break
            case _:
                print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
