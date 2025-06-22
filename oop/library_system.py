class Book:
    """Base class representing a book with title and author attributes."""
    
    def __init__(self, title, author):
        """Initialize a Book instance with title and author."""
        self.title = title
        self.author = author
    
    def __str__(self):
        """Return string representation of the Book."""
        return "Book: {} by {}".format(self.title, self.author)


class EBook(Book):
    """EBook class that inherits from Book with additional file_size attribute."""
    
    def __init__(self, title, author, file_size):
        """Initialize an EBook instance with title, author, and file_size."""
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """Return string representation of the EBook."""
        return "EBook: {} by {}, File Size: {}MB".format(self.title, self.author, self.file_size)


class PrintBook(Book):
    """PrintBook class that inherits from Book with additional page_count attribute."""
    
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook instance with title, author, and page_count."""
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """Return string representation of the PrintBook."""
        return "PrintBook: {} by {}, Page Count: {}".format(self.title, self.author, self.page_count)


class Library:
    """Library class that manages a collection of books using composition."""
    
    def __init__(self):
        """Initialize a Library instance with an empty list of books."""
        self.books = []
    
    def add_book(self, book):
        """Add a book instance to the library."""
        if isinstance(book, Book):
            self.books.append(book)
    
    def list_books(self):
        """Print details of each book in the library."""
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(str(book))


# Test implementation to match expected output
def main():
    # Create library instance
    my_library = Library()
    
    # Create book instances
    regular_book = Book("Pride and Prejudice", "Jane Austen")
    digital_book = EBook("Pride and Prejudice", "Jane Austen", 500)
    physical_book = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
    
    # Add books to library
    my_library.add_book(regular_book)
    my_library.add_book(digital_book)
    my_library.add_book(physical_book)
    
    # Display all books
    my_library.list_books()


if __name__ == "__main__":
    main()
