number = int(input("Integer: "))

is_divisible_3 = number % 3 == 0
is_divisible_2 = number % 2 == 0

if 1 <= number <= 99:
    if is_divisible_2 and is_divisible_3:
        print("BOTH")
    elif is_divisible_2:
        print("TWO")
    elif is_divisible_3:
        print("THREE")
    else:
        print("OTHER")
else:
    print("INVALID")