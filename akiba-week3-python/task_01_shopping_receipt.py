def calculate_subtotal(items):
    subtotal = 0 

    for item in items:
        price = item["price"]
        quantity = item["quantity"]

        if price < 0 or quantity < 0:
            return None

        item_total = price * quantity
        subtotal += item_total
    
    return subtotal


def calculate_discount(subtotal):
    if subtotal < 1000:
        return subtotal, 0
    
    elif subtotal <= 2999:
        discount_amount = subtotal * 0.05
        discounted_subtotal = subtotal - discount_amount
        return discounted_subtotal, discount_amount
    
    else:
        discount_amount = subtotal * 0.10
        discounted_subtotal = subtotal - discount_amount
        return discounted_subtotal, discount_amount


def calculate_tax(amount, tax_rate):
    if tax_rate < 0 or tax_rate > 1:
        return None
    
    tax_amount = amount * tax_rate
    return tax_amount
    

def generate_receipt(items, tax_rate):
    subtotal = calculate_subtotal(items)

    if subtotal is None:
        print("Error: Prices and quantities cannot be negative.")
        return

    discounted_subtotal, discount_amount = calculate_discount(subtotal)

    tax_amount = calculate_tax(discounted_subtotal, tax_rate)

    if tax_amount is None:
        print("Error: Invalid tax rate.")
        return

    final_amount = discounted_subtotal + tax_amount

    print("\n===== SHOPPING RECEIPT =====")
    print(f"Subtotal: {subtotal:.2f} Birr")
    print(f"Discount amount: {discount_amount:.2f} Birr")
    print(f"Discounted subtotal: {discounted_subtotal:.2f} Birr")
    print(f"Tax rate: {tax_rate * 100:.0f}%")
    print(f"Tax amount: {tax_amount:.2f} Birr")
    print(f"Final amount: {final_amount:.2f} Birr")


items = [
        {"name":"Notebook", "price":80, "quantity":3},
        {"name":"Pen", "price":15, "quantity":5}
    ]
tax_rate = 0.15
generate_receipt(items, tax_rate)
