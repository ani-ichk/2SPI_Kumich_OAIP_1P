import sqlite3
from typing import List, Dict


class Database:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        return self.conn

    def setup(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE,
                city TEXT NOT NULL
            )
        ''')
        conn.commit()

    def add_contact(self, name: str, phone: str, city: str) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO contacts (full_name, phone, city) VALUES (?, ?, ?)",
                (name, phone, city)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get_contacts(self) -> List[Dict]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM contacts")
        rows = cursor.fetchall()
        return [
            {"id": row[0], "full_name": row[1], "phone": row[2], "city": row[3]}
            for row in rows
        ]

    def update_contact(self, contact_id: int, name: str, phone: str, city: str) -> bool:
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE contacts SET full_name=?, phone=?, city=? WHERE id=?",
            (name, phone, city, contact_id)
        )
        self.conn.commit()
        return cursor.rowcount > 0

    def delete_contact(self, contact_id: int) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
        self.conn.commit()
        return cursor.rowcount > 0

    def close(self):
        if self.conn:
            self.conn.close()