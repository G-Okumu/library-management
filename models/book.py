class Book:
    
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.borrowers = [] # how many students have borrowd this book, many-to-many relationship
    
    
    def print_book_details(self):
        return f"{self.title} {self.isbn}"
    

