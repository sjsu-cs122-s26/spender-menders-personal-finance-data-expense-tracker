import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
  sys.path.insert(0, str(_PROJECT_ROOT))

from PyQt5.QtWidgets import QApplication
from src.gui.app import MainWindow

if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())

# import tkinter as tk
# from src.gui.tk_app import ExpenseTrackerApp

# def main():
#     root = tk.Tk()
#     app = ExpenseTrackerApp(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()

