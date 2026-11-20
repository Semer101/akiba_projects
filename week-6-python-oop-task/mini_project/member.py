class Member:
    def __init__(self, name, member_id):
        self.borrowed_books = []
        self.name = name
        self.member_id = member_id

    def get_borrowing_limit(self):
        return 3

    def borrow_book(self, book):
        if not book.is_available:
            print("Sorry, this book is unavailable.")
            return

        if len(self.borrowed_books) >= self.get_borrowing_limit():
            print("You have reached your borrowing limit.")
            return

        self.borrowed_books.append(book)
        book.update_availability(False)
        print(f"{book.title} borrowed successfully!")

    def return_book(self, isbn):
        for book in self.borrowed_books:
            if book.isbn == isbn:
                self.borrowed_books.remove(book)
                book.update_availability(True)
                print(f"{book.title} returned successfully!")
                return

        print("You haven't borrowed this book.")

class StudentMember(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)

    def get_borrowing_limit(self):
        return 5


class TeacherMember(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)

    def get_borrowing_limit(self):
        return 15

