from products import add_product, search_product, update_product, display_products
from sales import record_sale, generate_receipt
from reports import (
    calculate_total_revenue,
    calculate_inventory_value,
    display_low_stock_products,
    recorded_sales_summary
)

products = [
    {"product": "Apple", "price": 10, "stock": 50},
    {"product": "Car", "price": 5000, "stock": 5},
    {"product": "Bag", "price": 60, "stock": 20}
]

sales = []

def display_menu():
    print("\n===== AKIBA BUSINESS TOOLKIT =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Record Sale")
    print("6. View Reports")
    print("7. Exit")


while True:
    display_menu()
    choice = int(input("Choose an option: "))

    if choice == 1:
        product = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))
        add_product(product, price, stock, products)
        print("Product added successfully!")

    elif choice == 2:
        display_products(products)

    elif choice == 3:
        product = input("Enter product name to search: ")
        result = search_product(product, products)
        if result:
            print("Product found:", result)
        else:
            print("Product not found.")

    elif choice == 4:
        product = input("Enter product name: ")
        price = float(input("Enter new price: "))
        result = update_product(product, price, products)
        if result:
            print("Product updated:", result)
        else:
            print("Product not found.")

    elif choice == 5:
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        result = record_sale(product, quantity, sales, products)
        if result:
            print("Sale successful!")
            print("Sale details:", result)
            generate_receipt(result)
        else:
            print("Sale unsuccessful. Check product name and available stock.")
            
    elif choice == 6:
        print("\n===== BUSINESS REPORTS =====")
        revenue = calculate_total_revenue(sales)
        print("Total revenue:", revenue)
        inventory = calculate_inventory_value(products)
        print("Total inventory value:", inventory)
        low_stock = display_low_stock_products(products)
        print("Low stock products:")
        if low_stock:
            display_products(low_stock)
        else:
            print("No low-stock products.")
        print("\n===== SALES SUMMARY =====")
        recorded_sales_summary(sales)
        
    elif choice == 7:
        print("Thank you for using Akiba Business Toolkit!")
        break

    else:
        print("Invalid choice. Try again.")