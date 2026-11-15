names = ["John", "Mike", "Sarah", "David", "Alex"]

for index, names in enumerate(names):
    if index % 2 != 0:
        continue
    print(f"{names}")
