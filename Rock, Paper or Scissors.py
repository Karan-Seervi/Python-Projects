import random

ROCK='r'
PAPER='p'
SCISSORS='s'

emojis = {ROCK:'✊',PAPER:'✋',SCISSORS:'✌️'}
choices=tuple(emojis.keys())
print("Welcome to the game of Rock, Paper or Scissors!")
        
def get_user_choice():
    while True:
        user_choice = input('Rock, Paper or Scissors (r,p,s): ')
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice! Try again!")
        
def display_choices(user_choice,comp_choice):
    print(f"Your choice is: {emojis[user_choice]}")
    print(f"Computer choice is: {emojis[comp_choice]}")
    
def determine_winner(user_choice,comp_choice):
    if user_choice == comp_choice:
        print("Tie game!")
    elif (
            (user_choice == ROCK and comp_choice == SCISSORS) or
            (user_choice == PAPER and comp_choice == ROCK) or
            (user_choice == SCISSORS and comp_choice == PAPER)
            ):
        print("You win! Computer loses!")
    else:
        print("Computer wins! You lose!")

def play_game():
    while True:
        play_game_or_not = input("\nDo you want to play the game (y/n)? ")
        if play_game_or_not.lower() == 'n':
            print("Thanks for playing!")
            break
        elif play_game_or_not.lower() == 'y':
            user_choice = get_user_choice()
            
            comp_choice = random.choice(choices)
            
            display_choices(user_choice,comp_choice)
            
            determine_winner(user_choice, comp_choice)
        else:
            print("Invalid input! Try again!")
            
play_game()

            

    
    
