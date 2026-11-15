from Local_users import user

class Stock_Range_Error(Exception):
    pass

class Product_Not_Found_Error(Exception):
    pass

class Invalid_Quantity_Error(Exception):
    pass

class Insufficient_Balance_Error(Exception):
    pass

orders = []

def find_product(products, search_text):
    """Return the first product whose name or category matches the search."""
    if not search_text:
        return None

    lower_search = search_text.lower()

    for product in products:
        if (
            lower_search in product["name"].lower()
            or lower_search in product["category"].lower()
        ):
            return product
    return None

def validate_stock_range(product, quantity, user):
    """Check whether the requested quantity is valid for one product."""
    if quantity <= 0:
        raise Invalid_Quantity_Error(
            "Quantity must be greater than zero. Please enter a valid quantity."
        )

    elif quantity > product["stock"]:
        raise Stock_Range_Error(
            f"Product is not available in that quantity.\n"
            f"Available stock: {product['stock']}. Please enter a valid quantity."
        )

    elif user['balance'] < product["price"] * quantity or user['balance'] < quantity * product["price"] * 0.9:
        raise Insufficient_Balance_Error(
            "Insufficient balance to complete the purchase."
        )

def validate_quantity(quantity):
    if quantity <= 0:
        raise Invalid_Quantity_Error(
            "Quantity must be greater than zero. Please enter a valid quantity."
        )

def validate_product_exists(products, search_text):
    product = find_product(products, search_text)

    if product is None:
        raise Product_Not_Found_Error(
            f"Product '{search_text}' not found."
        )

    return product

def browse_products(products):
    if not products:
        print("No products available.")
        return

    for product in products:
        print(
            f"\nID: {product['id']}\n"
            f"Name: {product['name']}\n"
            f"Price: {product['price']}\n"
            f"Category: {product['category']}\n"
            f"Stock: {product['stock']}\n"
        )

def search_products(products, search_text):
    if not search_text:
        return []

    lower_search = search_text.lower()

    return [
        product
        for product in products
        if lower_search in product["name"].lower()
        or lower_search in product["category"].lower()
    ]

def add_product_order(products, search_text):
    try:
        product = validate_product_exists(products, search_text)
    except Product_Not_Found_Error as e:
        print(e)
        return

    while True:
        try:
            quantity = int(input("Enter quantity to order: "))
            validate_stock_range(product, quantity, user)
        except ValueError:
            print("Invalid quantity. Please enter a valid whole number.")
        except (Stock_Range_Error, Invalid_Quantity_Error, Insufficient_Balance_Error) as e:
            print(e)
        else:
            product["stock"] -= quantity

            order = {
                "id": product["id"],
                "name": product["name"],
                "price": product["price"],
                "category": product["category"],
                "quantity": quantity,
            }

            orders.append(order)

            print(
                f"Order placed for {quantity} of {product['name']}. "
                f"Remaining stock: {product['stock']}"
            )
            return

def add_more_product_order(products, search_text):
    try:
        product = validate_product_exists(products, search_text)
    except Product_Not_Found_Error as e:
        print(e)
        return

    order = next(
        (order for order in orders if order["id"] == product["id"]),
        None,
    )

    if order is None:
        print("Product not found in the order.")
        return

    while True:
        try:
            quantity = int(input("Enter additional quantity to order: "))
            validate_stock_range(product, quantity, user)
        except ValueError:
            print("Invalid quantity. Please enter a valid whole number.")
        except (Stock_Range_Error, Invalid_Quantity_Error, Insufficient_Balance_Error) as e:
            print(e)
        else:
            order["quantity"] += quantity
            product["stock"] -= quantity

            print(
                f"Added {quantity} more of {product['name']} to the order. "
                f"Remaining stock: {product['stock']}"
            )
            return

def remove_quantity_product_order(products, search_text, quantity):
    try:
        product = validate_product_exists(products, search_text)
        validate_quantity(quantity)
    except (Product_Not_Found_Error, Invalid_Quantity_Error) as e:
        print(e)
        return

    order = next(
        (order for order in orders if order["id"] == product["id"]),
        None,
    )

    if order is None:
        print("Product not found in the order.")
        return

    if quantity > order["quantity"]:
        print(
            f"Cannot remove {quantity}. "
            f"Only {order['quantity']} in the order."
        )
        return

    # Restore removed items to stock.
    product["stock"] += quantity
    order["quantity"] -= quantity

    if order["quantity"] == 0:
        orders.remove(order)
        print(f"Removed all of {order['name']} from the order.")
    else:
        print(
            f"Removed {quantity} of {order['name']} from the order. "
            f"Remaining quantity: {order['quantity']}"
        )

def remove_product_order(products, search_text):
    try:
        product = validate_product_exists(products, search_text)
    except Product_Not_Found_Error as e:
        print(e)
        return

    order = next(
        (order for order in orders if order["id"] == product["id"]),
        None,
    )

    if order is None:
        print("Product not found in the order.")
        return

    # Return the complete ordered quantity to stock.
    product["stock"] += order["quantity"]
    orders.remove(order)

    print(f"Removed {order['name']} from the order.")

def checkout_order(orders):
    if not orders:
        print("Your order is empty.")
        return

    print("Order Summary:")

    grand_total = 0
    try:
        for order in orders:
            total_price = order["price"] * order["quantity"]
            print(f"User: {user['name']}")
            
            if total_price > 100000:
                discounted_price = total_price * 0.9
                print(
                    f"Product: {order['name']}, "
                    f"Quantity: {order['quantity']}, "
                    f"Total Price: {discounted_price:.2f} "
                    f"(10% discount applied)"
                )
                grand_total += discounted_price
            else:
                    print(
                        f"Product: {order['name']}, "
                        f"Quantity: {order['quantity']}, "
                        f"Total Price: {total_price:.2f}"
                    )
                    grand_total += total_price

        print(f"Grand Total: {grand_total:.2f}")
    except Insufficient_Balance_Error as e:
        print(e)
        return

def order_history(orders):
    if not orders:
        print("Order History is empty.")
        return

    print("Order History:")

    for order in orders:
        total_price = order["price"] * order["quantity"]
        print(
            f"Product: {order['name']}, "
            f"Quantity: {order['quantity']}, "
            f"Total Price: {total_price:.2f}"
        )

def clear_order_history(orders, products=None):
    # Return ordered products to stock before clearing the order.
    if products is not None:
        for order in orders:
            product = next(
                (product for product in products if product["id"] == order["id"]),
                None,
            )
            if product is not None:
                product["stock"] += order["quantity"]

    orders.clear()
    print("Order history cleared.")
