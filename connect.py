import sqlite3

# Connecting to SQLite database
dbCon = sqlite3.connect("Python Project/filmflix.db")

if dbCon:
    print("Database is connected")
else:
    print("Database is not connected")

# Creating a cursor
dbCursor = dbCon.cursor()
