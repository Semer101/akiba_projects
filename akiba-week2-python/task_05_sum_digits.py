num = int(input("Enter a number: "))

sum = 0
for i in range(len(str(num))):
    sum += int(str(num)[i])
print(sum)