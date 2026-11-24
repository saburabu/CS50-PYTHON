# Delivery Cost System

# where user's input's thier data
Customer_name = input("Enter customer name: ")
Package_weight = float(input("Enter package weight in kg: "))
Distance = float(input("Enter distance in km: "))
Price_per_kg = float(input("Enter price per kg: "))
Price_per_km = float(input("Enter price per km: "))
#where functions are defined and logic of the system
def weight_charge(package_weight, price_per_kg):
    total_w = package_weight * price_per_kg
    return total_w
total_w = weight_charge(Package_weight, Price_per_kg)

def distance_charge(distance, price_per_km):
    total_d = distance * price_per_km
    return total_d
total_d = distance_charge(Distance, Price_per_km)

def final_cost(total_w, total_d):
    final_total = total_w + total_d
    return final_total
final_total = final_cost(total_w, total_d)
#where the reciept functions is being defined
def create_message(Customer_name, package_weight, distance, total_w, total_d, final_total):
    message = f"Customer: {Customer_name}\nPackage Weight: {Package_weight} kg\nDistance: {Distance} km\nWeight Charge: ${total_w:.2f}\nDistance Charge: ${total_d:.2f}\n----------------------------------------\nFinal Cost: ${final_total:.2f}"
    return message
message = create_message(Customer_name, Package_weight, Distance, total_w, total_d, final_total)
customer_name = Customer_name.strip().title()
#where the reciept is being printed
print("===================================")
print("         DELIVERY INVOICE          ")
print("===================================")
print(message)
print("===================================")
print(f"Thank you for using our delivery service, {customer_name}!")