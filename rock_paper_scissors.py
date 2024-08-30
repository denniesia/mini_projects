import random

def play():
    #List containing the choices
    choices = ['rock', 'paper', 'scissors']

    #keep runing till the user doesnt want to play again
    while True:
        print("\nRock, Paper, Scissors")
        print("Enter your choice:")
        player_choice = input().lower()

        if player_choice not in choices:
            print('Invalid choice! Please choose again.')
            continue

        #Use random pick for the computer
        computer_choice = random.choice(choices)
        print(f"\nYou: {player_choice}.")
        print(f"\nComputer: {computer_choice}.\n")

        #print the winner
        print(winner(player_choice,computer_choice))

        play_again = input('Do you want to play again? (y/n):').lower()

        if play_again != 'y':
            print('Thanks for playing!\n')
            break

    #function to determine the winner
def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'Its a tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors'
            or user_choice == 'paper' and computer_choice == 'rock'
            or user_choice == 'scissors' and computer_choice == 'paper'):
        return 'You win!!!'
    else:
        return 'Computer win!'

if __name__ == "__main__":
    play()