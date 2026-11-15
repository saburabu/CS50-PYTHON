students = [
    {"name": "John", "score": 85},
    {"name": "Mary", "score": 62},
    {"name": "Alex", "score": 94},
    {"name": "David", "score": 48}
]

for i, s in enumerate(students):
    print(f"index: {i} Name: {s["name"]}, Score: {s["score"]}")


average = sum(s["score"] for s in students) / len(students)
print(average)

highest = max(s["score"] for s in students)
print(f"{highest}")

passed = []
for s in students:
    if s["score"] >= 70:
        passed.append(s)

for s in passed:
    print(f"Name: {s["name"]}\nScore: {s["score"]}")