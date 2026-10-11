num = int(input("Enter a number: "))

sum = 0
while num > 0:
    rem = num % 10 #rem is short for remainder, aka last digit
    sum += rem
    num = num // 10 #divide by 10 to remove last digit entirely
print(sum)