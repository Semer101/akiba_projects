def calculate_total_revenue(sales):
    total = 0
    for sale in sales:
        total += sale["total"]
    return total


def calculate_inventory_value(products):
    inventory_value = 0
    for product in products:
        inventory_value += (product["price"] * product["stock"])
    return inventory_value


def display_low_stock_products(products):
    low_stock = []
    for product in products:
        if product["stock"] <= 5:
            low_stock.append(product)
    return low_stock


def recorded_sales_summary(sales):
    for sale in sales:
        print(f"Product: {sale['product']}")
        print(f"Quantity: {sale['quantity']}")
        print(f"Unit price: {sale['price']}")
        print(f"Total: {sale['total']}")
        print("-------------------")


