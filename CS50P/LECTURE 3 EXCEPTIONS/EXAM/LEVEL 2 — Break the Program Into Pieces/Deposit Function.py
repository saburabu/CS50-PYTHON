def deposit(balance):
    # Ask the user for the deposit amount
    amount = float(input("Enter amount to deposit: "))
    
    # Add the amount to the balance
    balance += amount
    
    # Return the new balance
    return balance

# Example usage:
balance = 1000  # starting balance
balance = deposit(balance)
print("Updated balance:", balance)
