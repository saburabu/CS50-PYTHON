students = {}

for student in range(3):
    name = str(input("Name: ")).strip().title()
    while True:
        try:
            age = int(input("Age: "))
        except ValueError:
            pass
        else:
            break
    while True:
        try:
            score = float(input("Score: "))
        except ValueError:
            pass
        else:
            break
    # due to the fact there is a python function called class class = grade
    grade = str(input("Class: ")).strip().title()
    while True:
        try:
            gpa =float(input("CGPA: "))
        except ValueError:
            pass
        else:
            break
        
    students[name] = {
        "Age" : age,
        "Score" : score,
        "Class" : grade,
        "CGPA" : gpa
    }

for ivy in students.items():
    print(f"{ivy}")
