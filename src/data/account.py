# Individual accounts.
# Savings account, checking account, Cash, etc.
class Account:
    def __init__(self, balance: float):
        self.balance = balance
        self.log = []

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        self.balance -= amount

    def get_balance(self) -> float:
        return self.balance
