from models.book import Book
from config import CONN, CURSOR

class BookRepository:
    
    @staticmethod
    def save(book: Book) -> Book:
        try:
            CURSOR.execute(
                "INSERT INTO books (title, library_id, is_borrowed) VALUES (?, ?, ?)",
                (book.title, book.library_id, int(book.is_borrowed))
            )
            CONN.commit()
            book.id = CURSOR.lastrowid
            print(f"Book '{book.title}' saved with ID {book.id}")
        except Exception as e:
            CONN.rollback()
            raise e
            
        