names = ["John", "Mike", "Sarah"]

for index, name in enumerate(names):
    print(index + 1, name)

for letter in reversed(range(5)):
    print(letter)

word = "hello"

for char in word:
    print(char)

count = 0

for char in word:
    if char == "a":
        count += 1

numbers = [5, 12, 3, 20]

for item in numbers:
    if item > 10:
        print(item)