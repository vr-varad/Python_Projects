import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


while (True):
    players = input('Enter the numbers of players (2-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('Must be between 2-4')
    else:
        print('Invalid Numeber Plaease try again')

max_score = 50
player_scores = [0 for _ in range(players)]
print(player_scores)

while max(player_scores) < max_score:
    for player_index in range(players):
        current_score = 0
        print(
            f'Player {player_index+1} turn started \n')
        print('Your Current Score is: ', current_score)
        while True:
            should_roll = input('Would you like to roll (y)?: ')
            if should_roll.lower() != 'y':
                break
            value = roll()
            if value == 1:
                print('You rolled a 1! Turns Dowm')
                current_score = 0
                break
            else:
                print("You rolled: ", value)
                current_score += value
                print(f"Your Score is {current_score}")
        player_scores[player_index] += current_score
        print(
            f"Your Total Score is : {player_scores[player_index]}\n")
max_score = max(player_scores)
winning_indx = player_scores.index(max_score)
print(f'Player {winning_indx+1} won with score {max_score}')
