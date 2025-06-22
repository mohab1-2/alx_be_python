class Book:
    """Base class representing a book with title and author attributes."""
    
    def __init__(self, title, author):
        """Initialize a Book instance with title and author."""
        self.title = title
        self.author = author
    
    def __str__(self):
        """Return string representation of the Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """EBook class that inherits from Book with additional file_size attribute."""
    
    def __init__(self, title, author, file_size):
        """Initialize an EBook instance with title, author, and file_size."""
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """Return string representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}MB"


class PrintBook(Book):
    """PrintBook class that inherits from Book with additional page_count attribute."""
    
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook instance with title, author, and page_count."""
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """Return string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Library class that manages a collection of books using composition."""
    
    def __init__(self):
        """Initialize a Library instance with an empty list of books."""
        self.books = []
    
    def add_book(self, book):
        """Add a book instance to the library."""
        self.books.append(book)
    
    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)


# Test the implementation
if __name__ == "__main__":
    # Create library
    library = Library()
    
    # Create books
    book1 = Book("Pride and Prejudice", "Jane Austen")
    ebook1 = EBook("Pride and Prejudice", "Jane Austen", 500)
    printbook1 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
    
    # Add books to library
    library.add_book(book1)
    library.add_book(ebook1)
    library.add_book(printbook1)
    
    # List all books
    library.list_books()class Book:
    """Base class representing a book with title and author attributes."""
    
    def __init__(self, title, author):
        """Initialize a Book instance with title and author."""
        self.title = title
        self.author = author
    
    def __str__(self):
        """Return string representation of the Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """EBook class that inherits from Book with additional file_size attribute."""
    
    def __init__(self, title, author, file_size):
        """Initialize an EBook instance with title, author, and file_size."""
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """Return string representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}MB"


class PrintBook(Book):
    """PrintBook class that inherits from Book with additional page_count attribute."""
    
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook instance with title, author, and page_count."""
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """Return string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Library class that manages a collection of books using composition."""
    
    def __init__(self):
        """Initialize a Library instance with an empty list of books."""
        self.books = []
    
    def add_book(self, book):
        """Add a book instance to the library."""
        self.books.append(book)
    
    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)


# Test the implementation
if __name__ == "__main__":
    # Create library
    library = Library()
    
    # Create books
    book1 = Book("Pride and Prejudice", "Jane Austen")
    ebook1 = EBook("Pride and Prejudice", "Jane Austen", 500)
    printbook1 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
    
    # Add books to library
    library.add_book(book1)
    library.add_book(ebook1)
    library.add_book(printbook1)
    
    # List all books
    library.list_books()
