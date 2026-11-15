x = 8
y = 3

if x > 5 and y + 2 == 5:
    print("A")
elif x % y == 2:
    print("B")
elif not x < y:
    print("C")
else:
    print("D")

# ANSWERS:
# 1. "A"
# 2. " basically if a condition is fulfilled the program stops running living the rest there
# thats why most people arrange conditions in preference of importance like special cases come first before others
# this for example
#number = int(input("Integer: "))
#is_divisible_3 = number % 3 == 0
#is_divisible_2 = number % 2 == 0
#if 1 <= number <= 99:
#    if is_divisible_2 and is_divisible_3:
#        print("BOTH")
#    elif is_divisible_2:
#        print("TWO")
#    elif is_divisible_3:
#        print("THREE")
#    else:
#        print("OTHER")
#else:
#    print("INVALID")