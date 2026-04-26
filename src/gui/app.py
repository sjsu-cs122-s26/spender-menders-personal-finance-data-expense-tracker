from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QLineEdit, \
  QPushButton, QTextEdit, QToolTip, QListWidget, QFrame, QGridLayout, QLayout
from PyQt5.QtGui import QFont, QIntValidator

from src.service.account_service import AccountService
import src.gui.app_util as app_util

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.setWindowTitle(app_util.GUI_TITLE)
    self.setFixedWidth(1800)
    self.validator = QIntValidator(0, 2147483647)

    #backend wiring
    self.service = AccountService()
    # self.service.create_account(app_util.ACCOUNT_NAME, app_util.ACCOUNT_BAL)
    # print(self.service.get_account(1))
    self.account = app_util.ACCOUNT_NAME

    summary_layout = QHBoxLayout()
    summary_layout.addWidget(self._balance())
    summary_layout.addWidget(self._expense())

    account_layout = QVBoxLayout()
    account_layout.addLayout(summary_layout)
    account_layout.addWidget(self._get_accounts())

    manage_layout = QHBoxLayout()
    manage_layout.addLayout(account_layout)
    manage_layout.addWidget(self._create_acc_ui())
    manage_layout.addWidget(self._del_acc_ui())

    layout = QVBoxLayout()
    layout.addWidget(self._dashboard())
    layout.addLayout(manage_layout)

    container = QWidget()
    container.setLayout(layout)
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
    
    layout.addWidget(dashboard_title)

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

    bal = self.service.get_account_balance(app_util.ACCOUNT_ID)
    if bal is None:
      bal = 0

    self.balance = f"${bal:.2f}"
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

    self.curr_exp = 0

    self.expense = f"-${self.curr_exp:.2f}"
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
    self.current_id = len(self.account_list)
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

# ------------------------------------------------------------------------------------------------ #
#                                          Create Account                                          #
# ------------------------------------------------------------------------------------------------ #

  def _create_acc_ui(self) -> QFrame:
    font = QFont("Helvetica", 13)
    font.setItalic(True)

    layout = QVBoxLayout()
    name_layout = QHBoxLayout()
    bal_layout = QHBoxLayout()

    label = QLabel("Create a new account")
    label.setFont(font)
    label.setAlignment(Qt.AlignCenter)
    name_label = QLabel("Account Name:")
    name_label.setFont(font)
    name_label.setFixedHeight(100)
    bal_label = QLabel("Balance Amount:")
    bal_label.setFont(font)
    bal_label.setFixedHeight(100)

    self.name = QLineEdit(self)
    self.name.setFont(font)
    self.bal = QLineEdit(self)
    self.bal.setFont(font)
    self.bal.setValidator(self.validator)

    submit = QPushButton("Confirm")
    submit.setFont(font)
    submit.setStyleSheet("""
                                QPushButton {
                                  background-color: #171717;
                                  color: white;
                                  border: 1px solid black;
                                }
                                QPushButton:hover {
                                  background-color: #b0b0b0;
                                  color: black;
                                }
                                """)
    submit.clicked.connect(self._create_acc)

    name_layout.addWidget(name_label)
    name_layout.setSpacing(10)
    name_layout.addWidget(self.name)
    bal_layout.addWidget(bal_label)
    bal_layout.setSpacing(10)
    bal_layout.addWidget(self.bal)

    layout.addWidget(label)
    layout.addLayout(name_layout)
    layout.addLayout(bal_layout)
    layout.addWidget(submit)
    layout.setSpacing(0)

    frame = QFrame()
    frame.setLayout(layout)
    frame.setStyleSheet(app_util.QFRAME_STYLE)

    return frame
  
  def _update_ui(self, item) -> None:
    index = self.list_widget.row(item)
    self.balance = "$" + str(self.service.get_account_balance(self.account_list[index].account_id))
    self.total_balance.setText(self.balance)
    self.expense = "-$200"
    self.exp_balance.setText(self.expense)

    self.transactions = f"{20} Transactions" # Dummy account
    self.bal_transactions.setText(self.transactions)
    self.exp_transactions.setText(self.transactions)

  def _create_acc(self):
    self.service.create_account(self.name.text(), int(self.bal.text()))
    self.account_list = self.service.get_all_accounts()
    print(self.account_list)
    self.current_id = len(self.account_list)
    print(self.current_id)
    self.name.clear()
    self.bal.clear()

    self.list_widget.addItem(self.account_list[self.current_id - 1].name)
    self.del_widget.addItem(self.account_list[self.current_id - 1].name)

# ------------------------------------------------------------------------------------------------ #
#                                       Delete/Update Account                                      #
# ------------------------------------------------------------------------------------------------ #
  def _del_acc_ui(self) -> QFrame:
    font = QFont("Helvetica", 13)
    font.setItalic(True)

    layout = QVBoxLayout()

    label = QLabel("Select an account\nto delete/update")
    label.setFont(font)
    label.setAlignment(Qt.AlignCenter)

    font = QFont("Helvetica", 13)
    font.setItalic(True)

    self.del_widget = QListWidget()
    if not self.account_list == None:
      for i in range(len(self.account_list)):
        self.del_widget.addItem(self.account_list[i].name)

    self.del_widget.setFont(font)
    self.del_widget.setStyleSheet(app_util.QLIST_STYLE)

    name_label = QLabel("New Account Name:")
    name_label.setFont(font)
    name_label.setFixedHeight(100)
    bal_label = QLabel("New Balance Amount:")
    bal_label.setFont(font)
    bal_label.setFixedHeight(100)

    self.new_name = QLineEdit(self)
    self.new_name.setFont(font)
    self.new_bal = QLineEdit(self)
    self.new_bal.setFont(font)
    self.new_bal.setValidator(self.validator)

    deleteBttn = QPushButton("Delete")
    deleteBttn.setFont(font)
    deleteBttn.setStyleSheet("""
                                QPushButton {
                                  background-color: #171717;
                                  color: white;
                                  border: 1px solid black;
                                }
                                QPushButton:hover {
                                  background-color: #b0b0b0;
                                  color: black;
                                }
                                """)
    deleteBttn.clicked.connect(self._del_acc)

    updateBttn = QPushButton("Update")
    updateBttn.setFont(font)
    updateBttn.setStyleSheet("""
                                QPushButton {
                                  background-color: #171717;
                                  color: white;
                                  border: 1px solid black;
                                }
                                QPushButton:hover {
                                  background-color: #b0b0b0;
                                  color: black;
                                }
                                """)
    updateBttn.clicked.connect(self._update_acc)

    name_layout = QHBoxLayout()
    bal_layout = QHBoxLayout()

    name_layout.addWidget(name_label)
    name_layout.setSpacing(10)
    name_layout.addWidget(self.new_name)
    bal_layout.addWidget(bal_label)
    bal_layout.setSpacing(10)
    bal_layout.addWidget(self.new_bal)

    button_layout = QHBoxLayout()
    button_layout.addWidget(deleteBttn)
    button_layout.addWidget(updateBttn)

    layout.addWidget(label)
    layout.addWidget(self.del_widget)
    layout.addLayout(name_layout)
    layout.addLayout(bal_layout)
    layout.addLayout(button_layout)
    layout.setSpacing(10)

    frame = QFrame()
    frame.setLayout(layout)
    frame.setStyleSheet(app_util.QFRAME_STYLE)

    return frame
  
  def _del_acc(self) -> None:
    index = self.del_widget.currentRow()
    print(index)
    print(self.account_list)
    print(self.account_list[index].account_id)
    print(self.service.delete_account(self.account_list[index].account_id))
    self.current_id -= 1

    item = self.del_widget.takeItem(index)
    del item
    item = self.list_widget.takeItem(index)
    del item
    del self.account_list[index]
    print(self.account_list)
    self.new_name.clear()
    self.new_bal.clear()

  def _update_acc(self) -> None:
    name = self.new_name.text()
    index = self.del_widget.currentRow()
    self.service.update_account(self.account_list[index].account_id, name, int(self.new_bal.text()))
    
    item = self.list_widget.item(index)
    item.setText(name)

    item = self.del_widget.item(index)
    item.setText(name)

    self.new_name.clear()
    self.new_bal.clear()