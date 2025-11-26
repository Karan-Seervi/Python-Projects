import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = MAX_LINES
COLS = 3

symbols_count = {
    'A' : 2,
    'B' : 3,
    'C' : 4,
    'D' : 6,
}

symbols_value = {
    'A' : 7,
    'B' : 6,
    'C' : 5,
    'D' : 4
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += bet * values[symbol]
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
           
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns, start = 1):
            if i != len(columns):
                print(column[row], end = ' | ')
            else:
                print(column[row])

def get_deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.replace('.', '', 1).isdigit():
            amount = float(amount)
            if amount > 0:
                return amount
            else:
                print("Enter a number greater than 0.")
        else:
            print("Please enter a valid number!")
            
def get_lines():
    while True:
        lines = input(f"For how many lines you want to put your bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Please enter a valid number of lines!")
        else:
            print("Please enter a valid number!")
     
def get_bet():
    while True:
        amount = input("Enter the amount you want to bet? $")
        if amount.replace('.', '', 1).isdigit():
            amount = float(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Please enter an amount between (${MIN_BET:.2f} - ${MAX_BET:.2f})!")
        else:
            print("Please enter a valid number!")
            
def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            break
        else:
            print(f"You do not have enought money to bet on. Your current balance is ${balance:.2f}")
            
    print(f"You are betting ${bet:.2f} on {lines} lines. Your total bet is ${total_bet:.2f}.")
            
    columns = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(columns)
                
    winnings, winning_lines = check_winnings(columns, lines, bet, symbols_value)
    print(f"You won ${winnings:.2f}!")
    print("You won on lines: ", 0 if not winning_lines else ', '.join(map(str, winning_lines)))
                    
    return winnings - total_bet
    
def main():
    total_deposits = []
    balance = get_deposit()
    total_deposits.append(balance)

    while True:
        choice = input("\nPress enter to play (q to quit): ").lower()
        if choice == 'q':  
            print("Thank you for playing!")           
            print(f"You deposited {len(total_deposits)} times with a total of: ${sum(total_deposits):.2f}.")
            print(f"You are returning with the amount: ${balance:.2f}")
            break
        else:            
            balance += spin(balance)
            print(f"Your current balance after spin is ${balance:.2f}")
            
            if balance <= 0:
                print("\nOops! You ran out of money.")
                
                wish = input("Do you wish to continue by depositing more money (n to quit)? ").lower()
                if wish == 'n':
                    print("Thank you for playing!")           
                    print(f"You deposited {len(total_deposits)} times with a total of: ${sum(total_deposits):.2f}.")
                    print("You are returning with no money!")                        
                    break
                else:
                    balance = get_deposit()
                    total_deposits.append(balance)
                
if __name__ == '__main__':
    main()

    