int = int(input("Integer: "))

is_divisible_2 = int % 2 == 0
is_divisible_5 = int % 5 == 0

if is_divisible_2 and is_divisible_5:
    print("DIVISIBLE BY 2 AND 5")
elif is_divisible_2:
    print("DIVISIBLE BY ONLY 2")
elif is_divisible_5:
    print("DIVISIBLE BY ONLY 3")
else:
    print("NEITHER")