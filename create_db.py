import sqlite3
import sys

db = sqlite3.connect("Files_hash.db")
cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Files_hash (ID INTEGER PRIMARY KEY AUTOINCREMENT, PATH TEXT NOT NULL, HASH TEXT NOT NULL)")

db.commit()

db.close()

sys.exit(0)