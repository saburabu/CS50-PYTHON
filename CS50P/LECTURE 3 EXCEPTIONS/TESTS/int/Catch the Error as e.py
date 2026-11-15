while True:
    try:
        number = int(input("Number: "))
        print(f"You entered {number}")
        break
    except ValueError as e:
        print(e)