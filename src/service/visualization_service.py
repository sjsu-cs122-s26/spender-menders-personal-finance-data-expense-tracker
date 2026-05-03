from src.data.df_utils import orm_to_df
from src.data.df_utils import convert_date_to_month
from src.data.models import Transaction
from src.service.category_service import CategoryService
from src.service.account_service import AccountService
from src.service.transaction_service import TransactionService

class VisualizationService: 
    '''Service to prepare data for visualization, such as charts and graphs.'''
    def __init__(self):
        self.account_service = AccountService()
        self.category_service = CategoryService()
        self.transaction_service = TransactionService()

    def get_transactions_merged_with_categories_df(self, account_id):
        whole_df = orm_to_df(self.transaction_service.get_merged_transactions_with_categories(), Transaction)
        df = whole_df[whole_df['account_id'] == account_id] # filter by account_id
        df['month'] = df['date'].apply(convert_date_to_month)
        return df
    
    def get_monthly_expenses_by_category(self, month):
        pass
    def get_monthly_income_by_category(self, month):
        pass
    def expenses_over_time(self):
        pass
    def expenses_by_category(self):
        pass
    def expense_versus_income(self):
        pass
    def expenses_by_month(self):
        pass
    def expenses_by_category_over_time(self):
        pass
    def expenses_versus_income_over_time(self): # trend line
        pass

        