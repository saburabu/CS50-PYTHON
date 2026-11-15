height = int(input("Height: "))
i = 1   # start from 1

while i <= height:
    print(" " * (height - i), end="")   # spaces
    print("#" * i)                      # hashes
    i += 1   # move to the next row
