number = int(input("Enter a number: "))

if number > 0 and (number % 2) == 0:
    print(f"The number {number} is even and positive")
elif number < 0 and (number % 2) == 0:
    print(f"The number {number} is even and negative")
elif number > 0 and (number % 2) != 0:
    print(f"The number {number} is odd and positive")
elif number < 0 and (number % 2) != 0:
    print(f"The number {number} is odd and negative")
else:
    print("The number is zero and even!")