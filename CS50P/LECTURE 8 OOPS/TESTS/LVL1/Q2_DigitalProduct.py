class Product:
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def show_product(self):
        return f"Product Name: {self.name}\nPrice: ${self.price:.2f}\nAvailable in stock: {self.stock}\nCategory: {self.category}"

    def change_price(self):
        print(f"Current price of {self.name}: ${self.price:.2f}")
        new_price = float(input(f"Enter the new price for {self.name}: "))
        self.price = new_price
        print(f"The price of {self.name} has been updated to ${self.price:.2f}.")

    def update_stock(self):
        print(f"Current stock of {self.name}: {self.stock} units.")
        new_stock = int(input(f"Enter the new stock quantity for {self.name}: "))
        if new_stock > self.stock:
            self.stock = new_stock
            print(f"The stock of {self.name} has been updated to {self.stock} units.")  
        else:
            # AS YOU SPECIFIED I CAN "Increase its available quantity"
            print("New stock quantity must be greater than the current stock.")
        
product1 = Product(name="Wireless Mouse", price=25.99, stock=150, category="Electronics")
product2 = Product(name="Bluetooth Headphones", price=59.99, stock=80, category="Electronics")
product3 = Product(name="Coffee Maker", price=89.99, stock=40, category="Home Appliances")
product4 = Product(name="Yoga Mat", price=19.99, stock=200, category="Fitness")
product5 = Product(name="Smartphone", price=699.99, stock=30, category="Electronics")

def main(product1, product2, product3, product4, product5):
    print("Welcome to the Digital Product Management System!")
    print("Here are the available products:\n")
    
    products = [product1, product2, product3, product4, product5]
    try:    
        while True:
            choice = input("Would you like to change the price or update the stock of a product? (yes/no) or would you like to check all products type ok: ").strip().lower()
            if choice == 'no':
                print("Thank you for using the Digital Product Management System. Goodbye!")
                break
            elif choice == 'yes':
                product_number = int(input(f"Enter the product number (1-{len(products)}) you want to modify: "))
                if 1 <= product_number <= len(products):
                    selected_product = products[product_number - 1]
                    action = input(f"Do you want to change the price or update the stock of {selected_product.name}? (price/stock): ").strip().lower()
                    if action == 'price':
                        selected_product.change_price()
                    elif action == 'stock':
                        selected_product.update_stock()
                    else:
                        print("Invalid action. Please choose 'price' or 'stock'.")
                else:
                    print(f"Invalid product number. Please choose a number between 1 and {len(products)}.")
            elif choice == 'ok':
                for product in products:
                    print(product.show_product())
                    print("-" * 40)
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

main(product1, product2, product3, product4, product5)