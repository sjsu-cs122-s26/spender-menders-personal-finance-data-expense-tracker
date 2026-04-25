from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QLineEdit, \
  QPushButton, QTextEdit, QToolTip, QListWidget, QFrame, QGridLayout, QLayout
from PyQt5.QtGui import QFont

from src.service.account_service import AccountService
import src.gui.app_util as app_util

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.setWindowTitle(app_util.GUI_TITLE)

    #backend wiring
    self.service = AccountService()
    # self.service.create_account(app_util.ACCOUNT_NAME, app_util.ACCOUNT_BAL)
    # print(self.service.get_account(1))
    self.account = app_util.ACCOUNT_NAME

    summary_layout = QHBoxLayout()
    summary_layout.addWidget(self._balance())
    summary_layout.addWidget(self._expense())

    layout = QVBoxLayout()
    layout.addWidget(self._dashboard())
    layout.addLayout(summary_layout)
    layout.addWidget(self._get_accounts())

    manage_layout = QHBoxLayout()
    manage_layout.addLayout(layout)
    manage_layout.addWidget(self._create_acc())

    container = QWidget()
    container.setLayout(manage_layout)
    self.setCentralWidget(container)

    self.setStyleSheet("""
                          QMainWindow {
                            background-color: #171717; 
                            color: #E6E6E6;  
                          }

                          QLabel { color: #d1d1d1; }
                          """)
    self.show()

  def _dashboard(self) -> QFrame:
    layout = QHBoxLayout()
    font = QFont("Helvetica", 13)
    button = QFont("Helvetica", 13)
    button.setBold(True)
    button.setItalic(True)

    dashboard_title = QLabel("My Dashboard")
    dashboard_title.setFont(font)
    dashboard_title.setStyleSheet("padding-left: 20px; padding-right: 150px;")

    create_button = QPushButton("Create")
    create_button.setFixedSize(100, 50)
    create_button.setFont(button)
    create_button.setStyleSheet("""
                                QPushButton {
                                  background-color: #2b2b2b;
                                  color: white;
                                  border: 1px solid black;
                                }
                                QPushButton:hover {
                                  background-color: #b0b0b0;
                                  color: black;
                                }
                                """)
    
    # create_button.clicked.connect()
    
    del_button = QPushButton("Delete")
    del_button.setFixedSize(100, 50)
    del_button.setFont(button)
    del_button.setStyleSheet("""
                                QPushButton {
                                  background-color: #2b2b2b;
                                  color: white;
                                  border: 1px solid black;
                                }
                                QPushButton:hover {
                                  background-color: #b0b0b0;
                                  color: black;
                                }
                                """)
    
    update_button = QPushButton("Update")
    update_button.setFixedSize(100, 50)
    update_button.setFont(button)
    update_button.setStyleSheet("""
                                QPushButton {
                                  background-color: #2b2b2b;
                                  color: white;
                                  border: 1px solid black;
                                }
                                QPushButton:hover {
                                  background-color: #b0b0b0;
                                  color: black;
                                }
                                """)
    
    layout.addWidget(dashboard_title)
    layout.addWidget(create_button)
    layout.addWidget(del_button)
    layout.addWidget(update_button)

    frame = QFrame()
    frame.setLayout(layout)

    return frame

  def _balance(self) -> QFrame:
    layout = QVBoxLayout()
    font = QFont("Helvetica", 13)
    font.setItalic(True)

    subtitle = QFont("Helvetica", 11)
    subtitle.setItalic(True)

    title = QLabel("Balance")
    title.setFont(font)
    title.setAlignment(Qt.AlignCenter)

    self.balance = "$" + str(self.service.get_account_balance(self.account))
    self.total_balance = QLabel(self.balance)
    self.total_balance.setFont(font)
    self.total_balance.setAlignment(Qt.AlignCenter)

    self.transactions = f"{10} Transactions" # Dummy account
    self.bal_transactions = QLabel(self.transactions)
    self.bal_transactions.setFont(subtitle)
    self.bal_transactions.setAlignment(Qt.AlignCenter)

    layout.addWidget(title)
    layout.addWidget(self.total_balance)
    layout.addWidget(self.bal_transactions)
    layout.setSpacing(0)
    
    frame = QFrame()
    frame.setLayout(layout)
    frame.setStyleSheet(app_util.QLABEL_STYLE)

    return frame
  
  def _expense(self) -> QFrame:
    layout = QVBoxLayout()
    font = QFont("Helvetica", 13)
    font.setItalic(True)

    subtitle = QFont("Helvetica", 11)
    subtitle.setItalic(True)

    title = QLabel("Expense")
    title.setFont(font)
    title.setAlignment(Qt.AlignCenter)

    self.expense = "-$100"
    self.exp_balance = QLabel(self.expense)
    self.exp_balance.setFont(font)
    self.exp_balance.setAlignment(Qt.AlignCenter)

    self.transactions = f"{10} Transactions" # Dummy account
    self.exp_transactions = QLabel(self.transactions)
    self.exp_transactions.setFont(subtitle)
    self.exp_transactions.setAlignment(Qt.AlignCenter)

    layout.addWidget(title)
    layout.addWidget(self.exp_balance)
    layout.addWidget(self.exp_transactions)
    layout.setSpacing(0)
    
    frame = QFrame()
    frame.setLayout(layout)
    frame.setStyleSheet(app_util.QLABEL_STYLE)

    return frame
  
  def _get_accounts(self) -> QFrame:
    font = QFont("Helvetica", 13)
    font.setItalic(True)

    layout = QVBoxLayout()

    label = QLabel("Accounts")
    label.setFont(font)

    self.list_widget = QListWidget()
    self.account_list = self.service.get_all_accounts()
    if not self.account_list == None:
      for i in range(len(self.account_list)):
        self.list_widget.addItem(self.account_list[i].name)

    self.list_widget.itemClicked.connect(self._update_ui)
    self.list_widget.setFont(font)
    self.list_widget.setStyleSheet(app_util.QLIST_STYLE)

    layout.addWidget(label)
    layout.addWidget(self.list_widget)
    layout.setSpacing(0)

    frame = QFrame()
    frame.setLayout(layout)
    frame.setStyleSheet(app_util.QLABEL_STYLE)

    return frame

  def _management(self):
    pass

  def _create_acc(self) -> QFrame:
    font = QFont("Helvetica", 13)
    font.setItalic(True)

    layout = QVBoxLayout()
    name_layout = QHBoxLayout()
    bal_layout = QHBoxLayout()

    label = QLabel("Create a new account")
    label.setFont(font)
    label.setAlignment(Qt.AlignCenter)
    name_label = QLabel("Insert Account Name:")
    name_label.setFont(font)
    bal_label = QLabel("Insert Balance Amount:")
    bal_label.setFont(font)

    self.name = QLineEdit(self)
    self.bal = QLineEdit(self)

    submit = QPushButton("Confirm")
    submit.setFont(font)
    submit.setStyleSheet("""
                                QPushButton {
                                  background-color: #2b2b2b;
                                  color: white;
                                  border: 1px solid black;
                                }
                                QPushButton:hover {
                                  background-color: #b0b0b0;
                                  color: black;
                                }
                                """)

    name_layout.addWidget(name_label)
    name_layout.addWidget(self.name)
    bal_layout.addWidget(bal_label)
    bal_layout.addWidget(self.bal)

    layout.addWidget(label)
    layout.addLayout(name_layout)
    layout.addLayout(bal_layout)
    layout.addWidget(submit)
    layout.setSpacing(0)

    frame = QFrame()
    frame.setLayout(layout)
    frame.setStyleSheet(app_util.QLABEL_STYLE)

    return frame
  
  def _update_ui(self, item):
    self.balance = "$" + str(self.service.get_account_balance(item.text()))
    self.total_balance.setText(self.balance)
    self.expense = "-$200"
    self.exp_balance.setText(self.expense)

    self.transactions = f"{20} Transactions" # Dummy account
    self.bal_transactions.setText(self.transactions)
    self.exp_transactions.setText(self.transactions)


