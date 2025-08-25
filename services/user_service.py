from repositories.user_repository import UserRepository
import hashlib

class UserService():
    def add_user(user):
        UserRepository.create_user(user)
        print(f"Thank you, you've just created {user.role}")
        
    def get_login_details(username):
        user = UserRepository.find_by_username(username)  ## destructure or unpack specific attributes from the tuple
        
        # For now, jsut access the values in an awkward manner,
        return user
    
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()