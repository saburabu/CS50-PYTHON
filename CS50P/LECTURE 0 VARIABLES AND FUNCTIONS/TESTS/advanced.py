#student_average()

# where student inputs thier name and scores
name = input("Enter your name: ")
score1 = float(input("Enter your first score: "))
score2 = float(input("Enter your second score: "))
score3 = float(input("Enter your third score: "))
# where the average is calculated and returned
def student_average( score1, score2, score3):
    average = (score1 + score2 + score3) / 3
    return average
# where the average is calculated and printed
average = student_average(score1, score2, score3)
print(f"Name: {name}".strip().title())
print(f"Score 1: {score1}")
print(f"Score 2: {score2}")
print(f"Score 3: {score3}") 
# users final average score is printed to the screen
print("============================================")
print(f"{name}, your average score is: {average:.2f}")
print("=============================================")

print("Thank you for using the Student Average Calculator!")
