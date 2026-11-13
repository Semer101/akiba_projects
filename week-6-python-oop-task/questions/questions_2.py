class BankAccount:
    def __init__(self, balance, account_holder):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__balance = balance
        self.account_holder = account_holder

    def deposit(self, amount):
        if amount <= 0:
            print("Enter a positive amount.")
        else:
            self.__balance += amount
            print(f"Deposited amount successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a positive amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Successful withdrawal.")

    def get_balance(self):
        print(f"Balance: {self.__balance}")

account1 = BankAccount(1000, "Bob")

account1.deposit(500)
account1.withdraw(200)
account1.get_balance()

"""
Ans1. Encapsulation contains attributes and methods in a single class. It allows access to attributes through methods and controls access to the attributes.
Ans2. To prevent direct access to the sensitive attribute data. Eg: we used deposit() method to access and modify __balance attribute.
Ans3. Name mangling in python automatically adds _ClassName as a prefix to private attributes.
Ans4. Public is accessed from anywhere, protected is intended for access within a class and its subclasses (single underscore prefix), and private uses name mangling to 
      avoid accidental access and naming conflicts with inheritance (double underscore prefix).
"""