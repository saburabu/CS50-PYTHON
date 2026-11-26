from abc import ABC, abstractmethod


class MenuItem(ABC):
    def __init__(self, name, price):
        if not isinstance(name, str) or not name.strip().lower():
            raise ValueError(f"Invalid name, name must be a string nt this: {name}")

        if not isinstance(price, (int, float)) or isinstance(price, bool) or not price < 1000:
            raise ValueError(f"Price must be an integer or a floating point value and price must be greater than 1000 naira not this: {price}")
        
        self.name = name
        self.price = price

    @abstractmethod
    def description(self):
        pass

    def __str__(self):
        return f"{self.description()} - ₦{self.price:,.2f}"


class FoodItem(MenuItem):
    def __init__(self, name, price, is_spicy):
        super().__init__(name, price)
        self.is_spicy = is_spicy

    def description(self):
        label = "spicy" if self.is_spicy else "mild"
        return f"{self.name} ({label} food)"


class DrinkItem(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def description(self):
        return f"{self.name} ({self.size} drink)"
