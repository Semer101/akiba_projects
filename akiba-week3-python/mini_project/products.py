def add_product(product, price, stock, products):
    products.append({"product" : product, "price" : price, "stock" : stock})
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




