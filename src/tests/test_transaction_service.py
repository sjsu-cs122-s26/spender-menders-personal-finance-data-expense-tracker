import unittest
from unittest.mock import MagicMock
from datetime import date

from src.service.transaction_service import TransactionService


class TestTransactionService(unittest.TestCase):
    def setUp(self):
        self.transaction_service = TransactionService()
        self.transaction_service.repo = MagicMock()
        self.transaction_service.category_service = MagicMock()
        self.transaction_service.account_service = MagicMock()

    def test_add_transaction_updates_account_balance(self):
        category = MagicMock()
        category.account_id = 1

        self.transaction_service.category_service.get_category.return_value = category
        self.transaction_service.category_service.get_signed_amount.return_value = 100.0
        self.transaction_service.account_service.get_account_balance.return_value = 500.0

        expected_tx = MagicMock()
        self.transaction_service.repo.add.return_value = expected_tx

        result = self.transaction_service.add_transaction(
            account_id=1,
            cat_id=10,
            amount=100.0,
            date=date(2026, 4, 28),
            description="Test income",
        )

        self.transaction_service.category_service.get_category.assert_called_once_with(10)
        self.transaction_service.account_service.get_account_balance.assert_called_once_with(1)
        self.transaction_service.account_service.update_account.assert_called_once_with(1, balance=600.0)
        self.transaction_service.repo.add.assert_called_once_with(
            1,
            10,
            100.0,
            date(2026, 4, 28),
            "Test income",
        )
        self.assertEqual(result, expected_tx)


if __name__ == "__main__":
    unittest.main()
