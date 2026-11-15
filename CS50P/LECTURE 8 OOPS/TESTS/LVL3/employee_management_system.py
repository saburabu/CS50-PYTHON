class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = float(basic_salary)

    def calculate_bonus(self):
        """Parent method meant to be overridden by child classes."""
        return 0.0

    def total_monthly_earnings(self):
        """Calculates total earnings by combining base salary and the specific bonus."""
        return self.basic_salary + self.calculate_bonus()

    def __repr__(self):
        return (f"{self.__class__.__name__}(ID: {self.emp_id}, Name: {self.name}, "
                f"Base: ₦{self.basic_salary:,.2f}, Bonus: ₦{self.calculate_bonus():,.2f}, "
                f"Total: ₦{self.total_monthly_earnings:,.2f})")


class GeneralEmployee(Employee):
    def calculate_bonus(self):
        # General employees get a flat 5% performance bonus of their basic salary
        return self.basic_salary * 0.05


class Manager(Employee):
    def __init__(self, emp_id, name, basic_salary, team_size):
        super().__init__(emp_id, name, basic_salary)
        self.team_size = team_size

    def calculate_bonus(self):
        # Managers get a flat allowance of ₦50,000 plus ₦5,000 per team member managed
        return 50000.0 + (self.team_size * 5000.0)


class Developer(Employee):
    def __init__(self, emp_id, name, basic_salary, bugs_fixed):
        super().__init__(emp_id, name, basic_salary)
        self.bugs_fixed = bugs_fixed

    def calculate_bonus(self):
        # Developers get a direct productivity bonus of ₦2,500 per bug resolved
        return self.bugs_fixed * 2500.0
