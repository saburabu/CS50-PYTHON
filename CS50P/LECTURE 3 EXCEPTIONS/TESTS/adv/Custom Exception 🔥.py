class InsufficientFundsError(Exception):
    pass
class ValueError(Exception):
    pass
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("INSUFFICIENTFUNDS: TRY AGAIN")
    elif amount < balance:
        x = balance - amount
        return x
    else:
        raise ValueError("PLEASE ENTER A NUMERICAL VALUE")
while True:
    try:
        amount = float(input("AMOUNT: "))
        balance = float(input("Balance: "))
        withdraw(balance, amount)
        print(f"AMOUNT: {amount}\nBALANCE: {balance}")
    except InsufficientFundsError as a:
        pass
        print(a)
    except ValueError("PLEASE ENTER A NUMERICAL VALUE") as b:
        pass
        print(b)
    else:
        print(f"====================\nNEW BALANCE: {withdraw(balance, amount)}\n====================")
        break
    finally:
        print("DONE!")