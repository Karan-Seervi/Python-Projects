import random

min_val=1
max_val=6

while True:
    dice_no=input("Enter the number of dices you want to play with(1-4): ")
    if dice_no.isdigit():
        dice_no=int(dice_no)
        if 1<=dice_no<=4:
            break
        else:
            print("Please choose the number between 1 and 4!")
    else:
        print("Invalid input!")

def roll():
    dice_roll=()
    for i in range(dice_no):
        dice=random.randint(min_val,max_val)
        dice_roll+=(dice,)
    return dice_roll   
        
print("Welcome to the Dice Rolling Game!")
name=input("Please enter your name: ")

count=0
while True:
    choice=input("Do you want to roll the dice(y,n): ")
    if choice.lower()=='y':
        die_roll=roll()
        print(f"You rolled {die_roll}")
        count+=1
    elif choice.lower()=='n':
        print(f"Thank you for playing, {name}! You rolled the dice {count} times.")        
        break
    else:
        print("Invalid input! Try again!")