from dataclasses import dataclass


@dataclass
class Product:
    product_id: int
    name: str
    price: int

    def __post_init__(self) -> None:
        if (
            isinstance(self.product_id, bool)
            or not isinstance(self.product_id, int)
            or self.product_id <= 0
        ):
            raise ValueError("product_id must be a positive integer")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("name must be a non-empty string")
        if (
            isinstance(self.price, bool)
            or not isinstance(self.price, int)
            or self.price < 0
        ):
            raise ValueError("price must be a non-negative integer")


class ProductCollection:

    def __init__(self) -> None:
        self._products: dict[int, Product] = {}

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Expected a Product instance")
        self._products[product.product_id] = product

    def __len__(self) -> int:
        return len(self._products)

    def __contains__(self, product_id: object) -> bool:
        return product_id in self._products


products = ProductCollection()
products.add_product(Product(1, "Laptop", 1500000))
products.add_product(Product(2, "Mouse", 15000))

print(len(products))  # 2
print(1 in products)  # True
print(5 in products)  # False
