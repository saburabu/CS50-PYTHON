from student_tools import create_student as cs
from student_tools import passed as p


students = []

for i in range(1):
    name = input("NAME: ").strip()
    age = int(input("AGE: "))

    skills = input("SKILLS: ").strip().split()

    score = float(input("SCORE: "))

    student = cs(name, age, skills, score)

    student["passed"] = p(student)

    students.append(student)


for stu in students:
    print(stu)