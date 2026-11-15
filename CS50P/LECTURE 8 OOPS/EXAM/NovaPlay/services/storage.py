import json
from pathlib import Path


class Storage:
    def __init__(self, folder):
        self.folder = Path(folder)
        self.folder.mkdir(exist_ok=True)

    def save_user(self, user):
        path = self.folder / f"{user.username}.json"
        data = {
            "username": user.username,
            "balance": user.wallet.balance,
            "games": [game.id for game in user.library.games],
            "purchase_history": [
                {
                    "game_id": item.game.id,
                    "amount": item.amount,
                    "created_at": item.created_at.isoformat(),
                    "refunded": item.refunded
                }
                for item in user.purchase_history
            ]
        }

        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load_user_data(self, username):
        path = self.folder / f"{username}.json"
        if not path.exists():
            return None

        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
