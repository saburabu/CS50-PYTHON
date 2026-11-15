while True:
    try:
        number = float(input("Number: "))
        break
    except ValueError:
        pass
        print("INVALID NUMBER!")