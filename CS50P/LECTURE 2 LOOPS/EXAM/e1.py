def get_number():
    while True:
        n = int(input("What is number? "))
        if n > 0:
            break
    return n
number = get_number()
def meow(n):
    for _ in range(n):
        print("meow")
meow(number)

