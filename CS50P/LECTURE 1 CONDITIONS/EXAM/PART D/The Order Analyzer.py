price = float(input("Price: "))
quantity = int(input("Quantity: "))
member = input("Member (yes/no): ").strip().lower()

def calculate_total(price, quantity, member):
    sub_total = price * quantity

    if sub_total >= 50000 and member == "yes":
        discount_rate = 0.20
        print("20% DISCOUNT")
    elif sub_total >= 50000:
        discount_rate = 0.10
        print("10% DISCOUNT")
    elif member == "yes":
        discount_rate = 0.05
        print("5% DISCOUNT")
    else:
        discount_rate = 0.0
        print("0% DISCOUNT")

    total = sub_total - (sub_total * discount_rate)
    return sub_total, total

sub_total, total = calculate_total(price, quantity, member)
print(f"Subtotal: {sub_total}")
print(f"Total: {total}")

