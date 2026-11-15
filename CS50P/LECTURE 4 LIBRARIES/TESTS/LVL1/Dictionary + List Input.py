class BeyondAgeRangeError(Exception):
    pass
def bare(age):
    if not 1 <= age <= 120:
        raise BeyondAgeRangeError("PLEASE ENTER A VALID AGE BTW 1 TO 120")
students = []
for i in range(3):
    name =  str(input("Name: ")).strip().title()
    while True:
        try:
            age = int(input("Age: "))
            bare(age)
        except ValueError as a:
            print(f"PLEASE ENTER AN INTEGER: {a}")
            pass
        except BeyondAgeRangeError as b:
            print(b)
            pass
        else:
            break
    skills = []
    for j in range(5):
        skill = str(input(f"SKill {j + 1}: "))
        skills.append(skill)

    student = {
        "Name": name,
        "Age": age,
        "Skills": skills
    }
    students.append(student)

for s in students:
    print(f"Name: {s["Name"]}\nAge: {s["Age"]}\nSkills: {s["Skills"]}")