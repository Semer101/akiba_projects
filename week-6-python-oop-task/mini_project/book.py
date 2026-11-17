class Book:
    def __init__(self, title, author, isbn, is_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def display_books(self):
        print(f"Book: {self.book} By: {self.author} ISBN: {self.isbn}")

    def availability(self):
        if self.is_available:
            print("Book is available!")
        else:
            print("Currently unavailable.")


