count = 0
scores = [
    {"name": "sabur", "scores": ["80", "90", "75"]},
    {"name": "mike", "scores": ["60", "55", "70"]},
    {"name": "john", "scores": ["95", "88", "92"]},
    {"name": "sarah", "scores": ["40", "65", "50"]}
]

for student in scores:
    # convert string scores to integers
    int_scores = [int(s) for s in student["scores"]]
    
    # calculate sum and average
    total = sum(int_scores)
    average = total / len(int_scores)
    
    def remark(average):
        if average >= 60:
            return "PASS"
        else:
            return "FAIL"
    rk = remark(average)
    
    if average >= 60:
        count += 1
        print(f"{student['name'].title()} → Total: {total}, Average: {average:.2f}, REMARK: {rk}" )
    else:
        print(f"{student['name'].title()} → Total: {total}, Average: {average:.2f}, REMARK: {rk}" )

print(f"PASSED:{count}")