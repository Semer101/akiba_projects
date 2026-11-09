Answer 1:
Writing a single function to manage products, sales and reports is a bad idea because it would become to confusing to edit and update any section of the code without affecting the other parts. 
We should use single purpose functions that do a single task which will be easier to test and debug later if any error comes up. Smaller functions are easier to check where the error occurs and quickly fix them and test them without running the other code snippets.
It will also be easier to edit the parameters and return values if we want to change the inputs and outputs of a function.
Also DRY (don't repeat yourself) principle is easier to do when we have a block of code that we can reuse instead of coding the same thing again and again.
I would separate the program into products, sales and reports files like i did for the mini-project.
Each file will have single-purpose functions eg: display function, add product function, record a sale function, etc.

def manage_all(product, price, quantity, products):
    products.append({"product" : product, "price" : price, "stock" : quantity})
    for product in products:
        print(product)
    for i in products:
        if i["product"].lower() == product.lower():
            return i
    return None

Here if i call the function manage_all it will add a product, display all the products and search for a product, when i only really wanted to just search for a product and not add it to the list of products.
So, I would separate the code into 3 functions where each does it separate task of adding a product, display products or search for a product.

Answer 2:
Here both the variable products and the parameter items point to the same list object so any change in one affects the other too.
Lists are mutable so they are changed in a function depending on the instructed code block inside the function.
Modifying an existing list is where the parameter points to the submitted argument whereas, in some functions a new list is created using the provided argument and that new list is modified and returned and the original list is unmodified.
Modifying the original list data is useful for keeping records of products in inventory, eg: adding a product.
Modifying the original list data is bad when the data needs to be unedited, eg: displaying inventory products.

names = ["Sara", "Ahmed"]
def display(names):
    for name in names:
        print(name)

Here the names list is unchanged and I only access it to display the names.

numbers = [1, 2, 3]
def more_nums(numbers):
    new_nums = numbers.copy()
    new_nums.append(4)
    new_nums.append(5)
    return new_nums

Here I created a new list where the original numbers list is not modified and only the new list new_nums is modified and returned.
This is because I created a new list object and copied numbers list into it and that new one is only updated not the original one.