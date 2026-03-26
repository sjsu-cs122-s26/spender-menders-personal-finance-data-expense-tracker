Team Name: Spender Menders

# Overview

This project is a personal finance **expense tracker** delivered as a **desktop GUI** (Python + Tkinter). (We will be transistioning to PyQt5). The goal is to help users record, manage, and analyze financial transactions. We plan to turn expense data into clearer summaries for budgeting.

# Team Members

- Daphne Phuong-Nghi Dao
- Heather Ho
- Solhee Tucker
- Allyson Wong

# Dataset

(Link and description to be added.)

---

## Tech stack

- **Python 3**
- **Tkinter
- **PyQt5
- **SQLite**


## How to run

From the **repository root** (the folder that contains `src/`):

```bash
python3 -m src.main
```

Alternatively:

```bash
python3 src/main.py
```

## What the GUI does today

- **Load Accounts** — loads accounts through `AccountService` and lists them.
- **Account list** — click an account to see **name** and **balance** in the detail line below the list.
- **Status line** — shows how many accounts were loaded (or that none were found).

The service layer still uses **stub data** for `get_account` (e.g. sample Savings / Checking accounts). The GUI is wired to `AccountService` and `AccountRepo`; full database-backed account loading will come as the data/service layers are completed.
