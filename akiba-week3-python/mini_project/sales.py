from products import search_product

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
    product_info = search_product(product, products)
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


def generate_receipt(sale):
    print("\n===== SALES RECEIPT =====")
    print(f"Product: {sale['product']}")
    print(f"Quantity: {sale['quantity']}")
    print(f"Unit price: {sale['price']}")
    print(f"Total cost: {sale['total']}")
    print("=========================")
