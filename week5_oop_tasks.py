# ==========================
# Task 1: Student Information System
# ==========================

class Student():
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")

student1 = Student("Alice", 22, "Mechanical Engineering")
student2 = Student("Adam", 23, "Software Engineering")
student3 = Student("Max", 24, "Business")

student1.display_info()
student2.display_info()
student3.display_info()

# ==========================
# Task 2: Rectangle Calculator
# ==========================

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.length + self.width)

rectangle1 = Rectangle(3, 4)
rectangle2 = Rectangle(5, 10)

print(f"Rectangle1 Area: {rectangle1.area()} Perimeter: {rectangle1.perimeter()}")
print(f"Rectangle2 Area: {rectangle2.area()} Perimeter: {rectangle2.perimeter()}")

# ==========================
# Task 3: Student Score Management
# ==========================

class Student():
    school_name = "Akiba Academy"

    def __init__(self, name, score, department):
        self.name = name
        self.score = score
        self.department = department

    def display(self):
        print(f"Name: {self.name}")
        print(f"Score: {self.score}")
        print(f"Department: {self.department}")
        print(f"School name: {self.school_name}")

student1 = Student("Alice", 70, "Mechanical Engineering")
student2 = Student("Adam", 85, "Software Engineering")
student3 = Student("Max", 97, "Business")

student1.score = 79
print(f"Updated score = {student1.score}")
student1.display()
student2.display()
student3.display()

#Ans1: Class attribute applies to all instances of the class, whereas instance attribute is specific to the single instance object created.
#Ans2: Each instance (self) has its own score attribute that is specific to it. 

# ==========================
# Task 4: Product Information System
# ==========================

class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product name: {self.name}, Price: {self.price}, Quantity: {self.quantity} "

    def total_value(self):
        return self.price * self.quantity

product1 = Product("Apple", 5, 20)
product2 = Product("Pen", 3, 50)
product3 = Product("Bag", 50, 10)

print(product1)
print(product2)
print(product3)

print(product1.total_value())
print(product2.total_value())
print(product3.total_value())

#Ans: __str__ method is used to display the object as a string when using print().

# ==========================
# Task 5: Bank Account Management
# ==========================

class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            print("Amount cannot be negative.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def display_balance(self):
        print(f"Current Balance: {self.balance}")

account1 = BankAccount("Sara", 1000)
account2 = BankAccount("Bob", 2000)

account1.deposit(500)
account1.withdraw(300)
account1.withdraw(2000)
account1.display_balance()

#Ans: When a withdrawal exceeds the balance, the program prints the message: "Insufficient funds." and cancels the withdrawal.