
score = float(input("what is your score? "))

match score:
    case score if 0 < score <= 39:
        print("LOW")
    case score if 40 <= score <= 69:
        print("PASS")
    case score if 70 <= score <= 100:
        print("HIGH")
    case _:
        print("INVALID") 

def is_even(n):
    return n % 2 == 0 and n >= 40 and n <= 100
if is_even(score):
    print("EVEN")
else:
    print("ODD")