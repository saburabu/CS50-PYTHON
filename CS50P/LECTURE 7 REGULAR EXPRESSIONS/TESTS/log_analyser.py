lazy import re

logs = """
2026-10-29 10:30:15 INFO User Sabur logged in
2026-10-29 10:31:20 ERROR Database connection failed
2026-10-29 10:32:10 WARNING High memory usage
2026-10-29 10:33:45 ERROR Payment request failed
2026-10-29 10:35:00 INFO User Mary logged out
"""

if logs and isinstance(logs, str):
    pattern = r"^\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\sERROR.+" # to be more specific
    # to be short and simple: pattern = r"^.*ERROR.*"
    if error := re.findall(pattern, logs, re.MULTILINE):
        print("Extracting data")
    else:
        print("Extraction FAILED")

count = len(error)
time_stamp = re.findall(r"^(.{19}).*ERROR.+", logs, re.MULTILINE)

print(f"ERROR MESSAGE: ", *error, sep="\n")
print(f"NUMBER OF ERROR MESSAGES: {count}")
print(f"TIMESTAMP: ", *time_stamp, sep="\n")