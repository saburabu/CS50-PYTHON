class InvalidScoreError(Exception):
    pass
def process_score(score):
    if not 0 <= score <= 100:
        raise InvalidScoreError("InvalidScore: TRY AGAIN")

while True:
    try:
        score = int(input("Score: "))
        process_score(score)
        print(f"SCORE: {score}")
    except InvalidScoreError as a:
        pass
        print(a)
    except ValueError("Kindly enter an integer") as b:
        pass
        print(b)
    else:
        break
    finally:
        print("DONE!")

        