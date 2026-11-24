class DeliveryItem:

    def __init__(self, name: str, quantity: int, weight: float):
        if not name or quantity is None or weight is None:
            raise ValueError("You must assign values to all of them bro")

        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not isinstance(quantity, int) or isinstance(quantity, bool):
         raise ValueError("Quantity must be an integer")
        if not isinstance(weight, (int, float)) or isinstance(weight, bool):
         raise ValueError("Weight must be an int or a float")

        if quantity <= 0:
         raise ValueError("Quantity must be at least 1")
        if weight <= 0:
         raise ValueError("Weight must be greater than 0")

        self.name = name
        self.quantity = quantity
        self.weight = weight

    def subtotal(self):
        return self.quantity * self.weight

class DeliveryOrder:

    def __init__(self):
        self.deliveries = {}

    def add_delivery_item(self, name, quantity, weight):
        item = DeliveryItem(name=name, quantity=quantity, weight=weight)
        self.deliveries[name] = item

    def remove_delivery_item(self, name, quantity=None):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a string")

        if name not in self.deliveries:
            raise ValueError("Name does not exist")

        if quantity is None:
            del self.deliveries[name]
            return

        if not isinstance(quantity, int) or isinstance(quantity, bool):
             raise ValueError("Quantity must be an integer")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        item = self.deliveries[name]
        if quantity >= item.quantity:
            del self.deliveries[name]
        else:
            item.quantity -= quantity

    def item_subtotal(self, name):
            if name not in self.deliveries:
                raise ValueError("Name does not exist")
            return self.deliveries[name].subtotal()

    def total_weight(self):
        return sum(item.subtotal() for item in self.deliveries.values())


    def assign_driver(self, driver):
        if not isinstance(driver, Driver):
            raise TypeError("Expected a Driver object")

        self.driver = driver

class Driver:

    def __init__(self, name):
        if not name or not isinstance(name, str):
            raise ValueError("Invalid driver name")

        self.name = name
        self.deliveries = []

    def assign_delivery(self, delivery):
        if delivery in self.deliveries:
            raise ValueError("Delivery already assigned")

        self.deliveries.append(delivery)
        delivery.assign_driver(self)

driver = Driver("James")

delivery1 = DeliveryOrder()
delivery2 = DeliveryOrder()

delivery1.add_delivery_item("Ham", 12, 5)
delivery2.add_delivery_item("Smth", 13, 4)
delivery1.add_delivery_item("Smth", 13, 2)

driver.assign_delivery(delivery1)
driver.assign_delivery(delivery2)        