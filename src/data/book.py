# Book keeps all the accounts
from src.data.repository import AccountRepo
from src.data.account import Account


class Book:
    def __init__(self):
        self.repo = AccountRepo()
        self.accounts = {}

    def add_account(self, name: str, account: Account):
        self.accounts[name] = account

    def get_all_accounts(self):
        return self.accounts

    def get_all_logs(self):
        self.repo.get_all_logs()

    def get_account_logs(self, name: str):
        pass

    def __str__(self):
        result = "Book:\n"
        for name, account in self.accounts.items():
            result += f"  {name}: {account.get_balance()}\n"
        return result