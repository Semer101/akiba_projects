#Answer 1
greeting = "Hello!"
fruits = ["apple", "orange"]
print(greeting)
print(fruits)
greeting = "Hi!" #string cannot be indexed and changed
fruits[1] = "pineapple" #fruits list can be modified
print(greeting)
print(fruits)

#Answer 3
numbers = [1, 2, 3]
values = numbers.copy() #create a new shallow copy
values.append(4)
print(numbers)
print(values)

#Answer 4
def update_list(items):
    new_items = items.copy() #new list created
    new_items.append(100)
    return new_items #return new list

scores = [50, 60, 70]
print(update_list(scores))
print(scores) #original list not modified

#Answer 5
colors = ["red", "blue"]
candy = colors
del colors
print(candy) #object still exists

