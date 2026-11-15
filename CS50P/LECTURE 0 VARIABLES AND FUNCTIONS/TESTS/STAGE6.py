#FUNCTION ARCHITECTURE
costumer_name = input("Enter customer name: ")
food_item = input("Enter food item: ")
price = float(input("Enter price of the food item: "))
quantity = int(input("Enter quantity of the food item: "))

def calculate_total(price, quantity):
    total = price * quantity
    return total
total = calculate_total(price, quantity)

def service_charge(total):
    service_fee = total * 0.10
    return service_fee
service_fee = service_charge(total)

def create_message(costumer_name, food_item, total, service_fee):
    return f"Customer name: {costumer_name}\nFood item: {food_item}\nTotal: ${total:.2f}\nService fee: ${service_fee:.2f}"

costumer_name = costumer_name.strip().title()
message = create_message(costumer_name, food_item, total, service_fee)
print("===================================")
print("          FOOD ORDER RECEIPT        ")
print("===================================")
print(message)
print("===================================")
def thanks(costumer_name):
    return f"Thank you for your order, {costumer_name}!"
print(thanks(costumer_name))