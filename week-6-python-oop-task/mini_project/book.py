class Book:
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def display_book(self):
        print(f"Book: {self.title} Author: {self.author} ISBN: {self.isbn}")

    def update_availability(self, available):
        self.is_available = available

    def availability(self):
        if self.is_available:
            print("Book is available!")
        else:
            print("Currently unavailable.")

