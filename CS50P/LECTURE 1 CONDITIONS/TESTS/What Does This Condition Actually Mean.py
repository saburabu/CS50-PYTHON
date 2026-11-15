a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if 10 <= a and b and c <= 99:
    if a or b or c in [15, 25, 35, 45, 55, 65, 75, 85, 95]:
        print("VALID SPECIAL")
    elif 10 <= a and b and c <= 99:
        print("VALID NORMAL")
else:
    print("INVALID")