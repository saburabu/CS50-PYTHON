from models.wallet import Wallet
from models.library import GameLibrary


class User:
    def __init__(self, username, wallet=None):
        self.username = username
        self.wallet = wallet or Wallet()
        self.library = GameLibrary()
        self.purchase_history = []

    def add_purchase(self, purchase):
        self.purchase_history.append(purchase)

    def __str__(self):
        return f"{self.username} | Balance: {self.wallet.balance}"
