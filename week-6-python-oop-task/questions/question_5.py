class Product:
    store_name = "Akiba Shop"

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_product(self):
        print(f"Product: {self.name} Price: {self.price}")

    @classmethod
    def change_store_name(cls, store_name):
        cls.store_name = store_name

    @staticmethod
    def is_valid_price(price):
        return price > 0

class ShoppingCart:

    def __init__(self):
        self.products_lst = []

    def add_product(self, product, quantity):
        self.products_lst.append({"Product" : product.name, "Price" : product.price, "Quantity" : quantity})

    def calculate_total(self):
        total = 0
        for i in self.products_lst:
            total += i["Price"] * i["Quantity"]
        return total

    def display_cart(self):
        for i in self.products_lst:
            print(i)
        print(f"Total: {self.calculate_total()}")


product1 = Product("Laptop", 50000)
product2 = Product("Mouse", 1000)

cart = ShoppingCart()

cart.add_product(product1, 2)
cart.add_product(product2, 3)

product1.display_product()
cart.display_cart()

Product.change_store_name("New Akiba Shop")
print(Product.store_name)

print(Product.is_valid_price(500))
print(Product.is_valid_price(-10))


"""
Ans1. Instance attributes are unique per object instance created, whereas class attribute stays the same for every object instance created.
Ans2. An instance method is used for object instance action eg: display a product. It uses self to access the object's attributes.
Ans3. A class method is used to change class attributes. It uses cls to access class attributes.
Ans4. A static method is used to validate inputs of object instances. It doesn't receive self or cls automatically.
Ans5. Composition is when a class uses objects of another class (A ShoppingCart has Products), while inheritance is when a child class inherits it's methods and attributes from a parent class (A Manager is an Employee).
"""
