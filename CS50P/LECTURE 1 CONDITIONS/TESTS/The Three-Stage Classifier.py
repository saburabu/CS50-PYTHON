# Your program must determine which relationship they have
a = int(input("what is a? "))
b = int(input("what is b? "))

if a < b:
    x = (b - a)
elif b < a:
    x = (a - b)

def d_2(n):
    return n % 2 == 0
def d_3(n):
    return n % 3 == 0

if a == b:
    print("STOP")
elif d_2(x) and d_3(x):
    print("SIX")
elif d_2(x):
    print("TWO")
elif d_3(x):
    print("THREE")
else:
    print("OTHER")
