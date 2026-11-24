import random

numbers = random.randint(1, 20)

while True:
    guess = int(input("Guess a number from 1 to 20 or 0 to quit: "))
    if guess == numbers:
        print("CORRECT")
        break
    elif guess == 0:
        print("YOU LOSER")
        break
    else:
        print("INCORRECT TRY AGAIN")
        pass