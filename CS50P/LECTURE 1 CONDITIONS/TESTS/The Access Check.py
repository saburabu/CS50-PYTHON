age = int(input("age: "))
code = int(input("code: "))

if 13 <= age <= 19:
    if code in [123, 456, 789]:
        print("ALLOWED")
else:
    print("DENIED")