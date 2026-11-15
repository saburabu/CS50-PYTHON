import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "age", "score"]
    )

    writer.writeheader()

    writer.writerow({
        "name": "Sabur",
        "age": 18,
        "score": 90
    })