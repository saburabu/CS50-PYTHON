import random as r

class Phone:
    def __init__(self, brand, model, storage_capacity, price, battery_percentage):
        self.brand = brand
        self.model = model
        self.storage_capacity = storage_capacity
        self.price = price
        self.battery_percentage = battery_percentage

    def display_specifications(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage Capacity: {self.storage_capacity} GB")

    def reduce_battery(self):
        reduce_by = r.randint(1, 100-self.battery_percentage)
        while True:
            if self.battery_percentage - reduce_by < 0:
                reduce_by = r.randint(1, 100-self.battery_percentage)
            else:
                break
        self.battery_percentage -= reduce_by
        print("Battery: " + str(self.battery_percentage) + "%")

    def recharge_battery(self):
        increase_by = r.randint(1, 100-self.battery_percentage)
        while True:
            if self.battery_percentage + increase_by > 100:
                increase_by = r.randint(1, 100-self.battery_percentage)
            else:
                break
        self.battery_percentage += increase_by
        print("Battery: " + str(self.battery_percentage) + "%")


phone1 = Phone("Apple", "iPhone 13", 128, 999, 50)
phone2 = Phone("Samsung", "Galaxy S21", 256, 799, 75)
phone3 = Phone("Google", "Pixel 6", 128, 599, 30)
phone4 = Phone("OnePlus", "9 Pro", 256, 969, 90)
phone5 = Phone("Xiaomi", "Mi 11", 128, 699, 60)

# example 1:
phone1.display_specifications()
# example 2:
phone2.reduce_battery()
# example 3:
phone3.recharge_battery()