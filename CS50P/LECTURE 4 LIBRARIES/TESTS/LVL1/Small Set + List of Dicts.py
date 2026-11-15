students = [
    {"name": "John", "skills": ["Python", "AI"]},
    {"name": "Mary", "skills": ["Python", "Web"]},
    {"name": "Alex", "skills": ["AI", "Data"]}
]
all_skills = set()
for student in students:
    all_skills.update(student["skills"])

print(all_skills)