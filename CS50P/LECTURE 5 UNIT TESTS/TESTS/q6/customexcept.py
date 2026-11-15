class InvalidScoreError(Exception):
    pass


def check_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError

    return score