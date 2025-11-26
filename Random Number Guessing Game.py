import random

min_val=1
max_val=100

print("Welcome to the Random Number Guessing Game!")
print("You have to guess a number between 1-100.")

while True:
    play_choice=input("\nDo you want to play(y/n)? ")
    if play_choice.lower()=='y':
        rand_no=random.randint(min_val,max_val)
        count=0
        while True:
            try:
                guess=int(input("Enter your guess: "))
                count+=1
            except ValueError:
                print("Invalid input! Try again!")
            else:
                if guess<rand_no:
                    print("Too low!")                    
                elif guess>rand_no:
                    print("Too high!")
                else:
                    print(f"Hooray! You guessed the number right in {count} turns!")
                    break
    elif play_choice.lower()=='n':
        print("Thank you playing!")
        break
    else:
        print("Invalid input! Try again!")