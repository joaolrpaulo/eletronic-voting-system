import sqlite3

from app import app
from flask import g


class Database:
    def __init__(self, file):
        self.file = file

    def conn(self):
        if not hasattr(g, 'sqlite_db'):
            g.sqlite_db = sqlite3.connect(self.file)
            g.sqlite_db = sqlite3.Row
        return g.sqlite_db

    def conn_cursor(self):
        conn = self.conn()
        cursor = conn.cursor()
        return conn, cursor

    def setup(self):
        conn, cursor = self.conn_cursor()
        with app.open_resource('schema.sql', mode = 'r') as f:
            cursor.executescript(f.read())
        conn.commit()

    @staticmethod
    @app.teardown_appcontext
    def close(error):
        if hasattr(g, 'sqlite_db'):
            g.sqlite_db.close()
