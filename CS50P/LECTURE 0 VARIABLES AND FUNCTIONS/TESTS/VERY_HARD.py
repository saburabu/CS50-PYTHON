#Student Report System
first_name = input("what is your firstname?:")
last_name = input("what is your lastname?:")
score1 = float(input("first score:"))
score2 = float(input("second score:"))
score3 = float(input("third score"))

def format_name(first_name, last_name):
    formatted_name = first_name.strip().title() + " " + last_name.strip().title()
    return formatted_name
formatted_name = format_name(first_name, last_name)

def calculate_average(score1, score2, score3):
    average = (score1 + score2 + score3) / 3
    return average
average = calculate_average(score1, score2, score3)

def create_report(name, average):
    x = create_report(name, average)

formatted_name = formatted_name.strip().title()
print("=================================")
print("           STUDENT REPORT        ")
print("=================================")
print(f"Student:{formatted_name}")
print(f"score:{average:.2f}")
print("=================================")











