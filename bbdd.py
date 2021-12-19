import sqlite3
DATABASE_NAME = "sarampion.db"


def obtener_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS datos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                code TEXT NOT NULL,
                tiempo INTEGER,
                tCode TEXT NOT NULL,
                porcentaje INTEGER

            )
            """
    ]
    db = obtener_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)