num = int(input("Enter a positive number:"))

even_count = 0
odd_count = 0
sum = 0
for i in range(1, num + 1):
    sum += i
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even numbers count = {even_count}\nOdd numbers count = {odd_count}\nSum of all numbers = {sum}")