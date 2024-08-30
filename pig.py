# A multiplayer game where players roll dice and accumulate scores.
# Each player decides if they want to continue rolling. If the player gets 1 the turn is done and the score is 0. The game continues untill one player gains max points.
import random

def roll(): #to roll the dice; possible numbers = 1 to 6
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value) # returns an integer number selected element from the specified range
    return roll

while True: #check if the players number is valid
    players = input('Enter the number of players (2-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            print("Great! Let's play." )
            break
        else:
            print('The number of players must be between 2 and 4 players! Please try again.')
    else:
        print('Invalid input! Please try again.')

max_score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:

    for player_idx in range(players):
        print(f"\nPlayer number {player_idx+1} turn has just started!\n")
        print(f"Your total score is {players_scores[player_idx]}\n")
        current_score = 0

        while True:
            should_roll = input(f"\nWould you like to roll (y/n)?")
            if should_roll.lower() != 'y':
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}")

            print(f"Your score is {current_score}")
        players_scores[player_idx] += current_score
        print(f"Your total score is: {players_scores[player_idx]}")

max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print(f"Player number {winning_idx+1} is the winner with the score of {max_score}.")
