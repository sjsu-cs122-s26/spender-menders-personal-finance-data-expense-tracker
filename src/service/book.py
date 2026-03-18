# Book keeps all the accounts
from src.service import Account


class Book:
    def __init__(self):
        self.accounts = {}

    def add_account(self, name: str, account: Account):
        self.accounts[name] = account

    def get_account(self, name: str) -> Account:
        return self.accounts.get(name)

    def get_all_accounts(self):
        return self.accounts