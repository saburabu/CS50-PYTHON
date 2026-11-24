from company import Company
from employees import FullTimeEmployee, PartTimeEmployee


def main():
    company = Company("Bright Future Ltd")
    company.add_employee(FullTimeEmployee("E01", "Chioma", 180000))
    company.add_employee(PartTimeEmployee("E02", "Tunde", 48, 2500))

    print(company.payroll_report())
    print("Found:", company.find_employee("E01"))


if __name__ == "__main__":
    main()
