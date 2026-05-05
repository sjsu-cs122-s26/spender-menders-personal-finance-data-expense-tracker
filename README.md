Team Name: Spender Menders

# Overview

This project is a personal finance **expense tracker** delivered as a **desktop GUI** with PyQt5. The goal is to help users record, manage, and analyze financial transactions. We plan to turn expense data into clearer summaries for budgeting.

# Team Members

- Daphne Phuong-Nghi Dao
- Heather Ho
- Solhee Tucker
- Allyson Wong

# Dataset

We created 3 mock datasets with CSV files:
- accounts.csv
- categories.csv
- transactions.csv

---

## Tech stack
- Python
- PyQt5
- Pandas
- SQLalchemy
- Matplotlib
- Seaborn

## Dependencies
Before running install:
- PyQt5.15
- python 3.11


## How to run

From the **repository root** (the folder that contains `src/`):

```bash
python3 -m src.main
```

Alternatively:

```bash
python3 src/main.py
```

## Releases

- New version v1.1 has been released 
- Download the SpenderMenders.exe and run

## What the GUI does today

- **Load Accounts** — loads accounts through `AccountService` and lists them.
- **Account list** — click an account to see **name** and **balance** in the detail line below the list.
- **Status line** — shows how many accounts were loaded (or that none were found).
- **Add account** — Create a new account with a name and balance
- **Update account** — Update an account's name or balance 
- **Delete account** — Delete selected account
- **Add transaction** — Add a transaction with one of the default categories, and category type (income/expense)
- **Visualize transactions** — Three charts are currently visible: Line plot(Total cumulative spending), Bar plot(Income vs. Spending), Categorical Plot(Total Spending by Category)


