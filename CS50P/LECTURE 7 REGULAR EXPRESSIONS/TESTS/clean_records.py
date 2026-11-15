import re

records = """John - 08012345678Mary: 07098765432Peter / 08123456789David | 09012345678"""

# Regex breakdown:
# ([A-Za-z]+) -> Group 1 (name): Matches one or more alphabetical characters
# \s*         -> Matches zero or more optional spaces
# [\-:/|]     -> Matches any of the separators: hyphen, colon, slash, or vertical bar
# \s*         -> Matches zero or more optional spaces
# (\d+)       -> Group 2 (phone): Matches one or more digits
pattern = r"([A-Za-z]+)\s*[\-:/|]\s*(\d+)"

# re.findall extracts all matching pairs as a list of tuples: [('John', '08012345678'), ...]
matches = re.findall(pattern, records)

# Convert the list of tuples into the expected list of dictionaries
cleaned_records = [{"name": name, "phone": phone} for name, phone in matches]

print(cleaned_records)
