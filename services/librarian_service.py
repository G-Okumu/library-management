from repositories.librarian_repository import LibrarianRepository
from .user_service import UserService
from models.librarian import Librarian
from models.user import User

class LibrarianService:
    
    def create_librarian(name, library_id):
        # When creating a librarian, we need to create a user role in advance before adding the librarian to the system
        # Remember the librarian needs a user_id to link to the user table
        user_id = UserService.add_user(User(name, "Password1234!", "librarian"))
        
        librarian = Librarian(name, library_id, user_id)
        LibrarianRepository.save(librarian)
