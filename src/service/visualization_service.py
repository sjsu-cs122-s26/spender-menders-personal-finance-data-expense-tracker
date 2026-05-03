from src.data.df_utils import orm_to_df
from src.data.df_utils import convert_date_to_month
from src.data.models import Transaction
from src.service.category_service import CategoryService
from src.service.account_service import AccountService
from src.service.transaction_service import TransactionService

def requires_account(func): # decorator to ensure account is set before calling visualization methods
    def wrapper(self, *args, **kwargs):
        if self.df is None:
            raise ValueError("Account not set. Please call set_account() first.")
        return func(self, *args, **kwargs)
    return wrapper

class VisualizationService: # each query will be account specific
    '''Service to prepare data for visualization, such as charts and graphs.'''
    def __init__(self):
        self.account_service = AccountService()
        self.category_service = CategoryService()
        self.transaction_service = TransactionService()
        self.df = None 
    
    def set_account(self, account_id): # create df for specific account
        # SET ACCOUNT FIRST BEFORE CALLING METHODS
        self.df = self.get_transactions_merged_with_categories_df(account_id)

    def get_transactions_merged_with_categories_df(self, account_id): # get transactions merged with categories as a dataframe, filter by account_id
        df = orm_to_df(self.transaction_service.get_merged_transactions_with_categories(), Transaction)
        account_df = df[df['account_id'] == account_id] # filter by account_id
        account_df['month'] = account_df['date'].apply(convert_date_to_month)
        return account_df
    
    @requires_account
    def filter_by_expense_type(self): # filter by category type(expenses only)
        expenses_df = self.df[self.df['type'] == 'expense']
        return expenses_df
    
    @requires_account
    def filter_by_income_type(self): # filter by category type(income only)
        income_df = self.df[self.df['type'] == 'income']
        return income_df
    
    @requires_account
    def filter_by_category_for_expenses(self, category_id): # filter by category id
        df = self.filter_by_expense_type() # only want to visualize expenses by category, not income
        category_df = df[df['cat_id'] == category_id]
        return category_df
    
    @requires_account
    def filter_by_month_for_expenses(self, month): # only want to visualize expenses by month, not income
        df = self.filter_by_expense_type()
        month_df = df[df['month'] == month]
        return month_df
    
    @requires_account
    def get_unique_categories_for_expenses(self): # get unique categories for expenses(for iterating dropdown menu)
        df = self.filter_by_expense_type()
        unique_categories = df['category_name'].unique()
        return unique_categories
    
    @requires_account
    def get_unique_months_for_expenses(self): # get unique months(for iterating dropdown menu)
        df = self.filter_by_expense_type()
        unique_months = df['month'].unique()
        return unique_months
    
    @requires_account
    def get_summed_expenses_by_category(self): # get total expenses for each category(for pie chart)
        df = self.filter_by_expense_type()
        summed_expenses = df.groupby('category_name')['amount'].sum().reset_index()
        return summed_expenses
    
    @requires_account
    def get_summed_expenses(self): # to compare with total income for expense vs income visualization
        df = self.filter_by_expense_type()
        total_expenses = df['amount'].sum()
        return total_expenses
    
    @requires_account
    def get_summed_income(self): # to compare with total expenses for expense vs income visualization
        df = self.filter_by_income_type()
        total_income = df['amount'].sum()
        return total_income
    
    @requires_account
    def get_summed_expenses_by_month(self): # get total expenses for each month(for bar chart)
        df = self.filter_by_expense_type()
        summed_expenses_by_month = df.groupby('month')['amount'].sum().reset_index()
        return summed_expenses_by_month
    
    @requires_account
    def get_summed_expenses_by_category_over_time(self): # get total expenses for each category over time(for bar chart)
        df = self.filter_by_expense_type()
        summed_expenses_by_category_over_time = df.groupby('category_name')['amount'].sum().sort_values(ascending=False).reset_index()
        return summed_expenses_by_category_over_time
    

        
    
    
    
    
    
 

        