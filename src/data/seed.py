from src.data.models import Category


def seed_categories(session):
    if session.query(Category).count() == 0:
        default_categories = [
            Category(name='Salary', type='income'),
            Category(name='Groceries', type='expense'),
            Category(name='Rent', type='expense'),
            Category(name='Utilities', type='expense'),
            Category(name='Entertainment', type='expense'),
            Category(name='Investment', type='income'),
            Category(name='Dining Out', type='expense'),
        ]

        session.add_all(default_categories)
        session.commit()
