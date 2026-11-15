names = []
text = str(input("Names: ")).split()
names = text
print(len(names))
print(names[0])
print(names[-1])
names[2] = "Sarah"
names.append("Mike")
names.insert(0, "Boss")
names.extend(["Tom", "Jerry"])
if "John" in names:
    print("YES JOHN EXIST")
names.remove("John")
p = names.pop(2)
print(f"{p} was removed")
