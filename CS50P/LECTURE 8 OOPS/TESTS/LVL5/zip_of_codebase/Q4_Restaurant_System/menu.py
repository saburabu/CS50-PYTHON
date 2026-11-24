from abc import ABC, abstractmethod


class MenuItem(ABC):
    def __init__(self, name, price):
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
