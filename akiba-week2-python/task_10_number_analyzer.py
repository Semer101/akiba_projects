numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

largest = numbers[0]
smallest = numbers[0]
total_sum = 0
even_count = 0
odd_count = 0
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    total_sum += num
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Largest: {largest}\nSmallest: {smallest}\nTotal Sum: {total_sum}\nAverage: {total_sum/10}\nEven numbers count: {even_count}\nOdd numbers count: {odd_count}")
    

