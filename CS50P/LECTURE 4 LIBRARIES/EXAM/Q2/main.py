import json, requests
from product_tools import create_product as CP
from product_tools import find_product as FP
from product_tools import show_products as SP

USER_FILE = "products.json"

def save_json(products):
    try:
        with open(USER_FILE, "w") as file:
            json.dump(products, file, indent=4)
    except (OSError, IOError) as e:
        print(f"Error saving products: {e}")

def load_json():
    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No saved products found, starting fresh.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
        return []

def show_products(products):
    try:
        return SP(products)
    except Exception as e:
        print(f"Error showing products: {e}")

def get_products():
    url = "https://dummyjson.com/products"
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        print(f"STATUS CODE: {response.status_code}")

        data = response.json()
        for product in data.get('products', []):
            print(f"Title: {product.get('title')}\n Price: {product.get('price')}")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except (KeyError, ValueError) as e:
        print(f"Error parsing response: {e}")

def post_product(products):
    try:
        number = int(input("How many products do you wish to add: "))
    except ValueError:
        print("Invalid number entered.")
        return

    for i in range(number):
        try:
            print(f"Product {i + 1}")
            product_name = input("Name of product: ").strip().title()
            price = float(input("Price: $"))
            category = input("Category: ").strip().title()

            new_product = CP(product_name, price, category)
            products.append(new_product)

            url = "https://dummyjson.com/products/add"
            response = requests.post(url, timeout=15, json=new_product)
            response.raise_for_status()
            print(f"STATUS: {response.status_code}")
            data = response.json()

            new_product['api_info'] = data
        except ValueError:
            print("Invalid price entered.")
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    save_json(products)

def put_product(products):
    product_name = input("Name of the desired product: ").strip().title()
    product = FP(product_name, products)
    if not product:
        print("NOT FOUND TRY AGAIN")
        return

    try:
        new_product_name = input("New product name: ").strip().title()
        new_price = float(input("Price of new product: $"))
        new_category = input("Category of new product: ").strip().title()
        replacement = CP(new_product_name, new_price, new_category)

        url = "https://dummyjson.com/products/1"
        response = requests.put(url, timeout=15, json=replacement)
        response.raise_for_status()
        print(f"STATUS: {response.status_code}")

        data = response.json()
        product.update(replacement)
        product["api_update"] = data
        save_json(products)
    except ValueError:
        print("Invalid price entered.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def patch_product(products):
    print("Enter the product you want to update:")
    name = str(input("Name of the desired product: ")).strip().title()
    find = FP(name, products)
    if not find:
        print("NO PRODUCT HAS THIS NAME")
        return
    while True:
        print("1.Change Price\n2.Change Category\n3.Exit")
        choice = str(input("Choice: ")).strip()

        if choice == "1":
            while True:
                try:
                    new_price = float(input("New price: $"))
                    break
                except ValueError as a:
                    print(a)
            update = {"price": new_price}
        elif choice == "2":
            new_category = str(input("New category: ")).strip().title()
            update = {"category": new_category}
        elif choice == "3":
            break
        else:
            print("INVALID INPUT ENTER SMTH BTW 1 - 3")

        url = "https://dummyjson.com/products/1"
        response = requests.patch(url, timeout=15, json=update)
        response.raise_for_status()
        print(f"STATUS: {response.status_code}")
        data = response.json()
        find.update(update)
        find["api_update"] = data

        save_json(products)

def delete_product(products):
    try:
        name = input("What do you want to delete: ").strip().title()
        product = FP(name, products)

        if not product:
            print("Product not found.")
            return

        # Call API (currently hardcoded to product 1 — ideally use product['id'])
        url = "https://dummyjson.com/products/1"
        response = requests.delete(url, timeout=10)
        response.raise_for_status()
        print(f"STATUS: {response.status_code}")

        data = response.json()

        # Remove only the found product from the list
        products.remove(product)
        print("Deleted locally:", product)

        # Optionally attach API response info
        product["api_delete"] = data  

        # Save updated list
        save_json(products)

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    products = [
    {"name": "Laptop", "price": 800, "category": "Electronics"},
    {"name": "Mouse", "price": 25, "category": "Electronics"},
    {"name": "Backpack", "price": 50, "category": "Accessories"}
    ]

    save_json(products)
    products = load_json()

    while True:
        print(
            "\n===== PRODUCT MANAGER =====\n"
            "1. Show products\n"
            "2. Get products from API\n"
            "3. Add product\n"
            "4. Replace product\n"
            "5. Update product\n"
            "6. Delete product\n"
            "7. Exit\n"
                    )

        choice = str(input("Choice: "))

        if choice == "1":
            show_products(products)
        elif choice == "2":
            get_products()
        elif choice == "3":
            post_product(products)
        elif choice == "4":
            put_product(products)
        elif choice == "5":
            patch_product(products)
        elif choice == "6":
            delete_product(products)
        elif choice == "7":
            break
        else:
            print("INVALID INPUT")


if __name__ == "__main__":
    main()