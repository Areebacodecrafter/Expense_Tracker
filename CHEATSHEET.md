# Python Cheat Sheet: Expense Tracker Project

A quick reference for every concept used in this project. Each section shows the idea, a tiny example, and where it appears in `tracker.py`.

---

## 1. Imports

Bring in built-in tools so you don't write everything from scratch.

```python
import json                      # read/write JSON files
import argparse                  # handle terminal commands
from datetime import date        # work with dates
from pathlib import Path         # work with file paths
```

`import x` loads a whole module. `from x import y` loads just one piece.

---

## 2. Variables and Constants

```python
DATA_FILE = Path("expenses.json")
```

- ALL_CAPS names are a convention for values that never change (constants).
- Python is **case-sensitive**: `DATA_FILE`, `Data_File` and `data_file` are three different names.

---

## 3. Functions

Reusable blocks of code. Define once, call many times.

```python
def add_expense(amount, category):   # parameters = inputs
    ...
    return something                 # optional output
```

- `def` defines a function. Call it with `add_expense(500, "food")`.
- `return` sends a value back, or exits the function early.
- Keep each function doing **one job**.

---

## 4. Lists

An ordered collection of items.

```python
expenses = []                 # empty list
expenses.append(item)         # add to the end
expenses.pop(0)               # remove item at index 0 and return it
len(expenses)                 # how many items
expenses[0]                   # first item (counting starts at 0!)
```

---

## 5. Dictionaries

Key-value pairs, like a mini notebook.

```python
expense = {"date": "2026-10-02", "amount": 500, "category": "food"}

expense["amount"]                  # get a value -> 500
expense["amount"] = 600            # change a value
totals.get("food", 0)              # get a value, or 0 if the key doesn't exist
```

**Grouping trick** (used in `summary`):

```python
totals = {}
for e in expenses:
    totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
```

---

## 6. Loops

```python
for e in expenses:                       # run once per item
    print(e)

for i, e in enumerate(expenses, start=1):  # get a counter + item
    print(i, e)
```

**Indentation matters!** Only indented lines are inside the loop.

```python
for e in expenses:
    do_this()        # runs once PER item
print("done")        # runs ONCE, after the loop
```

---

## 7. Conditions

```python
if not expenses:
    print("No expenses yet.")
elif number < 1 or number > len(expenses):
    print("Invalid number")
else:
    print("OK")
```

- `if` / `elif` ("else if") / `else` choose which code runs.
- Combine checks with `and`, `or`, `not`.
- An empty list is "falsy", so `if not expenses` means "the list is empty".

---

## 8. f-Strings and Formatting

Put variables inside text.

```python
print(f"Added: {amount} for {category}")
print(f"{amount:.2f}")        # 2 decimal places  -> 500.00
print(f"{name:<12}")          # left-align in 12 spaces
print(f"{total:>10.2f}")      # right-align in 10 spaces, 2 decimals
print("-" * 23)               # repeat a string 23 times
```

---

## 9. Working with JSON Files

```python
# Read
with open(DATA_FILE, "r") as f:
    data = json.load(f)

# Write
with open(DATA_FILE, "w") as f:
    json.dump(data, f, indent=2)
```

- `"r"` = read, `"w"` = write (overwrites the file).
- `with open(...)` closes the file automatically, even if an error happens.
- `json.load` turns file text into Python lists/dicts. `json.dump` does the reverse.
- `indent=2` makes the file readable.

**Check if a file exists first:**

```python
if not DATA_FILE.exists():
    return []
```

---

## 10. Dates

```python
from datetime import date
str(date.today())      # "2026-10-02"
```

---

## 11. argparse (Terminal Commands)

Turns `python tracker.py add 500 food` into variables.

```python
parser = argparse.ArgumentParser(description="Simple expense tracker")
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add", help="Add a new expense")
add_parser.add_argument("amount", type=float)
add_parser.add_argument("category")

args = parser.parse_args()
args.command     # "add"
args.amount      # 500.0
```

- `type=float` / `type=int` converts the text automatically and rejects bad input like `abc`.
- Run with no command, or with `-h`, to see the help menu.

---

## 12. Sorting with `sorted` and `lambda`

```python
sorted(totals.items(), key=lambda x: x[1], reverse=True)
```

- `.items()` gives (key, value) pairs.
- `lambda x: x[1]` is a tiny one-line function meaning "sort by the value".
- `reverse=True` puts the biggest first.

---

## 13. Input Validation

Always ask: **"What if the user types something silly?"**

```python
if number < 1 or number > len(expenses):
    print("No expense with that number.")
    return
```

Without this, `delete 99` would crash the program.

---

## 14. The `main()` Pattern

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

Runs `main()` only when you run the file directly, not when another file imports it.

---

## 15. Think Like a Programmer: Input, Process, Output

| Command | Input | Process | Output |
|---|---|---|---|
| `add` | amount, category | append to list, save | confirmation message |
| `list` | nothing | load and loop | numbered list |
| `summary` | nothing | group and sum by category | table with total |
| `delete` | number | validate, remove, save | confirmation message |

---

## 16. Reading Errors

1. Read the **last line** first. It names the error (`FileNotFoundError`, `NameError`...).
2. Look at the **line number** it points to.
3. Check spelling, capitalization and indentation.

| Error | Usual cause |
|---|---|
| `FileNotFoundError` | File doesn't exist yet, or wrong path |
| `NameError` | Typo or wrong capitalization in a name |
| `IndentationError` | Inconsistent spaces |
| `invalid choice` (argparse) | Command not registered in `main()` |

---

## 17. Terminal Commands Used

```powershell
python tracker.py add 500 food
python tracker.py list
python tracker.py summary
python tracker.py delete 1
python tracker.py -h
```

**Windows tip:** if `python` isn't recognized, add Python to PATH or set an alias:

```powershell
Set-Alias python "C:\Users\<you>\AppData\Local\Programs\Python\Python314\python.exe"
```

---

## 18. Git and GitHub Basics

```bash
git init                          # start tracking the folder
git add .                         # stage all files
git commit -m "Initial commit"    # save a snapshot
git branch -M main
git remote add origin https://github.com/<username>/expense-tracker.git
git push -u origin main           # upload to GitHub
```

**`.gitignore`** (keeps personal data off GitHub):

```
expenses.json
__pycache__/
```

---

## Quick Reference Table

| Concept | Syntax |
|---|---|
| Define function | `def name(params):` |
| Add to list | `list.append(x)` |
| Remove from list | `list.pop(index)` |
| Safe dict lookup | `d.get(key, default)` |
| Loop with counter | `for i, x in enumerate(list, start=1):` |
| Format decimals | `f"{x:.2f}"` |
| Read JSON | `json.load(f)` |
| Write JSON | `json.dump(data, f, indent=2)` |
| Today's date | `str(date.today())` |
| Convert to number | `float(x)` / `int(x)` |
