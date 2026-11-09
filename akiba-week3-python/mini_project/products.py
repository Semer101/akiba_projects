def add_product(product, price, products):
    products.append({"product" : product, "price" : price})
    return products


def search_product(product, products):
    for i in products:
        if i["product"].lower() == product.lower():
            return i
    return None


def update_product(product, price, products):
    for i in products:
        if i["product"].lower() == product.lower():
            i["price"] = price
            return i
    return None


def display_products(products):
    for i in products:
        print(i)


products = [
    {"product" : "Apple", "price" : 10},
    {"product" : "Car", "price" : 5000},
    {"product" : "Bag", "price" : 60}
]

add_product("Pen", 20, products)
display_products(products)
