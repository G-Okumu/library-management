from services.auth_service import AuthenticationService 
from services.user_service import UserService
from models.user import User

def main():
    auth_service = AuthenticationService()

    print("Login required")
    username = input("Username: ")
    password = input("Password: ")

    try:
        current_user = auth_service.login(username, password)
    except Exception as e:
        print("Login failed:", e)
        return

    print(f"Welcome {current_user.username} ({current_user.role})")
    
        
if __name__ == "__main__":
    main()    