from src.data.account import Account


class MockAccount(Account):
    def __init__(self, balance: float):
        super().__init__(balance)

    def deposit(self, amount: float):
        super().deposit(amount)

    def withdraw(self, amount: float):
        super().withdraw(amount)
