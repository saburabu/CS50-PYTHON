# shopping reciept

# WHERE THE USER INPUTS THE ITEM NAME, PRICE, AND QUANTITY
item = input("Enter the item name: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))
# where the total bill is calculated and returned
def calculate_bill(item, price, quantity):
    total = price * quantity
    return total
# where the total bill is calculated and printed
total = calculate_bill(item, price, quantity)
item = item.strip().title()
print("-------------------------------")
print(f"Item: {item}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: ${total:.2f}")
print("-------------------------------")
print("Thank you for shopping with us!")