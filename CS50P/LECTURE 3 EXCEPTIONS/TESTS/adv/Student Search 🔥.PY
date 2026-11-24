students = {
    "John": 85,
    "Sarah": 92,
    "Mike": 78
}

while True:
    name = input("Enter student name: ").strip().title()
    if name.lower() == "quit":
        break
    try:
        score = students.get(name)
        if score is None:
            raise KeyError("Student not found.")
        print(f"{name}'s score is {score}")
    except KeyError as e:
        print(e)

