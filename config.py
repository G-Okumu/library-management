import sqlite3

CONN = sqlite3.connect('DB/library.db')
CURSOR = CONN.cursor()
