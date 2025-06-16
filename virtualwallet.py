import json
import os

# Load and Save Helpers
def load_users():
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            return json.load(file)
    return {}

def save_users(users):
    with open("data.json", "w") as file:
        json.dump(users, file, indent=4)

# Registration
def register_user():
    users = load_users()
    phone = input(" Enter phone number: ")
    if phone in users:
        print(" User already exists.")
        return
    name = input(" Enter your name: ")
    bank = input(" Enter bank name: ")
    pin = input(" Set a 4-digit PIN: ")

    users[phone] = {
        "name": name,
        "bank": bank,
        "pin": pin,
        "balance": 0,
        "transactions": []
    }
    save_users(users)
    print(" Registration successful!")

# Login
def login():
    users = load_users()
    phone = input(" Enter phone number: ")
    pin = input(" Enter PIN: ")
    if phone in users and users[phone]["pin"] == pin:
        print(f" Login successful! Welcome, {users[phone]['name']}")
        user_dashboard(phone)
    else:
        print(" Invalid phone or PIN.")

# User Dashboard
def user_dashboard(phone):
    while True:
        print("\n User Dashboard")
        print("1. Check Balance")
        print("2. Add Money")
        print("3. Send Money")
        print("4. View Transaction History")
        print("5. Search User by Name")
        print("6. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(phone)
        elif choice == "2":
            add_money(phone)
        elif choice == "3":
            send_money(phone)
        elif choice == "4":
            transaction_history(phone)
        elif choice == "5":
            search_user_by_name()
        elif choice == "6":
            print("Logged out.")
            break
        else:
            print("Invalid choice.")

# Feature Functions
def check_balance(phone):
    users = load_users()
    print(f" Your current balance: ₹{users[phone]['balance']}")

def add_money(phone):
    users = load_users()
    amount = int(input("Enter amount to add: ₹"))
    users[phone]['balance'] += amount
    users[phone]['transactions'].append(f"+₹{amount} Added to Wallet")
    save_users(users)
    print(f" ₹{amount} added! New balance: ₹{users[phone]['balance']}")

def send_money(sender_phone):
    users = load_users()
    receiver_phone = input("Enter recipient's phone number: ")

    if receiver_phone not in users:
        print(" Recipient not found.")
        return

    amount = int(input("Enter amount to send: ₹"))
    pin = input("Enter your PIN to confirm: ")

    if users[sender_phone]['pin'] != pin:
        print(" Incorrect PIN.")
        return

    if users[sender_phone]['balance'] < amount:
        print(" Insufficient balance.")
        return

    # Transfer money
    users[sender_phone]['balance'] -= amount
    users[receiver_phone]['balance'] += amount

    # Record transactions
    users[sender_phone]['transactions'].append(f"-₹{amount} Sent to {receiver_phone}")
    users[receiver_phone]['transactions'].append(f"+₹{amount} Received from {sender_phone}")

    save_users(users)
    print(f" ₹{amount} sent to {receiver_phone}!")

def transaction_history(phone):
    users = load_users()
    print(" Transaction History:")
    for t in users[phone]["transactions"]:
        print("-", t)

def search_user_by_name():
    users = load_users()
    name = input("Enter name to search: ").lower()
    found = False
    for phone, user in users.items():
        if user["name"].lower() == name:
            print(" User Found:")
            print(f"Name: {user['name']}")
            print(f"Phone: {phone}")
            print(f"Bank: {user['bank']}")
            found = True
    if not found:
        print(" No user found with that name.")

# Main Menu
while True:
    print("\n📲 Welcome to SamPay - Your Virtual Wallet!")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        register_user()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Thank you for using SamhitaPay. Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please try again.")
