class GameLibrary:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)
        return True

    def remove_game(self, game):
        if game in self.games:
            self.games.remove(game)
            return True
        return False

    def has_game(self, game):
        return game in self.games

    def __len__(self):
        return len(self.games)
