class Student:
    def __init__(self, name, age, department, reg_number):
        self.name = name
        self.age = age
        self.department = department
        self.reg_number = reg_number

    def show_student(self):
        return f"Name: {self.name}\nAge: {self.age}\nDepartment: {self.department}\nRegistration Number: {self.reg_number}"

student1 = Student(name="Alice Johnson", age=19, department="Computer Science", reg_number="REG001\n")
student2 = Student(name="Bob Smith", age=21, department="Mechanical Engineering", reg_number="REG002\n")
student3 = Student(name="Chidi Okafor", age=20, department="Business Administration", reg_number="REG003\n")

print(student1.show_student())
print(student2.show_student())
print(student3.show_student())