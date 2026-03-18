from dataclasses import dataclass, field


@dataclass
class TransactionLog:
    def __init__(
            self,
            transaction_id: str,
            timestamp: str,
            amount: float,
            account: str = field(default="")):
        self.transaction_id = transaction_id
        self.timestamp = timestamp
        self.amount = amount
        self.account = account

    def __str__(self):  # for development and debugging purposes
        return (f"Timestamp: {self.timestamp}\n"
                f"Amount: {self.amount}\n"
                f"Description:{self.description}")


@dataclass
class DepositLog(TransactionLog):
    def __init__(self, transaction_id: str, timestamp: str, amount: float, account: str):
        TransactionLog.__init__(self, transaction_id, timestamp, amount, account)
        self.type = "Deposit"


@dataclass
class WithdrawLog(TransactionLog):
    def __init__(self, transaction_id: str, timestamp: str, amount: float, account: str):
        TransactionLog.__init__(self, transaction_id, timestamp, amount, account)
        self.type = "Withdraw"
