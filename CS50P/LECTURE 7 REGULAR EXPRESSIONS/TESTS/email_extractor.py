lazy import re

# 1. Using the data block containing messy text and invalid email samples
data = """
Contact us:
support@example.com
admin@company.org
invalid-email
sales@store.net
another-invalid@
hello@gmail.com
"""

# 2. Initialize the destination dictionary
domain_directory = {}

# 3. Clean and split the text into a list of individual lines
lines = data.strip().split("\n")

# 4. Loop through each line to search and extract
for line in lines:
    # Trims trailing/leading spaces from the line before checking
    clean_line = line.strip()
    
    # CS50P Style: Captures username in group 1, and the extension in group 2
    if matches := re.search(r"^(\w+)@\w+\.(org|com|net)$", clean_line):
        user = matches.group(1)
        extension = matches.group(2)

        # 5. Build the dictionary step-by-step
        if extension not in domain_directory:
            domain_directory[extension] = [user]  # Create a new list for it
        else:
            domain_directory[extension].append(user)  # Add user to existing list

# 6. Print the cleanly organized result
print(domain_directory)