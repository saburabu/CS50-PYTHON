age = int(input("Age: "))

if age >= 13 <= 19:
    print("TEEN")
elif age >= 20 < 65:
    print("ADULT")
elif age >= 60  <= 120:
    print("SENIOR")
else:
    print("INVALID")