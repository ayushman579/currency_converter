import sqlite3

DB_NAME = "conversions.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            base_currency TEXT NOT NULL,
            target_currency TEXT NOT NULL,
            amount REAL NOT NULL,
            converted_amount REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_conversion(base_currency, target_currency, amount, converted_amount):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO conversions (base_currency, target_currency, amount, converted_amount)
        VALUES (?, ?, ?, ?)
    """, (base_currency, target_currency, amount, converted_amount))
    conn.commit()
    conn.close()

def fetch_conversions():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM conversions ORDER BY timestamp DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    return rows


