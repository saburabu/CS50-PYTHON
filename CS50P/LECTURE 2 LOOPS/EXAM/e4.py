scores = []   # empty list to store all students

for _ in range(3):   # loop for 3 students
    name = input("Enter name (or 'done' to finish): ")
    if name.lower() == "done":
        break
    
    # collect scores
    s1 = int(input("Score 1: "))
    s2 = int(input("Score 2: "))
    s3 = int(input("Score 3: "))
    
    # build dictionary and append to list
    student = {"name": name, "scores": [s1, s2, s3]}
    scores.append(student)

# show results
for student in scores:
    print(student["name"], student["scores"])
