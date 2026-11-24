import json
students = []

class BeyondRangeError(Exception):
    pass
class BeyondAgeRangeError(Exception):
    pass

def bre(score):
    if not 0 <= score <= 100:
        raise BeyondRangeError("INVALID NUMBER: ENTER A VALUE WITHIN 0 TO 100")

def bare(age):
    if not 1 <= age <= 120:
        raise BeyondAgeRangeError("PLEASE ENTER A VALID AGE BTW 1 TO 120")
    
def add_students():
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
        while True:
                try:
                    score = float(input("Score: "))
                    bre(score)
                except ValueError as a:
                    print(f"MUST BE A NUMBER: {a}")
                except BeyondRangeError as b:
                    print(f"{b}")
                else:
                    break
        student = {
            "Name": name,
            "Age": age,
            "Score": score
        }
        students.append(student)

def conv_json():
    if len(students) == 0:
        print("ADD STUDENTS FIRST")
        return

    print("1.CONVERT TO JSON\n2.CONVERT BACK TO PYTHON")
    choice = str(input("Choose: "))

    if choice == "1":
        for student in students:
            my_json = json.dumps(student)
            print(my_json)
    elif choice == "2":
        for student in students:
            my_json = json.dumps(student)
            my_py = json.loads(my_json)
            print(my_py)
    else:
        print("ENTER EITHER 1 OR 2")

def above_80():
    for student in students:
        if student["Score"] >= 80:
            print(f"Name: {student['Name']}\n Score: {student['Score']}")

def choose():
    while True:
        choice = str(input("1.Add Student\n2.Convert To Either Json Or Python\n3.Show Students Whom Got Above 80\n4.QUIT\n"))
        if choice == "1":
            add_students()
        elif choice == "2":
            conv_json()
        elif choice == "3":
            above_80()
        elif choice == "4":
            print("GOODBYE")
            break
        else:
            print("ENTER A VALID OPTION")
            pass

choose()
