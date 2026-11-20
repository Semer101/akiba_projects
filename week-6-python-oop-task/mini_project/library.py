from book import Book

class Library:
    def __init__(self):
        self.book_collection = []

    def add_book(self, book):
        for existing_book in self.book_collection:
            if existing_book.isbn == book.isbn:
                print("A book with this ISBN already exists.")
                return

        self.book_collection.append(book)
        print("Book added successfully!")

    def remove_book(self, isbn):
        for book in self.book_collection:
            if book.isbn == isbn:
                self.book_collection.remove(book)
                print("Book removed successfully!")
                return

        print("Book not found.")

    def display_books(self):
        if not self.book_collection:
            print("There are no books in the library.")
            return

        for book in self.book_collection:
            book.display_book()
            book.availability()

    def search_book(self, title):
        for book in self.book_collection:
            if book.title.lower() == title.lower():
                book.display_book()
                book.availability()
                return book

        print("Book not found.")
        return None

