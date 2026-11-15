import re

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}')"


class Library:
    def __init__(self):
        self._books = []

    def add_books(self, title, author, isbn):
        if all([title, author, isbn]) and all(isinstance(x, str) for x in [title, author, isbn]) and re.fullmatch(r"\d{12}", isbn):
            for index, value in enumerate(self._books):
                if value.isbn == isbn:
                    raise ValueError(f"Hafa you dey bust cana guy isbn already dey see the book {value.title} by {value.author}")
            book = Book(title, author, isbn)
            self._books.append(book)
            return f"{book} has been added to {self._books}"

        raise ValueError("Hafa guy you no dey try oo skiiii")

    def remove_books(self, isbn):
        if not isbn or not isinstance(isbn, str) or not re.fullmatch(r"\d{12}", isbn):
            raise ValueError("Hafa guy you no dey try oo skiiii")

        for index, value in enumerate(self._books):
            if value.isbn == isbn:
                del self._books[index]
                return f"{isbn} has been removed"
        raise ValueError("Hafa this you isbn no dey oo guy")

    def find_books(self, isbn):
        if not isbn or not isinstance(isbn, str) or not re.fullmatch(r"\d{12}", isbn):
            raise ValueError("Hafa guy you no dey try oo skiiii")
        
        for index, value in enumerate(self._books):
            if value.isbn == isbn:
                return f"Here is the book skiii\nName: {value.title}, Author: {value.author}"

        raise ValueError("Omo g you dey bust cana guy book no dey")

    def __repr__(self):
        return f"Here are all our books skii:\n{self._books}"

    def __len__(self):
        return len(self._books)

    def __contains__(self, isbn):
        # i dont have strength for validation guy too much stress
        return any(book.isbn == isbn for book in self._books)

lib = Library()

# 1. Valid calls: print() displays the returned strings
print(lib.add_books("Things Fall Apart", "Chinua Achebe", "123456789012"))
print(lib.add_books("All That Gliters", "Chinua Achebe", "123456789013"))
print(lib.remove_books("123456789012"))
print(lib.add_books("All That Gliters", "Chinua Achebe", "123456789012"))
print(lib.find_books("123456789012"))
print(lib)
print(len(lib._books))


# 2. Invalid calls: try/except catches the ValueError so you can print it cleanly
try:
    print(lib.remove_books(True))
except ValueError as e:
    print(f"Error: {e}")
