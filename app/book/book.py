class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        self.is_checked_out = True
        print(f"{self.title} by {self.author} has been checked out.")

    def check_in(self):
        self.is_checked_out = False
        print(f"{self.title} by {self.author} has been checked in.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} by {book.author} has been added to the library.")

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_checked_out:
                book.check_out()
                return
        print(f"Sorry, {title} is not available.")
        # ADDED CODE HERE TO PASS THE TEST
        return False

    def check_in_book(self, title):
        for book in self.books:
            if book.title == title and book.is_checked_out:
                book.check_in()
                return
        print(f"Sorry, {title} is not in the library.")
        # ADDED CODE HERE TO PASS THE TEST
        return False


class Client:
    def __init__(self, name):
        self.name = name
        self.checked_out_books = []

    def check_out_book(self, library, title):
        for book in library.books:
            if book.title == title and not book.is_checked_out:
                book.check_out()
                self.checked_out_books.append(book)
                return
        print(f"Sorry, {title} is not available.")
        # raise ValueError(f"Sorry, {title} is not available.")

    def check_in_book(self, library, title):
        for book in self.checked_out_books:
            if book.title == title:
                book.check_in()
                self.checked_out_books.remove(book)
            return
        print(f"Sorry, {title} is not checked out.")
        # raise ValueError(f"Sorry, {title} is not checked out.")


library = Library()
book1 = Book("To Kill a Mockingbird", "Harper Lee")
library.add_book(book1)
book2 = Book("Pride and Prejudice", "Jane Austen")
library.add_book(book2)
client1 = Client("John Doe")
client1.check_out_book(library, "To Kill a Mockingbird")
client1.check_out_book(library, "Pride and Prejudice")
client2 = Client("Jane Doe")
client2.check_out_book(library, "To Kill a Mockingbird")
client1.check_in_book(library, "To Kill a Mockingbird")
