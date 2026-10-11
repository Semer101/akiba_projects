start_num = int(input("Enter starting number: "))
end_num = int(input("Enter ending number: "))

for i in range(start_num, end_num + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    