from src.data.database import DatabaseManager
from src.data.account_repository import AccountRepository


class AccountService:
    def __init__(self):
        db = DatabaseManager()
        db.init_db()
        self.repo = AccountRepository(db.get_session())

    def create_account(self, name, balance=0.0):
        return self.repo.add(name, balance)

    def get_account(self, account_id):
        if account_id is None:
            return self.repo.get_all()
        return self.repo.get_by_id(account_id)

    def get_all_accounts(self):
        return self.repo.get_all()

    def get_account_balance(self, account_id): # update to update balance based on transactions?
        account = self.repo.get_by_id(account_id)
        return account.balance if account else None

    def update_account(self, account_id, name=None, balance=None):
        return self.repo.update(account_id, name=name, balance=balance)

    def delete_account(self, account_id):
        return self.repo.delete(account_id)
