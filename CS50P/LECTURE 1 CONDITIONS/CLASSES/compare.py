x = float(input("Enter a number: "))
y = float(input("Enter another number: "))

if x > y:
    print(f"{x} is greater than {y}.")
elif x < y:
    print(f"{x} is less than {y}.")
else:
    print(f"{x} is equal to {y}.")

# if where trying to differentiate between the two number in being equal or not equal we can do
if x != y:
    print(f"{x} is not equal to {y}.")
else:
    print(f"{x} is equal to {y}.")

# OR we can do
if x == y:
    print(f"{x} is equal to {y}.")
else:
    print(f"{x} is not equal to {y}.")

# Or we can do
if x < y or x > y:
    print(f"{x} is not equal to {y}.")
else:
    print(f"{x} is equal to {y}.")




