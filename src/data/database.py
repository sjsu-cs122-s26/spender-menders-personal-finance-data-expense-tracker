import sqlite3


class DatabaseManager:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path
        self.conn = None
        self.connect()

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.execute('PRAGMA foreign_keys = ON;')  # Enable foreign key support
            print("Database connection established.")
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            self.conn = None

    def get_cursor(self):
        if self.conn:
            return self.conn.cursor()
        else:
            raise ConnectionError("Database connection is not established.")

    def commit(self):
        if self.conn:
            self.conn.commit()
        else:
            raise ConnectionError("Database connection is not established.")

    def close(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
        else:
            print("No database connection to close.")
