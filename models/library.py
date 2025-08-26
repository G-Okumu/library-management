"""

This class will manage books<Borrowing/Return> of Books

"""

class Library:
    
    def __init__(self, name):
        self.id = None
        self.name = name
        # self.books = [] # library to books one-to-many , one library can contain many books