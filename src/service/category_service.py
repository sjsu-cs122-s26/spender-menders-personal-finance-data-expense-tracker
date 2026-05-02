from src.data.database import DatabaseManager
from src.data.category_repository import CategoryRepository


class CategoryService:
    def __init__(self):
        db = DatabaseManager()
        db.init_db()
        self.repo = CategoryRepository(db.get_session())

    def add_category(self, name, type_):
        return self.repo.add(name, type_)

    def get_category(self, category_id):
        if category_id is None:
            return self.repo.get_all()
        return self.repo.get_by_id(category_id)

    def get_categories_by_type(self, type_):
        return self.repo.get_by_type(type_)

    def get_all_categories(self):
        return self.repo.get_all()

    def get_category_type(self, category_id):
        category = self.repo.get_by_id(category_id)
        return category.type if category else None

    def get_signed_amount(self, cat_id, amount):
        category = self.repo.get_by_id(cat_id)
        if category.type == 'expense':
            return -abs(amount)
        else:
            return abs(amount)

    def update_category(self, category_id, name=None, type_=None):
        return self.repo.update(category_id, name=name, type=type_)

    def delete_category(self, category_id):
        return self.repo.delete(category_id)
