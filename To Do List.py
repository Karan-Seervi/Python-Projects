def get_user_choice() -> int:
    features = ['Add a task', 'Remove a task', 'Show my tasks' ,'Exit']
    while True:
        print("\nWelcome to the To Do List App :)")
        print("--------------------")
        for i, feature in enumerate(features, start = 1):
            print(f"{i}. {feature}")
            
        choice = input("What do you wish to do (1-4)? ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 4:
                break
            else:
                print("Please select from (1-4).")
        else:
            print('Invalid input! Try again!')

    return choice

def add_task(tasks: list[str]) -> None:
    task = input("Enter the task you wish to add for today: ")
    if task in tasks:
        print("Your mentioned task is already in your To Do List.")
    else:
        tasks.append(task)
        print(f"Your task '{task}' has been added to your To Do List.")
        
def show_tasks(tasks: list[str]) -> None:
    if tasks:
        print("Your tasks are:")
        for i, task in enumerate(tasks, start = 1):
            print(f"{i}. {task}")
    else:
        print("Your To Do List is empty.")
        
def remove_task(tasks: list[str]) -> None:
    if not tasks:
        print("Your To Do List is empty.")
        return 
        
    show_tasks(tasks)
    no_of_tasks = len(tasks)
    
    while True:
        task = input(f"Enter the task number you want to remove from your To Do List (1-{no_of_tasks}): ")
        if task.isdigit():
            task = int(task)
            if 0 < task <= no_of_tasks:
                actual_task = tasks[task - 1]
                tasks.pop(task - 1)
                print(f"Your task of '{actual_task}' has been removed from To Do List.")
                break
            else:
                print("Please select from above mentioned numbers.")
        else:
            print("Invalid input! Try again!")
                
def main():
    tasks = []
    
    while True:
        choice = get_user_choice()
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            remove_task(tasks)
        elif choice == 3:
            show_tasks(tasks)
        elif choice == 4:
            print("Thank you for using To Do List App!")
            break
        
if __name__ == '__main__':
    main()        
    