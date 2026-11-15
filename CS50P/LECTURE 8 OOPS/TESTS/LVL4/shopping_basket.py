class BasketItem:
    def __init__(self, product_name: str, unit_price: int | float, quantity: int) -> None:
        if not isinstance(product_name, str) or not product_name.strip():
            raise ValueError("Product name must be a non-empty string")
        if (
            isinstance(unit_price, bool)
            or not isinstance(unit_price, (int, float))
            or unit_price <= 0
        ):
            raise ValueError("Unit price must be a positive int or float")
        if (
            isinstance(quantity, bool)
            or not isinstance(quantity, int)
            or quantity <= 0
        ):
            raise ValueError("Quantity must be a positive integer")

        self.name = product_name
        self._unit_price = unit_price
        self._quantity = quantity

    def subtotal(self) -> int | float:
        return self._unit_price * self._quantity


class ShoppingBasket:
    def __init__(self) -> None:
        self.products: dict[str, int | float] = {}

    def add_products(self, product_name: str, unit_price: int | float, quantity: int) -> None:
        item = BasketItem(product_name=product_name, unit_price=unit_price, quantity=quantity)
        self.products[product_name] = item.subtotal()

    def remove_products(self, product_name: str) -> None:
        if product_name not in self.products:
            raise ValueError("Product not in shopping basket")
        del self.products[product_name]

    def grand_total(self) -> int | float:
        return sum(self.products.values())

    def __len__(self) -> int:
        return len(self.products)


# Example usage
basket = ShoppingBasket()
basket.add_products("Keyboard", 17000, 3)
basket.add_products("Mouse", 5000, 1)
basket.add_products("Laptop", 3000000, 2)

print(len(basket))          # 3
print(basket.grand_total()) # 6056000
basket.remove_products("Mouse")
print(len(basket))          # 2
print(basket.grand_total()) # without mouse