while True:
    try:
        first = float(input("First Number: "))
        second = float(input("Second Number: "))
        ave = first / second
        print(f"{first}/{second} = {ave}")
       
    except ValueError:
        pass
        print("INVALID NUMBER")
    except ZeroDivisionError:
        pass
        print("NONE OF THE NUMBERS MUST BE ZERO")
    else:
        break
    

