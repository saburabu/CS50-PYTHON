class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age =age 
        self.student_id = student_id

student1 = Student("Sabur", 16, 4949)
student2 = Student("Sabur", 16, 4949)

print(student1 is student2)
print(student1 == student2)

student1.name = "Davis"

print(student1.name)
print(student2.name)

# basically student1 is another object using the same student classes blueprint its like now for example
# me and my brother we are twins same name we meet an architect to get us a building plan now
# even if the house is the same same colour they arent the same house so like if i damage one of thier house the second persons own is the same
# so basically thats it