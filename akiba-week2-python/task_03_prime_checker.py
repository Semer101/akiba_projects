number = int(input("Enter a number to check if prime: "))

if number == 0 or number == 1:
    print(f"The number {number} is not prime.")
elif number == 2:
    print(f"The number {number} is prime!")
else:
    for i in range(2, number):
        if number % i == 0 : #i just need 1 number (other than 1 and itself) that divides it to prove its not prime
            #if the number is divisible by other than 1 or itself it's not a prime number
            print(f"The number {number} is not prime.")
            break
    else: #for's else executes after successfully completing all iterations of for loop without finding divisor, doesn't execute if break happens
        print(f"The number {number} is prime!")
    