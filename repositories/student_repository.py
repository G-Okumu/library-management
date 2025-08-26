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
        