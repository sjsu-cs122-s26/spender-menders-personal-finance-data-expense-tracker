from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QLineEdit, \
  QPushButton, QTextEdit, QToolTip, QListWidget, QFrame, QGridLayout, QLayout
from PyQt5.QtGui import QFont

from src.data.repository import AccountRepo
from src.service.account_service import AccountService

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.setWindowTitle("Expense Tracker")

    #backend wiring
    self.repo = AccountRepo()
    self.service = AccountService(self.repo)

    layout = QVBoxLayout()
    container = QWidget()
    container.setLayout(self._current_balance())
    self.setCentralWidget(container)

    self.setStyleSheet("""
                          QMainWindow {
                            background-color: #171717; 
                            color: #E6E6E6;  
                          }

                          QLabel { color: #d1d1d1; }
                          """)
    self.show()

  def _current_balance(self):
    layout = QHBoxLayout()
    font = QFont("Helvetica", 13)
    font.setBold(True)
    font.setItalic(True)

    title = QLabel("Total Balance")
    title.setFont(font)

    self.total_balance = QLabel(str(self.service.get_account_balance(None)))
    self.total_balance.setFont(font)

    layout.addWidget(title)
    layout.addSpacing(100)
    layout.addWidget(self.total_balance)

    return layout
