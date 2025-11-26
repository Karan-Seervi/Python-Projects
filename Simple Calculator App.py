print("Welcome to Simple Calculator App!")

def get_user_input():
    operators = ['+', '-', '*', '/']
    while True:
        choice = input("\nEnter the operator you want to operate with (+, -, *, /): ")
        if choice in operators:
            break
        else:
            print("Invalid input! Please use the operators mentioned above.")

    while True:
        num1 = input("Enter the first number: ")
        if num1.replace('-', '', 1).replace('.', '', 1).isdigit():
            num1 = float(num1)
            break
        else:
            print("Invalid number! Try again!")

    while True:
        num2 = input("Enter the second number: ")
        if num2.replace('-', '', 1).replace('.', '', 1).isdigit():
            num2 = float(num2)
            break
        else:
            print("Invalid number! Try again!")

    return choice, num1, num2

def operation(choice, num1, num2):
    if choice == '+':
        return round((num1 + num2), 4)
    if choice == '-':
        return round((num1 - num2), 4)
    if choice == '*':
        return round((num1 * num2), 4)
    if choice == '/':
        if num2 == 0:
            return "Sorry, you can't divide a number by 0"
        else:
            return round((num1 / num2), 4)
def main():
    
    choice, num1, num2 = get_user_input()

    result = operation(choice, num1, num2)
    if isinstance(result, float):
        print (f"\n{num1} {choice} {num2} = {result}")
    else:
        print("\nSorry, you can't divide a number by 0")

if __name__ == '__main__':
    main()
