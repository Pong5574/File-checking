import os
import hashlib
import sys
import sqlite3

path = "C:\\"

db = sqlite3.connect("Files_hash.db")
cursor = db.cursor()

sum = 0

for curr_path, folders, files in os.walk(path):
    for file in files:
        sha256 = hashlib.sha256()

        file_path = os.path.join(curr_path, file)

        # print("file : ", file, " in path : ", curr_path)

        try:
            with open(file_path, "rb") as file_ob:
                while chuck := file_ob.read(4096):
                    sha256.update(chuck)

            file_hash = sha256.hexdigest()

            cursor.execute("INSERT INTO Files_hash (PATH, HASH) VALUES (?, ?)", (file_path, file_hash))

            sum += 1
        except (PermissionError, OSError):
            print("Skip Path : ", file_path)
            continue

db.commit()

print("Insert files total : ", sum)

db.close()

sys.exit(0)