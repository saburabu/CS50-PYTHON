def create_product(product_name, price, category):
    return {
        "name": product_name,
        "price": price,
        "category": category
    }

def find_product(product_name, products):
    if not isinstance(product_name, str):
        return None

    for product in products:
        if product.get('name') == product_name.strip().title():
            return product
    return None

def show_products(products):
    for product in products:
        print(f"Name: {product['name']} -- Price: {product['price']} -- Category: {product['category']}")