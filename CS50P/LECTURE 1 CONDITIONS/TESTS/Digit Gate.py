# Write a program that asks the user for a positive integer.
x = int(input("Give me a number "))

if  0 <= x <= 10:
    print("SMALL")

elif x % 2 == 0 and x >= 11:
    print("EVEN")
else:
    print("ODD")