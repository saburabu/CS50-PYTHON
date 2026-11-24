import json

# Step 1: Create the dictionary
student = {
    "name": "Sabur",
    "age": 18,
    "scores": [80, 92, 75]
}

# Step 2: Convert dictionary into a JSON string
student_json = json.dumps(student)
print("JSON string:")
print(student_json)

# Step 3: Convert JSON string back into a Python dictionary
student_dict = json.loads(student_json)
print("\nBack to dictionary:")
print(student_dict)

# Step 4: Print the student's name and average score
average_score = sum(student_dict["scores"]) / len(student_dict["scores"])
print(f"\nStudent Name: {student_dict['name']}")
print(f"Average Score: {average_score:.2f}")
