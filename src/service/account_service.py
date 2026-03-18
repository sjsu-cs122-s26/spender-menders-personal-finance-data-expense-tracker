from src.data.account import Account
from src.data.transaction_log import DepositLog, WithdrawLog


class AccountService:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def create_account(self, account_data):
        # return True if account creation is successful, False otherwise
        return True

    def get_account(self, account_id):
        # TODO: Implement logic to retrieve account by ID
        acc1 = Account("Savings", 10000.0)
        acc2 = Account("Checking", 5000.0)
        l = [acc1, acc2]
        return l

    def get_all_accounts(self):
        return ["Savings", "Checking"]

    def get_all_logs(self):
        # return list of all logs
        raw_data = [
            DepositLog("1", "2023-10-27 10:00:00", 50000.0, "Savings"),
            DepositLog("2", "2023-10-27 11:30:05", 12000.0, "Checkings"),
            WithdrawLog("3", "2023-10-28 09:15:22", 100000.0, "Savings")
        ]
        return raw_data

    def get_account_logs(self, account_name):
        # return list of logs for the specified account
        raw_data = [
            DepositLog("1", "2023-10-27 10:00:00", 50000.0, "Savings"),
            WithdrawLog("3", "2023-10-28 09:15:22", 100000.0, "Savings")
        ]
        return raw_data

    def get_account_balance(self, account_name):
        return 1234.56

    def update_account(self, account_id, update_data):
        # Update account information
        acc1 = Account("Savings", 10000.0)
        # return None if account not found, otherwise return updated account
        return acc1

    def delete_account(self, account_id):
        # Delete account by ID
        # return False if account not found, otherwise return True
        return True
