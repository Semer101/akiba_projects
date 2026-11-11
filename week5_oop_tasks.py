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

