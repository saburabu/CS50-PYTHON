from models.game import Game
from models.purchase import Purchase


class Store:
    def __init__(self, storage):
        self.storage = storage
        self.games = []
        self.users = []

    def add_game(self, game_id, title, price, category="Uncategorised"):
        game = Game(game_id, title, price, category)
        self.games.append(game)
        return game

    def find_game(self, game_id):
        for game in self.games:
            if game.id == game_id:
                return game
        return None

    def save_user(self, user):
        self.users.append(user)
        self.storage.save_user(user)

    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def purchase(self, user, game):
        if user.library.has_game(game):
            return False

        if user.wallet.spend(game.price):
            user.library.add_game(game)
            purchase = Purchase(user, game)
            user.add_purchase(purchase)
            self.storage.save_user(user)
            return True

        return False
