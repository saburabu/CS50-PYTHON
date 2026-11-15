class InvalidScoreError(Exception):
    pass

def check_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("InvalidScoreError: Must be between 0 and 100")

while True:
    try:
        score = float(input("Score: "))
        check_score(score)
        print(f"SCORE: {score}")
    except InvalidScoreError as a:
        pass
        print(a)
    except ValueError as e:
        pass
        print(e)
        print("Must be an INTEGER between 0 and 100")
    else:
        break
    finally:
        print("DONE!")
