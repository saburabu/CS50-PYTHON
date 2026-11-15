age = int(input("Age: "))
student = str(input("Student(yes/no): "))
student = student.strip().lower()

if 13 <= age <= 19 or "yes" in student:
    print("DISCOUNT")
else:
    print("FULL PRICE")