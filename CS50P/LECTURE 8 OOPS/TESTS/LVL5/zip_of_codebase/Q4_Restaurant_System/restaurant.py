class Table:
    def __init__(self, number, seats):
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
        # BUG: closed orders can still be changed.
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
        # BUG: this permits multiple open orders for the same table.
        order = Order(table)
        table.current_order = order
        self.orders.append(order)
        return order

    def close_order(self, order):
        # BUG: table.current_order is not cleared after closing.
        order.close()
        return order.total()

    def table_summary(self, table):
        if table.current_order is None:
            return f"{table}: no current order"
        return f"{table}: {len(table.current_order)} item(s), {table.current_order.status}"
