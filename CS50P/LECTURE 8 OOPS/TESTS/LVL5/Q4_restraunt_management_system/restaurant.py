class Table:
    def __init__(self, number: int, seats: int):
        if not isinstance(number, int) or isinstance(number, bool) or number <= 0:
            raise ValueError("Table number must be a positive integer.")
        if not isinstance(seats, int) or isinstance(seats, bool) or seats <= 0:
            raise ValueError("Seats must be a positive integer.")

        self.number = number
        self.seats = seats
        self.current_order = None

    def __str__(self):
        return f"Table {self.number} ({self.seats} seats)"


class Order:
    def __init__(self, table):
        self.table = table
        self.items = []
        self.status = "open"

    def add_item(self, item):
        if self.status == "closed":
            raise ValueError("Cannot add items to a closed order.")
        self.items.append(item)

    def total(self):
        return sum(item.price for item in self.items)

    def close(self):
        self.status = "closed"

    def __len__(self):
        return len(self.items)


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.tables = []
        self.orders = []

    def add_table(self, table):
        self.tables.append(table)

    def open_order(self, table):
        if table not in self.tables:
            raise ValueError(f"{table} is not registered in {self.name}.")
        if table.current_order is not None:
            raise ValueError(f"{table} already has an open order.")
        order = Order(table)
        table.current_order = order
        self.orders.append(order)
        return order

    def close_order(self, order):
        if order.status == "closed":
            raise ValueError("Order is already closed.")
        order.close()
        order.table.current_order = None
        return order.total()

    def table_summary(self, table):
        if table.current_order is None:
            return f"{table}: no current order"
        return f"{table}: {len(table.current_order)} item(s), {table.current_order.status}"
