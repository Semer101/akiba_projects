num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

if num1 == num2 and num1 == num3: #check if all 3 are equal
    print(f"All three numbers {num1},{num2} and {num3} are equal!")
elif num2 == num3: #check if 2 and 3 are equal
    if num2 > num1: 
        print(f"The numbers {num2} and {num3} are equal and are larger than {num1}!")
    else:
        print(f"The numbers {num2} and {num3} are equal and {num1} is the largest!")
elif num1 == num3: #check if 1 and 3 are equal
    if num1 > num2:
        print(f"The numbers {num1} and {num3} are equal and are larger than {num2}!")
    else:
        print(f"The numbers {num1} and {num3} are equal and {num2} is the largest!")
elif num1 == num2: #check if 1 and 2 are equal
    if num1 > num3:
        print(f"The numbers {num1} and {num2} are equal and are larger than {num3}!")
    else:
        print(f"The numbers {num1} and {num2} are equal and {num3} is the largest!")
else: #no equal numbers
    if num1 > num2 and num1 > num3:
        print(f"The largest number is {num1}!")
    elif num2 > num1 and num2 > num3:
        print(f"The largest number is {num2}!")
    else:
        print(f"The largest number is {num3}!")