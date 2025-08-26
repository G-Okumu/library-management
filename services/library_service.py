from repositories.library_repository import LibraryRepository

class LibraryService():
    
    def create_library(name):
        LibraryRepository.save(name)
        
