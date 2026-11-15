import json
import requests
from student_tools import create_students as cs
from student_tools import filter_passed as p
from student_tools import find_student as fs

students = []

# Collect student details
for i in range(1):
    name = str(input("Name: ")).strip().title()
    age = int(input("Age: "))
    skills = input("SKILLS: ").strip().split()
    score = float(input("SCORE: "))

    student = cs(name, age, skills, score)
    student["passed"] = p(student)
    students.append(student)

# Print local students
for stu in students:
    print(
        f"\nName: {stu['name']}\n"
        f"Age: {stu['age']}\n"
        f"Skills: {stu['skills']}\n"
        f"Score: {stu['score']}\n"
        f"Passed: {stu['passed']}\n"
    )

# Save initial data to JSON
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

# Load data back from JSON
with open("students.json", "r") as file:
    json_open = json.load(file)

print(f"LOADED FROM JSON: {json_open}")

# Fetch API data
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url, timeout=10)
response.raise_for_status()

data = response.json()

# Match user names and attach API info to the matched student
for user in data:
    matched_student = fs(user["name"], students)
    if matched_student:
        matched_student["api_info"] = {
            "username": user["username"],
            "email": user["email"],
            "city": user["address"]["city"],
        }
    else:
        print(f"User '{user['name']}' NOT IN TYPICODE MATCHES")

# Save updated students list with API info
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nFINAL STUDENTS DATA:")
print(json.dumps(students, indent=4))