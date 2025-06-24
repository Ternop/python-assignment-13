# Andrew Ternopolsky
# Capstone Project - Personal Finance Tracker

# This program helps users track their expenses by category using a dictionary.

def print_menu():
    # Displays the menu options
    print("\nWhat would you like to do?")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Exit")


def add_expense(data):
    # Adds a new expense to the dictionary
    try:
        description = input("Enter expense description: ").strip()
        if not description:
            raise ValueError("Description cannot be empty.")

        category = input("Enter category: ").strip()
        if not category:
            raise ValueError("Category cannot be empty.")

        amount_input = input("Enter amount: ").strip()
        amount = float(amount_input)  # Convert amount to float

        if category not in data:
            data[category] = []  # Create category if it doesn't exist
        data[category].append((description, amount))  # Add the expense

        print("Expense added successfully.")
    except ValueError:
        print("Invalid input. Please enter valid data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def view_expenses(data):
    # Displays all expenses grouped by category
    if not data:
        print("No expenses to show.")
        return

    for category, expenses in data.items():
        print(f"\nCategory: {category}")
        for description, amount in expenses:
            print(f"  - {description}: ${amount:.2f}")


def view_summary(data):
    # Shows total spending per category
    if not data:
        print("No expenses to summarize.")
        return

    print("\nSummary:")
    for category, expenses in data.items():
        total = sum(amount for _, amount in expenses)
        print(f"{category}: ${total:.2f}")


# Main program starts here
print("Welcome to the Personal Finance Tracker!")

expenses_data = {}  # Dictionary to hold all expenses

while True:
    print_menu()
    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_expense(expenses_data)
    elif choice == "2":
        view_expenses(expenses_data)
    elif choice == "3":
        view_summary(expenses_data)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
