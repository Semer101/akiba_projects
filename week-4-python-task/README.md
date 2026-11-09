Student Information
             # Akiba Technologies — Week 4 Python Tasks
                 Name: Semer Nuru
                 Course: Python Programming
                 Week: 4 
Topics Covered
              - Mutable and immutable objects in python
              - References and object identity
              - Python memory management, object references and garbage collection.
    
Completed Tasks
            Question 1: Mutable and Immutable Objects
            Question 2: References and Object Identity
            Question 3: Shared References and Side Effects
            Question 4: Function Arguments and Mutability
            Question 5: Memory Management and Garbage Collection
            Practical Mini-Project: Student Marks Manager

Theory Answers:
Ans1: Mutable objects are objects that can be modified once created eg: lists, dictionaries.
Immutable objects cannot be modified once created eg: string, tuples.
In questions.py I modified the list by index but cannot modify string using index and had to change the whole string word. But I can create a new string and assign it to the variable.
Code in questions.py file.

Ans2: True, False and True.
"is" is used to mean that the referred object is the same and has the same identity. Whereas "==" is used to mean that just the value is equal.
Because a object was created first and then object c was created separately later in a different memory space even if they have the same value they are 2 separate objects created. And b refers to a's list object.

Ans3: [1, 2, 3, 4]
      [1, 2, 3, 4]
    Because both the variables refer to the same list object.
    Code in questions.py file.

Ans4: [50, 60, 70, 100]
    The parameter items and the variable scores both point to the same list object which causes any changes in the function to change the original list.
    Code in questions.py file.

Ans5: Python checks for objects that are stuck in a cycle of refering to each other and trashes them. If an object has 0 variable refering to it python disposes of the object, it does this by keeping count of number of referencing variable of the object.
Code in questions.py file.
del removes the variable referencing the list object, colors doesn't exist anymore.
Not if it has another variable referencing it.
It gets removed by garbage collection whe it's not referenced.


Project Reflection:
Why does modifying a shared reference affect the original list?
Because the reference points to the original object.

Why does modifying the copied list not affect the original list?
Yes, it doesn't affect the original because they are 2 different objects.

What is the difference between equality and identity in Python?
Equality compares values, identity checks if the referred object is the same.


Setup and execution instructions:

cd week-4-python-task

python questions.py
python student_marks_manager.py
