class Game:
    def __init__(self, game_id, title, price, category="Uncategorised"):
        self.id = game_id
        self.title = title
        self.price = price
        self.category = category
        self.reviews = []

    def add_review(self, username, rating, comment):
        self.reviews.append({
            "username": username,
            "rating": rating,
            "comment": comment
        })

    def __str__(self):
        return f"[{self.id}] {self.title} — NGN {self.price:,.2f} ({self.category})"
