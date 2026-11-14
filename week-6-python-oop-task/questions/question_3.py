class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Programming Language: {self.programming_language}")

employee1 = Employee("Alice", 10000)
manager1 = Manager("Bob", 12000, "IT")
developer1 = Developer("Kate", 15000, "Python")

employee1.display_info()
manager1.display_info()
developer1.display_info()

"""
Ans1. Inheritance is when a child class inherits the attributes and methods from a parent class.
Ans2. Parent class is on the top on the heriarchy and child class inherits the parent's attributes and methods.
Ans3. Method overriding is when a child class modifies the method inherited from a parent class.
Ans4. super() is used to access the parent class's methods eg: calling the parent contructor to initialize the inherited attributes.
Ans5. Single inheritance is inheriting from a single parent class, whereas multiple inheritance is inheriting from multiple parent classes.
"""