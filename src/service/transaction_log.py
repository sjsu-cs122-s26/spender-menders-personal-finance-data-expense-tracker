from dataclasses import dataclass, field


@dataclass
class TransactionLog:
    transaction_id: str
    timestamp: str
    amount: float
    description: str = field(default="")

    def __str__(self):  # for development and debugging purposes
        return (f"Timestamp: {self.timestamp}\n"
                f"Amount: {self.amount}\n"
                f"Description:{self.description}")


@dataclass
class DepositLog(TransactionLog):
    pass


@dataclass
class WithdrawLog(TransactionLog):
    pass
