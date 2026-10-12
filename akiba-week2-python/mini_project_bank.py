correct_pin = 1234
count = 0
pin = 0
access = False
while count < 3 and pin != correct_pin:
    pin = int(input("===== AKIBA BANK =====\nEnter your PIN: "))
    count += 1
    if pin == correct_pin:
        print("PIN correct!\nWelcome to Akiba Bank.")
        access = True
    else:
        print(f"Incorrect PIN.")
        if count < 3:
            print(f"Attempts remaining: {3 - count}")
        else:
            print("Too many incorrect attempts.\nYour account is locked.")
            access = False

menu_choice = 0
balance = 1000
transactions = 0

while access:
    menu_choice = int(input(f"===== AKIBA BANK =====\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit\nChoose an option:"))

    if menu_choice == 1:
        print(f"Your current balance is: {balance} Birr")
    
    elif menu_choice == 2:
        deposit = int(input("Enter deposit amount: "))
        while deposit <= 0:
            print("Please enter an amount greater than zero.")
            deposit = int(input("Enter deposit amount: "))
        
        balance += deposit
        transactions += 1
        print(f"Deposit successful!\nYour new balance is: {balance} Birr")
        print(f"Transactions made: {transactions}")
    
    elif menu_choice == 3:
        withdrawal = int(input("Enter withdrawal amount: "))
        if withdrawal <= 0:
            print("Please enter an amount greater than zero.")
        elif withdrawal > balance:
            print("Insufficient balance!")
        else:
            balance -= withdrawal
            transactions += 1
            print(f"Withdrawal successful!\nYour new balance is: {balance} Birr")
            print(f"Transactions made: {transactions}")
    
    elif menu_choice == 4:
        print(f"Thank you for using Akiba Bank!\nGoodbye!")
        break
    
    else:
        print(f"Invalid option.\nPlease choose a valid option.")
