# Ask the user for an integer
numbers = int(input("number: "))

if numbers in [30, 40, 50]:
    print("SPECIAL")
elif 20 <= numbers <= 50:
    print("SAFE")
else:
    print("UNSAFE")
