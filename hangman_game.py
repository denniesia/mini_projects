import random
import time

choice_of_words = [
    "benevolent", "eloquent", "candid", "meticulous", "resilient",
    "pragmatic", "enthusiastic", "diligent", "vivid", "charismatic"
]

chosen_word = random.choice(choice_of_words)
word_display = ["_" for _ in range(len(chosen_word))]
wrong_letters = 0


print("Welcome to the game!")
print("You can have only 4 mistakes. Be careful!")
time.sleep(0.5)
while True:
    answer = input("Are you ready to start (y/n)? ")
    if answer == "y":
        break
time.sleep(0.5)

while wrong_letters != 4 and '_' in word_display:

    print("\nThis is your word. Try to guess it.\n")
    print("".join(word_display))
    guess = input('Guess a letter: ').lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print('That letter does not appear in the word! Try again.')
        time.sleep(0.5)
        wrong_letters += 1
        print(f"\nLeft mistakes: {4-wrong_letters}\n")
    if wrong_letters == 4:
        break

if '_' not in word_display:
    print("You guessed the word!")
    print(''.join(word_display))
else:
    print('You lost!')
    print(f"The word was: {chosen_word}")


