import pandas as pd

from src.data.df_utils import orm_to_df
from src.data.models import Category, Account, Transaction
from src.service.account_service import AccountService
from src.service.category_service import CategoryService
from src.service.transaction_service import TransactionService

class Manage:
  def __init__(self):
    self.service = AccountService()
    self.category = CategoryService()
    self.transaction = TransactionService()

    self._to_df()

  def _to_df(self):
      # TODO: separate layers
      self.cat_df = orm_to_df(self.category.get_all_categories(), Category)
      self.acc_df = orm_to_df(self.service.get_all_accounts(), Account)
      self.trans_df = orm_to_df(self.transaction.get_all_transactions(), Transaction)

      self.merge_df = self.trans_df.merge(self.cat_df, on="cat_id")

  def get_total_expense(self):
    return self.merge_df[self.merge_df["type"] == "expense"]
  
  def get_expense_by_type(self, id):
    return self.merge_df[(self.merge_df["account_id"] == id) & (self.merge_df["type"] == "expense")]

  def get_expense_sum(self, id):
    expense = self.get_expense_by_type(id)
    return expense["amount"].sum()

  def get_total_income(self):
    return self.merge_df[self.merge_df["type"] == "income"]
  
  def get_income_by_type(self, id):
    return self.merge_df[(self.merge_df["account_id"] == id) & (self.merge_df["type"] == "income")]
  
  def get_income_sum(self, id):
    income = self.get_income_by_type(id)
    return income["amount"].sum()

  def get_balance_by_id(self, id):
    balance = (self.merge_df[self.merge_df["account_id"] == id]
               .groupby("type")["amount"]
               .sum()
               .pipe(lambda x: x.get("income", 0) - x.get("expense", 0)))
    return balance
  
  def get_all_transactions(self, id):
    self._to_df()
    self.merge_df["date"] = pd.to_datetime(self.merge_df["date"])
    self.merge_df = self.merge_df.sort_values(by="date", ascending=False)
    return self.merge_df[self.merge_df["account_id"] == id]
  