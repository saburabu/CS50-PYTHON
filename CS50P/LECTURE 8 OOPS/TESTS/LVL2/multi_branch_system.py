import copy

class Company:
    """Manages shared company-wide settings."""
    def __init__(self, name: str, default_currency: str, max_discount: float):
        self.name = name
        self._default_currency = default_currency
        self._max_discount = max_discount

    @property
    def default_currency(self) -> str:
        return self._default_currency

    @default_currency.setter
    def default_currency(self, currency: str):
        if not currency or not isinstance(currency, str):
            raise ValueError("Invalid currency format.")
        self._default_currency = currency

    @property
    def max_discount(self) -> float:
        return self._max_discount

    @max_discount.setter
    def max_discount(self, value: float):
        if not (0 <= value <= 100):
            raise ValueError("Discount must be between 0% and 100%.")
        self._max_discount = value


class Branch:
    """Manages an individual branch's inventory, manager, and setting overrides."""
    def __init__(self, name: str, manager: str, company: Company):
        self.name = name
        self.manager = manager
        self.company = company
        self._products = {}  # Format: {product_name: quantity}
        self._overrides = {}  # Stores local overrides (e.g., 'currency', 'max_discount')

    # --- Inventory Management ---
    def add_product(self, product_name: str, quantity: int):
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")
        self._products[product_name] = self._products.get(product_name, 0) + quantity

    def update_quantity(self, product_name: str, quantity: int):
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")
        if product_name not in self._products:
            raise KeyError(f"Product '{product_name}' does not exist in this branch.")
        self._products[product_name] = quantity

    def backup_inventory(self) -> dict:
        """Returns an independent, deep copy of the current inventory."""
        return copy.deepcopy(self._products)

    # --- Settings & Overrides (Fallbacks to Company defaults) ---
    @property
    def currency(self) -> str:
        return self._overrides.get('currency', self.company.default_currency)

    @currency.setter
    def currency(self, value: str):
        self._overrides['currency'] = value

    def reset_currency_to_default(self):
        self._overrides.pop('currency', None)

    @property
    def max_discount(self) -> float:
        return self._overrides.get('max_discount', self.company.max_discount)

    @max_discount.setter
    def max_discount(self, value: float):
        if not (0 <= value <= 100):
            raise ValueError("Discount must be between 0% and 100%.")
        self._overrides['max_discount'] = value

    # --- Display System ---
    def display_info(self):
        print(f"\n=== Branch: {self.name} ===")
        print(f"Manager: {self.manager}")
        print(f"Currency: {self.currency} " + ("(Overridden)" if 'currency' in self._overrides else "(Company Default)"))
        print(f"Max Discount: {self.max_discount}% " + ("(Overridden)" if 'max_discount' in self._overrides else "(Company Default)"))
        print("Inventory:")
        if not self._products:
            print("  [No products in stock]")
        for prod, qty in self._products.items():
            print(f"  - {prod}: {qty} units")
        print("=" * (12 + len(self.name)))


# =====================================================================
# VERIFICATION & TESTING SCENARIOS
# =====================================================================
if __name__ == "__main__":
    print("--- Initializing Company and Branches ---")
    my_company = Company(name="Global Retail Corp", default_currency="USD", max_discount=20.0)
    branch_A = Branch(name="Branch A (New York)", manager="Alice", company=my_company)
    branch_B = Branch(name="Branch B (London)", manager="Bob", company=my_company)

    # Scenario 1: A product is added to Branch A. Does it appear in Branch B?
    print("\nScenario 1 Test: Isolated Inventories")
    branch_A.add_product("Laptop", 10)
    print(f"Branch A has Laptop? {'Laptop' in branch_A._products}")
    print(f"Branch B has Laptop? {'Laptop' in branch_B._products}")

    # Scenario 2: Branch A's inventory is backed up. Does changing the original affect the backup?
    print("\nScenario 2 Test: Independent Backups")
    inventory_backup = branch_A.backup_inventory()
    branch_A.update_quantity("Laptop", 5)  # Changing original
    print(f"Original Branch A Laptop Qty: {branch_A._products['Laptop']}")
    print(f"Backup Inventory Laptop Qty: {inventory_backup['Laptop']}")

    # Scenario 3: The company changes its default currency. What happens to branches using the default?
    print("\nScenario 3 Test: Global Currency Updates")
    print(f"Before global change -> Branch A Currency: {branch_A.currency}, Branch B Currency: {branch_B.currency}")
    my_company.default_currency = "EUR"
    print(f"After global change  -> Branch A Currency: {branch_A.currency}, Branch B Currency: {branch_B.currency}")

    # Scenario 4: One branch overrides its currency. Does that affect other branches?
    print("\nScenario 4 Test: Local Setting Overrides")
    branch_B.currency = "GBP"  # Override London to GBP
    my_company.default_currency = "JPY"  # Global shift to Yen
    print(f"After global change to JPY -> Branch A (Default): {branch_A.currency}")
    print(f"After global change to JPY -> Branch B (Overridden): {branch_B.currency}")

    # Scenario 5: Someone attempts to set a negative product quantity or invalid discount.
    print("\nScenario 5 Test: Validation Safeguards")
    try:
        branch_A.add_product("Phone", -5)
    except ValueError as e:
        print(f"Caught expected error: {e}")

    try:
        branch_A.max_discount = 150  # Over 100%
    except ValueError as e:
        print(f"Caught expected error: {e}")

    # Display Final State
    print("\n--- Final Branch Displays ---")
    branch_A.display_info()
    branch_B.display_info()
