# Book keeps all the accounts
from src.service.account import Account


class Book:
    def __init__(self):
        self.accounts = {}

    def add_account(self, name: str, account: Account):
        self.accounts[name] = account

    def get_account(self, name: str) -> Account:
        return self.accounts.get(name)

    def get_all_accounts(self):
        return self.accounts

    def __str__(self):
        result = "Book:\n"
        for name, account in self.accounts.items():
            result += f"  {name}: {account.get_balance()}\n"
        return result