inventory = {}

for _ in range(3):
    item = input("Enter an Item: ").strip().title()
    quantity = int(input("Enter the quantity of the item: "))
    inventory[item] = inventory.get(item, 0) + quantity  # add to existing quantity

for item, qty in inventory.items():
    print(item, qty)
