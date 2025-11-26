import time
import random

questions = [
    {
     "prompt" : "What is the capital of France?",
     "options" : ["A. Paris", "B. Berlin", "C. London", "D. Madrid"],
     "answer" : "A"
     },
    {
     "prompt" : "Who is the founder of Facebook?",
     "options" : ["A. Jeff Bezos", "B. Elon Musk", "C. Mark Zuckerberg", "D. Steve Jobs"],
     "answer" : "C"
     },
    {
     "prompt" : "What is the smallest prime number?",
     "options" : ["A. 1", "B. 2", "C. 3", "D. 4"],
     "answer" : "B"
     },
    {
     "prompt" : "What is the most spoken language in the world?",
     "options" : ["A. English", "B. Spanish", "C. Latin", "D. Mandarin"],
     "answer" : "D"
     },
]

no_of_questions = len(questions)

def display_questions(question):
    print(question['prompt'])
    for option in question['options']:
        print(option)
        
def run_quiz(questions):
    print("Welcome to the quiz!")
    print(f"You have {no_of_questions} questions to answer with a timer recording you.")
    start_game = input("Press key to start the quiz: ")
    print("\n--------------------")
    start_time = time.time()
    
    random.shuffle(questions)
    
    score = 0
    wrong = 0
    choices = ('A', 'B', 'C', 'D')
    
    for question in questions:
        display_questions(question)
        while True:
            
            guess = input("Enter your guess (A,B,C or D) : ").upper()
            
            if guess in choices:
                if guess == question['answer']:
                    score+=1
                    print("Hooray! You got the right answer!\n")
                    break
                else:
                    wrong += 1
                    print("Oops! You answered wrong. The correct answer is: ",question['answer'],'\n')
                    break
            else:
                print("Invalid guess! Please guess (A,B,C or D)!")           
            
    print('--------------------')
    end_time = time.time()
    total_time = end_time - start_time
    avg_time = total_time / no_of_questions
    
    print(f"\nYou finished the quiz in {total_time:.2f} seconds!")
    print(f"Your score is {score} and you got {wrong} wrong answers.")
    print(f"You took average of {avg_time:.2f} seconds for each question.")
    print("Thank you for playing!")
    
run_quiz(questions)
       
        
       
            
            
                                                                                       
                
