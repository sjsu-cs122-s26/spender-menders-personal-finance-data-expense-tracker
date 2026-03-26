Team Name: Spender Menders

# Overview

This project is a personal finance **expense tracker** delivered as a **desktop GUI** (Python + Tkinter). The goal is to help users record, manage, and analyze financial transactions. Using the dataset (link TBD), we plan to turn expense data into clearer summaries for budgeting.

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
- **Tkinter / `ttk`** — cross-platform desktop UI (included with standard Python on macOS and most Windows installs)
- **SQLite** — local database via `AccountRepo` (`accounts.db` at project root; ignored by Git)

No extra pip packages are required for the current GUI entry point.

## How to run

From the **repository root** (the folder that contains `src/`):

```bash
python3 -m src.main
```

Alternatively:

```bash
python3 src/main.py
```

On macOS, use `python3` if `python` is not available.

## What the GUI does today

- **Load Accounts** — loads accounts through `AccountService` and lists them.
- **Account list** — click an account to see **name** and **balance** in the detail line below the list.
- **Status line** — shows how many accounts were loaded (or that none were found).

The service layer still uses **stub data** for `get_account` (e.g. sample Savings / Checking accounts). The GUI is wired to `AccountService` and `AccountRepo`; full database-backed account loading will come as the data/service layers are completed.

## Project layout (high level)

| Path | Role |
|------|------|
| `src/main.py` | Entry point: creates the Tk root and starts `ExpenseTrackerApp` |
| `src/gui/app.py` | Main window layout, styles, list, selection handling |
| `src/service/` | Business logic (e.g. `AccountService`) |
| `src/data/` | Models, repository, SQLite access |

## Git notes

- Local SQLite files (`*.db`) are listed in `.gitignore` so machine-specific databases are not committed.
