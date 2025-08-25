class Librarian():
    
    def __init__(self, name, librarian_id):
        self.name = name
        self.librarian_id = librarian_id
        
    # Librarian adding the book to Library
    def add_book(self, library, book):
        library.add_book(book)
        
    def get_details(self):
        return f"Librarian name is {self.name} and  (ID is: {self.librarian_id})"