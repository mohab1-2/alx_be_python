class Book:
    """Book class with public attributes title and author, and private attribute is_checked_out"""
    
    def __init__(self, title, author):
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self.__is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """Method to check out a book - marks it as unavailable"""
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        else:
            return False
    
    def return_book(self):
        """Method to return a book - marks it as available"""
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        else:
            return False
    
    def is_available(self):
        """Method to check if book is available"""
        return not self.__is_checked_out
    
    def __str__(self):
        """String representation of the book"""
        status = "Available" if self.is_available() else "Checked out"
        return f"{self.title} by {self.author} - {status}"


class Library:
    """Library class with private list _books to store instances of Book"""
    
    def __init__(self):
        self.__books = []  # Private list to store Book instances
    
    def add_book(self, book):
        """Method to add a Book instance to the library"""
        if isinstance(book, Book):
            self.__books.append(book)
            return f"Book '{book.title}' added to the library."
        else:
            return "Only Book instances can be added to the library."
    
    def check_out_book(self, title):
        """Method to check out a book by title"""
        for book in self.__books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    return f"'{title}' has been checked out successfully."
                else:
                    return f"'{title}' is already checked out."
        return f"Book '{title}' not found in the library."
    
    def return_book(self, title):
        """Method to return a book by title"""
        for book in self.__books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    return f"'{title}' has been returned successfully."
                else:
                    return f"'{title}' was not checked out."
        return f"Book '{title}' not found in the library."
    
    def list_available_books(self):
        """Method to list all available books"""
        available_books = [book for book in self.__books if book.is_available()]
        if available_books:
            print("Available books after setup:")
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
    
    def listavailablebooks(self):
        """Method to list all available books (returns list for testing)"""
        available_books = [book for book in self.__books if book.is_available()]
        return available_books


# Test script (main.py functionality)
def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))
    
    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()
    
    print()  # Empty line for readability
    
    # Simulate checking out a book
    result = library.check_out_book("1984")
    print(f"Checking out book: {result}")
    print("Available books after checking out '1984':")
    library.list_available_books()
    
    print()  # Empty line for readability
    
    # Simulate returning a book
    result = library.return_book("1984")
    print(f"Returning book: {result}")
    print("Available books after returning '1984':")
    library.list_available_books()


if __name__ == "__main__":
    main()
