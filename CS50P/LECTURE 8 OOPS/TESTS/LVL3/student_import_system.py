class Student:
    university = "Wigwe University"
    
    def __init__(self, name, id, age):
        if Student.validate_id(id):
            self.name = name
            self.id = id
            self.age = age
        else:
            print("Invalid ID format")

    def __repr__(self):
        return f"Student(name='{self.name}', id='{self.id}', age={self.age}, university='{self.university}')"

    @classmethod
    def from_csv(cls, student_string):
        if student_string and isinstance(student_string, str):
            name, id, age = [item.strip() for item in student_string.split(",")]
            
            if cls.validate_id(id):
                return cls(name, id, int(age))
        return None

    @classmethod
    def from_dict(cls, student_dict):
        if student_dict and isinstance(student_dict, dict):
            if len(student_dict) == 3:
                name = student_dict.get("name")
                id = student_dict.get("id") or student_dict.get("student_id")
                age = student_dict.get("age")
                
                if cls.validate_id(id):
                    return cls(name, id, int(age))
                
        return "Invalid Input try again"

    @staticmethod
    def validate_id(student_id):
        if student_id and isinstance(student_id, str) and student_id.startswith("STU-"):
            return True
        return False

    @classmethod
    def change_school(cls, new_school):
        if new_school and isinstance(new_school, str):
            cls.university = new_school
            return f"New institution: {cls.university}"
        return None


# Test code execution
Student.change_school("Nile university abuja")

student1 = Student("Sabur", "STU-001", 18)
student2 = Student.from_csv("John,STU-002,19")
student3 = Student.from_dict({
    "name": "Mary",
    "student_id": "STU-003",
    "age": 17
})

# Displaying info on screen
print(student1)
print(student2)
print(student3)
