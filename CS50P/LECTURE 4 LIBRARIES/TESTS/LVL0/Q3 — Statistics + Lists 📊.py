import statistics as s

numbers = []
for number in range(5):
    number = int(input("Number: "))
    numbers.append(number)

mean = s.mean(numbers)
median = s.median(numbers)

print(f"MEAN: {mean}\nMEDIAN: {median}")