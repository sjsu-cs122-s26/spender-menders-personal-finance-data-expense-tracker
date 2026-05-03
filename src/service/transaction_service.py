from src.data.database import DatabaseManager
from src.data.transaction_repository import TransactionRepository
from src.service.category_service import CategoryService
from src.service.account_service import AccountService

class TransactionService:
    def __init__(self):
        db = DatabaseManager()
        db.init_db()
        self.repo = TransactionRepository(db.get_session())
        self.category_service = CategoryService()
        self.account_service = AccountService()
    
    def add_transaction(self, account_id, cat_id, amount, date, description=""): # update balance after transcation
        category = self.category_service.get_category(cat_id) # check if category exists
        if category:
            signed_amount = self.category_service.get_signed_amount(cat_id, amount) # get signed amount based on category type
        new_balance = self.account_service.get_account_balance(account_id) + signed_amount # calculate new balance
        self.account_service.update_account(account_id, balance=new_balance) # update account balance
        tx = self.repo.add(account_id, cat_id, amount, date, description) # add transaction

        return tx

    def get_transaction(self, tx_id):
        if tx_id is None:
            return self.repo.get_all()
        return self.repo.get_by_id(tx_id)
    
    def get_transactions_by_cat(self, cat_id):
        return self.repo.get_by_category(cat_id)

    def get_transactions_by_date_range(self, start, end):
        return self.repo.get_by_date_range(start, end)
    
    def get_all_transactions(self):
        return self.repo.get_all()
    
    def update_transaction(self, tx_id, amount=None, date=None, description=None, cat_id=None):
        return self.repo.update(tx_id, amount=amount, date=date, description=description, cat_id=cat_id)
    
    def delete_transaction(self, tx_id):
        return self.repo.delete(tx_id)
    
    def get_merged_transactions_with_categories(self):
        return self.repo.get_merged_transactions_with_categories()
    
    
                                
