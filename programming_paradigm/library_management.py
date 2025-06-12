class Book:
    """Book class with public attributes title and author, and private attribute is_checked_out"""
    
    def __init__(self, title, author):
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """Check out method"""
        self._is_checked_out = True
    
    def return_book(self):
        """Return book method"""
        self._is_checked_out = False
    
    def is_available(self):
        """Check if book is available"""
        return not self._is_checked_out


class Library:
    """Library class with private list _books to store instances of Book"""
    
    def __init__(self):
        self._books = []  # Private list to store Book instances
    
    def add_book(self, book):
        """Add book method"""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out book method"""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False
    
    def return_book(self, title):
        """Return book method"""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False
    
    def listavailablebooks(self):
        """List available books method"""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")


# Test the implementation
if __name__ == "__main__":
    # Create library
    library = Library()
    
    # Create books
    book1 = Book("Brave New World", "Aldous Huxley")
    book2 = Book("1984", "George Orwell")
    
    # Add books to library
    library.add_book(book1)
    library.add_book(book2)
    
    # Show available books
    print("Available books after setup:")
    for book in library.listavailablebooks():
        print(f"{book.title} by {book.author}")
    
    # Check out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    for book in library.listavailablebooks():
        print(f"{book.title} by {book.author}")
    
    # Return the book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    for book in library.listavailablebooks():
        print(f"{book.title} by {book.author}")
