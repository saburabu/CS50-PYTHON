# track how many positives were added
def analyze(numbers):
    total = 0        # accumulator
    count = 0        # counter
    
    for number in numbers:   # loop through list
        if number < 0:
            continue        # skip negatives
        if number == 0:
            break           # stop completely
        total += number     # add positives
        count += 1          # increment counter
    
    return total, count      # return both values


# Example usage
numbers = [15, -4, 8, 20, -7, 3, 0, 100]
result_total, result_count = analyze(numbers)
print(f"Total: {result_total}")
print(f"Count: {result_count}")