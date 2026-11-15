door_number = int(input("Door number: "))

if door_number in [3, 7, 22, 27, 44, 49]:
    print("SPECIAL DOOR")
elif 1 <= door_number <= 10:
    print("DOOR A")
elif 20 <= door_number <= 30:
    print("DOOR B")
elif 40 <= door_number <= 50:
    print("DOOR C")
else:
    print("NO DOOR")