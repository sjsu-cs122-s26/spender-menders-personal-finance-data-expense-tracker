from src.data.database import DatabaseManager
from src.service.category_service import CategoryService
from src.service.account_service import AccountService
from src.service.transaction_service import TransactionService
#TODO: add function to database manager to join transactions with categories and accounts for easier data retrieval

class VisualizationService: 
    '''Service to prepare data for visualization, such as charts and graphs.'''
    def __init__(self):
        self.account_service = AccountService()
        self.category_service = CategoryService()
        self.transaction_service = TransactionService()
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

        