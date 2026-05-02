from src.data.df_utils import orm_to_df
from src.data.models import Account, Category, Transaction
from src.service.account_service import AccountService
from src.service.category_service import CategoryService
from src.service.transaction_service import TransactionService


class ManageService:
    def __init__(self):
        self.account_service = AccountService()
        self.category_service = CategoryService()
        self.transaction_service = TransactionService()

    def get_expense_sum(self, account_id):
        self._refresh()
        df = self._merge_df
        return float(
            df[(df["account_id"] == account_id) & (df["type"] == "expense")]["amount"].sum()
        )

    def get_income_sum(self, account_id):
        self._refresh()
        df = self._merge_df
        return float(
            df[(df["account_id"] == account_id) & (df["type"] == "income")]["amount"].sum()
        )

    def get_balance(self, account_id):
        balance = self.account_service.get_account_balance(account_id)
        return float(balance) if balance is not None else 0.0

    def _refresh(self):
        cats = self.category_service.get_all_categories()
        accs = self.account_service.get_all_accounts()
        trans = self.transaction_service.get_all_transactions()

        self._cat_df = orm_to_df(cats, Category)
        self._acc_df = orm_to_df(accs, Account)
        self._trans_df = orm_to_df(trans, Transaction)
        self._merge_df = self._trans_df.merge(self._cat_df, on="cat_id")
