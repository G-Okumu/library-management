from .user_service import UserService

class AuthenticationService():
    
    def login(self, username, password):
        user = UserService.get_login_details(username)
                    
        if not user or UserService.hash_password(password) != user[2]:
            raise Exception("Invalid credentials")
        
        return user
        