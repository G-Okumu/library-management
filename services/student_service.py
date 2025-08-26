from repositories.student_repository import StudentRepository
from .user_service import UserService
from models.student import Student
from models.user import User

class StudentService:
    
    def create_student(name):
        user_id = UserService.add_user(User(name, "Password1234!", "student"))
        
        student = Student(name, user_id) # This user_id not saved in the DB?? I dont know why, maybe I check it later within the constructor
        StudentRepository.save(student)
    
    # During refactoring, these methods can be combined into one method in the future
    def borrow_book(student_id, book_id):
        StudentRepository.borrow_book(student_id, book_id)
        
    def return_book(student_id, book_id):
        StudentRepository.return_book(student_id, book_id)
        
    def list_borrowed_books(student_id):
        return StudentRepository.list_borrowed_books(student_id)