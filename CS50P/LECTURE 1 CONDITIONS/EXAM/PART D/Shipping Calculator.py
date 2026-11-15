weight = float(input("Weight of product(Kg): "))
distance = float(input("Distance(Km): "))

def shipping_cost(weight, distance):
    if weight <= 5:
        weight_charge = 1000
    else:
        weight_charge = 2000

    if distance <= 50:
        distance_charge = 1500
    else:
        distance_charge = 3000

    shipping = weight_charge + distance_charge
    return shipping

shipping = shipping_cost(weight, distance)
print(f"Shipping cost: ₦{shipping}")