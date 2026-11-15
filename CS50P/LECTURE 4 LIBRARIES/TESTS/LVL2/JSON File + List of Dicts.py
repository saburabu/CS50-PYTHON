import json
students = [
    {"name": "John", "score": 75},
    {"name": "Mary", "score": 91},
    {"name": "Alex", "score": 64}
]

with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

with open("student.json", "r") as file:
    data = json.load(file)

print(f"\n{data}")

print(f"\nNumber of Students: {len(data)}")
high = max(student["score"] for student in students)
for stu in students:
    print(f"\nName: {stu['name']}\nScore: {stu['score']}")

print(f"\nHighest: {high}")

print("\nSTUDENTS WHO PASSED")
for student in students:
    if student["score"] >= 70:
        print(f"Name: {student['name']}\nScore: {student['score']}")