# ------------------------------------------------------------------------------------------------ #
#                                           Account Setup                                          #
# ------------------------------------------------------------------------------------------------ #

ACCOUNT_NAME: str = 'Test2'
ACCOUNT_BAL:  int = 150
ACCOUNT_ID:   int = 1

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

CREATE_BTTN: str = "Create"
DELETE_BTTN: str = "Delete"
UPDATE_BTTN: str = "Update"