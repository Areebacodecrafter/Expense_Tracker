import json
import argparse
from datetime import date 
from pathlib import Path

Data_File = Path("expenses.json")


def load_expenses():
    if not Data_File.exists():
        return []
    with open(Data_File, "r") as f:
        return json.load(f)

def save_expenses(expenses):
    with open(Data_File, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(amount, category):
    expenses = load_expenses()
    expense = {
        "date": str(date.today()),
        "amount": amount,
        "category": category,
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Added expense: {amount} for {category}")


def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
        return
    for i,e in enumerate(expenses, start=1):
        print(f"{i}. {e['date']} | {e['amount']}")

def summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
        return
    
    totals = {}
    for e in expenses:
        category = e["category"]
        totals[category] = totals.get(category, 0) + e["amount"]
    print("--------Spending Summary--------")
    for category, total in sorted(totals.items(), key=lambda x: x[1], reverse= True):
            print(f"{category:<12}: {total:>10.2f}")
    print("-" * 23)
    print(f"{'TOTAL':12} {sum(totals.values()):>10.2f}")

def delete_expense(number):
    expenses = load_expenses()
    if number < 1 or number > len(expenses):
        print(f"No expense with number {number}. Run 'list' to see valid numbers.")
        return
    removed = expenses.pop(number - 1)
    save_expenses(expenses)
    print(f"Deleted: {removed['amount']:.2f} for {removed['category']}")


def main():
    parser = argparse.ArgumentParser(description="Expense tracker")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("amount", type=float, help = "How much you spent")
    add_parser.add_argument("category", help = "What you spent it on")
    subparsers.add_parser("list", help= "Show all expenses")
    subparsers.add_parser("summary", help="Show total spending by category")
    delete_parser = subparsers.add_parser("delete", help="Delete an expense by its number")
    delete_parser.add_argument("number", type=int, help="The number shown in 'list'")
    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.amount, args.category)
    elif args.command == "list":
        list_expenses()
    elif args.command == "summary":
        summary()
    elif args.command == "delete":
        delete_expense(args.number)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()