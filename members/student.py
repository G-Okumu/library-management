from .member import Member

class Student(Member):
    
    def __init__(self, name, member_id, grade_level):
        super().__init__(name, member_id)
        self.grade_level = grade_level
        self.borrowed_books = []
        
    # Allow student to borrow the book
    def borrow_book(self, book):
        self.borrowed_books.append(book)
        
    # Returning  a book
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            print("Yoooooh!! You are returning a wrong book")
        
    # prints all books that the student has borrrowed
    def print_all_books_borrowed(self):
        return self.borrowed_books
        
    def get_student_details(self):
        return super().get_details()
        


