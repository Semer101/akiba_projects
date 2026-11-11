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

