from services.auth_service import AuthenticationService 
from services.user_service import UserService
from services.library_service import LibraryService
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

    print(f"Welcome {current_user[1]} to the ({current_user[3]}) portal")
    
    while True:
        if current_user[3] == 'admin':
            print("                                            ")
            print("What do you want to achieve today?")
            
            print("\n1. Create a Library")
            print("2. Add a Librarian")
            print("2. Add a user")
            print("3. Add a student")
            print("4. Exit")
            
            choice = input("  :")
            
            if choice == "1":
                library_name = input("Enter library name: ")
                LibraryService.create_library(library_name)
                
            elif choice == "2":
                username = input("Enter users username: ")
                password = input("Create a unique password for the user: ")
                role = input("Assign role to the user: ")
                
                user = User(username, password, role)
                
                UserService.add_user(user)
            else:
                break
        
if __name__ == "__main__":
    main()    