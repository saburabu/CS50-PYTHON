# i used while true to check out my skills
balance = 1000
count = 0

while True:
    deposit = float(input("How much do you want to deposit: "))
    print(f"InitialBalance: {balance}")
    balance += deposit
    count += 1
    print(f"FinalBalance: {balance}")
    print(f"TotalDeposits: {count}")
    q = str(input("Are you done with your deposit(yes/no): ")).strip().lower()
    if q == "yes":
        break
    else:
        pass