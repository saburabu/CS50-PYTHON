numbers = ["10", "20", "hello", "30", "cat", "40"]
int_scores = []

for item in numbers:
    try:
        int_scores.append(int(item))
    except ValueError:
        # Skip non-numeric values
        continue

print(int_scores)
