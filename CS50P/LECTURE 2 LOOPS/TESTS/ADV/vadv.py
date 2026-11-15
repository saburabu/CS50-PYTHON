students = {}

while True:
    name = str(input("Name/Quit to stop: ")).strip().title()
    if name == "Quit":
        break
    while True:
        try:
            score = float(input("Score: "))
        except ValueError:
            pass
        else:
            break


    students[name] = {
        "Score": score
}

for name, details in students.items():
    if details["Score"] >= 70:
        print(f"{name}: {details}")


    