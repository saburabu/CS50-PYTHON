class InvalidScoreError(Exception):
    pass


students = {}


def add_student():
    name = input("Name: ")

    if name in students:
        print("Student already exists.")
        return

    try:
        score = int(input("Score: "))

        if score < 0 or score > 100:
            raise InvalidScoreError("Score must be between 0 and 100.")

        students[name] = score
        print("Student added.")

    except ValueError as e:
        print("Score must be an integer.")

    except InvalidScoreError as e:
        print(e)


def find_student():
    name = input("Name: ")

    score = students.get(name)

    if score is None:
        print("Student not found.")
    else:
        print(name, ":", score)


def delete_student():
    name = input("Name: ")

    if name not in students:
        print("Student not found.")
    else:
        del students[name]
        print("Student deleted.")


def show_students():
    if not students:
        print("No students.")
        return

    for name, score in students.items():
        print(name, ":", score)


while True:
    print("\n1. Add student")
    print("2. Find student")
    print("3. Delete student")
    print("4. Show students")
    print("5. Quit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        find_student()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        show_students()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")