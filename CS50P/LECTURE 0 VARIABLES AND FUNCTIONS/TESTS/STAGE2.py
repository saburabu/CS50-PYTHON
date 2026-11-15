# Two Functions + Function Calling
item = str(input("Enter an item: "))
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))

def calculate_total(price, quantity):
    total = price * quantity
    return total

def create_message(item, total):
    return f"The total cost of {quantity} {item}(s) is ${total:.2f}"

print("===================================")
print("          RECEIPT                   ")
print("===================================")
print(f"Item: {item}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")

total = calculate_total(price, quantity)
message = create_message(item, total)
print(message)
print("===================================")
print("Thank you for shopping with us!") 