from src.data.models import Account


class AccountRepository:
    def __init__(self, session):
        self.session = session

    def add(self, name, balance=0.0):
        account = Account(name=name, balance=balance)
        self.session.add(account)
        self.session.commit()
        return account

    def get_by_id(self, account_id):
        return self.session.query(Account).filter_by(account_id=account_id).first()

    def get_by_name(self, name):
        return self.session.query(Account).filter_by(name=name).first()

    def get_all(self):
        return self.session.query(Account).all()

    def update(self, account_id, name=None, balance=None):
        account = self.get_by_id(account_id)
        if account is None:
            return None
        if name is not None:
            account.name = name
        if balance is not None:
            account.balance = balance
        self.session.commit()
        return account

    def delete(self, account_id):
        account = self.get_by_id(account_id)
        if account is None:
            return False
        self.session.delete(account)
        self.session.commit()
        return True
