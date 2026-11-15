students = []
for i in range(2):
    name = str(input("Name: ")).strip().title()
    
    scores = []
    for j in range(3):
        scores.append(float(input(f"Score{j+1}: ")))

    student = {
        "Name": name,
        "Score": scores
    }
    students.append(student)

at_least_70 = [s for s in students 
        if sum(s["Score"]) / len(s["Score"]) >= 70] 
print(at_least_70)