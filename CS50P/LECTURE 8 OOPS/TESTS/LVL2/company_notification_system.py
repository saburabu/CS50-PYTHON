class Employee:
    # 2. Shared default notification preference (Class Variable)
    DEFAULT_NOTIFICATION_PREFERENCE = {"email": True, "sms": False}

    def __init__(self, name, department):
        # Every employee has a name and department
        self.name = name
        self.department = department
        # Starts as None because they don't have an individual override yet
        self.custom_preference = None

    # 3. Allow individual employees to override the default
    def change_notification_preference(self, email, sms):
        self.custom_preference = {"email": email, "sms": sms}

    # Helper method to get the current preference (either custom or default)
    def get_preference(self):
        if self.custom_preference is not None:
            return self.custom_preference
        
        # Fallback to the class-level default if no custom preference exists
        return Employee.DEFAULT_NOTIFICATION_PREFERENCE


# --- Execution Program ---

# 1. Create at least five employees
emp1 = Employee("John Doe", "Engineering")
emp2 = Employee("Jane Smith", "Marketing")
emp3 = Employee("Alice Johnson", "Sales")
emp4 = Employee("Bob Brown", "HR")
emp5 = Employee("Abu Sabur Osimua", "Autonomy Software Engineer")

# Put them in a list for easy tracking and loops
all_employees = [emp1, emp2, emp3, emp4, emp5]

# --- Step A: Display initial preferences (Everyone is on default) ---
print("--- Initial Preferences (All on Default) ---")
for emp in all_employees:
    print(f"{emp.name} ({emp.department}): {emp.get_preference()}")

# --- Step B: Override preferences for specific employees ---
print("\n[Action] John and Abu update their individual preferences...")
emp1.change_notification_preference(email=True, sms=True)
emp5.change_notification_preference(email=False, sms=True)

# --- Step C: 4. Change the company-wide default preference ---
print("\n[Action] Changing the shared company default preference...")
Employee.DEFAULT_NOTIFICATION_PREFERENCE = {"email": False, "sms": False}

# --- Step D: 5. Display the final preferences of all employees ---
print("\n--- Final Preferences (After Company Default Change) ---")
for emp in all_employees:
    # Important: Changing the default did not overwrite individual overrides
    print(f"{emp.name} ({emp.department}): {emp.get_preference()}")
