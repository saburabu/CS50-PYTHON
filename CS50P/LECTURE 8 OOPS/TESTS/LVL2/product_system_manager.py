class DiscountError(Exception):
    pass

products = []

class Product:
    maximum_discount_percentage = 0.5

    def __init__(self, product_name, base_price, discount_percentage):
        discount_percentage = discount_percentage/100
        # 1. Fix the type checking logic
        if not isinstance(product_name, str):
            raise TypeError("Product name must be a string")
            
        if not isinstance(base_price, (int, float)) or not isinstance(discount_percentage, (int, float)):
            raise TypeError("Price and discount must be numbers")

        # 2. Validate price
        if base_price >= 500:
            self.__price = base_price
        else:
            raise ValueError(f"Price can't be {base_price}. It must be 500 naira or greater")

        # 3. Validate discount
        if discount_percentage > self.maximum_discount_percentage:
            raise DiscountError(f"Greater than maximum discount percentage which is {self.maximum_discount_percentage * 100}")
        elif discount_percentage < 0:
            raise DiscountError("Discount must be 0 or greater")
        else:
            self.__discount = discount_percentage

        # 4. Assign remaining attributes
        self.name = product_name
        self.maximum_discount = self.maximum_discount_percentage

        product = {
            "product_name": self.name,
            "product_price": self.__price,
            "product_discount": self.__discount
        }

        products.append(product)

    @ property
    def price(self):
        return (self.__price, self.__discount)

    @price.setter
    def price(self, value):
        """Fulfills the setter structure but explicitly rejects ALL direct assignments."""
        raise AttributeError("You cant assign a value!!!!")

    def total(self):
    # Calculate the actual total price (Price - Discount amount)
        discount_amount = self.__discount * self.__price
        total_price = self.__price - discount_amount

        return (
            f"{'-' * 15}\n"
            f"Product name: {self.name}\n"
            f"Price: {self.__price}\n"
            f"Discount: {self.__discount * 100}%\n"
            f"{'-' * 15}\n"
            f"Total price: #{total_price}\n"
            f"{'-' * 15}"
        )

product1 = Product("keyboard", 1660, 50)
print(product1.total())
print(products)

# 1. Test the Getter (This will print your tuple cleanly)
print("\n--- Testing Getter ---")
print("Retrieved via getter:", product1.price)  # Output: (1660, 0.5)

# 2. Test the Setter (This will successfully trigger your custom error)
print("\n--- Testing Setter ---")
try:
    product1.price = 1000  # This targets the actual property setter!
except AttributeError as e:
    print(f"SUCCESS! Setter blocked change with message: {e}")

"""Testing changing maximum_discount"""

Product.maximum_discount_percentage = 0.3

product1 = Product("keyboard", 1660, 50)
print(product1.total())