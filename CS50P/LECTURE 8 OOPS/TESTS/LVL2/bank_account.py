lazy import re

class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance):
        # Patterns: 
        # Holder: Matches "First Last" or "First Middle Last"
        account_holder_pattern = r"^[A-Za-z]+\s(?:[A-Za-z]+)?(?:\s[A-Za-z]+)*$"
        # Number: Must be exactly 10 digits (Nigerian NUBAN standard)
        account_number_pattern = r"^\d{10}$"

        # 1. Validate Account Holder Name
        if re.fullmatch(account_holder_pattern, account_holder.strip()):
            self.account_holder = account_holder.strip()
        else:
            raise ValueError("Invalid Name! Must be First and Last name containing only letters.")

        # 2. Validate Account Number
        if re.fullmatch(account_number_pattern, str(account_number)):
            self.account_number = str(account_number)
        else:
            raise ValueError("Invalid Account Number! Must be exactly 10 numeric digits.")

        # 3. Validate and set initial balance directly to the hidden field at birth
        if isinstance(initial_balance, (int, float)) and initial_balance >= 0:
            self.__balance = initial_balance
        else:
            raise ValueError("Initial balance cannot be negative.")

    # --- 1. THE GETTER PROPERTY ---
    @property
    def balance(self):
        """Allows reading the balance safely like an attribute."""
        return self.__balance

    # --- 2. THE SETTER PROPERTY (THE LOCKDOWN TRAP) ---
    @balance.setter
    def balance(self, amount):
        """Fulfills the setter structure but explicitly rejects ALL direct assignments."""
        raise AttributeError("Direct balance modification is strictly forbidden! Use deposit() or withdraw().")

    # --- Controlled Transaction Methods ---
    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            # Modify the hidden variable directly to bypass the setter lock
            self.__balance += amount
            return f"Amount deposited: ₦{amount:,} | Final balance: ₦{self.__balance:,}"
        return "Invalid deposit amount! Must be a positive number."

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            return "Invalid withdrawal amount! Must be a positive number."
        
        if amount > self.__balance:
            return f"Transaction Denied: Insufficient funds! Available: ₦{self.__balance:,}."
            
        # Modify the hidden variable directly to bypass the setter lock
        self.__balance -= amount
        return f"Amount withdrawn: ₦{amount:,} | Final balance: ₦{self.__balance:,}"


# --- Verification Tests ---
account = BankAccount("Abu Sabur Osimua", "0123456789", 50000)

# 1. Reading the balance via the getter works perfectly!
print(f"Initial balance check: ₦{account.balance:,}") 

# 2. Modifying via formal banking operations works seamlessly!
print(account.deposit(25000))
print(account.withdraw(10000))

# 3. CHALLENGE TEST: Trying to assign a value directly (even a valid positive one)
print("\n[Action] Attempting direct assignment: account.balance = 90000...")
try:
    account.balance = 90000  # This hits the setter guard and immediately trips the block
except AttributeError as error:
    print(f"🛡️ Security Blocked: {error}")

# Confirming that the data completely avoided any assignment
print(f"Final safe balance verification: ₦{account.balance:,}")

