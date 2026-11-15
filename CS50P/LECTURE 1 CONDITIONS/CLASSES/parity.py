x = float(input("What is x? "))

if x % 2 == 0:
    print(f"{x} is even.")
else:
    print(f"{x} is odd.")
# define a function to check if a number is even or odd
def main():
    x = float(input("What is x? "))
    if is_even(x):
        print(f"{x} is even.")
    else:
        print(f"{x} is odd.")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
# another way to do this taks using pythonic expressions
def main():
    x = float(input("What is x? "))
    if is_even(x):
        print(f"{x} is even.")
    else:
        print(f"{x} is odd.")
# as you can see we collapsed the 4 lines into 1 clean line of code
def is_even(n):
    return True if n % 2 == 0 else False

main()
# you can also do it without the boolean expression so this is what we are going to do
def main():
    x = float(input("What is x? "))
    if is_even(x):
        print(f"{x} is even.")
    else:
        print(f"{x} is odd.")
# without the boolean expression
def is_even(n):
    return n % 2 == 0
main()