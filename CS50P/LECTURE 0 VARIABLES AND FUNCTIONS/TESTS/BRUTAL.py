# Mini Banking Transaction
account_holder = input("what is you your name\"fullname\" ")
balance = float(input("what is your starting balance "))
deposit = float(input("how much will you like to deposit "))
withdrawal = float(input("how much will you like to withdraw "))

def calculate_deposit(balance, deposit):
    total_1 = balance + deposit
    return total_1

def calculate_withdrawal(balance, withdrawal):
    total_2 = balance - withdrawal
    return total_2

account_holder = account_holder.strip().title()
def create_statement(name, starting_balance, deposit, withdrawal, final_balance):
    print("===============================================")
    print("                 BANK STATEMENT                ")
    print("===============================================")
    print(f"Account-holder:{account_holder}")
    print("                                               ")
    print(f"Starting balance: {balance:,.2f}")
    print(f"Deposit:          {deposit:,.2f}")
    print(f"Withdrawal:       {withdrawal:,.2f}")
    print(f"Final Balance:")