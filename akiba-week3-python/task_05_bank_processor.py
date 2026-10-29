def deposit(amount, balance, transactions):
    if amount <= 0:
        print("Invalid deposit amount.")
    else:
        balance += amount
        record_transaction("deposit", amount, balance, transactions)
        print("Deposit successful!")

    return balance
    

def withdraw(amount, balance, transactions, withdrawn_today, daily_limit):
    if amount <= 0:
        print("Invalid withdrawal amount.")
    elif amount > balance:
        print("Insufficient balance.")
    elif withdrawn_today + amount > daily_limit:
        print("Daily withdrawal limit exceeded.")
    else:
        balance -= amount
        withdrawn_today += amount
        record_transaction("withdrawal", amount, balance, transactions)
        print("Withdrawal successful!")
    return balance, withdrawn_today
    

def check_balance(balance):
    return balance


def record_transaction(transaction_type, amount, balance, transactions):
    transaction = {
        "type" : transaction_type,
        "amount" : amount,
        "balance_after" : balance
    }
    transactions.append(transaction)
    return transactions


def menuselector(balance, transactions, daily_limit):
    withdrawn_today = 0

    while True:
        choice = int(input("Choose one of the following:\n1.Deposit\n2.Withdraw\n3.Check balance\n4.Exit"))
        if choice == 1:
            amount = float(input("Enter a deposit amount:"))
            balance = deposit(amount, balance, transactions)
        elif choice == 2:
            amount = float(input("Enter withdrawal amount:"))
            balance, withdrawn_today = withdraw(amount, balance, transactions, withdrawn_today, daily_limit)
        elif choice == 3:
            print(f"Balance: {check_balance(balance)} Birr")
        elif choice == 4:
            print("Good Bye!")
            break
        else:
            print("Invalid choice.")

    return balance
        
def transaction_summary(balance, transactions):
    total_deposited = 0
    total_withdrawn = 0

    for transaction in transactions:
        if transaction["type"] == "deposit":
            total_deposited += transaction["amount"]
        elif transaction["type"] == "withdrawal":
            total_withdrawn += transaction["amount"]

    print("\n========== TRANSACTION SUMMARY ==========")
    print(f"Total deposited: {total_deposited} Birr")
    print(f"Total withdrawn: {total_withdrawn} Birr")
    print(f"Final balance: {balance} Birr")
    print("Transaction history:")

    for transaction in transactions:
        print(transaction)

opening_balance = 1000
daily_limit = 2000
transactions = []

final_balance = menuselector(opening_balance, transactions, daily_limit)
transaction_summary(final_balance, transactions)
