total = 0   # initialize once, outside the loop
while True:
    number = int(input("Number: "))
    if number < 0:
        continue   # skip negatives
    if number == 0:
        break      # stop when 0 is entered
    total += number
print(f"Total: {total}")

