age = int(input("Age: "))

if 10 <= age <= 17:
    print("YOUNG")

elif 18 <= age <= 64:
    print("ADULT")

elif age >= 65:
    print("SENIOR")

else:
    print("INVALID")