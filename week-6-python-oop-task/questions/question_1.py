class Student:
    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}, Student ID: {self.student_id}, Department: {self.department}")

    def introduce(self):
        print(f"My name is {self.name}. I am studying in {self.department} department. I am a student at Addis Ababa University.")

student1 = Student("Alice", "ID1234", "Software Engineering")
student2 = Student("Bob", "ID5678", "Biomedical Engineering")
student3 = Student("Patricia", "ID9012", "Electrical Engineering")

student1.display_info()
student2.display_info()
student3.display_info()

student1.introduce()
student2.introduce()
student3.introduce()

"""
Ans1. Class is a blueprint for creating objects.
Ans2. An object is an instance of a class, eg: student1 is an instance of Student class.
Ans3. __init__ method initializes the object's attributes when an object is created.
Ans4. Attribute is a variable that stores an object's data, whereas method performs an action for the object.
"""