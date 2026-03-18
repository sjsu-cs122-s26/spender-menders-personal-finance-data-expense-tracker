import sqlite3

class AccountRepo:
    def __init__(self):
        self.db_path = "accounts.db"
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self._init_db()

    def _init_db(self):
        init_query = '''
            CREATE TABLE IF NOT EXISTS accounts (
                name TEXT PRIMARY KEY,
                balance REAL DEFAULT 0.0
            )
        '''
        self.cursor.execute(init_query)
        self.conn.commit()

    def update_account(self, name: str, balance: float):
        query = "INSERT OR REPLACE INTO accounts (name, balance) VALUES (?, ?)"
        self.cursor.execute(query, (name, balance))
        self.conn.commit()

    def get_all_logs(self, name: str):
        raw_data = [
            (1, "2023-10-27 10:00:00", "deposit", 50000.0, "savings"),
            (2, "2023-10-27 11:30:05", "withdraw", 12000.0, "checkings"),
            (3, "2023-10-28 09:15:22", "deposit", 100000.0, "savings")
        ]
        return raw_data

    def close(self):
        self.conn.close()
