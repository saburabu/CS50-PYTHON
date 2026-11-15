class Coordinate:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Coordinates must be an integer or float")

        self.x = x
        self.y = y

    # This makes the coordinate print beautifully!
    def __repr__(self):
        return f"Coordinate({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Coordinate):
            return NotImplemented

        return Coordinate(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        if not isinstance(other, Coordinate):
            return NotImplemented

        return Coordinate(
            self.x - other.x,
            self.y - other.y
        )

    def __eq__(self, other):
        if not isinstance(other, Coordinate):
            return NotImplemented

        return self.x == other.x and self.y == other.y


# Testing the updated code:
coordinate1 = Coordinate(2, 5)
coordinate2 = Coordinate(2, 5)

print(coordinate1 + coordinate2)  # Outputs: Coordinate(7, 5)
print(coordinate1 - coordinate2)  # Outputs: Coordinate(-3, 1)
print(coordinate2 == coordinate1)  # Outputs: True
