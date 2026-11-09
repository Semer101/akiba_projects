student_marks = [80, 90, 77, 94, 86]
points = student_marks
new_student_marks = student_marks.copy()
new_student_marks.append(73)

print(f"Original marks: {student_marks}")
print(f"Shared reference: {points}")
print(f"Copied marks: {new_student_marks}")

print(f"Original and shared reference are identical: {student_marks is points}")
print(f"Original and copied lists are identical: {student_marks is new_student_marks}")
print(f"Original and copied lists have equal values: {student_marks == new_student_marks}")