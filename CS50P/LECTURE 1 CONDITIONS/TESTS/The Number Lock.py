# A security system accepts an integer code
code = int(input("What is your code? "))
# defining functions
def d_2(x):
    return x % 2 == 0
def d_3(x):
    return x % 3 == 0
def d_5(x):
    return x % 5 == 0
#where the logic operates
if not code >= 100 <= 999:
    print("INVALID")
elif d_5(code) and d_3(code) and d_2(code): 
    print("TRIPLE")
elif d_2(code) and d_3(code) or d_3(code) and d_5(code) or d_2(code) and d_5(code):
    print("DOUBLE")
elif d_2(code) or d_5(code) or d_3(code):
    print("SINGLE")
# even or odd
if not code >= 100 <= 999:
    print("         ")
elif code % 2 == 0:
    print("EVEN")
else:
    print("ODD")