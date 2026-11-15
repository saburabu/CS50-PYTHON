
a = float(input("What is A? "))
b = float(input("What is B? "))

def add(a, b):
    x = a + b
    return x
x = add(a, b)
def sub(a, b):
    y = a - b
    return y
y = sub(a, b)
def mul(a, b):
    z = a * b
    return z
z = mul(a, b)

print(f"Addition: {x}")
print(f"Subtraction: {y}")
print(f"Multiply: {z}")
