word = str(input("Word: ")).strip().lower()
ca = 0
for a in word:
    if a == "a":
        ca += 1
print(f"A: {ca}")
ce = 0
for e in word:
    if e == "e":
        ce += 1
print(f"E: {ce}")
ci = 0
for i in word:
    if i == "i":
        ci += 1
print(f"I: {ci}")
co = 0
for o in word:
    if o == "o":
        co += 1
print(f"O: {co}")
cu = 0
for u in word:
    if u == "u":
        cu += 1
print(f"U: {cu}")