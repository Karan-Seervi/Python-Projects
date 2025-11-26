import random

german_words = [
    {"german": "Hallo", "english": ["Hello"]},
    {"german": "Guten Morgen", "english": ["Good Morning"]},
    {"german": "Bitte", "english": ["Please"]},
    {"german": "Danke", "english": ["Thank You"]},
    {"german": "Entschuldigung", "english": ["Sorry", "Excuse Me"]},
    {"german": "Ja", "english": ["Yes"]},
    {"german": "Nein", "english": ["No"]},
    {"german": "Vielleicht", "english": ["Maybe"]},
    {"german": "Ich", "english": ["I"]},
    {"german": "Du", "english": ["You"]},
    {"german": "Er", "english": ["He"]},
    {"german": "Sie", "english": ["She", "They", "You (formal)"]},
    {"german": "Wir", "english": ["We"]},
    {"german": "Hier", "english": ["Here"]},
    {"german": "Dort", "english": ["There"]},
    {"german": "Heute", "english": ["Today"]},
    {"german": "Morgen", "english": ["Tomorrow"]},
    {"german": "Gestern", "english": ["Yesterday"]},
    {"german": "Tag", "english": ["Day"]},
    {"german": "Nacht", "english": ["Night"]},
    {"german": "Freund", "english": ["Friend"]},
    {"german": "Familie", "english": ["Family"]},
    {"german": "Haus", "english": ["House"]},
    {"german": "Auto", "english": ["Car"]},
    {"german": "Schule", "english": ["School"]},
    {"german": "Arbeit", "english": ["Work"]},
    {"german": "Stadt", "english": ["City"]},
    {"german": "Land", "english": ["Country"]},
    {"german": "Wasser", "english": ["Water"]},
    {"german": "Essen", "english": ["Food"]},
    {"german": "Trinken", "english": ["Drink"]},
    {"german": "Hund", "english": ["Dog"]},
    {"german": "Katze", "english": ["Cat"]},
    {"german": "Buch", "english": ["Book"]},
    {"german": "Film", "english": ["Movie"]},
    {"german": "Musik", "english": ["Music"]},
    {"german": "Spiel", "english": ["Game"]},
    {"german": "Sport", "english": ["Sport"]},
    {"german": "Reise", "english": ["Travel"]},
    {"german": "Straße", "english": ["Street"]},
    {"german": "Zimmer", "english": ["Room"]},
    {"german": "Fenster", "english": ["Window"]},
    {"german": "Tür", "english": ["Door"]},
    {"german": "Schön", "english": ["Beautiful"]},
    {"german": "Klein", "english": ["Small"]},
    {"german": "Groß", "english": ["Big"]},
    {"german": "Alt", "english": ["Old"]},
    {"german": "Neu", "english": ["New"]},
    {"german": "Gut", "english": ["Good"]},
    {"german": "Schlecht", "english": ["Bad"]}
]

def run_quiz(german_words):
    random.shuffle(german_words)
    score = 0
    wrong = 0

    for word in german_words:
        guess = input(f"What is the english translation for {word['german']}? ").lower()
        correct_word = word['english']
        
        for word in word['english']:
            word = word.lower()
                                    
        if guess in word['english']:
            print(f"Woo! You guessed the answer right!")
            score += 1
        else:
            
            print(f"Your guess is wrong! Translation of {word['german']} is {word['english'] if len(word['english']) == 1 else ', '.join(word['english'])}")
            wrong += 1
    print(f"Your total score is {score}!")
    print(f"You guessed {wrong} wrong answers!")

def main(german_words):
    while True:
        print("Welcome to the quiz where you are going to get some foreign language words and you have to give english translation of it!")
        choice = input("Do you want to play (y/n)? ")
        if choice.lower() == 'n':
            break
        elif choice.lower() == 'y':
            run_quiz(german_words)
        else:
            print("Invalid input! Try again!")

if __name__ == '__main__':
    main(german_words)
