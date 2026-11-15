class Department:

    academic_year = 2026

    def __init__(self, department_name, number_students):
        self.department = department_name
        self.students = number_students

    def display_info(self):
        return f"Name of department: {self.department}, number of students: {self.students}, academic_year: {self.academic_year}"

dep1 = Department("Computer Science", 120)
dep2 = Department("Mathematics", 80)
dep3 = Department("Physics", 60)
dep4 = Department("Chemistry", 90)

print(dep1.display_info())
print(dep2.display_info())
print(dep3.display_info())
print(dep4.display_info())

Department.academic_year = 2027

print(dep1.display_info())
print(dep2.display_info())
print(dep3.display_info())
print(dep4.display_info())

dep1.academic_year = 2025

print(dep1.display_info())
print(dep2.display_info())
print(dep3.display_info())
print(dep4.display_info())