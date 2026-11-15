a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

special_numbers = [15, 25, 35, 45, 55]

if a in special_numbers or b in special_numbers or c in special_numbers:
    print("SPECIAL")
else:
    print("NORMAL")