def display_question(questions):
    correct_count = 0
    incorrect_count = 0
    for i in range(len(questions)):
        print(questions[i]["question"], questions[i]["options"] )
        answer = input("Choose the correct option: ")
        answer = validate_answer(answer)
        if correct_answer(answer, questions[i]):
            print("Correct answer!")
            correct = True
            correct_count, incorrect_count = update_score(correct,  correct_count, incorrect_count)
        else:
            print("Incorrect answer.")
            correct = False
            correct_count, incorrect_count = update_score(correct,  correct_count, incorrect_count)
    return correct_count, incorrect_count


def validate_answer(answer):
    answer = answer.upper().strip()
    while answer not in ["A", "B", "C", "D"]:
        print("Enter a valid option: ")
        answer = input("Enter your answer: ")
        answer = answer.upper().strip()
    return answer


def correct_answer(answer, question):
    return answer == question["answer"]
    

def update_score(correct, correct_count, incorrect_count):
    if correct:
        correct_count +=1
    else:
        incorrect_count +=1
    return correct_count, incorrect_count


def result_display(questions, correct_count, incorrect_count):
    final_percent = (correct_count/len(questions)*100)

    print(f"Final score: {correct_count}/{len(questions)}")
    print(f"Final percentage: {final_percent:.2f}%")
    print(f"Correct answers: {correct_count}/{len(questions)}")
    print(f"Incorrect answers: {incorrect_count}/{len(questions)}")

    if final_percent >= 50:
            print("Quiz Passed!")
    else:
        print("Quiz Failed.")
        

questions = [
    {
        "question" : "How many days are in a week?",
        "options" : ["A. 5 ", "B. 7 ", "C. 8 ", "D. 6 "],
        "answer" :  "B"
    },
    {
        "question" : "What is H2O commonly known as?",
        "options" : ["A. water ", "B. Hydrochloric acid ", "C. Hydroxide ", "D. Helium"],
        "answer" : "A"
    },
    {
        "question" : "How many continents are there?",
        "options" : ["A. 12 ", "B. 4 ", "C. 9 ", "D. 7 "],
        "answer" : "D"
    },
    {
        "question" : "What is the largest mammal in the world?",
        "options" : ["A. elephant ", "B. lion ", "C. blue whale ", "D. octopus "],
        "answer" : "C"
    },
    {
        "question" : "What is the closest star to Earth?",
        "options" : ["A. pluto ", "B. sun ", "C. mercury ", "D. neptune"],
        "answer" : "B"
    },
]

while True:
    correct_count, incorrect_count = display_question(questions)

    result_display(questions, correct_count, incorrect_count)

    choice = input("Would you like to play again? (yes/no): ")

    if choice.strip().lower() != "yes":
        print("Goodbye! Have a great day!")
        break
