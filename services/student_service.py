from repositories.student_repository import StudentRepository
from .user_service import UserService
from models.student import Student
from models.user import User

class StudentService:
    
    def create_student(name):
        user_id = UserService.add_user(User(name, "Password1234!", "student"))
        
        student = Student(name, user_id) # This user_id not saved in the DB?? I dont know why, maybe I check it later within the constructor
        StudentRepository.save(student)
