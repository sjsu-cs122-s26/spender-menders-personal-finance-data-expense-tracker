from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QLineEdit, \
  QPushButton, QTextEdit, QToolTip, QListWidget, QFrame, QGridLayout, QLayout, QTableWidget, \
  QTableWidgetItem, QHeaderView, QComboBox, QDateEdit
from PyQt5.QtGui import QFont, QIntValidator
from src.gui.management import Manage
import src.gui.app_util as app_util

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.setWindowTitle(app_util.GUI_TITLE)
    self.setFixedWidth(1800)
    self.validator = QIntValidator(0, 2147483647)

    #backend wiring
    # self.service = AccountService()
    # self.service.create_account(app_util.ACCOUNT_NAME, app_util.ACCOUNT_BAL)
    # print(self.service.get_account(1))
    self.acc_manage = Manage()
    print(type(self.acc_manage.get_all_transactions(1)))
    self.account = app_util.ACCOUNT_NAME

    summary_layout = QHBoxLayout()
    summary_layout.addWidget(self._balance())
    summary_layout.addWidget(self._expense())
    summary_layout.addWidget(self._income())

    account_layout = QVBoxLayout()
    account_layout.addLayout(summary_layout)
    account_layout.addWidget(self._get_accounts())
    # self._get_transactions()
    # account_layout.addWidget(self._get_transactions())

    manage_layout = QHBoxLayout()
    manage_layout.addLayout(account_layout)
    manage_layout.addWidget(self._create_acc_ui())
    manage_layout.addWidget(self._add_transactions_ui())

    transaction_layout = QHBoxLayout()
    transaction_layout.addWidget(self._get_transactions())

    layout = QVBoxLayout()
    layout.addWidget(self._dashboard())
    layout.addLayout(manage_layout)
    layout.addLayout(transaction_layout)

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
    button.setItalic(True)

    dashboard_title = QLabel("My Dashboard")
    dashboard_title.setFont(font)
    dashboard_title.setStyleSheet("padding-left: 20px; padding-right: 150px;")

    new_acc_bttn = QPushButton(app_util.CREATE_BTTN)
    new_acc_bttn.setFont(button)
    new_acc_bttn.setStyleSheet(app_util.QBUTTON_STYLE)
    new_acc_bttn.setFixedWidth(200)
    new_acc_bttn.clicked.connect(self._update_form_ui)
    delete_bttn = QPushButton(app_util.DELETE_BTTN)
    delete_bttn.setFont(button)
    delete_bttn.setStyleSheet(app_util.QBUTTON_STYLE)
    delete_bttn.setFixedWidth(200)
    delete_bttn.clicked.connect(self._update_form_ui)
    update_bttn = QPushButton(app_util.UPDATE_BTTN)
    update_bttn.setFont(button)
    update_bttn.setStyleSheet(app_util.QBUTTON_STYLE)
    update_bttn.setFixedWidth(200)
    update_bttn.clicked.connect(self._update_form_ui)

    self._init_form_ui()
    
    layout.addWidget(dashboard_title)
    layout.addWidget(new_acc_bttn)
    layout.addWidget(delete_bttn)
    layout.addWidget(update_bttn)

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

    self.bal = self.acc_manage.get_balance_by_id(app_util.ACCOUNT_ID)
    if self.bal is None:
      self.bal = 0

    self.balance = f"${self.bal:.2f}"
    self.total_balance = QLabel(self.balance)
    self.total_balance.setFont(font)
    self.total_balance.setAlignment(Qt.AlignCenter)

    self.bal_transaction_count = len(self.acc_manage.get_all_transactions(app_util.ACCOUNT_ID))
    self.transactions = f"{self.bal_transaction_count} Transactions" # Dummy account
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

    self.curr_exp = self.acc_manage.get_expense_sum(app_util.ACCOUNT_ID)

    self.expense = f"-${self.curr_exp:.2f}"
    self.exp_balance = QLabel(self.expense)
    self.exp_balance.setFont(font)
    self.exp_balance.setAlignment(Qt.AlignCenter)

    self.exp_transaction_count = len(self.acc_manage.get_expense_by_type(app_util.ACCOUNT_ID))
    self.exp_transactions_str = f"{self.exp_transaction_count} Transactions" # Dummy account
    self.exp_transactions = QLabel(self.exp_transactions_str)
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
  
  def _income(self) -> QFrame:
    layout = QVBoxLayout()
    font = QFont("Helvetica", 13)
    font.setItalic(True)

    subtitle = QFont("Helvetica", 11)
    subtitle.setItalic(True)

    title = QLabel("Income")
    title.setFont(font)
    title.setAlignment(Qt.AlignCenter)

    self.curr_income = self.acc_manage.get_income_sum(app_util.ACCOUNT_ID)

    self.income = f"${self.curr_income:.2f}"
    self.income_balance = QLabel(self.income)
    self.income_balance.setFont(font)
    self.income_balance.setAlignment(Qt.AlignCenter)

    self.income_transaction_count = len(self.acc_manage.get_income_by_type(app_util.ACCOUNT_ID))
    self.income_transactions_str = f"{self.income_transaction_count} Transactions" # Dummy account
    self.income_transactions = QLabel(self.income_transactions_str)
    self.income_transactions.setFont(subtitle)
    self.income_transactions.setAlignment(Qt.AlignCenter)

    layout.addWidget(title)
    layout.addWidget(self.income_balance)
    layout.addWidget(self.income_transactions)
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
    self.account_list = self.acc_manage.service.get_all_accounts()
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
  
  def _add_transactions_ui(self) -> QFrame:
    font = QFont("Helvetica", 13)
    font.setItalic(True)
    self.cat_list = self.acc_manage.category.get_all_categories()

    self.transactions_ui_layout = QVBoxLayout()
    acc_layout = QHBoxLayout()
    expense_layout = QHBoxLayout()
    date_layout = QHBoxLayout()
    amount_layout = QHBoxLayout()
    desc_layout = QHBoxLayout()

    label = QLabel("Add Transaction")
    label.setFont(font)
    label.setFixedHeight(50)
    label.setAlignment(Qt.AlignCenter)

    # Select Account
    choose_acc_label = QLabel("Select Account")
    choose_acc_label.setFont(font)
    choose_acc_label.setFixedHeight(50)
    self.acc_combo = QComboBox(self)
    self.acc_combo.setFont(font)
    self.acc_combo.setStyleSheet(app_util.QCOMBO_STYLE)

    for i in range(len(self.account_list)):
      self.acc_combo.addItem(self.account_list[i].name)
    
    # Select Category
    expense_label = QLabel("Select Category")
    expense_label.setFont(font)
    expense_label.setFixedHeight(50)
    self.t_combo = QComboBox(self)
    self.t_combo.setFont(font)
    self.t_combo.setStyleSheet(app_util.QCOMBO_STYLE)

    for i in range(len(self.cat_list)):
      self.t_combo.addItem(self.cat_list[i].name)

    # Select Date
    date_label = QLabel("Select Date")
    date_label.setFont(font)
    date_label.setFixedHeight(50)
    self.date = QDateEdit(self)
    self.date.setFont(font)
    self.date.setDate(QDate.currentDate())
    self.date.setCalendarPopup(True)
    self.date.setStyleSheet(app_util.QDATE_STYLE)

    # Amount
    amount_label = QLabel("Amount")
    amount_label.setFont(font)
    amount_label.setFixedHeight(50)
    self.amount = QLineEdit()
    self.amount.setFont(font)
    self.amount.setValidator(self.validator)

    # Description
    desc_label = QLabel("Write a Description")
    desc_label.setFont(font)
    desc_label.setFixedHeight(50)
    self.desc = QTextEdit()
    self.desc.setFont(font)
    self.desc.setStyleSheet(app_util.QTEXTEDIT_STYLE)
    self.desc.setFixedSize(500, 100)

    # Submit
    self.add_transact_bttn = QPushButton("Add")
    self.add_transact_bttn.setFont(font)
    self.add_transact_bttn.setStyleSheet(app_util.QBUTTON_STYLE)
    self.add_transact_bttn.clicked.connect(self._add_transaction)

    # Layout
    acc_layout.addWidget(choose_acc_label)
    acc_layout.addSpacing(50)
    acc_layout.addWidget(self.acc_combo)

    expense_layout.addWidget(expense_label)
    expense_layout.addSpacing(50)
    expense_layout.addWidget(self.t_combo)

    date_layout.addWidget(date_label)
    date_layout.addSpacing(50)
    date_layout.addWidget(self.date)

    amount_layout.addWidget(amount_label)
    amount_layout.addSpacing(150)
    amount_layout.addWidget(self.amount)

    desc_layout.addWidget(desc_label)
    desc_layout.addSpacing(50)
    desc_layout.addWidget(self.desc)

    self.transactions_ui_layout.addWidget(label)
    self.transactions_ui_layout.addLayout(acc_layout)
    self.transactions_ui_layout.addLayout(expense_layout)
    self.transactions_ui_layout.addLayout(date_layout)
    self.transactions_ui_layout.addLayout(amount_layout)
    self.transactions_ui_layout.addLayout(desc_layout)
    self.transactions_ui_layout.addSpacing(20)
    self.transactions_ui_layout.addWidget(self.add_transact_bttn)
    self.transactions_ui_layout.setSpacing(0)

    frame = QFrame()
    frame.setLayout(self.transactions_ui_layout)
    frame.setStyleSheet(app_util.QFRAME_STYLE)

    return frame
  
  def _get_transactions(self) -> QFrame:
    font = QFont("Helvetica", 13)
    font.setItalic(True)

    label = QLabel("Transactions")
    label.setFont(font)

    self.transactions_widget = QTableWidget()
    self.transactions_df = self.acc_manage.get_all_transactions(app_util.ACCOUNT_ID)
    t_row_len = self.transactions_df.shape[0]
    # print(self.transactions_df)
    # print(t_row_len)

    self.transactions_widget.setRowCount(t_row_len)
    self.transactions_widget.setColumnCount(app_util.T_COL)
    self.transactions_widget.setHorizontalHeaderLabels(app_util.T_COL_NAME)

    for i in range(t_row_len):
      self.transactions_widget.setItem(i, 0, QTableWidgetItem(str(self.transactions_df["transaction_id"].iloc[i])))
      self.transactions_widget.setItem(i, 1, QTableWidgetItem(str(self.transactions_df["date"].iloc[i])))
      self.transactions_widget.setItem(i, 2, QTableWidgetItem(str(self.transactions_df["name"].iloc[i])))
      self.transactions_widget.setItem(i, 3, QTableWidgetItem(str(self.transactions_df["description"].iloc[i])))
      self.transactions_widget.setItem(i, 4, QTableWidgetItem(str(self.transactions_df["amount"].iloc[i])))
      self.transactions_widget.setItem(i, 5, QTableWidgetItem(str(self.transactions_df["type"].iloc[i])))

    self.transactions_widget.horizontalHeader().setStretchLastSection(True)
    self.transactions_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    self.transactions_widget.setStyleSheet(app_util.QTABLE_STYLE)

    return self.transactions_widget
  
  def _add_transaction(self):
    account_id = self.acc_combo.currentIndex()
    cat_id = self.t_combo.currentIndex()
    date = self.date.date().toPyDate()
    amount = self.amount.text()
    description = self.desc.toPlainText()

    self.acc_manage.transaction.add_transaction(int(account_id) + 1, int(cat_id) + 1, int(amount), date, description)
    self._update_ui_after_add(int(account_id) + 1)
    self.amount.clear()
    self.desc.clear()

# ------------------------------------------------------------------------------------------------ #
#                                          Create Account                                          #
# ------------------------------------------------------------------------------------------------ #

  def _create_acc_ui(self) -> QFrame:
    font = QFont("Helvetica", 13)
    font.setItalic(True)

    self.form_ui_layout = QVBoxLayout()
    name_layout = QHBoxLayout()
    bal_layout = QHBoxLayout()

    self.acc_label = QLabel("Create a new account")
    self.acc_label.setFont(font)
    self.acc_label.setAlignment(Qt.AlignCenter)
    self.acc_label.setFixedHeight(50)
    self.name_label = QLabel("Account Name:")
    self.name_label.setFont(font)
    self.name_label.setFixedHeight(50)
    self.bal_label = QLabel("Balance Amount:")
    self.bal_label.setFont(font)
    self.bal_label.setFixedHeight(50)

    self.name = QLineEdit(self)
    self.name.setFont(font)
    self.bal_text = QLineEdit(self)
    self.bal_text.setFont(font)
    self.bal_text.setValidator(self.validator)

    self.create_submit = QPushButton("Create")
    self.create_submit.setFont(font)
    self.create_submit.setStyleSheet(app_util.QBUTTON_STYLE)
    self.create_submit.clicked.connect(self._create_acc)

    name_layout.addWidget(self.name_label)
    name_layout.setSpacing(10)
    name_layout.addWidget(self.name)
    bal_layout.addWidget(self.bal_label)
    bal_layout.setSpacing(10)
    bal_layout.addWidget(self.bal_text)

    self.form_ui_layout.addWidget(self.acc_label)
    self.form_ui_layout.addLayout(name_layout)
    self.form_ui_layout.addLayout(bal_layout)
    self.form_ui_layout.addWidget(self.create_submit)
    self.form_ui_layout.setSpacing(0)

    frame = QFrame()
    frame.setLayout(self.form_ui_layout)
    frame.setStyleSheet(app_util.QFRAME_STYLE)

    return frame
  
  def _update_ui(self, item) -> None:
    index = self.list_widget.row(item)
    index += 1
    self.transactions_df = self.acc_manage.get_all_transactions(index)
    
    # Total balance
    self.bal = self.acc_manage.get_balance_by_id(index)
    self.balance = f"${self.bal:.2f}"
    self.total_balance.setText(self.balance)

    self.bal_transaction_count = len(self.transactions_df)
    self.transactions = f"{self.bal_transaction_count} Transactions"
    self.bal_transactions.setText(self.transactions)

    # Expense
    self.curr_exp = self.acc_manage.get_expense_sum(index)

    self.expense = f"-${self.curr_exp:.2f}"
    self.exp_balance.setText(self.expense)

    self.exp_transaction_count = len(self.acc_manage.get_expense_by_type(index))
    self.exp_transactions_str = f"{self.exp_transaction_count} Transactions" # Dummy account
    self.exp_transactions.setText(self.exp_transactions_str)

    # Income
    self.curr_income = self.acc_manage.get_income_sum(index)

    self.income = f"${self.curr_income:.2f}"
    self.income_balance.setText(self.income)

    self.income_transaction_count = len(self.acc_manage.get_income_by_type(index))
    self.income_transactions_str = f"{self.income_transaction_count} Transactions" # Dummy account
    self.income_transactions.setText(self.income_transactions_str)

    # Transactions
    self.transactions_widget.setRowCount(0)
    t_row_len = self.transactions_df.shape[0]

    self.transactions_widget.setRowCount(t_row_len)
    self.transactions_widget.setColumnCount(app_util.T_COL)
    self.transactions_widget.setHorizontalHeaderLabels(app_util.T_COL_NAME)

    for i in range(t_row_len):
      self.transactions_widget.setItem(i, 0, QTableWidgetItem(str(self.transactions_df["transaction_id"].iloc[i])))
      self.transactions_widget.setItem(i, 1, QTableWidgetItem(str(self.transactions_df["date"].iloc[i])))
      self.transactions_widget.setItem(i, 2, QTableWidgetItem(str(self.transactions_df["name"].iloc[i])))
      self.transactions_widget.setItem(i, 3, QTableWidgetItem(str(self.transactions_df["description"].iloc[i])))
      self.transactions_widget.setItem(i, 4, QTableWidgetItem(str(self.transactions_df["amount"].iloc[i])))
      self.transactions_widget.setItem(i, 5, QTableWidgetItem(str(self.transactions_df["type"].iloc[i])))

    self.transactions_widget.horizontalHeader().setStretchLastSection(True)
    self.transactions_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

  def _update_ui_after_add(self, index) -> None:
    self.transactions_df = self.acc_manage.get_all_transactions(index)
    print(self.transactions_df)
    
    # Total balance
    self.bal = self.acc_manage.get_balance_by_id(index)
    self.balance = f"${self.bal:.2f}"
    self.total_balance.setText(self.balance)

    self.bal_transaction_count = len(self.transactions_df)
    self.transactions = f"{self.bal_transaction_count} Transactions"
    self.bal_transactions.setText(self.transactions)

    # Expense
    self.curr_exp = self.acc_manage.get_expense_sum(index)

    self.expense = f"-${self.curr_exp:.2f}"
    self.exp_balance.setText(self.expense)

    self.exp_transaction_count = len(self.acc_manage.get_expense_by_type(index))
    self.exp_transactions_str = f"{self.exp_transaction_count} Transactions" # Dummy account
    self.exp_transactions.setText(self.exp_transactions_str)

    # Income
    self.curr_income = self.acc_manage.get_income_sum(index)

    self.income = f"${self.curr_income:.2f}"
    self.income_balance.setText(self.income)

    self.income_transaction_count = len(self.acc_manage.get_income_by_type(index))
    self.income_transactions_str = f"{self.income_transaction_count} Transactions" # Dummy account
    self.income_transactions.setText(self.income_transactions_str)

    # Transactions
    self.transactions_widget.setRowCount(0)
    t_row_len = self.transactions_df.shape[0]

    self.transactions_widget.setRowCount(t_row_len)
    self.transactions_widget.setColumnCount(app_util.T_COL)
    self.transactions_widget.setHorizontalHeaderLabels(app_util.T_COL_NAME)

    for i in range(t_row_len):
      self.transactions_widget.setItem(i, 0, QTableWidgetItem(str(self.transactions_df["transaction_id"].iloc[i])))
      self.transactions_widget.setItem(i, 1, QTableWidgetItem(str(self.transactions_df["date"].iloc[i])))
      self.transactions_widget.setItem(i, 2, QTableWidgetItem(str(self.transactions_df["name"].iloc[i])))
      self.transactions_widget.setItem(i, 3, QTableWidgetItem(str(self.transactions_df["description"].iloc[i])))
      self.transactions_widget.setItem(i, 4, QTableWidgetItem(str(self.transactions_df["amount"].iloc[i])))
      self.transactions_widget.setItem(i, 5, QTableWidgetItem(str(self.transactions_df["type"].iloc[i])))

    self.transactions_widget.horizontalHeader().setStretchLastSection(True)
    self.transactions_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

  def _create_acc(self):
    self.acc_manage.service.create_account(self.name.text(), int(self.bal_text.text()))
    self.account_list = self.acc_manage.service.get_all_accounts()
    self.current_id = len(self.account_list)
    self.name.clear()
    self.bal_text.clear()

    self.list_widget.addItem(self.account_list[self.current_id - 1].name)
    self.del_widget.addItem(self.account_list[self.current_id - 1].name)

  def _update_form_ui(self):
    button = self.sender()
    self._hide_form_ui()

    if button.text() == app_util.CREATE_BTTN:
      self.acc_label.show()
      self.name_label.show()
      self.name.show()
      self.bal_label.show()
      self.bal_text.show()
      self.create_submit.show()
      self.acc_label.setText("Create a new account")

    if button.text() == app_util.DELETE_BTTN:
      self.acc_label.show()
      self.del_widget.show()
      self.deleteBttn.show()
      self.acc_label.setText("Select an account to delete")

    if button.text() == app_util.UPDATE_BTTN:
      self.acc_label.show()
      self.del_widget.show()
      self.name_label.show()
      self.name.show()
      self.bal_label.show()
      self.bal_text.show()
      self.updateBttn.show()
      self.acc_label.setText("Select an account to update")
      self.name_label.setText("New Account Name")
      self.bal_label.setText("New Balance Amount")

  def _hide_form_ui(self):
    # Hide create widgets
    self.acc_label.hide()
    self.name_label.hide()
    self.name.hide()
    self.bal_label.hide()
    self.bal_text.hide()
    self.create_submit.hide()

    # Hide delete widgets
    self.del_widget.hide()
    self.deleteBttn.hide()

    # Hide update widgets
    self.updateBttn.hide()

  def _init_form_ui(self):
    font = QFont("Helvetica", 13)
    font.setItalic(True)
    self.del_widget = QListWidget()
    if not self.account_list == None:
      for i in range(len(self.account_list)):
        self.del_widget.addItem(self.account_list[i].name)

    # Delete widgets
    self.del_widget.setFont(font)
    self.del_widget.setStyleSheet(app_util.QLIST_STYLE)
    self.del_widget.setFixedHeight(100)

    self.deleteBttn = QPushButton("Delete")
    self.deleteBttn.setFont(font)
    self.deleteBttn.setStyleSheet(app_util.QBUTTON_STYLE)
    self.deleteBttn.clicked.connect(self._del_acc)

    self.form_ui_layout.addWidget(self.del_widget)
    self.form_ui_layout.addWidget(self.deleteBttn)

    self.del_widget.hide()
    self.deleteBttn.hide()

    # Update widgets
    self.updateBttn = QPushButton("Update")
    self.updateBttn.setFont(font)
    self.updateBttn.setStyleSheet(app_util.QBUTTON_STYLE)
    self.updateBttn.clicked.connect(self._update_acc)

    self.form_ui_layout.addWidget(self.updateBttn)
    self.updateBttn.hide()

# ------------------------------------------------------------------------------------------------ #
#                                       Delete/Update Account                                      #
# ------------------------------------------------------------------------------------------------ #
  
  def _del_acc(self) -> None:
    index = self.del_widget.currentRow()
    self.acc_manage.service.delete_account(self.account_list[index].account_id)
    self.current_id -= 1

    item = self.del_widget.takeItem(index)
    del item
    item = self.list_widget.takeItem(index)
    del item
    del self.account_list[index]
    print(self.account_list)

  def _update_acc(self) -> None:
    name = self.name.text()
    index = self.del_widget.currentRow()
    self.acc_manage.service.update_account(self.account_list[index].account_id, name, int(self.bal_text.text()))
    
    item = self.list_widget.item(index)
    item.setText(name)

    item = self.del_widget.item(index)
    item.setText(name)

    self.name.clear()
    self.bal_text.clear()