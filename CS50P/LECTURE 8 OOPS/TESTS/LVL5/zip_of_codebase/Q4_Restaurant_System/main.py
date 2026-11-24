from menu import DrinkItem, FoodItem
from restaurant import Restaurant, Table


def main():
    restaurant = Restaurant("The Learning Spoon")
    table = Table(4, 4)
    restaurant.add_table(table)

    order = restaurant.open_order(table)
    order.add_item(FoodItem("Jollof Rice", 2500, True))
    order.add_item(DrinkItem("Zobo", 700, "large"))

    print(restaurant.table_summary(table))
    for item in order.items:
        print(item)
    print(f"Bill: ₦{order.total():,.2f}")

    restaurant.close_order(order)
    print(restaurant.table_summary(table))


if __name__ == "__main__":
    main()
