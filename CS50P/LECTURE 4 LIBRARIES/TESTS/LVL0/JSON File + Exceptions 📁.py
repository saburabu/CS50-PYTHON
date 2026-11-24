import json
class BeyondRangeError(Exception):
    pass

def bre(score):
    if not 0 <= score <= 100:
        raise BeyondRangeError("INVALID NUMBER: ENTER A VALUE WITHIN 0 TO 100")

students = {}
def add_students():
    for _ in range(1):
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
my_dict = json.dumps(students)

def show_students():
    my_dict_again = json.loads(my_dict)
    print(my_dict_again)

while True:
    print("1.Add student\n2.Show students\n.3.QUIT")
    choice = str(input("Choose: "))
    if choice == "1":
        add_students()
    elif choice == "2":
        show_students()
    elif choice == "3":
        break
    else:
        print("TRY AGAIN MORON")



