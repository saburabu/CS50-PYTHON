def get_positive_number():
    while True:
        try:
            number = int(input("Number: "))  # force integer input
            if number <= 0:
                raise ValueError("Number must be positive.")
            return number
        except ValueError as e:
            if str(e) == "Number must be positive.":
                print("Number must be positive.")
            else:
                print("Invalid number.")
get_positive_number()