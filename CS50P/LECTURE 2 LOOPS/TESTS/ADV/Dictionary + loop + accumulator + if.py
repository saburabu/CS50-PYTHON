count = 0
total = 0
scores = [
    {'name': "Sabur", "score": "85"},
    {"name": "Mike", "score": "72"},
    {"name": "John", "score": "91"},
    {"name": "Sarah", "score": "64"},
    {"name": "David", "score": "88"}
]

# Convert score to integer
for s in scores:
    s["score"] = int(s["score"])

for s in scores:
    if s["score"] >= 80:  
        print(f"{s['name']}: {s['score']}")
        count += 1
        total += s["score"]

print(f"PASSED: {count}")
print(f"TOTAL: {total}")

print()