from models.student import Student
from config import CONN, CURSOR

class StudentRepository():
    def save(student: Student) -> Student:
        try:
            CURSOR.execute(
            """
                insert into students (name, user_id) values (?, ?)
            """,
            (student.name, student.user_id)
            )
            
            CONN.commit()
            student.id = CURSOR.lastrowid
            print(f"Student {student.name} added with default password 'Password1234!' and username {student.name.lower()}_{student.name[0].lower()} is, let the Student change it.")
        except Exception as e:
            raise Exception("Failed to save Student: " + str(e))
    
    def borrow_book(student_id, book_id):
        try:
            # Update the book's is_borrowed status to True
            CURSOR.execute(
                """
                UPDATE books
                SET is_borrowed = 1
                WHERE id = ?;
                """,
                (book_id,)
            )
            
            # then insert a record into the borrowed_books table
            CURSOR.execute(
                """
                INSERT INTO borrowed_books (student_id, book_id) VALUES (?, ?);
                """,
                (student_id, book_id)
            )
            
            CONN.commit()
            print(f"Book borrowed successfully. Enjoy your reading!")
        except Exception as e:
            CONN.rollback() # Rollback means undo all the db operations if any of them fails
            raise Exception("Failed to borrow book: " + str(e))
        
    def return_book(student_id, book_id):
        try:
            # Update the book's is_borrowed status to False
            CURSOR.execute(
                """
                UPDATE books
                SET is_borrowed = 0
                WHERE id = ?;
                """,
                (book_id,)
            )
            
            # then remove the record from the borrowed_books table
            CURSOR.execute(
                """
                DELETE FROM borrowed_books
                WHERE student_id = ? AND book_id = ?;
                """,
                (student_id, book_id)
            )
            
            CONN.commit()
            print(f"Book returned successfully. Hope you enjoyed reading it!")
        except Exception as e:
            CONN.rollback()
            raise Exception("Failed to return book: " + str(e))
        
    # The Join query joins books and borrowed_books tables to get the list of books borrowed by a specific student
    # Incase you dontt understand the query, ask me via mattermost
    @staticmethod
    def list_borrowed_books(student_id):
        try:
            CURSOR.execute(
                """
                SELECT b.id, b.title 
                FROM books b
                JOIN borrowed_books bb ON b.id = bb.book_id
                WHERE bb.student_id = ?;
                """,
                (student_id,)
            )
            return CURSOR.fetchall()
        except Exception as e:
            raise Exception("Failed to list borrowed books: " + str(e))