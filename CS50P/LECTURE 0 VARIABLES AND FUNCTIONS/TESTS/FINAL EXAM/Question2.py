# Debug + Rebuild

# where customer inputs their information
customer = input("Customer name: ")
item = input("Item name: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))
discount = float(input("Discount percentage: "))
# where the functions are defined
def calculate_subtotal(price, quantity):
    subtotal = price * quantity
    return subtotal
subtotal = calculate_subtotal(price, quantity)
# where the functions are defined
def calculate_discount(subtotal, discount):
    discount_amount = subtotal * discount * 0.01
    final_total = subtotal - discount_amount
    return final_total
final_total = calculate_discount(subtotal, discount)
# where the function is printed and the customer details are formatted
customer = customer.strip().title()
item = item.strip().title()
def create_receipt(customer, item, final_total):
    message = f"{customer}: {item} costs ${final_total}"
    return message
message = create_receipt(customer, item, final_total)

print(message)














