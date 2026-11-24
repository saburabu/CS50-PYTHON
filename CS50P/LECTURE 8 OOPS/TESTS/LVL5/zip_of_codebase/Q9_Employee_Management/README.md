# Q9 — Employee Management System (Revised for your current OOP notes)

## Scenario
A company manages employees with different pay arrangements. The current program runs, but some employee information and payroll rules are not protected correctly. Inspect and improve the existing code.

## Run it
From this folder, run:

```bash
python main.py
```

No packages need to be installed.

## Files
- `employees.py` — abstract employee parent and employee types
- `company.py` — company employee collection and payroll report
- `main.py` — demonstration

## Requirements
1. Every employee must have a non-empty ID and name.
2. Pay-related values must not be negative.
3. A full-time employee's monthly pay is their monthly salary.
4. A part-time employee's monthly pay is hours worked multiplied by hourly rate.
5. Salary and pay information must be protected from invalid later assignments. Use a property where appropriate.
6. A company must not accept two employees with the same ID.
7. Searching by ID must return the matching employee or `None`.
8. Removing an employee must update the company's employee collection accurately.
9. The payroll report must show every employee once and calculate the correct total.
10. Add a `ContractEmployee` class. Its monthly pay is a fixed contract amount, and it must work with the existing payroll report without rewriting that report.

## Boundaries
- Keep the abstract `Employee` parent and use inheritance and polymorphism.
- Use concepts from your notes: ABCs, abstract methods, `super()`, overriding, properties, encapsulation and object collections.
- No database, API, file storage, advanced typing, decorators, or complex payroll rules are required.
- Do not build a full HR application. Implement the requirements and keep the demo runnable.
