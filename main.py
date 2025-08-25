from services.user_service import UserService
from models.user import User

def main():
    print("Hello user, welcome to Library management System")
    print("I guess you are an admin, feel free to add users now")
    
    while True:
        print("\n1. Add user")
        print("2. Add Librarian")
        print("3. Exit")
        
        choice = input("choose:  ")
        
        if choice == "1":
            print("                                                                      ")
            print("Good choice, seems like you are the admin, now give out the following:")
            
            username = input("Enter a username: ")
            password = input("Create password for this user: ")
            role = input("Add role for this person: ")
            
            try:
                UserService.add_user(User(username, password, role))
            except Exception as e:
                print(f"Exception {e} occured")
            
        
        elif choice == "2":
            pass
        else:
            break
            
    
    
        
if __name__ == "__main__":
    main()    