from employees import Employee


class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        # BUG: duplicate employee IDs are currently accepted.
        self.employees.append(employee)

    def find_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def remove_employee(self, employee_id):
        employee = self.find_employee(employee_id)
        if employee is None:
            raise LookupError("Employee not found.")
        self.employees.remove(employee)

    def payroll_report(self):
        lines = [f"Payroll for {self.name}"]
        total = 0
        for employee in self.employees:
            pay = employee.monthly_pay()
            total += pay
            lines.append(f"- {employee}: ₦{pay:,.2f}")
        lines.append(f"Total: ₦{total:,.2f}")
        return "\n".join(lines)
