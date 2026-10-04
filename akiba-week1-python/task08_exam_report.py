student_name = input("Enter student name: ")
python_score = float(input("Enter python score: "))
english_score = float(input("Enter english score: "))
mathematics_score = float(input("Enter mathematics score: "))

average_score = (python_score + english_score + mathematics_score) / 3

print("========================================")
print("             STUDENT RESULT             ")
print("========================================")
print()
print(f"Student: {student_name}")
print()
print(f"Python: {python_score}")
print(f"English: {english_score}")
print(f"Mathematics: {mathematics_score}")
print("----------------------------------------")
print(f"Average: {average_score:.2f}")
print("========================================")
