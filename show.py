import sqlite3
import sys

db = sqlite3.connect("Files_hash.db")
cursor = db.cursor()

cursor.execute("SELECT * FROM Files_hash")

rows = cursor.fetchall()

for row in rows:
    print(row)

db.close()

sys.exit(0)