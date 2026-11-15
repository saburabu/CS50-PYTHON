#Mini Calculator
print("Welcome to the Mini Calculator!")

price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))

def calculate_total(price, quantity):
    total = price * quantity
    return total


total = calculate_total(price, quantity)
print(f"The total cost is: ${total:.2f}")




































