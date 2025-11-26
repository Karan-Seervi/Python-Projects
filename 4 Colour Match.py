import random

COLOURS = ['R', 'O', 'G', 'Y', 'B', 'W']
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []
    for _ in range(CODE_LENGTH):
        colour = random.choice(COLOURS)
        code.append(colour)
        
    return code

def user_guess_code():
    while True:
        guess = input("Enter your guess (X X X X): ").upper().split(' ')
        if len(guess) != CODE_LENGTH:
            print(f"You must enter {CODE_LENGTH} colours!")
            continue
        
        for colour in guess:
            if colour not in COLOURS:
                print(f"Invalid guess: {colour}! Please enter from {COLOURS}.")
                break
        else:
            break
               
    return guess

def check_code(guess_code, real_code):
    real_code_copy = real_code[:]
    correct_pos = 0
    incorrect_pos = 0
    
    for i, (guess_colour, real_colour) in enumerate(zip(guess_code, real_code)):
        if guess_colour == real_colour:
            correct_pos += 1
            real_code_copy[i] = None
            
    for i, colour in enumerate(guess_code):
        if colour in real_code_copy:
            if colour != real_code[i]:
                incorrect_pos += 1
                real_code_copy[real_code_copy.index(colour)] = None
    return correct_pos, incorrect_pos

def game():
    real_code = generate_code()
            
    for attempts in range(1, TRIES + 1):
        guess_code = user_guess_code()
        correct_pos, incorrect_pos = check_code(guess_code, real_code)
            
        if correct_pos == CODE_LENGTH:
            print(f"Congratulations, You guessed the correct code in {attempts} tries!")
            break
                
        print(f"Correct position : {correct_pos} | Correct colour in incorrect position : {incorrect_pos}")
        print(f"You got {TRIES - 1} tries left to guess!")
    else:
        print("You ran out of tries. The correct code is: ", *real_code)

def play_game():
    print(f"Welcome to mastermind! You have {TRIES} tries to guess the code...")
    print("Valid colours are:", *COLOURS)
    while True:
        choice = input("Do you want to play (y/n)? ").lower()
        if choice == 'n':
            print("Thank you for playing!")
            break
        elif choice == 'y': 
            game()
        else:
            print("Invalid input! Try again!")  
            
if __name__ == '__main__':
    play_game()      
        
       
        
        
    