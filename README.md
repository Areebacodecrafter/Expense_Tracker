# Expense_Tracker
A simple command-line expense tracker built with pure Python. Add, list, delete, and summarize spending, saved to JSON.
Expense Tracker CLI

A simple command-line expense tracker built with pure Python (no external libraries). Add, list, delete, and summarize your spending right from the terminal. Data is saved in a local JSON file.

I built this to keep my Python skills sharp while learning C++.

Features
Add an expense with an amount and a category
List all expenses with numbered entries
Delete an expense by its number
Summary of total spending per category, sorted from highest to lowest
Input validation (invalid commands or numbers won't crash the app)
Data saved automatically to expenses.json
Requirements
Python 3.8 or newer
No extra packages needed (uses only json, argparse, datetime, pathlib)
Usage
bash
python tracker.py add 500 food
python tracker.py add 120 transport
python tracker.py list
python tracker.py summary
python tracker.py delete 1
python tracker.py -h
Example output

list

1. 2026-10-02 | 500.0 | food
2. 2026-10-02 | 120.0 | transport

summary

--- Spending Summary ---
food             500.00
transport        120.00
-----------------------
TOTAL            620.00

delete with a bad number

No expense with number 99. Run 'list' to see valid numbers.
Project Structure
expense-tracker/
├── tracker.py       # all the code
├── expenses.json    # your data (auto-created, not uploaded to GitHub)
├── CHEATSHEET.md    # Python concepts used in this project
├── README.md
└── .gitignore
What I Learned:
Reading and writing JSON files
Lists, dictionaries, and functions
Building terminal commands with argparse
Formatting output with f-strings
Input validation and handling edge cases
Debugging (indentation, case-sensitivity, file paths)

See CHEATSHEET.md for a quick reference of every concept used.

Future Ideas
Filter expenses by month
Export to CSV
Monthly spending chart with matplotlib
Edit an existing expense
Budget limits with warnings
Author

Made by [Areeba]. Feel free to open an issue or suggest improvements!
