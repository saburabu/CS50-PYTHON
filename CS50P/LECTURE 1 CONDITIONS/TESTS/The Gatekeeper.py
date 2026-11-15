# Write a program that asks for three integers
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if not a or b or c >= 10 <= 99:
    print("REJECTED")

if not a < b < c:
    print("REJECTED")

def total(a, b, c):
    x = a + b + c
    return x
x = total(a, b, c)
def d_3(x):
    p = x % 3 == 0
    return p
p = d_3(x)

if not d_3(x):
    print("REJECTED")

def is_even(p):
    return p % 2 == 0

print("OPEN")
if p:
    print("EVEN TRIO")
elif p:
    print("ODD TRIO")
else:
    print("MIXED")


