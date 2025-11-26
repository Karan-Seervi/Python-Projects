import random
import time

Operators=None
Min_val=None
Max_val=None

print("Difficulty Levels:")
print("1. Easy")
print("2. Moderate")
print("3. Hard")
while True:
    difficulty=input("Enter Difficulty Level(1-3): ")
    if difficulty.isdigit():
        difficulty=int(difficulty)
        if difficulty==1:
            Operators=['+','-']
            Min_val=2
            Max_val=15
            break
        elif difficulty==2:
            Operators=['+','-','*']
            Min_val=5
            Max_val=20
            break
        elif difficulty==3:
            Operators=['+','-','*']
            Min_val=7
            Max_val=25
            break
        else:
            print("Please enter a number between 1 and 3")
    else:
        print("Invalid input! Try again!")
        
while True:
    Total_problems = input("Enter the number of problems to solve(5-30): ")
    if Total_problems.isdigit():
        Total_problems = int(Total_problems)
        if 5 <= Total_problems <= 30:
            break
        else:
            print("Please choose a number between 5 and 30.")
    else:
        print("Invalid input! Try again!")
        


def generate_problems():
    left = random.randint(Min_val,Max_val)
    right = random.randint(Min_val,Max_val)
    operator = random.choice(Operators)
    expr = str(left)+ ' ' + operator + ' ' +str(right)
    answer = eval(expr)
    return expr,answer

wrong=0
start=input("Press enter to start: ")
print("--------------------")
start_time=time.time()

for i in range(Total_problems):
    expr,answer=generate_problems()
    while True:
        guess=input(f"Problem {i+1}: {expr} = ")
        if guess==str(answer):
            break
        else:
            wrong+=1

end_time=time.time()
total_time=end_time-start_time
print("--------------------")

print(f"\nWooow! You have finished your problems in difficulty level {difficulty} in {total_time:.2f} seconds.")
print(f"You got {wrong} wrong answers.")
avg_time=total_time/Total_problems
print(f"It took average of {avg_time:.2f} seconds to solve one problem. ")    

