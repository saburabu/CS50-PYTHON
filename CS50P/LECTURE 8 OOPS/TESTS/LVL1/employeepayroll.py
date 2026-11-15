class Employee:
    def __init__(self, name, job_title, monthly_salary, worked_months):
        self.name = name
        self.job_title = job_title
        self.monthly_salary = monthly_salary
        self.worked_months = worked_months

    def total_earnings(self):
        return self.monthly_salary * self.worked_months

    def display_information(self):
        return f"Name: {self.name}, Job Title: {self.job_title}, Monthly Salary: ${self.monthly_salary}, Worked Months: {self.worked_months}, Total Earnings: ${self.total_earnings()}"

emp1 = Employee("Alice", "Software Engineer", 50000.23, 12)
emp2 = Employee("Bob", "Data Analyst", 45000.50, 10)
emp3 = Employee("Charlie", "Project Manager", 60000.75, 15)
emp4 = Employee("Diana", "UX Designer", 48000.00, 8)

# Displaying information for each employee
print(emp1.display_information())
print(emp2.display_information())
print(emp3.display_information())
print(emp4.display_information())
# total earnings for each employee
print(f"{emp1.name}'s Total Earnings: ${emp1.total_earnings()}")
print(f"{emp2.name}'s Total Earnings: ${emp2.total_earnings()}")
print(f"{emp3.name}'s Total Earnings: ${emp3.total_earnings()}")
print(f"{emp4.name}'s Total Earnings: ${emp4.total_earnings()}")