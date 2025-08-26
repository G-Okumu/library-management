from repositories.book_repository import BookRepository
from models.book import Book
        
class BookService:
    def create_book(title, library_id):
        book = Book(title, library_id)
        return BookRepository.save(book)