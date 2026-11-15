from dataclasses import dataclass


@dataclass
class Product:
    product_id: int
    name: str
    price: int | float

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
            or not isinstance(self.price, (int, float))
            or self.price < 0
        ):
            raise ValueError("price must be a non-negative number")


class ProductCatalogue:
    def __init__(self) -> None:
        self._products: dict[int, Product] = {}

    def __setitem__(self, product_id: int, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Value must be a Product instance")
        if product_id != product.product_id:
            raise ValueError(
                f"Key {product_id} does not match product.product_id ({product.product_id})"
            )
        self._products[product_id] = product

    def __getitem__(self, product_id: int) -> Product:
        if product_id not in self._products:
            raise KeyError(f"Product with ID {product_id} not found in catalogue")
        return self._products[product_id]

    def __contains__(self, product_id: object) -> bool:
        return product_id in self._products


catalogue = ProductCatalogue()
catalogue[101] = Product(101, "Keyboard", 45000)

print(catalogue[101])      # Product(product_id=101, name='Keyboard', price=45000)
print(101 in catalogue)    # True
print(999 in catalogue)    # False
