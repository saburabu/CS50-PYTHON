score = int(input("Score: "))

def get_status(score):
    if 80 <= score <= 100:
        return "A"
    elif 60 <= score <= 79:
        return "B"
    elif 50 <= score <= 59:
        return "C"
    elif 0 <= score <= 49:
        return "F"
    else:
        return "INVALID"

print(get_status(score))