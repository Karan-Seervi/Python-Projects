import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
from datetime import datetime
import os

FORMAT = '%d-%m-%Y'
CATEGORIES = {"I" : "Income", "E" : "Expense"}

def get_date(prompt, allow_default = False):
    date_str = input(prompt).lower()
    if allow_default and date_str == 'y':
        return datetime.today().strftime(format = FORMAT)
    
    try:
        valid_date = datetime.strptime(date_str, FORMAT)
        return valid_date.strftime(FORMAT)
    except ValueError:
        print("Please enter your date in (dd-mm-yyyy) format!")
        return get_date(prompt, allow_default)

def get_amount():
    amount = input("Enter the amount: ")
    if amount.replace('.', '', 1).isdigit():
        amount = float(amount)
        if amount > 0:
            return amount
        else:
            print("Amount entered should be a positive value.")
            return get_amount()
    else:
        return get_amount()
    
def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    else:
        print("Please enter the above category: ('I' for Income or 'E' for Expense).")
        return get_category()
    
def get_description():
    description = input("Enter the desciption (optional): ")
    return description                    

class CSV:
    CSV_FILE = "C:\\Users\\karan\\OneDrive\\Desktop\\Python Projects\\Personal Finance Tracker\\finance_tracker.csv"
    COLUMNS = ['Date', 'Amount', 'Category', 'Description']
    
    @classmethod
    def csv_initialization(cls):
        try:
            finance_df = pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            finance_df = pd.DataFrame(columns = cls.COLUMNS)
            finance_df.to_csv(cls.CSV_FILE, index = False)
            
    @classmethod
    def get_dates(cls):
        finance_df = pd.read_csv(cls.CSV_FILE)
        finance_df['Date'] = pd.to_datetime(finance_df['Date'], format = FORMAT)
        updated_finance_df = finance_df.sort_values('Date').copy()
        updated_finance_df = updated_finance_df.set_index('Date')
        start_date = datetime.strftime(updated_finance_df.index[0], format = FORMAT)
        end_date = datetime.strftime(updated_finance_df.index[-1], format = FORMAT)
        return start_date, end_date
    
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            'Date' : date,
            'Amount' : amount,
            'Category' : category,
            'Description' : description
        }    
    
        with open(cls.CSV_FILE, mode = 'a', newline = '') as file:
            writer = csv.DictWriter(file, fieldnames = cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully!")
        
    @classmethod
    def get_transactions(cls, start_date, end_date):
        finance_df = pd.read_csv(cls.CSV_FILE)
        finance_df['Date'] = pd.to_datetime(finance_df['Date'], format = FORMAT)
        start_date = datetime.strptime(start_date, FORMAT)
        end_date = datetime.strptime(end_date, FORMAT)
        
        mark = (finance_df['Date'] >= start_date) & (finance_df['Date'] <= end_date)
        filtered_finance_df = finance_df.loc[mark].copy()
        filtered_finance_df = filtered_finance_df.sort_values(by = ['Date'])
        
        if filtered_finance_df.empty:
            print(f"No Transactions have been done between {start_date.strftime(format = FORMAT)} - {end_date.strftime(format = FORMAT)}.")
        else:
            print(f"\nTransactions from {start_date.strftime(format = FORMAT)} to {end_date.strftime(format = FORMAT)}:")   
            print(filtered_finance_df.to_string(index = False, formatters = {'Date' : lambda x : x.strftime(format = FORMAT)}))
            print('\nTransation Summary:')
            total_income = filtered_finance_df[filtered_finance_df['Category'] == 'Income']['Amount'].sum()
            total_expense = filtered_finance_df[filtered_finance_df['Category'] == 'Expense']['Amount'].sum()
            print(f"Total Income earned: ${total_income:.2f}")
            print(f"Total Expense spent: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income - total_expense):.2f}\n")
            
        return filtered_finance_df
            
def add_data():
    CSV.csv_initialization()
    date = get_date(
        "Enter the date of transaction in dd-mm-yyyy format and enter ('y') if it's today's date: ", allow_default = True
        )
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)
    
def get_plot(filtered_finance_df):
    plot_df = filtered_finance_df.set_index('Date').copy()
    income_df = plot_df[plot_df['Category'] == 'Income'].resample('D').sum().reindex(plot_df.index, fill_value = 0)
    expense_df = plot_df[plot_df['Category'] == 'Expense'].resample('D').sum().reindex(plot_df.index, fill_value = 0)
    
    plt.figure(figsize = (10,5))
    sns.lineplot(x = income_df.index, y = income_df['Amount'], color = 'blue', marker = 'o', linewidth = 2, label = 'Income')
    sns.lineplot(x = expense_df.index, y = expense_df['Amount'], color = 'red', marker = 'D', linewidth = 2, label = 'Expense')
    plt.title("Income & Expense Plot", fontsize = 14)
    plt.xlabel('Date', fontsize = 12)
    plt.ylabel('Amount', fontsize = 12)
    plt.grid()
    plt.legend()
    plt.show()
    
def delete_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)
        print("\nYour data along with file has been deleted!")
    else:
        print("\nThere exists no file to delete your data")
        
def get_choice():
    options = ['Add a new transaction', 'View summary of transaction between a time range along with plot', 'Delete your data permanently', 'Exit']
    while True:   
        print("Welcome to Personal Finance Tracker!")
        print("\nMenu:")
        for i, option in enumerate(options, start = 1):
            print(f"{i}. {option}")
            
        choice = input(f"Please enter your choice (1-{len(options)}): ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice) 
        else:
            print(f"Please enter a number between 1 and {len(options)}.")
            return get_choice()
        
def main():
    while True:
        choice = get_choice()
        
        if choice == 1:
            add_data()
            
        elif choice == 2:
            while True:
                choose = input("Do you want a summary of all dates (y) or to get summary of specified dates (n)? ").lower()
                if choose == 'y':
                    start_date, end_date = CSV.get_dates()
                    break
                elif choose == 'n':
                    start_date = get_date("Enter the start date (dd-mm-yyyy): ")
                    end_date = get_date("Enter the end date (dd-mm-yyyy): ")
                    break
                else:
                    print("Please enter 'y' or 'n'.")
            
            filtered_finance_df = CSV.get_transactions(start_date, end_date)
            
            while True:
                plot = input("Do you want to see the plot of the current summary (y/n): ").lower()
                if plot == 'y':
                    get_plot(filtered_finance_df)
                    break
                elif plot == 'n':
                    break
                else:
                    print("Please enter 'y' or 'n'!")
        
        elif choice == 3:
            delete_file(CSV.CSV_FILE)
            
        elif choice == 4:
            print("Thank you for using Personal Finance Tracker!")
            break
        
if __name__ == '__main__':
    main()