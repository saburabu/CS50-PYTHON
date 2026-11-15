import json

n = int(input("How many students: "))
lists = []

for _ in range(n):
    name = input("Name: ").strip().title()
    age = int(input("Age: "))
    country = input("Country: ").strip().title()

    d = {
        "Name": name,
        "Age": age,
        "Country": country
    }
    lists.append(d)

# Convert to JSON string
my_json = json.dumps(lists, indent=4)
print(my_json)

# Convert back from JSON string to Python list
my_lists = json.loads(my_json)

# Loop through each student dictionary
for student in my_lists:
    print(f"Name: {student['Name']},\nAge: {student['Age']}\nCountry: {student['Country']}\n")


name_1 = str(input("Name: ")).strip().title()
age_1 = int(input("Age: "))

p1 = {}
p1[name_1] = age_1

# Write to file
with open("student.json", "w") as file:
    json.dump(p1, file, indent=4)

# Read back from file
with open("student.json", "r") as file:
    data = json.load(file)

print("Loaded from file:", data)