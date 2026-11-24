class BeyondRangeError(Exception):
    pass

def bre():
    if not 1 <= guess <= 50:
        raise BeyondRangeError("INVALID NUMBER ENTER SMTH WITHIN THE RANGE OF 1 AND 50 ")

import random as r

numbers = r.randint(1, 50)

while True:
    try:
        guess = int(input("Guess a number from 1 to 50 or 0 to quit: "))
        bre()

        if guess == numbers:
            print("CORRECT")
            break
        elif guess > numbers and guess <= 50:
            print("TOO HIGH ")
            pass
        elif guess < numbers and guess >= 1:
            print("TOO LOW ")
            pass
        elif guess == 0:
            print("YOU LOSER")
            break
    except ValueError as a:
        print(f"Must be an integer TRY AGAIN\n{a}")
    except BeyondRangeError as b:
        print(f"{b}")

