#Employee Pay Calculator
employee_name = input("Enter the employee's name: ")
hours_worked = float(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the hourly rate: "))
# where the pay is calculated and returned
def calculate_pay(name, hours, rate):
    pay = hours * rate
    return pay
# where the pay is calculated and printed
pay = calculate_pay(employee_name, hours_worked, hourly_rate)
employee_name = employee_name.strip().title()
print(f"{employee_name} has earned ${pay:.2f}")
print("Thank you for using the Employee Pay Calculator!")