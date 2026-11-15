# q1
numbers = [10, 20, 30, 40, 50]
print(f"Firstnumber: {numbers[0]}\nLastnumber: {numbers[-1]}")
numbers.append(60)
print(numbers)

#q2
texts = []
name = str(input("Names: ")).title()
text = name.split()
texts.append(text)
for x in texts[0]:
    print(x, end="\n") 

# q3
n = [int(n) for n in input("Number: ")]
