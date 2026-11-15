numbers = [int(x) for x in input("Enter numbers: ").split()]
print(numbers)
print(numbers[0])
print(numbers[-1])
print(len(numbers))
numbers[1] = 100
numbers.append(999)
numbers.insert(1, 50)
numbers.extend([7, 8, 9])
numbers.remove(50)
person = numbers.pop()
for index, x in enumerate(numbers):
    print(f"{index + 1}, {x}")

print(f"\n\n WITH SLICING {numbers[1:6]}")

even = [q for q in numbers if q % 2 == 0]
print(even)


square = [num ** 2 for num in numbers]
print(square)

if 100 in numbers:
    print("100")
elif not 100 in numbers:
    print("no")
