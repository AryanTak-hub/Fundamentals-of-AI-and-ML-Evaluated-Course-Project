import csv
import os

FILE_NAME = "expenses.csv"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Category", "Description"])

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/etc): ")
    description = input("Enter description: ")

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, description])

    print("✅ Expense added!")

def view_expenses():
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def total_expense():
    total = 0
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[0])
    print(f"💰 Total Expense: {total}")

def category_summary():
    summary = {}
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = row[1]
            amount = float(row[0])
            summary[category] = summary.get(category, 0) + amount

    print("📊 Category-wise spending:")
    for category, amount in summary.items():
        print(f"{category}: {amount}")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        total_expense()
    elif choice == '4':
        category_summary()
    elif choice == '5':
        break
    else:
        print("❌ Invalid choice")
