while True:
    try:
        age = int(input("Age: "))
        print(f"Your {age} years old")
        break
    except ValueError:
        pass
        print("ENTER A VALID NUMBER")
