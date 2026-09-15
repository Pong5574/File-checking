import hashlib
import sqlite3
import os

def get_file_hash(file_path):
    try:
        with open(file_path, "rb") as file_ob:

            file_hash = hashlib.sha256()

            while True:
                data = file_ob.read(4096)

                if not data:
                    break

                file_hash.update(data)

            return file_hash.hexdigest()

    except (PermissionError, OSError) as err:

        print("Cannot read :", file_path)
        print("Reason :", err)

        return None

db = sqlite3.connect("Files_hash.db")
cursor = db.cursor()

cursor.execute("SELECT PATH, HASH FROM Files_hash")

row = cursor.fetchall()

for file_path, old_hash in row:
    if not os.path.exists(file_path):

        print("DELETED :", file_path)
        continue

    new_hash = get_file_hash(file_path)

    if new_hash is None:

        continue

    if new_hash == old_hash:

        print("Ok :", file_path)

    else:

        print("MODIFIED :", file_path)

db.close()
