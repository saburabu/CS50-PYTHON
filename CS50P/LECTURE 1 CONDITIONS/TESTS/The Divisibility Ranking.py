n = int(input("number: "))

is_divisible_2 = n % 2 == 0
is_divisible_3 = n % 3 == 0
is_divisible_5 = n % 5 == 0

if n in [30, 60, 90, 120]:
    print("SPECIAL")
elif n < 0:
    print("INVALID")
elif is_divisible_2 and is_divisible_3 and is_divisible_5:
    print("SUPER")
elif is_divisible_2 and is_divisible_3 or is_divisible_2 and is_divisible_5 or is_divisible_3 and is_divisible_5:
    print("DOUBLE")
elif is_divisible_2 or is_divisible_3 or is_divisible_5:
    print("SINGLE")
else:
    print("NONE")

    