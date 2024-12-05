import sqlite3

class Database:
    def __init__(self, db_name="rps_game.db"):
        # Initialize the database with a default name
        self.db_name = db_name

    def initialize(self):
        # Create tables if they don't exist
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS players (
                    id INTEGER PRIMARY KEY,
                    name TEXT UNIQUE
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS games (
                    id INTEGER PRIMARY KEY,
                    player_id INTEGER,
                    player_choice TEXT,
                    computer_choice TEXT,
                    outcome TEXT,
                    FOREIGN KEY (player_id) REFERENCES players (id)
                )
            """)
            conn.commit()

    def execute_query(self, query, params=()):
        # Execute queries for INSERT, UPDATE, DELETE
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()

    def fetch_one(self, query, params=()):
        # Fetch a single row
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()

    def fetch_all(self, query, params=()):
        # Fetch all rows
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

