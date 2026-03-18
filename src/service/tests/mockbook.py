from src.data.book import Book
from src.service.tests.mockaccount import MockAccount


class MockBook(Book):
    def __init__(self):
        super().__init__()
        accounts = {
            "Checking": 1000.0,
            "Savings": 5000.0,
            "Cash": 200.0
        }
        for name, balance in accounts.items():
            self.add_account(name, MockAccount(balance))
