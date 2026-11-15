total = 0
for number in range(0, 5):
    number = int(input("Number: "))
    if number < 0:
        continue
    total += number

print(total)
