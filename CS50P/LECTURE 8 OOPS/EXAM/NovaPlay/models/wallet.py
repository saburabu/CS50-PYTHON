class Wallet:
    currency = "NGN"

    def __init__(self, balance=0):
        self.balance = balance

    def add_funds(self, amount):
        self.balance += amount
        return True

    def spend(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def __str__(self):
        return f"{self.currency} {self.balance:,.2f}"
