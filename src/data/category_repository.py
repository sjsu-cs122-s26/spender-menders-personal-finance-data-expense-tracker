from src.data.models import Category


class CategoryRepository:
    def __init__(self, session):
        self.session = session

    def add(self, name, type_):
        category = Category(name=name, type=type_)
        self.session.add(category)
        self.session.commit()
        return category

    def get_by_id(self, cat_id):
        return self.session.query(Category).filter_by(cat_id=cat_id).first()

    def get_by_name(self, name):
        return self.session.query(Category).filter_by(name=name).first()

    def get_all(self):
        return self.session.query(Category).all()

    def get_by_type(self, type_):
        # type_ = "income" or "expense"
        return self.session.query(Category).filter_by(type=type_).all()

    def update(self, cat_id, name=None, type_=None):
        category = self.get_by_id(cat_id)
        if category is None:
            return None
        if name is not None:
            category.name = name
        if type_ is not None:
            category.type = type_
        self.session.commit()
        return category

    def delete(self, cat_id):
        category = self.get_by_id(cat_id)
        if category is None:
            return False
        self.session.delete(category)
        self.session.commit()
        return True
