from config import CONN, CURSOR
from models.librarian import Librarian

class LibrarianRepository:
    
    def save(librarian: Librarian) -> Librarian:
        try:
            CURSOR.execute(
            """
                insert into librarians (name, library_id, user_id) values (?, ?, ?)
            """,
            (librarian.name, librarian.library_id, librarian.user_id)
            )
            
            CONN.commit()
            librarian.id = CURSOR.lastrowid
            print(f"Librarian {librarian.name} added with default password 'Password1234!' and username {librarian.name.lower()}_{librarian.name[0].lower()} is, let the librarian change it.")
        except Exception as e:
            raise Exception("Failed to save librarian: " + str(e))
            
    