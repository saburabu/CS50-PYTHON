from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    @abstractmethod
    def monthly_pay(self):
        pass

    def profile(self):
        return f"{self.employee_id}: {self.name}"

    def __str__(self):
        return self.profile()


class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, monthly_salary):
        super().__init__(employee_id, name)
        self.monthly_salary = monthly_salary

    def monthly_pay(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, hours_worked, hourly_rate):
        super().__init__(employee_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def monthly_pay(self):
        # BUG: the values should be used to calculate pay, not added together.
        return self.hours_worked + self.hourly_rate
