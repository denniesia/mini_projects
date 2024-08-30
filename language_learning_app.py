#Learning app, asking for the translation of 10 random words
import random

words = [
    {"spanish": "el", "english": ["the"]},
    {"spanish": "de", "english": ["of", "from"]},
    {"spanish": "que", "english": ["that", "which"]},
    {"spanish": "y", "english": ["and"]},
    {"spanish": "a", "english": ["to", "at"]},
    {"spanish": "en", "english": ["in", "on"]},
    {"spanish": "un", "english": ["a", "an"]},
    {"spanish": "ser", "english": ["to be"]},
    {"spanish": "se", "english": ["oneself", "itself"]},
    {"spanish": "no", "english": ["no","not"]},
    {"spanish": "haber", "english": ["to have"]},
    {"spanish": "por", "english": ["for","by"]},
    {"spanish": "con", "english": ["with"]},
    {"spanish": "su", "english": ["his","her","your","their"]},
    {"spanish": "para", "english": ["for","to"]},
    {"spanish": "como", "english": ["like","as"]},
    {"spanish": "estar", "english": ["to be"]},
    {"spanish": "tener", "english": ["to have"]},
    {"spanish": "le", "english": ["him", "her", "you"]},
    {"spanish": "lo", "english": ["it", "him","you"]}
]


def quiz_user(words):
    selected_words = random.sample(words,10)
    score = 0

    for word in selected_words:
        print(f"What is the English translation of {word['spanish']}?")
        user_answer = input("Your answer: ").strip().lower()
        correct = False

        for answer in word['english']:
            if user_answer == answer.lower():
                correct = True
                break

        if correct:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{', '.join(word['english'])}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(selected_words)}")


def main():
    print('Welcome to the language App!')
    print("Here we learn Spanish.")
    print("Please press enter to start the quiz.")
    quiz_user(words)

if __name__ == "__main__":
    main()