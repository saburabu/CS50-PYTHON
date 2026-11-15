class DiscountCalculator:
    def __init__(self, discount_percentage):
        if 0 <= discount_percentage <= 100  and isinstance(discount_percentage, (int, float)):
            discount = discount_percentage/100
            self.discount = discount
        else:
            raise ValueError("Discount must be an integer or a float and must be btw 0 and 100")

    def __call__(self, price):
        if price > 0 and isinstance(price, (int, float)):
            self.price = price
            self.discount_amount = self.price * self.discount
            return self.price - self.discount_amount

        return f"Price cant be this{self.price} it ust be a float or an int and must be greater than 0"


discount = DiscountCalculator(20.0)

print(discount(10000))