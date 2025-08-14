from books.library import Library
from members.librarian import Librarian
from members.student import Student
from books.book import Book


def main():
    # creating  instances
    sekotiek_library = Library("Sekotiek")
    
    book1 = Book("Mathematics B8", "6726763KL")
    book2 = Book("Chemistry", "8932892CM")

    librarian = Librarian("Ayub Karanja", 89993)
    
    student1 = Student("Newton", "LMS-67263", 7)
    student2 = Student("Natasha", "LMS-8976K", 9)
    
    
    # librarian adding books
    librarian.add_book(sekotiek_library, book1)
    librarian.add_book(sekotiek_library, book2)

    
    ## display books in library
    for ab in sekotiek_library.list_books():
        print(ab.title, ab.isbn)
        
    ## students borrowing and returning
    student1.borrow_book(book1)
    student1.borrow_book(book2)
    
    student1.return_book(book1)
    
    print("======================")
    print("======================")
    
    # display all student borrowed books
    print("Books Borrowed by:", student1.name)
    for student_book in student1.print_all_books_borrowed():
        print({"book_name": student_book.title, "isbn": student_book.isbn})
       
    
    

if __name__ == "__main__":
    main()