# 1. Simple Quiz Game
# Concepts Involved: Basic Syntax, Conditional Statements, Loops, Functions
# Description: Create a text-based quiz game where users answer multiple-choice questions. The program should track the score and provide feedback on whether answers are correct or not.
# Features:
# Start with a predefined set of questions.
# Ask the user one question at a time.
# At the end of the quiz, display the total score.
import random
import time

print('Welcome!')
time.sleep(0.5)

questions = [
    {
        'question': 'What is the capital of Spain?',
        'choices': ['A) Valencia', 'B) Paris', 'C) Madrid', 'D) Rome'],
        'answer': 'C'
     },
    {
        'question': 'How many letters are in the english alphabet?',
        'choices': ['A) 30', 'B) 31', 'C) 26', 'D) 25'],
        'answer': 'C'
     },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "C"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "choices": ["A) Oxygen", "B) Gold", "C) Osmium", "D) Hydrogen"],
        "answer": "A"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "choices": ["A) Oxygen", "B) Gold", "C) Osmium", "D) Hydrogen"],
        "answer": "A"
    },
    {
        "question": "Which of the following is not a programming language?",
        "choices": ["A) Python", "B) Java", "C) HTML", "D) C++"],
        "answer": "C"
    },
    {
        "question": "Which of the following animals is native to Australia?",
        "choices": ["A) Kangaroo", "B) Elephant", "C) Panda", "D) Polar bear"],
        "answer": "A"
    },
    {
        "question": "What is the capital of Japan?",
        "choices": ["A) Seoul", "B) Beijing", "C) Tokyo", "D) Bangkok"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "A"
    },
    {
        "question": "Which famous physicist developed the theory of relativity?",
        "choices": ["A) Isaac Newton", "B) Nikola Tesla", "C) Albert Einstein", "D) Marie Curie"],
        "answer": "C"
     }
]

def run_quiz():
    score = 0
    random_questions = random.sample(questions,5)

    for i, question in enumerate(random_questions, 1):
        print(f"Question {i}: {question['question']}")
        print("\n".join(question['choices']))
        print()
        user_answer = input('Enter your answer (A,B,C or D): ').strip().upper()

        if user_answer == question['answer']:
            print('Correct!\nYou won a point!')
            score += 1
            time.sleep(0.5)
            print(f'Current score: {score}')
        else:
            print(f"Wrong! The correct answer was {question['answer']}.\n")
    print(f"Quiz completed! Your total score is {score} out of 5.")

while True:
    run_quiz()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break