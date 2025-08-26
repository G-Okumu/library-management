from config import CONN, CURSOR
import sqlite3

class LibraryRepository():
    
    def save(name):
        try:
            CURSOR.execute(
                """
                    insert into libraries (name) values (?)
                """,
                (name,)
            )
            
            CONN.commit()
            print("Library added successfully.")
        except sqlite3.Error as e:
            print(f"Error {e} occured")