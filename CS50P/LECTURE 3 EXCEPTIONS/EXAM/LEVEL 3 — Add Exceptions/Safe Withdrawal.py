class InsufficientFundsError(Exception):
    pass

def deposit(balance):
    try:
        amount = int(input("Deposit amount: "))

        if amount <= 0:
            raise ValueError("Deposit must be positive.")

        return balance + amount

    except ValueError as e:
        print(e)
        return balance

def withdraw(balance):
    try:
        amount = int(input("Withdraw amount: "))

        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")

        if amount > balance:
            raise InsufficientFundsError("Not enough money.")

        return balance - amount

    except ValueError as e:
        print(e)
        return balance

    except InsufficientFundsError as e:
        print(e)
        return balance

balance = 1000

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Quit")

    choice = input("Choose: ")

    if choice == "1":
        balance = deposit(balance)

    elif choice == "2":
        balance = withdraw(balance)

    elif choice == "3":
        print("Balance:", balance)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")

