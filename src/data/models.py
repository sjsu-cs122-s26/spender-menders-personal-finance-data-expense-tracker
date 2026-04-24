# ORM Classes

from sqlalchemy import Column, Integer, String, Float, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Category(Base):
    __tablename__ = "categories"

    cat_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # "income" or "expense"

    transactions = relationship("Transaction", back_populates="category")

    def __repr__(self):
        return "<Category(name='%s', type='%s')>" % (self.name, self.type)


class Transaction(Base):
    __tablename__ = "transactions"

    transactions_id = Column(Integer, primary_key=True)
    expense_cat_id = Column(Integer, ForeignKey("categories.cat_id"), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    description = Column(Text)

    category = relationship("Category", back_populates="transactions")

    def __repr__(self):
        return "<Transaction(amount=%s, date='%s')>" % (self.amount, self.date)