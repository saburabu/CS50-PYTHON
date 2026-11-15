numbers = [10, -5, 7, 20, -3, 8, 0, 100, 50]
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
