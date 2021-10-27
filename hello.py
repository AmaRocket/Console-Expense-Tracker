from os import name
from expense import Expense
import expensesSDK


def print_menu():
    print(""" 
    Choose an option
    1. Print all expenses
    2. Add  expense
    3. Update expense
    4. Delete expense
    """)

while True:
    print_menu()
    response = int(input())
    if response == 1:
        print("""Printing all expenses: 
        """)
        for expense in expensesSDK.get_expenses():
            print(expense)

    elif response == 2:
        print("""Add expense: 
        """)
        title = input("What is the cost item? : ")
        cost = (input("How much did it cost? : "))
        expense = Expense(title, cost)
        expensesSDK.add_expense(expense)
        
    elif response == 3:
        print("""Update expense: 
        """)
        current_title = input("What is the current cost item? : ")
        current_cost = (input("How much does it cost now? : "))
        new_title = input("New item(s for same): ")
        if str.lower(new_title) == 's':
            new_title = current_title
        new_cost = (input("New cost(s for same): "))
        if str.lower(new_cost) == 's':
            new_cost = current_cost
        expensesSDK.update_expense(Expense(current_title, current_cost), new_title, new_cost)
    
    elif response == 4:
        print("""Delete expense: 
        """)
        title = input("What is the cost item? : ")
        cost = int(input("How much did it cost? : "))
        expensesSDK.delete_expense(Expense(title, cost))

    else:
        print("""Thnx for using this app :)
        """)
        break