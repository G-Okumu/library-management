from repositories.user_repository import UserRepository
import hashlib

class UserService():
    # Change this method later on to only generate user_id but not save
    # which means in the user repository, we will have to split the create_user method into two
    # one that generates user_id and another that saves the user to the database
    def add_user(user):
        user_id = UserRepository.create_user(user)        
        return user_id
        
    def get_login_details(username):
        user = UserRepository.find_by_username(username)
        
        # For now, jsut access the values in an awkward manner,
        return user
    
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()