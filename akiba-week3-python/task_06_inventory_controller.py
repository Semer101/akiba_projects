def add_product(inventory, name, price, quantity):
    if not name or not name.strip():  #reject None, empty strings, and strings containing only spaces
        print("Enter a valid product name.")
        return

    name = name.strip()

    if name in inventory:
        print("Product already exists.")
    elif price < 0 or quantity < 0:
        print("Price and quantity cannot be negative.")
    else:
        inventory[name] = {"price":price, "quantity":quantity}
        print("Product added successfully.")


def search_product(inventory, name):
    name = name.strip()
    if name in inventory:
        print(f"Product: {name}\nPrice: {inventory[name]['price']}\nQuantity: {inventory[name]['quantity']}")
    else:
        print("Product not found")


def update_price(inventory, name, new_price):
    name = name.strip()
    if name not in inventory:
        print("Product not found.")
    elif new_price < 0:
        print("Price cannot be negative.")
    else:
        inventory[name]["price"] = new_price
        print("Price updated successfully.")


def increase_stock(inventory, name, new_quantity):
    name = name.strip()
    if name not in inventory:
        print("Product not found.")
    elif new_quantity < 0:
        print("Quantity cannot be negative.")
    else:
        inventory[name]["quantity"] += new_quantity
        print("Stock increased successfully.")


def sell_product(inventory, name, purchase_quantity):
    name = name.strip()
    if name not in inventory:
        print("Product not found.")
    elif purchase_quantity <= 0:
        print("Purchase quantity must be positive.")
    elif inventory[name]["quantity"] < purchase_quantity:
        print("Not enough stock available.")
    else:
        inventory[name]["quantity"] -= purchase_quantity
        print("Purchase made successfully.")


def calculate_value(inventory):
    total = 0
    for key in inventory:
        total += (inventory[key]["price"] * inventory[key]["quantity"])
    return total


def low_stock_report(inventory, min_amount=5):
    if min_amount <= 0:
        print("Minimum amount must be greater than zero.")
        return

    found = False

    for key in inventory:
        if inventory[key]["quantity"] < min_amount:
            print(f"Low stock {key}. {inventory[key]['quantity']} remaining.")
            found = True
    if not found:
        print("No low-stock products.")


inventory = {}

add_product(inventory, "Laptop", 30000, 3)
add_product(inventory, "Laptop", 30000, 5)  
add_product(inventory, "   ", 500, 2)      

increase_stock(inventory, "Laptop", 2)
sell_product(inventory, "Laptop", 4)

search_product(inventory, "Laptop")

print("Inventory value:", calculate_value(inventory))
low_stock_report(inventory)

