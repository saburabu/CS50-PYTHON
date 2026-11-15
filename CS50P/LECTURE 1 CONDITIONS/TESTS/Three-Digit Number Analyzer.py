number = int(input("What is the number? "))

def divisible_3(n):
    return n % 3 == 0
def divisible_5(n):
    return n % 5 == 0
def is_even(n):
    return n % 2 == 0

if not 100 <= number <= 999:
    print("NOT A THREE DIGIT NUMBER")
elif divisible_3(number):
        print("DIVISIBLE BY 3")
elif divisible_5(number):
        print("DIVISIBLE BY 5")
elif divisible_3(number) and divisible_5(number):
        print("DIVISIBLE BY BOTH 5 AND 3")
else:
        print("NEITHER")

if number % 2 == 0:
      print("EVEN")
else:
      print("ODD")

