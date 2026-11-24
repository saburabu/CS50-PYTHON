class BeyondRangeError(Exception):
    pass

def bre(score):
    if not 0 <= score <= 100:
        raise BeyondRangeError("INVALID NUMBER: ENTER A VALUE WITHIN 0 TO 100")

import random as r

students = {}

for _ in range(5):
    name = input("Name: ")
    while True:
        try:
            score = float(input("Score: "))
            bre(score)
        except ValueError as a:
            print(f"MUST BE A NUMBER: {a}")
        except BeyondRangeError as b:
            print(f"{b}")
        else:
            students[name] = score
            break  

# Pick a random student
student = r.choice(list(students.items()))
print(f"Randomly selected: Name: {student[0]}, Score: {student[1]}")

# Print all students
for name, s in students.items():
    print(f"Name: {name}, Score: {s}")

                
