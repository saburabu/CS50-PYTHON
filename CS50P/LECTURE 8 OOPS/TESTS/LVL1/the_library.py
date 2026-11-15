class Book:
    def __init__(self, title, author, available_copies):
        self.title = title
        self.author = author
        self.available_copies = available_copies
        self.original_stock = available_copies

    def borrow_book(self, quantity):
        try:
            if quantity > self.available_copies:
                print(f"Quantity exceeds available quantity")
            elif self.available_copies == 0:
                print(f"No available copies!!")
            elif quantity <= 0:
                print(f"MUST BE GERATER THAN 0")
            else:
                print(f"INITIAL QUANTITY IN STOCK: {self.available_copies}")
                self.available_copies -= quantity
                print(f"CURRENT QUANTITY IN STOCK: {self.available_copies}")
                return self.available_copies
        except Exception as e:
            print(e)

    def return_book(self, quantity):
        try:
            if self.available_copies + quantity > self.original_stock:
                print(f"exceeeds original quantity")
            elif quantity <= 0:
                print(f"MUST BE GREATER THAN 0")
            else:
                print(f"INITIAL QUANTITY IN STOCK: {self.available_copies}")
                self.available_copies += quantity
                print(f"CURRENT QUANTITY IN STOCK: {self.available_copies}")
                return self.available_copies
        except Exception as e:
            print(e)

    def display_availability(self):
        return f"AVAILABLE COPIES: {self.available_copies}"

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 5)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 3)
book3 = Book("1984", "George Orwell", 8)
book4 = Book("Pride and Prejudice", "Jane Austen", 2)

# borrow_books
book1.borrow_book(10)
book2.borrow_book(-10)
book3.borrow_book(7)
book4.borrow_book(1)
book1.borrow_book(5)
# return_books
book1.return_book(-10)
book2.return_book(5)
book3.return_book(3)
book3.return_book(0)
# display_availability
print(book1.display_availability())
print(book2.display_availability())
print(book3.display_availability())
print(book4.display_availability())