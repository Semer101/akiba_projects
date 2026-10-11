correct_pin = 1234
count = 0
pin = 0
while count < 3 and pin != correct_pin:
    pin = int(input("Enter PIN: "))
    count += 1
    if pin == correct_pin:
        print("Access verified!")
    else:
        print(f"Incorrect PIN.")
        if count < 3:
            print(f"Attempts remaining: {3 - count}")
        else:
            print("Maximum attempts reached. Access denied.")