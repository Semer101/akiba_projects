#Part A: Polymorphism
class Dog:
    def make_sound(self):
        print("Bark!")

class Cat:
    def make_sound(self):
        print("Meow!")
class Cow:
    def make_sound(self):
        print("Moo!")

dog1 = Dog()
dog1.make_sound()

cat1 = Cat()
cat1.make_sound()

cow1 = Cow()
cow1.make_sound()

#Part B: Abstraction
from abc import ABC, abstractmethod

class Shape(ABC): #abstract base class
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        print(f"Rectangle area: {self.length * self.width}")

class Circle(Shape):
    PI = 3.14
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        print(f"Circle area: {self.PI * self.radius**2}")

rectangle1 = Rectangle(4, 3)
circle1 = Circle(5)

rectangle1.calculate_area()
circle1.calculate_area()

"""
Ans1. Polymorphism is when a single method is used in different classes and has different implementations.
Ans2. Abstraction hides unnecessary implementation details and exposes only the essential features of an object.
Ans3. An abstract class cannot be instantiated directly and has abstract methods that must be implemented by child classes.
Ans4. TypeError message when creating an object of the child class.
Ans5. Abstraction is hiding complex logic and implementation details, encapsulation is containing the methods and attributes in a single class and controlling access to internal data.
"""
