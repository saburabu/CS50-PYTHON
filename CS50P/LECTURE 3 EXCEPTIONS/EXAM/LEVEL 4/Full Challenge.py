class InvalidScoreError(Exception):
    pass

students = {}

def add_students():
    while True:
        name = str(input("Name: "))
        while True:
            try:
                score = float(input("Score: "))
                if score < 0 or score > 100:
                    raise InvalidScoreError("SCORE MUST BE BTW 0 AND 100")
            except ValueError as a:
                print(f"SCORE MUST BE AN INTEGER: TRY AGAIN\n{a}")
            except InvalidScoreError as b:
                print(f"{b}")
            else:
                break
        if name in students:
            print("STUDENT ALREADY EXISTS!")
        else:
            students[name] = score
            print(f"{name} ADDED")
            break

def find_students():
    name = str(input("Name: "))
    find = students.get(name)

    if find is None:
        print("Not in contacts")
        print("1.DO YOU WISH TO ADD STUDENT\n2.DON'T WANT TO ADD STUDENT")
        while True:
            choose = str(input("Choose:"))
            if choose == "1":
                add_students()
                break
            elif choose == "2":
                break
            else:
                print("TRY AGAIN")
    else:
        print(find)

def update_score():
    name = str(input("Name: "))
    while True:
        try:
            score = float(input("New Score: "))
            if score < 0 or score > 100:
                raise InvalidScoreError("SCORE MUST BE BTW 0 AND 100")
        except ValueError as a:
            print(f"SCORE MUST BE AN INTEGER: TRY AGAIN\n{a}")
        except InvalidScoreError as b:
            print(f"{b}")
        else:
            break

    students[name] = score
    print("Score updated")

def delete_students():
    name = str(input("Name: "))
    if name in students:
        del students[name]
    else:
        print("STUDENT NOT FOUND")
        print("1.DO YOU WISH TO ADD STUDENT\n2.DON'T WANT TO ADD STUDENT")
        while True:
            choose = str(input("Choose:"))
            if choose == "1":
                add_students()
                break
            elif choose == "2":
                break
            else:
                print("TRY AGAIN")

def show_students():
    for name, score in students.items():
        print(f"Name: {name}, Score: {score}")

def show_average():
    total = 0
    for name, score in students.items():
        total += score
    average = total / len(students)
    print("Average:", average)
    if 80 <= average <= 100:
        print("EXCELLENT")

    elif 60 <= average <= 79:
        print("AWESOME")

    elif 40 <= average <= 59:
        print("TRY HARDER YOU ARE AMAZING")

    elif 0 <= average <= 39:
        print("READ YOUR BOOK")

    else:
        print("      ")

while True:
    print("1.Add student\n2.Find student\n3.Update score\n4.Delete student\n5.Show all students\n6.Show average of all students\n7.QUIT")
    choice = str(input("CHOOSE: "))

    if choice == "1":
        add_students()
    elif choice == "2":
        find_students()
    elif choice == "3":
        update_score()
    elif choice == "4":
        delete_students()
    elif choice == "5":
        show_students()
    elif choice == "6":
        show_average()
    elif choice == "7":
        break
    else:
        print("WRONG INPUT TRY AGAIN")



