from config import CONN, CURSOR
from models.user import User
import sqlite3

class UserRepository():
    
    # Adding users
    def create_user(user: User) -> User:
        try:
            CURSOR.execute(
                """
                    insert into users (username, password, role) values (?, ?, ?)
                """,
                (user.username, user.password, user.role)
            )
            
            CONN.commit()        
        except sqlite3.Error as error:
            print(f"Error {error} occured")

            

    
    # method to find user by username