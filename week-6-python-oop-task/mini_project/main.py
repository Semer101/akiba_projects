from book import Book
from library import Library
from member import Member, StudentMember, TeacherMember


library = Library()
members = {}

while True:
    print("========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book\n2. Display All Books\n3. Search Book\n4. Register Member\n5. Borrow Book\n6. Return Book\n7. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter book title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        book = Book(title, author, isbn)
        library.add_book(book)

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        title = input("Enter book title: ")
        library.search_book(title)

    elif choice == 4:
        name = input("Enter member name: ")
        member_id = input("Enter member ID: ")

        if member_id in members:
            print("This member ID is already registered.")
            continue

        print("1.Student\n2.Teacher")

        member_type = int(input("Select member type: "))

        if member_type == 1:
            member = StudentMember(name, member_id)
        elif member_type == 2:
            member = TeacherMember(name, member_id)
        else:
            print("Invalid member type.")
            continue

        members[member_id] = member
        print("Member registered successfully!")
        
    elif choice == 5:
        member_id = input("Enter member ID: ")
        isbn = input("Enter book ISBN: ")

        if member_id not in members:
            print("Member not found.")
            continue

        book = None
        for b in library.book_collection:
            if b.isbn == isbn:
                book = b
                break

        if book is None:
            print("Book not found.")
        else:
            members[member_id].borrow_book(book)
        
    elif choice == 6:
        member_id = input("Enter member ID: ")
        isbn = input("Enter book ISBN: ")

        if member_id not in members:
            print("Member not found.")
            continue

        members[member_id].return_book(isbn)
        
    elif choice == 7:
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Please enter an appropriate option number.")


"""
Ans1. I used inheritance in member.py, where StudentMember and TeacherMember inherit from parent class Member.
Ans2. By having all the related attributes and methods in their own classes and calling them when needed.
Ans3. In member.py for the method get_borrowing_limit(), each child class has it's own implementation of that method.
Ans4. The classes interact through objects. Eg: the Library class has a collection of Book objects.
Ans5. Object oriented programming is useful for large software applications because we can have encapsulation where 
related data and functionality is kept together, polymorphism where different objects can have their own implementations
of the same method, inheritance where the repititive code blocks can be reused by allowing child classes to inherit from
parent classes.
"""