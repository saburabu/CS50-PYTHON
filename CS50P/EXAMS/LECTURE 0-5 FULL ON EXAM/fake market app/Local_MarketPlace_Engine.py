import json
from Local_tools import (
    add_more_product_order,
    orders,
    validate_stock_range,
    search_products,
    add_product_order,
    remove_quantity_product_order,
    remove_product_order,
    checkout_order,
    clear_order_history,
    order_history,
)
from Local_users import user

def save_orders_to_file(data, filename):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except OSError as e:
        print(f"Error saving data to file: {e}")
    except TypeError as e:
        print(f"Error: data could not be converted to JSON: {e}")


def load_orders_from_file(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty list.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from file: {e}. Starting with an empty list.")
        return []
    except OSError as e:
        print(f"Error reading file: {e}. Starting with an empty list.")
        return []


def browse(products):
    from Local_tools import browse_products
    browse_products(products)


def search_menu(products):
    print("\nSearch products:")
    print("1. By Name/Category")
    print("2. Back to Main Menu")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        search_text = input("Enter product name or category: ").strip()

        if not search_text:
            print("Search cannot be empty.")
            return

        results = search_products(products, search_text)

        if not results:
            print("No products found.")
            return

        for product in results:
            print(
                f"ID: {product['id']}\n"
                f"Name: {product['name']}\n"
                f"Price: {product['price']}\n"
                f"Category: {product['category']}\n"
                f"Stock: {product['stock']}\n"
            )

            # Use the first matching product, matching the original project's design.
    if len(results) == 0:
        print("No results found.")
        selected_product = None
    elif len(results) == 1:
        # Only one result, just take it
        selected_product = results[0]
    else:
        # Multiple results, let user pick
        print("Multiple results found. Please choose one:")
        for i, product in enumerate(results, start=1):
            print(f"{i}. {product['name']}\nID: {product['id']}\nCategory: {product['category']}\nPrice: {product['price']}\nStock: {product['stock']}\n")

        choice = int(input("Enter the number of the product you want: "))
        selected_product = results[choice - 1]

    if selected_product:
        product_id = selected_product["id"]
        in_order = any(order["id"] == product_id for order in orders)
        print(f"Selected product ID: {product_id}, In order: {in_order}")


        if in_order:
            print(
                "1. Add to order\n"
                "2. Add more of the same product\n"
                "3. Remove a specific quantity from order\n"
                "4. Remove entire product from order\n"
                "5. Back to main menu"
            )
        else:
            print("1. Add to order\n2. Back to main menu")

        action = input("Enter your choice: ").strip()

        if action == "1":
            add_product_order(products, search_text)
        elif action == "2" and in_order:
            add_more_product_order(products, search_text)
        elif action == "3" and in_order:
            try:
                quantity = int(input("Enter quantity to remove: "))
                remove_quantity_product_order(products, search_text, quantity)
            except ValueError:
                print("Please enter a valid whole number.")
        elif action == "4" and in_order:
            remove_product_order(products, search_text)
        elif (action == "2" and not in_order) or (action == "5" and in_order):
            return
        else:
            print("Invalid choice.")


def checkout_menu(products):
    print(
        "\n1. Checkout"
        "\n2. View Order History"
        "\n3. Clear Order History"
        "\n4. Back to Main Menu"
    )

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        checkout_order(orders)
        save_orders_to_file(orders, "orders.json")
    elif choice == "2":
        order_history(orders)
    elif choice == "3":
        clear_order_history(orders, products)
        save_orders_to_file(orders, "orders.json")
        save_orders_to_file(products, "products.json")
    elif choice == "4":
        return
    else:
        print("Invalid choice.")


def main():
    products = load_orders_from_file("products.json")

    if not products:
        print("No products loaded.")
        return

    while True:
        print(f"\nuser: {user['name']}")
        print("Welcome to the Local Marketplace Engine!")
        print("1. Browse Products")
        print("2. Search Products")
        print("3. Checkout")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            browse(products)
        elif choice == "2":
            search_menu(products)
        elif choice == "3":
            checkout_menu(products)
        elif choice == "4":
            save_orders_to_file(orders, "orders.json")
            save_orders_to_file(products, "products.json")
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()