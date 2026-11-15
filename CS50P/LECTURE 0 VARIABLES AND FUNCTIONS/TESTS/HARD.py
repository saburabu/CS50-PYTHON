#Receipt Generator
#user inputs for name, items, prices, and quantities
name = input("Enter your name: ")
item_1 = input("Enter the name of the first item: ")
price_1 = float(input("Enter the price of the first item: "))
quantity_1 = int(input("Enter the quantity of the first item: "))
item_2 = input("Enter the name of the second item: ")
price_2 = float(input("Enter the price of the second item: "))
quantity_2 = int(input("Enter the quantity of the second item: "))
item_3 = input("Enter the name of the third item: ")
price_3 = float(input("Enter the price of the third item: "))
quantity_3 = int(input("Enter the quantity of the third item: "))
# where the total for each item is calculated and returned for each item
def calculate_total_1(item_1, price_1, quantity_1):
    total_1 = price_1 * quantity_1
    return total_1

def calculate_total_2(item_2, price_2, quantity_2):
    total_2 = price_2 * quantity_2
    return total_2

def calculate_total_3(item_3, price_3, quantity_3):
    total_3 = price_3 * quantity_3
    return total_3
# where the grand total is calculated and returned
def grand_total(total1, total2, total3):
    grand_total = total1 + total2 + total3
    return grand_total
#where the total for each item and the grand total is calculated
total_1 = calculate_total_1(item_1, price_1, quantity_1)
total_2 = calculate_total_2(item_2, price_2, quantity_2)
total_3 = calculate_total_3(item_3, price_3, quantity_3)
grand_total = grand_total(total_1, total_2, total_3)
# where the receipt is printed
name = name.strip().title()
def create_receipt(customer, item1, total1, item2, total2, item3, total3):
    print("===================================")
    print("           store receipt           ")
    print(f"Customer: {customer}")
    print("                                             ")
    print(f"Item 1: {item1} - Total: ${total1:.2f}")
    print(f"Item 2: {item2} - Total: ${total2:.2f}")
    print(f"Item 3: {item3} - Total: ${total3:.2f}")
    print("                                             ")
    print(f"Grand Total: ${grand_total:.2f}")
    print("===================================")
    print(f"Thank you for shopping with us, {customer}!")
    print("HAVE A GREAT DAY!")
