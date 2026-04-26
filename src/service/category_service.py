from src.data.database import DatabaseManager
from src.data.account_repository import CategoryRepository

class CategoryService:
    def __init__(self):
        db = DatabaseManager()
        db.init_db()
        self.repo = CategoryRepository(db.get_session())
    