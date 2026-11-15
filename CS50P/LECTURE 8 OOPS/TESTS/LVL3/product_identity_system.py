class Product:
    def __init__(self, product_id: str, name: str, price: float):
        self._product_id = product_id  # Primary identifier (treated as immutable)
        self.name = name
        self.price = price

    @property
    def product_id(self) -> str:
        return self._product_id

    def __eq__(self, other):
        """Requirements 2: Two products are equal if they share the same product_id."""
        if not isinstance(other, Product):
            return NotImplemented
        return self.product_id == other.product_id

    def __hash__(self):
        """Requirements 4 & 6: Equal objects have equal hashes. 

        Uses only the immutable product_id.
        """
        return hash(self.product_id)

    def __repr__(self):
        return f"Product(id={self.product_id}, name='{self.name}', price={self.price})"


# --- Demonstration with 3 Product Objects ---

# 1. Create three product objects where two have the identical product ID but different details
p1 = Product(product_id="PROD-100", name="Wireless Mouse", price=29.99)
p2 = Product(product_id="PROD-100", name="Gaming Mouse (Updated)", price=45.50)  # Same ID as p1
p3 = Product(product_id="PROD-200", name="Mechanical Keyboard", price=89.99)

print("--- Product Details ---")
print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p3: {p3}\n")

# 2. Demonstrate Equality & Hash Requirements
print("--- Equality and Hashing Proof ---")
print(f"Is p1 equal to p2? {p1 == p2}")  # True
print(f"Is p1 equal to p3? {p1 == p3}")  # False
print(f"Do p1 and p2 have matching hashes? {hash(p1) == hash(p2)}\n")  # True

# 3. Demonstration of Set Behavior (Requirement 3 & 5)
# Because p1 == p2, a set will consider them duplicates and only keep the first one inserted.
product_set = {p1, p2, p3}
print("--- Set Membership Behavior ---")
print(f"Set size (expected 2): {len(product_set)}")
print(f"Set elements: {product_set}\n")

# 4. Demonstration of Dictionary Key Behavior (Requirement 3 & 5)
# Because p1 == p2 and share the same hash, p2 will overwrite p1's value in a dictionary.
product_catalog = {}
product_catalog[p1] = "Aisle 4 - Electronics"
product_catalog[p2] = "Promo Display - Front Desk"  # Overwrites p1 entry

print("--- Dictionary Key Behavior ---")
print(f"Dictionary size (expected 2): {len(product_catalog)}")
print(f"Location of p1: {product_catalog[p1]}")  # Returns the updated value from p2

