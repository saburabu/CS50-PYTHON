#q1
numbers = [int(x) for x in input("Number: ").split()]
print(f"Largest number: {max(numbers)}")
print(f"Smallest number: {min(numbers)}")
average = sum(numbers) / len(numbers)
print(f"Average: {average}")

# q2
# Start with an empty set
words_set = set()

# First input
words = input("Word: ").title().split()
for w in words:
    words_set.add(w)

print("Current set size:", len(words_set))

# Second input
word = input("Another word: ").title()
if word not in words_set:
    words_set.add(word)
    print("Added:", word)
else:
    print("ALREADY EXISTS")

# q3
stu_list = []

def add_students():
    while True:
        print("1. Add student\n2. Quit")
        choose = input("CHOOSE: ").strip()
        
        if choose == "1":
            name = input("Name: ").strip().title()
            age = int(input("Age: "))
            score = float(input("Score: "))
            
            student = {
                "Name": name,
                "Age": age,
                "Score": score
            }
            stu_list.append(student)
            print("Student added successfully!\n")
        
        elif choose == "2":
            print("Exiting...")
            break
        
        else:
            print("INVALID INPUT\n")

def average_score():
    if len(stu_list) == 0:
        print("No students in the list yet.")
        return
    
    total = sum(student["Score"] for student in stu_list)
    avg = total / len(stu_list)
    print(f"Average Score:{avg:.2f}")

def highest_score():
    if len(stu_list) == 0:
        print("No students in the list yet.")
        return

    top_student = max(stu_list, key=lambda s: s["Score"])
    print(top_student)

def students_above_70():
    if len(stu_list) == 0:
        print("No students in the list yet.")
        return
    
    above_70 = [student for student in stu_list if student["Score"] > 70]
    
    if above_70:
        print("Students with scores above 70:")
        for s in above_70:
            print(f"Name: {s['Name']}, Age: {s['Age']}, Score: {s['Score']}")
    else:
        print("No student scored above 70.")

def age_set():
    ages_set = {student["Age"] for student in stu_list}
    print(f"Unique Ages: {ages_set}")

# --- MAIN MENU ---
def menu():
    while True:
        print("\n=== Student Management Menu ===")
        print("1. Add Students")
        print("2. Show Average Score")
        print("3. Show Highest Score")
        print("4. Show Students Above 70")
        print("5. Show Unique Ages")
        print("6. Quit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_students()
        elif choice == "2":
            average_score()
        elif choice == "3":
            highest_score()
        elif choice == "4":
            students_above_70()
        elif choice == "5":
            age_set()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("INVALID INPUT\n")

# Run the menu
menu()

# q4
import math
# Step 1: Collect 3 points
points = []
for i in range(3):
    x = float(input(f"Point {i+1} - x: "))
    y = float(input(f"Point {i+1} - y: "))
    coordinate = (x, y)   # store as tuple
    points.append(coordinate)

# Step 2: Print all points
print("\nAll points:")
for p in points:
    print(p)

# Step 3: Calculate distance between first two points
(x1, y1) = points[0]   # unpack tuple
(x2, y2) = points[1]
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"\nDistance between first two points: {distance:.2f}")

# Step 4: Check if third point has greater x than the first two
(x3, y3) = points[2]
if x3 > x1 and x3 > x2:
    print("The third point has a greater x value than the first two.")
else:
    print("The third point does NOT have a greater x value than the first two.")
