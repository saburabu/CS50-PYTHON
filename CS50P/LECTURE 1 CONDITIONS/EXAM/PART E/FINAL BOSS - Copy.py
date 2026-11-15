name = input("What is your fullname? ").strip().title()
age = int(input("How old are you? "))
department = input("What department are you in? ").strip().title()
access_code = int(input("What is your access code? "))
day = input("Day(day's of the week): ").strip().title()

department_name = ["Cs", "Engineering", "Math"]
is_divisible_2 = access_code % 2 == 0
is_divisible_5 = access_code % 5 == 0


def check_access(age, department, access_code, day):
    if age >= 16 and department in department_name and 1000 <= access_code <= 9999:
        if (is_divisible_2 and is_divisible_5) or (department == "Cs" and day.lower() == "friday"):
            print(f"Name: {name}\nAge: {age}\nDepartment: {department}\nAccess code: {access_code}\nDay: {day}\nSPECIAL ACCESS")
        else:
            print(f"Name: {name}\nAge: {age}\nDepartment: {department}\nAccess code: {access_code}\nDay: {day}\nNORMAL ACCESS")
    else:
        print("INVALID USER")


check_access(age, department, access_code, day)