from src.data.models import Transaction


class TransactionRepository:
    def __init__(self, session):
        self.session = session

    def add(self, cat_id, amount, date, description=""):
        tx = Transaction(
            cat_id=cat_id,
            amount=amount,
            date=date,
            description=description,
        )
        self.session.add(tx)
        self.session.commit()
        return tx

    def get_by_id(self, tx_id):
        return self.session.query(Transaction).filter_by(transaction_id=tx_id).first()

    def get_all(self):
        return self.session.query(Transaction).all()

    def get_by_category(self, cat_id):
        return self.session.query(Transaction).filter_by(cat_id=cat_id).all()

    def get_by_date_range(self, start, end):
        return (
            self.session.query(Transaction)
            .filter(Transaction.date >= start)
            .filter(Transaction.date <= end)
            .all()
        )

    def update(self, tx_id, amount=None, date=None, description=None, cat_id=None):
        tx = self.get_by_id(tx_id)
        if tx is None:
            return None
        if amount is not None:
            tx.amount = amount
        if date is not None:
            tx.date = date
        if description is not None:
            tx.description = description
        if cat_id is not None:
            tx.cat_id = cat_id
        self.session.commit()
        return tx

    def delete(self, tx_id):
        tx = self.get_by_id(tx_id)
        if tx is None:
            return False
        self.session.delete(tx)
        self.session.commit()
        return True