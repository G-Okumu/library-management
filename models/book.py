class Book:
    
    def __init__(self, title, library_id, isbn=None, is_borrowed=False):
        self.title = title
        self.library_id = library_id
        self.isbn = isbn
        self.is_borrowed = is_borrowed 
    
    # def print_book_details(self):
    #     return f"{self.title} {self.isbn}"
    

