def score_validator(score):
    if score < 0 or score > 100:
        print("Invalid score. Enter a score between 0 and 100.")
        return False
    else: 
        return True

def grade_calculator(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def average_calculator(students):
    if len(students) == 0:
        return None

    total = 0
    for i in range(len(students)):
        total += students[i]["score"]

    average_score = total / len(students)
    return average_score
        

def highest_score_lowest_score(students):
    if len(students) == 0:
        return None, None

    highest_score = students[0]["score"]
    lowest_score = students[0]["score"]

    for student in students:
        score = student["score"]

        if score > highest_score:
            highest_score = score

        if score < lowest_score:
            lowest_score = score

    return highest_score, lowest_score

def count_pass_or_fail(students):
    pass_count = 0
    fail_count = 0
    for student in students:
        if student["score"] >= 50:
            pass_count += 1
        else:
            fail_count +=1

    return pass_count, fail_count

def report_generator(students):
    if len(students) == 0:
        print("No student data available.")
        return

    for student in students:
        if not score_validator(student["score"]):
            return

    average_score = average_calculator(students)
    highest_score, lowest_score = highest_score_lowest_score(students)

    pass_count, fail_count = count_pass_or_fail(students)


    print("===== STUDENT REPORT =====")
    for student in students:
        grade = grade_calculator(student["score"])
        print(
            f'{student["name"]}: '
            f'Score = {student["score"]}, Grade = {grade}'
        )
    print(f"Average: {average_score}")
    print(f"Highest score: {highest_score}")
    print(f"Lowest score: {lowest_score}")
    print(f"Passed count: {pass_count}")
    print(f"Failed count: {fail_count}")

    print("Students above class average:")
    for student in students:
        if student["score"] > average_score:
            print(student["name"])
    

students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]
report_generator(students)