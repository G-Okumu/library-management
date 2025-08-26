from models.user import User

from services.auth_service import AuthenticationService 
from services.user_service import UserService
from services.library_service import LibraryService
from services.librarian_service import LibrarianService
from services.student_service import StudentService
from services.book_service import BookService

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
            elif choice == "4":
                name = input("Enter Student's name: ")
                
                StudentService.create_student(name)
            else:
                break
        if current_user[3] == 'librarian':
            print("                                            ")
            print("What do you want to achieve today?")
            
            print("\n1. Record a book")
            print("2. Approve a book borrow request")
            print("3. Approve a book return request")
            print("4. Exit")
            print("                     ")
            
            choice = input("")
            if choice == "1":
                title = input("Enter book title: ")
                
                print("Choose library ID from the following list: \n")
                libraries = LibraryService.list_libraries()
                for lib in libraries:
                    print(f"ID: {lib[0]}, Name: {lib[1]}")
            
                library_id = int(input("\nEnter library ID: "))
                
                BookService.create_book(title, library_id)
                
            elif choice == "2":
                pass
                
            elif choice == "3":
                pass
            else:
                break
            
        if current_user[3] == 'student':
            print("                                            ")
            print("What do you want to achieve today?")
            
            print("\n1. Borrow a book")
            print("2. Return a book")
            print("3. Logout")
            print("                     ")
            
            choice = input("")
            if choice == "1":
                print("Books available to borrow: \n")
                books = LibraryService.list_books()
                for book in books:
                    print(f"ID: {book[0]}, Title: {book[1]}")
                
                book_id = int(input("\nEnter the ID of the book you want to borrow: "))
                
                StudentService.borrow_book(current_user[0], book_id)
                
            elif choice == "2":
                print("Below are the Books you have borrowed: \n")
                books = StudentService.list_borrowed_books(current_user[0])
                for book in books:
                    print(f"ID: {book[0]}, Title: {book[1]}")
                
                book_id = int(input("\nEnter the ID of the book you want to return: "))
                StudentService.return_book(current_user[0], book_id)
            else:
                break
                    
        
if __name__ == "__main__":
    main()    