# ------------------------------------------------------------------------------------------------ #
#                                           Account Setup                                          #
# ------------------------------------------------------------------------------------------------ #

ACCOUNT_NAME: str = 'Test2'
ACCOUNT_BAL:  int = 150
ACCOUNT_ID:   int = 1

T_COL: int = 6
T_COL_NAME: list = ["ID", "DATE", "NAME", "DESCRIPTION", "AMOUNT", "TYPE"]

# ------------------------------------------------------------------------------------------------ #
#                                             GUI STYLE                                            #
# ------------------------------------------------------------------------------------------------ #

GUI_TITLE: str = 'Expense Tracker'
QLABEL_STYLE: str = " QLabel {background-color: #262626; border: none; color: white; }"
QLIST_STYLE: str = " QListWidget {background-color: #262626; color: white; }"
QFRAME_STYLE: str = """
                          QFrame {
                              background-color: #2b2b2b;
                          }
                          QLabel {
                              color: white;
                          }
                          QLineEdit {
                              background-color: #3a3a3a;
                              color: white;
                              border: 1px solid #555;
                          }
                      """
QTABLE_STYLE: str = """
                          QTableWidget {
                              background-color: #2b2b2b;
                              gridline-color: #ccc;
                              color: white;
                          }
                          QHeaderView::section {
                            background-color: #2b2b2b;
                            gridline-color: #ccc;
                            color: white;
                          }
                          QTableCornerButton::section {
                            background-color: #2b2b2b;
                          }
                          QScrollBar:vertical {
                            background-color: #2b2b2b;
                          }
                          QScrollBar:horizontal {
                            background-color: #2b2b2b;
                          }
                      """
QBUTTON_STYLE: str = """
                      QPushButton {
                        background-color: #171717;
                        color: white;
                        border: 1px solid black;
                      }
                      QPushButton:hover {
                        background-color: #b0b0b0;
                        color: black;
                      }
                      """
QCOMBO_STYLE: str = """
                      QComboBox {
                        background-color: #171717;
                        color: white;
                        border: 1px solid black;
                      }
                      """

QDATE_STYLE: str = """
                      QDateEdit {
                        background-color: #171717;
                        color: white;
                        border: 1px solid black;
                      }
                      """

QTEXTEDIT_STYLE: str = """
                      QTextEdit {
                        background-color: #171717;
                        color: white;
                        border: 1px solid black;
                      }
                      """

QSCROLL_AREA: str = """
                      QScrollArea {
                        background-color: #171717;
                        border: none;
                      }

                      QScrollArea > QWidget > QWidget {
                        background-color: #171717;
                      }

                      QScrollArea QWidget {
                        background-color: #171717;
                      }
                      """

CREATE_BTTN: str = "New Account"
DELETE_BTTN: str = "Delete Account"
UPDATE_BTTN: str = "Update Account"