def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
        
    return True

def get_divisors(number): #give an empty list for 0 and -ve numbers
    lst = []
    if number <= 0:
        return lst
    
    for i in range(1, number+1):
        if number % i == 0:
            lst.append(i)
    return lst

def sum_of_digits(number):
    rem = 0
    total = 0
    number = abs(number) #calculates the absolute value for -ve numbers
    while number > 0: #total is 0 for 0 value inputs
        rem = number % 10
        total += rem
        number = number // 10

    return total

def reverse_number(number):
    rem = 0
    reversed_num = 0
    original_number = number
    number = abs(number)

    while number > 0:
        rem = number % 10
        reversed_num = reversed_num * 10 + rem #shift digits from right to left and add rem 
        number = number // 10

    if original_number < 0:
        reversed_num = -reversed_num

    return reversed_num

def analyze_number(number):
    prime_num = is_prime(number)
    divisors = get_divisors(number)
    total = sum_of_digits(number)
    reversed_num = reverse_number(number)
    even_odd = ""
    if number % 2 == 0:
        even_odd = "Even"
    else:
        even_odd = "Odd"

    print("============= Analyze Numbers =============")
    print(f"The number {number} is {even_odd}")
    if prime_num:
        print(f"The number {number} is prime")
    else:
        print(f"The number {number} is not prime")
    print(f"The number {number}'s sum is {total}")
    print(f"The number {number}'s reversed value is {reversed_num}")
    print(f"The number {number}'s divisors are: ")
    if len(divisors) > 0:
        for divisor in divisors:
            print(divisor)
    else:
        print("No positive divisors for zero or negative numbers.")

    
analyze_number(-123)