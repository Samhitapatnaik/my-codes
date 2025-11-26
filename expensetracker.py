import sqlite3
connection=sqlite3.connect('expense.db')
cursor=connection.cursor()
command1=""" create table if not exists expense(
  amount real,
  category text,
  month text
)"""
cursor.execute(command1)
connection.commit()
print("EXPENSIVE TRACKER ")

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    month = input("Enter month: ")
    cursor.execute("Insert into expense (amount , category , month) values (? , ? ,?)", (amount, category, month))
    connection.commit()

def view_expenses():
      wanted=input("Enter Expense's month/category ")
      cursor.execute("select * from expense where month=? or category=? " , (wanted,wanted))
      rows=cursor.fetchall()
      if rows:
          for r in rows:
            print(r)
      else:
            print("no expense found")
          
def total_spent():
    cursor.execute("select amount from expense ")
    rows=cursor.fetchall()
    total=0
    for r in rows:
        total+=r
    print(" Total expensive " , total)    

# Main program loop
while True:
    print("\n*****MENU CARD*****")
    print("1) ADD EXPENSE")
    print(
"2) VIEW EXPENSES")
    print("3) TOTAL SPENT")
    print("4) EXIT")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice==3:
        total_spent()
    elif choice == 4:
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 4.")