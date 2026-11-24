class Course:
    def __init__(self, title):
        if not title or not isinstance(title, str):
            raise ValueError("Course title must be a non-empty string")
        self.title = title
        self._students = []

    def get_students(self):
        return self._students


class Student:
    def __init__(self, name, courses=None):
        # 1. Check name properly (outside the 'if not name' block)
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")

        self.name = name
        self._courses = []

        # 2. If courses are passed at creation, use register() so BOTH objects update!
        if courses is not None:
            if not isinstance(courses, list):
                raise ValueError("Courses must be passed as a list of Course objects")
            for course in courses:
                self.register(course)

    # Req 2, 4, 5: Register, update both objects, and prevent duplicates
    def register(self, course):
        if not isinstance(course, Course):
            raise ValueError("You can only register a valid Course object")
        
        if course not in self._courses:
            self._courses.append(course)
            course._students.append(self)  # Updates the Course side too!

    # Req 6: Withdraw and keep both sides consistent
    def withdraw(self, course):
        if course in self._courses:
            self._courses.remove(course)
            course._students.remove(self)  # Removes from Course side too!

    # Req 7: Retrieve all courses belonging to a student
    def get_courses(self):
        return self._courses


math = Course("MTH 101")
csc = Course("CSC 102")

# Using your classmethod!
s1 = Student("Chisom", [math, csc])

print([c.title for c in s1.get_courses()])     # ['MTH 101', 'CSC 102']
print([s.name for s in math.get_students()])   # ['Chisom']

s1.withdraw(math)
print([s.name for s in math.get_students()])   # [] (Consistent!)
