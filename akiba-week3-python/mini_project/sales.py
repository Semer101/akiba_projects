def find_product(product, products):
    for i in products:
        if i["product"].lower() == product.lower():
            return i
    return None


def validate_quantity(quantity, product_info):
    if quantity <= 0:
        return False
    if product_info["stock"] >= quantity:
        return True
    return False


def reduce_stock(product_info, quantity):
    product_info["stock"] -=quantity
    return product_info


def calculate_sale_total(quantity, price):
    return quantity * price


def record_sale(product, quantity, sales, products):
    product_info = find_product(product, products)
    if product_info is None:
        return None
    if not validate_quantity(quantity, product_info):
        return None

    total = calculate_sale_total(quantity, product_info["price"])
    
    reduce_stock(product_info, quantity)

    sale = {
        "product": product_info["product"],
        "quantity": quantity,
        "price": product_info["price"],
        "total": total
    }

    sales.append(sale)

    return sale


products = [
    {"product": "Apple", "price": 10, "stock": 50},
    {"product": "Car", "price": 5000, "stock": 5},
    {"product": "Bag", "price": 60, "stock": 20}
]

sales = []

result = record_sale("Apple", 3, products, sales)

if result:
    print("Sale successful:", result)
else:
    print("Sale unsuccessful.")

print("Remaining stock:", products[0]["stock"])