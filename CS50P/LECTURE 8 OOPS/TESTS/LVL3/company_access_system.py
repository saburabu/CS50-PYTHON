class Employee:
    def check_permissions(self):
        print("-> Processing inside: Employee")

class Manager(Employee):
    def check_permissions(self):
        print("-> Processing inside: Manager")
        super().check_permissions()

class SecurityManager(Employee):
    def check_permissions(self):
        print("-> Processing inside: SecurityManager")
        super().check_permissions()

class Administrator(Manager, SecurityManager):
    def check_permissions(self):
        print("-> Starting chain reaction inside: Administrator")
        super().check_permissions()

# --- DEMONSTRATION CODE (Required to fully answer the question) ---

# Requirement 7: Print the MRO of Administrator
print("=== Requirement 7: Method Resolution Order (MRO) ===")
for i, cls in enumerate(Administrator.__mro__, 1):
    print(f"{i}. {cls.__name__}")

print("\n" + "="*50 + "\n")

# Requirement 8: Demonstrate the order in which methods execute
print("=== Requirement 8: Actual Method Execution Order ===")
admin = Administrator()
admin.check_permissions()
