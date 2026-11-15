total = 0
count = 0
while True:
   # track how many positives were added
    numbers = int(input("Number: "))
    if numbers < 0:
        continue   # skip negatives
    if numbers == 0:
        break      # stop at 0
    total += numbers
    count += 1     # increment count for each positive added

print(f"TOTAL: {total}")
print(f"COUNT: {count}")
