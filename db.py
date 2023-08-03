import sqlite3
import logging

database = sqlite3.connect("db.db")
cursor = database.cursor()

try:
    # creates table with new users and their referrals
    cursor.execute('''CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        username TEXT,
        info_type TEXT,
        brand TEXT,
        photo TEXT,
        metric TEXT,
        size REAL,
        message_id TEXT
    )''')
except Exception as ex:
    logging.error(f'Users table already exists. {ex}')

# cursor.execute("DELETE FROM referrals WHERE id<>1000")
# database.commit()