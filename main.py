from services.auth_service import AuthenticationService 
from services.user_service import UserService
from services.library_service import LibraryService
from services.librarian_service import LibrarianService
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
            print("3. Add a user")
            print("4. Add a student")
            print("5. Exit")
            print("                     ")
            choice = input("")
            
            if choice == "1":
                library_name = input("Enter library name: ")
                LibraryService.create_library(library_name)
            
            elif choice == "2":
                name = input("Enter librarian's name: ")
                print("Choose library ID from the following list: \n")
                
                libraries = LibraryService.list_libraries()
                for lib in libraries:
                    print(f"ID: {lib[0]}, Name: {lib[1]}")
            
                library_id = int(input("\nEnter library ID: "))
                
                LibrarianService.create_librarian(name, library_id)
                
            elif choice == "3":
                username = input("Enter users username: ")
                password = input("Create a unique password for the user: ")
                role = input("Assign role to the user: ")
                
                user = User(username, password, role)
                
                UserService.add_user(user)
            else:
                break
        
if __name__ == "__main__":
    main()    