from datetime import datetime


class Purchase:
    def __init__(self, user, game):
        self.username = user.username
        self.game = game
        self.amount = game.price
        self.created_at = datetime.now()
        self.refunded = False

    def __str__(self):
        return (
            f"{self.game.title} | NGN {self.amount:,.2f} | "
            f"{self.created_at:%Y-%m-%d %H:%M}"
        )
