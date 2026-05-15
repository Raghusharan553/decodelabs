def ask_question(question, options, correct_answer):
    print("\n" + question)
    for option in options:
        print(option)
    user_answer = input("Enter your answer: ").strip().lower()
    if user_answer == correct_answer:
        print("Correct Answer!")
        return 1
    else:
        print("Wrong Answer!")
        return 0

def start_quiz():
    score = 0
    score += ask_question(
        "1. What is the capital of France?",
        ["a) London", "b) Paris", "c) Rome", "d) Berlin"],
        "b"
    )
    score += ask_question(
        "2. Which planet is called the Red Planet?",
        ["a) Earth", "b) Mars", "c) Venus", "d) Jupiter"],
        "b"
    )
    score += ask_question(
        "3. Who invented Python?",
        ["a) Elon Musk", "b) James Gosling", "c) Guido van Rossum", "d) Bill Gates"],
        "c"
    )
    score += ask_question(
        "4. Which keyword is used to create a function in Python?",
        ["a) function", "b) fun", "c) define", "d) def"],
        "d"
    )
    score += ask_question(
        "5. How many days are there in a leap year?",
        ["a) 365", "b) 364", "c) 366", "d) 367"],
        "c"
    )
    print("FINAL RESULT")
    print(f"Your Score: {score}/5")
    if score == 5:
        print("Excellent Performance!")
    elif score >= 3:
        print("Good Job!")
    else:
        print("Keep Practicing!")
while True:
    start_quiz()
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("\nThank you for playing the Quiz Game!")
        break