def add_expense(description, category, amount, expenses):
    expenses.append({"description":description, "category":category, "amount":amount})
    return expenses


def calculate_total_expenses(expenses):
    total = 0
    for i in range(len(expenses)):
        total += expenses[i]["amount"]
    return total


def calculate_category_spending(expenses):
    category_spendings = {}
    for i in range(len(expenses)):
        category = expenses[i]["category"]
        amount = expenses[i]["amount"]
        if category not in category_spendings:
            category_spendings[category] = 0
        category_spendings[category] += amount
    return category_spendings
            

def find_largest_expense(expenses):
    if not expenses:
        return None
    largest_expense = expenses[0]
    for i in range(len(expenses)):
        if expenses[i]["amount"] > largest_expense["amount"]:
            largest_expense = expenses[i]
    return largest_expense
    

def expenses_over_threshold(expenses, threshold_amount):
    over_limit_expenses = []
    for i in range(len(expenses)):
        if expenses[i]["amount"] > threshold_amount:
            over_limit_expenses.append(expenses[i]["description"])
    return over_limit_expenses


def category_percentage(expenses):
    categories = calculate_category_spending(expenses)
    total = calculate_total_expenses(expenses)
    if total == 0:
        return
    for category, amount in categories.items():
        percentage = (amount / total) * 100
        print(f"{category}: {percentage:.2f}%")


def highest_spending_category(expenses):
    categories = calculate_category_spending(expenses)
    if not categories:
        return None
    highest_category = max(categories, key=categories.get) # key=categories.get compares values instead of keys
    return highest_category


def spending_report(description, category, amount, threshold_amount, expenses):
    expenses = add_expense(description, category, amount, expenses)
    total = calculate_total_expenses(expenses)
    category_spendings = calculate_category_spending(expenses)
    largest_expense = find_largest_expense(expenses)
    over_limit_expenses = expenses_over_threshold(expenses, threshold_amount)
    highest_category = highest_spending_category(expenses)
    
    print(f"Total: {total}")
    print(f"Category spendings: ")
    for category, amount in category_spendings.items():
        print(f"{category}: {amount}")
    print(f"Largest: {largest_expense}")
    print(f"Expenses exceeding threshold: {over_limit_expenses}")
    print("Category percentages:")
    category_percentage(expenses)
    print(f"Highest spending category: {highest_category}")


expenses = [
    {"description": "Lunch", "category": "Food", "amount": 180},
    {"description": "Taxi", "category": "Transport", "amount": 120},
    {"description": "Groceries", "category": "Food", "amount": 450},
    {"description": "Internet", "category": "Bills", "amount": 300}
]

spending_report("Dinner", "Food", 200, 250, expenses)