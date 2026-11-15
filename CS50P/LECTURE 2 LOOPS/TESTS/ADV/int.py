students = {}

for student in range(5):
    name = str(input("Name: "))
    score = int(input("Score: "))
    students[name] = score

print(students)