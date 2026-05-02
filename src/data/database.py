from contextlib import contextmanager
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # Project root
_DB_PATH = _PROJECT_ROOT / "database.db"


class Base(DeclarativeBase):
    pass


class DatabaseManager:
    def __init__(self, db_url: str = f"sqlite:///{_DB_PATH}"):
        self.engine = create_engine(db_url, echo=False)
        self._Session = sessionmaker(bind=self.engine)

    def init_db(self):
        Base.metadata.create_all(self.engine)

    @contextmanager
    def session_scope(self):
        session = self._Session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def get_session(self):
        return self._Session()

    def close(self):
        self.engine.dispose()
