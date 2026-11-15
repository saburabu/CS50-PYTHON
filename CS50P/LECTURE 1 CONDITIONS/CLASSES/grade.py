# where the user inputs the student's name and score
name = input("Student's Name: ")
score = float(input("Score: "))
# where the logic is to check the score and assign a grade based on the score and formatted
name = name.strip().title()
if score >= 90 and score <= 100:
    print(f"{name} has an A.")
elif score >= 80 and score < 90:
    print(f"{name} has a B.")
elif score >= 70 and score < 80:
    print(f"{name} has a C.")
elif score >= 60 and score < 70:
    print(f"{name} has a D.")
elif score >=50 and score < 60:
    print(f"{name} has an E.")
else:    
    print(f"{name} has a  F.")

# however there's a shorter way to do this without the "and"
if score >= 90 <= 100:
    print(f"{name} has an A.")
elif score >= 80 < 90:
    print(f"{name} has a B.")
elif score >= 70 < 80:
    print(f"{name} has a C.")
elif score >= 60 < 70:
    print(f"{name} has a D.")
elif score >=50 < 60:
    print(f"{name} has an E.")
else:    
    print(f"{name} has a  F.")

# moreover, we can still do this it's a more shorter way than using both an upper bound and a lower bound
if score >= 90:
    print(f"{name} has an A.")
elif score >=80:
    print(f"{name} has a B.")
elif score >= 70:
    print(f"{name} has a C.")
elif score >= 60:
    print(f"{name} has a D.")
elif score >=50:
    print(f"{name} has an E.")
else:    
    print(f"{name} has a  F.")