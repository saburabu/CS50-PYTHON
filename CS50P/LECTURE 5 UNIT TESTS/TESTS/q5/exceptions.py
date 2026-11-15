def calculate_average(scores):
    if not scores:
        raise ValueError("No scores provided")

    return sum(scores) / len(scores)