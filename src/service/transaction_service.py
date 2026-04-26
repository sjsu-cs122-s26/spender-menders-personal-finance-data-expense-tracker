from src.data.database import DatabaseManager
from src.data.transaction_repository import TransactionRepository

class TransactionService:
    def __init__(self):
        db = DatabaseManager()
        db.init_db()
        self.repo = TransactionRepository(db.get_session())
    
    def add_transaction(self, cat_id, amount, date, description=""):
        return self.repo.add(cat_id, amount, date, description)
    
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
                                
