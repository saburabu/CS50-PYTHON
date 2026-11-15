import re

class Student:
    @staticmethod
    def validate_name(name):
        name_pattern = r"^[A-Za-z]+(?:\s[A-Za-z]+){1,2}$"
        return bool(re.fullmatch(name_pattern, name))
    
    @staticmethod
    def validate_id(student_id):
        # Default parent pattern: STU- followed by letters/digits
        id_pattern = r"^STU-[A-Za-z0-9]+$"
        return bool(re.fullmatch(id_pattern, student_id))

    @staticmethod
    def validate_dep(department):
        dep_pattern = r"^[A-Za-z]+(?:\s[A-Za-z]+)*$"
        return bool(re.fullmatch(dep_pattern, department))

    def __init__(self, name: str, student_id: str, department: str):
        if not all(isinstance(x, str) for x in [name, student_id, department]):
            raise TypeError("All arguments must be strings!")

        if self.validate_name(name):
            self.name = name.strip().title()
        else:
            raise ValueError("Invalid name format!!!")
            
        # DYNAMIC CHECK: Changed 'Student.validate_id' to 'self.validate_id' 
        # so it respects child class overrides!
        if self.validate_id(student_id):
            self.__student_id = student_id.strip().upper() # Keep IDs uniform
        else:
            raise ValueError(f"Invalid student id format for {self.__class__.__name__}")
            
        if self.validate_dep(department):
            self.department = department.strip().title()
        else:
            raise ValueError("Invalid department format")
            
    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', id='{self.__student_id}', department='{self.department}')"


class UnderGraduate(Student):
    def __init__(self, name: str, student_id: str, department: str, level: int):
        super().__init__(name, student_id, department)

        if isinstance(level, int) and re.fullmatch(r"^\d{3}$", str(level)):
            self.level = level
        else:
            raise ValueError("Level must be a 3 digit integer!!!")

    @staticmethod
    def validate_id(student_id):
        ug_id_pattern = r"^STU-UG-[A-Za-z0-9]+$"
        return bool(re.fullmatch(ug_id_pattern, student_id, re.IGNORECASE))

    # Clean way to append level to the parent repr string
    def __repr__(self):
        parent_repr = super().__repr__()  # Gets everything up to the closing ')'
        return f"{parent_repr[:-1]}, level={self.level})"


class PostGraduate(Student):
    def __init__(self, name: str, student_id: str, department: str, research_area):
        super().__init__(name, student_id, department)
    
        if isinstance(research_area, str) and re.fullmatch(r"^[A-Za-z]+(?:\s[A-Za-z]+){1,2}$", research_area):
            self.research_area = research_area.strip().title()
        else:
            raise ValueError("Invalid research area format!!!")
    
    @staticmethod
    def validate_id(student_id):
        pg_id_pattern = r"^STU-PG-[A-Za-z0-9]+$"
        return bool(re.fullmatch(pg_id_pattern, student_id, re.IGNORECASE))

    # Clean way to append research area to the parent repr string
    def __repr__(self):
        parent_repr = super().__repr__()
        return f"{parent_repr[:-1]}, research_area='{self.research_area}')"

ug = UnderGraduate("Sabur Tunde", "STU-UG-2026", "Computer Science", 400)
pg = PostGraduate("Mary John", "STU-PG-8089", "Data Science", "Machine Learning")

print(ug)
# Output: UnderGraduate(name='Sabur Tunde', id='STU-UG-2026', department='Computer Science', level=400)

print(pg)
# Output: PostGraduate(name='Mary John', id='STU-PG-8089', department='Data Science', research_area='Machine Learning')