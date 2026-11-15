
ticket_number = int(input("Tickect number: "))
day = str(input("A day: "))

day = day.strip().lower()
is_divisible_2 = ticket_number % 2 == 0
is_divisible_3 = ticket_number % 3 == 0
is_divisible_5 = ticket_number % 5 == 0
days = ["saturday", "sunday"]

if 100 <= ticket_number <= 999 and day in days:
    if ticket_number in [111, 222, 333]:
        print("SPECIAL\nACCEPTED")
    elif is_divisible_2 and is_divisible_3 and is_divisible_5:
        print("TRIPLE\nACCEPTED")
    elif is_divisible_2 and is_divisible_3 or is_divisible_2 and is_divisible_5 or is_divisible_3 and is_divisible_5:
        print("DOUBLE\nREJECTED")
    elif is_divisible_2 or is_divisible_3 or is_divisible_5:
        print("SINGLE\nREJECTED")
    else:
        print("NONE")
else:
    print("REJECTED")