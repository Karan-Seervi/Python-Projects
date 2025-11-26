import random

def roll():
    min_val=1
    max_val=6
    roll=random.randint(min_val,max_val)
    return roll

players=input("Enter the number of players(2-4): ")
while True:
    if players.isdigit():
        players=int(players)
        if 2<= players <=4:
            break
        else:
            print("The number of players should be between 2 and 4!")
    else:
        print("Invalid input! Try again!")

max_score=50
player_scores=[0 for _ in range(players)]

while max(player_scores)<=max_score:
    for player in range(players):
        print(f"\nPlayer {player+1}'s chance starts now")
        print("Total score is :",player_scores[player],'\n')
        current_score=0

        while True:
            choice=input("Do you want to roll your dice(y,n)? ")
            if choice.lower()=='n':
                break
            elif choice.lower()=='y':
                value=roll()
                if value==1:
                    current_score=0
                    print("Oops! Your roll was 1. Turn's over!")
                    break
                else:
                    current_score+=value
                    print("Your roll was: ",value)
                print("Total score: ",current_score)
            else:
                print("Invalid input! Try again!")
        player_scores[player]+=current_score
        print("Total score after this chance: ",player_scores[player])

winning_score=max(player_scores)
winner_idx=player_scores.index(winning_score)
print(f"\nPlayer {winner_idx+1} is the winner! Score of player {winner_idx+1}: {winning_score}")
        
