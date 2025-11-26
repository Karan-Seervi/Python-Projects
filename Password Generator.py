import random
import string

def generate_password(min_length, numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special_chars
        
    meets_criteria = False
    has_number = False
    has_special = False
    
    pwd = ''
    while not meets_criteria or len(pwd) < min_length:
        random_char = random.choice(characters)
        pwd += random_char
        if random_char in digits:
            has_number = True
        elif random_char in special_chars:
            has_special = True
        
        meets_criteria = True    
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria  = meets_criteria and has_special
            
    return pwd

def get_user_inputs():
    while True:
        min_length = input("Enter the minimum length of your password (5-30 characters): ")
        if min_length.isdigit():
            min_length = int(min_length)
            if 5 <= min_length <= 30:
                break
            else:
                print("Your password should be between 5-30!")
                continue
        else:
            print("Invalid input! Please enter a number.")
            
    while True:
        want_number = input("Do you want to have number in your password (y/n)? ").lower()
        if want_number in ['y', 'n']:
            numbers = want_number == 'y'
            break
     
    while True:
        want_special = input("Do you want to have special characters in your pasword (y/n)? ").lower()
        if want_special in ['y', 'n']:
            special_characters = want_special == 'y'
            break
        
    return min_length, numbers, special_characters

def main():
    print("Welcome to password generator!") 
    
    min_length, numbers, special_characters = get_user_inputs()
    
    password = generate_password(min_length, numbers, special_characters)
     
    print("\nYour generated password is: ", password) 
    
if __name__ == '__main__':
    main()
        