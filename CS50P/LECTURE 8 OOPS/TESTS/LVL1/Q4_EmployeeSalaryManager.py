lazy import random
class Employee:
    def __init__(self, employee_id, name, monthly_salary, department):
        self.employee_id = employee_id
        self.name = name
        self.monthly_salary = monthly_salary
        self.department = department

    def display_employee_details(self):
        return f"Employee ID: {self.employee_id}\nName: {self.name}\nMonthly Salary: ${self.monthly_salary:.2f}\nDepartment: {self.department}" 

    def increase_salary(self):
        print(f"Current monthly salary of {self.name}: ${self.monthly_salary:.2f}")
        increase_percentage = random.uniform(0.01, 0.5)
        self.monthly_salary += self.monthly_salary * increase_percentage
        print(f"The monthly salary of {self.name} has been updated to ${self.monthly_salary:.2f}.")

    def annual_salary(self):
        return self.monthly_salary * 12

    def change_department(self):
        print(f"Current department of {self.name}: {self.department}")
        new_department = input(f"Enter the new department for {self.name}: ")
        self.department = new_department
        print(f"The department of {self.name} has been updated to {self.department}.")

employee1 = Employee(employee_id=101, name="Alice", monthly_salary=5000, department="HR")
employee2 = Employee(employee_id=102, name="Bob", monthly_salary=6000, department="Finance")
employee3 = Employee(employee_id=103, name="Charlie", monthly_salary=5500, department="IT")
employee4 = Employee(employee_id=104, name="David", monthly_salary=7000, department="Marketing")
employee5 = Employee(employee_id=105, name="Eve", monthly_salary=6500, department="Sales")

# example 1:
print(employee1.display_employee_details())
# example 2:
employee2.increase_salary()
# example 3:
print(f"Annual salary of {employee3.name}: ${employee3.annual_salary():.2f}")
# example 4:
employee4.change_department()