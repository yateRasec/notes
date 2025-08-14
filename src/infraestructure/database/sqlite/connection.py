import sqlite3

from src.domain.repositories.iconnection_database import IConnectionDatabase


class HandlerSQLite(IConnectionDatabase):
    def __init__(self, db_path: str = "database.db"):
        self.db_path = db_path
        self.connect()

    def connect(self) -> None:
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

    def close(self) -> None:
        self.conn.close()

    def run_query(self, query: str) -> None:
        return self.conn.execute(query)

    def confirm(self):
        self.conn.commit()
