import sqlite3
from expense import Expense

def cursor():
    return sqlite3.connect('expenses.db').cursor()

c = cursor()
c.execute('CREATE TABLE IF NOT EXISTS expenses (title TEXT, cost INTEGER)')
c.connection.close()

def add_expense(expense):
    c = cursor()

    with c.connection:
        c.execute('INSERT INTO expenses VALUES(?, ?)', (expense.title, expense.cost))
        #c.connection.close()
    
    return c.lastrowid


def get_expenses():
    c = cursor()
    expenses = []

    with c.connection:

        for expense in c.execute('SELECT * FROM expenses'):
            expenses.append(Expense(expense[0], expense[1]))
    c.connection.close()
    return expenses


def get_expense_by_title(title):
    c = cursor()
    with c.connection:
        c.execute('SELECT * FROM expenses WHERE title=?',  (title, ))
    data =  c.fetchone()
    c.connection.close()
    if not data:
        return None

    return Expense(data[0], data[1])

def update_expense(expense, new_title, new_cost):
    c = cursor()
    with c.connection: #don't forget this part.
        c.execute('UPDATE expenses SET title=?, cost=? WHERE title=? AND cost=?', 
        (new_title, new_cost, expense.title, expense.cost))
    expense = get_expense_by_title(expense.title) #after commit
    c.connection.close()
    return expense


def delete_expense(expense):
    c = cursor()
    with c.connection:
        c.execute('DELETE FROM expenses WHERE title=? AND cost=?', (expense.title, expense.cost))
        rows = c.rowcount
        #c.connection.close()
    return rows

