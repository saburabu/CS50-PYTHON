

def get_name(first, last):
    return first.title() + " " + last.title()

def calculate_total(price, quantity):
    total = price * quantity
    return total

def create_message(name, total):
    return f"{name}, your total is ${total:.2f}"

first = input("First name: ")
last = input("Last name: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))

name = get_name(first, last)
total = calculate_total(price, quantity)
message = create_message(name, total)

print(message)