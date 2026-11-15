total = 0
for number in range(1, 6):
    number = int(input("Number: "))
    if number == 0:
        break
    total += number

print(f"Total: {total}")
