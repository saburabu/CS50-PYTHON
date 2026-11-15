int = int(input("Integer: "))

if 10 <= int <= 50:
    if not int in [20, 30, 40]:
        print("GREEN")
    else:
        print("RED")
elif 51 <= int <= 100 or int in [5, 7, 9]:
    print("YELLOW")
else:
    print("")