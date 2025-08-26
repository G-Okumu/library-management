from repositories.library_repository import LibraryRepository

class LibraryService():
    
    def create_library(name):
        LibraryRepository.save(name)
        
    def list_libraries():
        return LibraryRepository.get_all_libraries()
        
