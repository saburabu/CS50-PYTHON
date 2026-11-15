numbers = [12, 5, -3, 20, 7, 0, 15, -8, 30]
total = 0
count = 0   # track how many positives were added

for number in numbers:
    if number < 0:
        continue   # skip negatives
    if number == 0:
        break      # stop at 0
    total += number
    count += 1     # increment count for each positive added

print(f"TOTAL: {total}")
print(f"COUNT: {count}")
