import sqlite3


class CatDatabase:
    def __init__(self, db_path=":memory:"): # :memory: означает базу в оперативной памяти
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                breed TEXT,
                color TEXT
            )
        ''')
        self.conn.commit()

    def add_cat(self, name, age, breed="неизвестно", color="разный"):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO cats (name, age, breed, color)
            VALUES (?, ?, ?, ?)
        ''', (name, age, breed, color))
        self.conn.commit()
        return cursor.lastrowid

    def get_all_cats(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM cats')
        return cursor.fetchall()

    def update_cat(self, cat_id, name=None, age=None, breed=None, color=None):
        cursor = self.conn.cursor()
        updates = []
        params = []

        if name:
            updates.append("name = ?")
            params.append(name)
        if age:
            updates.append("age = ?")
            params.append(age)
        if breed:
            updates.append("breed = ?")
            params.append(breed)
        if color:
            updates.append("color = ?")
            params.append(color)

        if updates:
            params.append(cat_id)
            query = f"UPDATE cats SET {', '.join(updates)} WHERE id = ?"
            cursor.execute(query, params)
            self.conn.commit()
            return cursor.rowcount
        return 0

    def delete_cat(self, cat_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM cats WHERE id = ?', (cat_id,))
        self.conn.commit()
        return cursor.rowcount

    def close(self):
        self.conn.close()