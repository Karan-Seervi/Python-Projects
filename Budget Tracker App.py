import json
from datetime import date, datetime
import os

def add_expenses(expenses, description, amount, date_of_expense):
    expenses.append({'description' : description, 'amount' : amount, 'date_of_expense' : date_of_expense })
    print(f"Added expense : {description} Amount : ${amount} Date of expense(yyyy-mm-dd) : {date_of_expense}")
    
def get_total_spent(expenses):
    total = 0
    for expense in expenses:
        total += expense['amount']
    return total

def get_remaining_budget(budget, expenses):
    return budget - get_total_spent(expenses)
    
def show_budget_details(budget, expenses):
    print("\nYour budget details:")
    print(f"Total budget: ${budget}")
    print("Total expenses:")
    for expense in expenses:
        print(f"--> {expense['description']} ${expense['amount']} {expense['date_of_expense']}")
    print("Total spent: $",get_total_spent(expenses))
    print("Remaining budget: $",get_remaining_budget(budget, expenses))
        
def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []
    else:
        return data['initial_budget'], data['expenses']
    
def save_budget_data(filepath, budget, expenses):
    data = {
        'initial_budget' : budget,
        'expenses' : expenses
        }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
        
def delete_data_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)
        print("\nYour data has been deleted along with the file.")
    else:
        print("\nYour file doesn't exist to delete it.")
        
def choose_what_to_do(budget, expenses, filepath):
    while True:
        what_to_do = ['Add an expense', 'Show budget details', 'Delete data', 'Exit']
        print("\nWhat do you want to do?")
        for i, whats in enumerate(what_to_do):
            print(f"{i+1} {whats}")
        
        choice = input("Enter your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                description = input("Enter the description of your expense: ")
                
                while True:
                    amount = input(f"Enter the amount you spent on {description}: ")
                    if amount.replace('.', '', 1).isdigit():
                        amount = float(amount)
                        break
                    else:
                        print("Invalid input!")
                
                while True:
                    choose_date = input("Is the expenditure of today (y,n)? ").lower()
                    if choose_date == 'y': 
                        date_of_expense = str(date.today())
                        break
                    elif choose_date == 'n':
                        while True:
                            date_of_expense = input("Please enter the date of purchase in (yyyy-mm-dd): ")
                            try:
                                datetime.strptime(date_of_expense,'%Y-%m-%d')
                                break
                            except ValueError:
                                print("Invalid date format! Try again!")
                        break
                    else:
                        print("Invalid input! Try again!")
                
                add_expenses(expenses, description, amount, date_of_expense)  
                
            elif choice == 2:
                show_budget_details(budget, expenses)
                
            elif choice == 3:
                delete_data_file(filepath)
                break
            
            elif choice == 4:
                save_budget_data(filepath, budget, expenses)
                print("\nThank you for using Budget Tracker App!")
                break
                
        else:
            print("Invalid input! Try again!")

def main():
    print("Welcome to Budget Tracker App!")
    filepath = "C:\\Users\\karan\\OneDrive\\Desktop\\Python Projects\\Budget Tracker\\budget_data.json"
    initial_budget, expenses = load_budget_data(filepath)
    if initial_budget == 0:
        while True:
            initial_budget = input("Enter your initial budget: ")
            if initial_budget.replace('.','', 1).isdigit():
                initial_budget = float(initial_budget)
                break
    budget = initial_budget
    
    choose_what_to_do(budget, expenses, filepath)
            
if __name__ == '__main__':
    main()
                
                
                      
                    