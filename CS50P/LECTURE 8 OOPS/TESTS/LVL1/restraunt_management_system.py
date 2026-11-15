class RestrauntTable:
    def __init__(self, table_number, seat_capacity, current_occupancy=0):
        self.table_number = table_number
        self.seat_capacity = seat_capacity
        self.current_occupancy = current_occupancy
        self.available_seats = self.seat_capacity - self.current_occupancy

    def seat_costumers(self, number):
        if number <= 0:
            return f"Number of custommers must be greater than 0"
        elif number > self.available_seats:
            return f"Customers are greater than the available seats in table {self.table_number}"

        self.current_occupancy += number
        self.available_seats -= number
        return f"Current occupancy in Table{self.table_number} is {self.current_occupancy} available seats {self.available_seats}"

    def remove_customers(self, number):
        if number > self.current_occupancy or number > self.seat_capacity:
            return f"INVALID YOU CANT REMOVE THAT NUMBER OF CUSTOMERS"
        elif number <= 0:
            return f"INVALID NUMBER OF CUSTOMERS"

        self.available_seats += number
        self.current_occupancy -= number

        return f"Current occupancy in Table{self.table_number} is {self.current_occupancy} available seats {self.available_seats}"

    def display_info(self):
        return f"Table Number: {self.table_number}\nSeat Capacity: {self.seat_capacity}\nCurrent Occupancy: {self.current_occupancy}\nAvailable Seats: {self.available_seats}"

table1 = RestrauntTable(1, 4, 0)
table2 = RestrauntTable(2, 6, 5)
table3 = RestrauntTable(3, 2, 1)
table4 = RestrauntTable(4, 8, 4)
table5 = RestrauntTable(5, 10, 8)

## Example Usage:
# Seat customers at table 1
print(table1.seat_costumers(3))  # Should seat 3 customers
# edge cases
print(table1.seat_costumers(5))  # Should return an error (not enough seats)
print(table2.seat_costumers(-1))  # Should return an error (not enough seats)
print(table3.seat_costumers(0))  # Should return an error (not enough seats)
print(table4.seat_costumers(5))  # Should seat 5 customers
# Remove customers from table 2
print(table2.remove_customers(3))  # Should remove 3 customers
print(table2.remove_customers(10))  # Should return an error (not enough customers)
print(table2.remove_customers(-1))  # Should return an error (not enough customers
# display table information
print(table1.display_info())
