# this is your edition of the list
#scores = {
#    "Sabur": 85,
#    "Mike": 72,
#    "John": 91,
#    "Sarah": 64
#}

# this my edition it clean and perfect and reusable
scores = [
    {'name': "sabur", "score": "85"},
    {"name": "mike", "score": "72"},
    {"name": "john", "score": "91"},
    {"name": "sarah", "score": "64"}
]

# Convert score to integer
for s in scores:
    s["score"] = int(s["score"])

for s in scores:
    if s["score"] >= 80:
        print(f"{s['name']}: {s['score']}")
