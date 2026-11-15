int = int(input("What is the int: "))

is_divisible_2 = int % 2 == 0
is_divisible_3 = int % 3 == 0

if 1 <= int <= 100:
    if is_divisible_2 and is_divisible_3:
        print("C")
elif 1 <= int <= 100 and is_divisible_2:
    print("A")
elif 1 <= int <100 and is_divisible_3:
    print("B")
else:
    print("OTHER")

    
