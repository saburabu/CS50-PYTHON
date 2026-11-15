balance = 0
def deposit(balance):
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")
        else:
            balance += amount
            return balance
    except ValueError as e:
        print("MUST BE NUMBER:", e)
        return balance 

balance = deposit(balance)
print("Updated balance:", balance)

