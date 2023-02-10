import unittest
import sys

sys.path.insert(0, "../../../..")
from app.book.book import *


class TestBook(unittest.TestCase):
    def test_check_out(self):
        book = Book("To Kill a Mockingbird", "Harper Lee")
        book.check_out()
        self.assertTrue(book.is_checked_out)

    def test_check_in(self):
        book = Book("To Kill a Mockingbird", "Harper Lee")
        book.check_out()
        book.check_in()
        self.assertFalse(book.is_checked_out)

    def test_check_out_limits(self):
        book = Book("To Kill a Mockingbird", "Harper Lee")
        for i in range(100):
            book.check_out()
        self.assertTrue(book.is_checked_out)

    def test_check_in_limits(self):
        book = Book("To Kill a Mockingbird", "Harper Lee")
        for i in range(100):
            book.check_out()
        for i in range(100):
            book.check_in()
        self.assertFalse(book.is_checked_out)


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("To Kill a Mockingbird", "Harper Lee")
        self.library.add_book(self.book1)
        self.book2 = Book("Pride and Prejudice", "Jane Austen")
        self.library.add_book(self.book2)

    def test_add_book(self):
        self.assertEqual(len(self.library.books), 2)

    def test_check_out_book(self):
        self.library.check_out_book("To Kill a Mockingbird")
        self.assertTrue(self.book1.is_checked_out)
        self.library.check_out_book("To Kill a Mockingbird")
        self.assertEqual(len(self.library.books), 2)

    def test_check_in_book(self):
        self.library.check_out_book("To Kill a Mockingbird")
        self.library.check_in_book("To Kill a Mockingbird")
        self.assertFalse(self.book1.is_checked_out)
        self.library.check_in_book("To Kill a Mockingbird")
        self.assertEqual(len(self.library.books), 2)

    def test_check_out_book_input_error(self):
        self.library = Library()
        self.book1 = Book("To Kill a Mockingbird", "Harper Lee")
        self.library.add_book(self.book1)
        self.book2 = Book("Pride and Prejudice", "Jane Austen")
        self.library.add_book(self.book2)

        if self.library.check_out_book("The Great Gatsby"):
            raise ValueError("The Great Gatsby book should not be out")

    def test_check_in_book_input_error(self):
        self.library = Library()
        self.book1 = Book("To Kill a Mockingbird", "Harper Lee")
        self.library.add_book(self.book1)
        self.book2 = Book("Pride and Prejudice", "Jane Austen")
        self.library.add_book(self.book2)

        if self.library.check_in_book("The Great Gatsby"):
            raise ValueError("The Great Gatsby book should not be in")


class TestClient(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("To Kill a Mockingbird", "Harper Lee")
        self.library.add_book(self.book1)
        self.book2 = Book("Pride and Prejudice", "Jane Austen")
        self.library.add_book(self.book2)
        self.client = Client("John Doe")

    def test_check_out_book(self):
        self.client.check_out_book(self.library, "To Kill a Mockingbird")
        self.assertTrue(self.book1.is_checked_out)
        self.assertEqual(len(self.client.checked_out_books), 1)
        self.client.check_out_book(self.library, "Pride and Prejudice")
        self.assertEqual(len(self.client.checked_out_books), 2)
        self.client.check_out_book(self.library, "To Kill a Mockingbird")
        self.assertEqual(len(self.client.checked_out_books), 2)

    def test_check_in_book(self):
        self.client.check_out_book(self.library, "To Kill a Mockingbird")
        self.client.check_in_book(self.library, "To Kill a Mockingbird")
        self.assertFalse(self.book1.is_checked_out)
        self.assertEqual(len(self.client.checked_out_books), 0)

    def test_check_out_book_case_error(self):
        self.library = Library()
        self.book1 = Book("To Kill a Mockingbird", "Harper Lee")
        self.library.add_book(self.book1)
        self.book2 = Book("Pride and Prejudice", "Jane Austen")
        self.library.add_book(self.book2)
        self.client = Client("John Doe")

        self.client.check_out_book(self.library, "to kill a mockingbird")
        self.assertEqual(len(self.library.books), 2)

    def test_check_in_book_case_error(self):
        self.library = Library()
        self.book1 = Book("To Kill a Mockingbird", "Harper Lee")
        self.library.add_book(self.book1)
        self.book2 = Book("Pride and Prejudice", "Jane Austen")
        self.library.add_book(self.book2)
        self.client = Client("John Doe")

    def test_check_out_limit(self):
        for i in range(10):
            self.client.check_out_book(self.library, "To Kill a Mockingbird")
        self.assertFalse(
            self.client.check_out_book(self.library, "To Kill a Mockingbird")
        )
        self.assertEqual(len(self.client.checked_out_books), 10)

    def test_check_out_error(self):
        self.assertFalse(self.client.check_out_book(self.library, "Non-Existent Book"))

    def test_check_in_error(self):
        self.assertFalse(self.client.check_in_book(self.library, "Non-Existent Book"))
