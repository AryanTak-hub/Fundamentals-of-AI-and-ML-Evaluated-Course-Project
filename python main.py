import csv
import os
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"
BUDGET = 2000   


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

def total_expense():
    total = 0
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[0])

    print(f"💰 Total Expense: {total}")

    if total > BUDGET:
        print("⚠️ Warning: You exceeded your budget!")
    else:
        print(f"✅ You have {BUDGET - total} left")

def category_summary():
    summary = {}
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = row[1]
            amount = float(row[0])
            summary[category] = summary.get(category, 0) + amount

    print("\n📊 Category-wise Spending:")
    for category, amount in summary.items():
        print(f"{category}: {amount}")

def show_graph():
    summary = {}
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = row[1]
            amount = float(row[0])
            summary[category] = summary.get(category, 0) + amount

    categories = list(summary.keys())
    amounts = list(summary.values())

    plt.bar(categories, amounts)
    plt.xlabel("Categories")
    plt.ylabel("Amount")
    plt.title("Expense Distribution")
    plt.show()

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. Total Expense")
    print("3. Category Summary")
    print("4. Show Graph")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        total_expense()
    elif choice == '3':
        category_summary()
    elif choice == '4':
        show_graph()
    elif choice == '5':
        break
    else:
        print("Invalid choice")
