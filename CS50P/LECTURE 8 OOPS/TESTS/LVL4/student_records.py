import re
from dataclasses import dataclass, field

@dataclass
class Student:
    _student_id: str
    name: str
    courses: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.validate()

    @property
    def student_id(self) -> str:
        """Provides read-only access to _student_id."""
        return self._student_id

    def validate(self):
        if not isinstance(self._student_id, str) or not isinstance(self.name, str) or not isinstance(self.courses, list):
            raise TypeError("ID and name must be strings, and courses must be a list.")

        student_id_pattern = r"^STU-[A-Za-z0-9]+$"
        if not re.fullmatch(student_id_pattern, self._student_id, re.IGNORECASE):
            raise ValueError("ID must begin with 'STU-' followed by letters or numbers.")

        if not self.courses:
            raise ValueError("Courses list cannot be empty.")

    def __repr__(self):
        return f"Student id: {self._student_id}, Name: {self.name}, Courses: {self.courses}"
    def enroll(self, course: str):
        if not isinstance(course, str):
            raise TypeError("Course must be a string.")
            
        # Matches 2 to 4 uppercase letters, a hyphen, and 3 digits (e.g., CS-101, MATH-204)
        if not re.fullmatch(r"^[A-Z]{2,4}-\d{3}$", course):
            raise ValueError("Course must follow format 'DEPT-101' (e.g., CS-101).")
            
        if course not in self.courses:
            self.courses.append(course)

        return f"{self.name}, {course} has been added to your courses so your list of courses are: {self.courses}"

student1 = Student(name="Sabur Abu", courses=["CSC-101", "COS-303", "MATH101"], _student_id="STU-001")
print(student1)
print(student1.enroll("STAT-102"))