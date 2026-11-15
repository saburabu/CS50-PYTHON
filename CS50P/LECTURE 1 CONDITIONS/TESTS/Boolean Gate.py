age = int(input("Age: "))
day = input("Day: ")
code = int(input("Code: "))

day = day.strip().lower()
weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]

if 13 <= age <= 19 and day in weekdays:
    if day == "friday" and code == 222:
        print("PRIORITY")
    elif code in [111, 222, 333]:
        print("ALLOWED")
    else:
        print("DENIED")
else:
    print("DENIED")
    