"""

This class will manage books<Borrowing/Return> of Books

"""

class Library:
    
    def __init__(self, name):
        self.name = name
        self.books = [] # library to books one-to-many , one library can contain many books
        
    # This add book is an instance method taking the book object
    def add_book(self, book):
        self.books.append(book)
        
    
    # List all books that are in the Library
    def list_books(self):
        return self.books
        
        
