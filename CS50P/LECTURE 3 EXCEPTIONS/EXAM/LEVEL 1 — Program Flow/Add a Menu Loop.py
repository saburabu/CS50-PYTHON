balance = 1000
count_d = 0
count_w = 0
while True:
    print(f"1.Deposit\n2.Withdraw\n3.CheckBalance\n4.Quit")

    choice = str(input("Choice: "))

    if choice == "1":
        deposit = int(input("How much will you like to deposit: "))
        print(f"InitialBalance: {balance}")
        balance += deposit
        count_d += 1
        print(f"FinalBalance: {balance}")
        print(f"TotalDeposits: {count_d}")
    elif choice == "2":
        withdraw = int(input("How much will you like to withdraw: "))
        print(f"InitialBalance: {balance}")
        balance -= withdraw
        count_w += 1
        print(f"FinalBalance: {balance}")
        print(f"TotalWithdraw's: {count_w}")
    elif choice == "3":
        print(f"AccountBalance: {balance}")
    else:
        if choice == "4":
            print(f"You have used your banking app {count_w + count_d} times today")
            break
