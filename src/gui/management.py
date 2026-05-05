import pandas as pd

from src.data.df_utils import orm_to_df
from src.data.models import Category, Account, Transaction
from src.service.account_service import AccountService
from src.service.category_service import CategoryService
from src.service.transaction_service import TransactionService
from src.service.visualization_service import VisualizationService
from src.service.manage_service import ManageService
import src.gui.app_util as app_util

class Manage:
    def __init__(self):
        self.service = AccountService()
        self.category = CategoryService()
        self.transaction = TransactionService()
        self.managing = ManageService()
        self.visual = VisualizationService()

        self._to_df()

    def _to_df(self):
        # TODO: separate layers
        self.cat_df = orm_to_df(self.category.get_all_categories(), Category)
        self.acc_df = orm_to_df(self.service.get_all_accounts(), Account)
        self.trans_df = orm_to_df(self.transaction.get_all_transactions(), Transaction)

        self.merge_df = self.trans_df.merge(self.cat_df, on="cat_id")
        self.visual.set_account(app_util.ACCOUNT_ID)

    def get_total_expense(self):
        return self.merge_df[self.merge_df["type"] == "expense"]

    def get_expense_by_type(self, id):
        return self.merge_df[(self.merge_df["account_id"] == id) & (self.merge_df["type"] == "expense")]

    def get_expense_sum(self, id):
        return self.managing.get_expense_sum(id)

    def get_total_income(self):
        return self.merge_df[self.merge_df["type"] == "income"]

    def get_income_by_type(self, id):
        return self.merge_df[(self.merge_df["account_id"] == id) & (self.merge_df["type"] == "income")]

    def get_income_sum(self, id):
        return self.managing.get_income_sum(id)

    def get_balance_by_id(self, id):
        return self.managing.get_balance(id)

    def get_all_transactions(self, id):
        self._to_df()
        self.merge_df["date"] = pd.to_datetime(self.merge_df["date"])
        self.merge_df = self.merge_df.sort_values(by="date", ascending=False)
        return self.merge_df[self.merge_df["account_id"] == id]
    
    def get_spending_overtime(self, id):
        sorted = self.get_expense_by_type(id)
        sorted = sorted.sort_values('date')
        sorted['cumulative'] = sorted['amount'].cumsum()
        return sorted
    
    def get_group_expenses(self, id):
        expense = self.get_expense_by_type(id)
        group_exp = expense.groupby('name')['amount'].sum().sort_values(ascending=False)
        # print(group_exp)
        return group_exp
