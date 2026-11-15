def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print(f"You deposited {amount}.")
    return balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print(f"You withdrew {amount}.")
    return balance

# Menu loop
balance = 0  # starting balance
while True:
    print("\n--- Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        balance = deposit(balance)
    elif choice == "2":
        balance = withdraw(balance)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
    
    print(f"Current balance: {balance}")
