import statistics as stats
students = [
    {"name": "John", "score": 80},
    {"name": "Mary", "score": 95},
    {"name": "Alex", "score": 70},
    {"name": "David", "score": 85}
]
stu = []
for student in students:
    stu.append(student['score'])

ave = stats.mean(stu)
print(f"AVERAGE: {ave}")