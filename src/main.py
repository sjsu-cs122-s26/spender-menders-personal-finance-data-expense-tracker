import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

import tkinter as tk
from src.gui.app import ExpenseTrackerApp

def main():
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
