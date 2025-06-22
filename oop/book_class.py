class Book:
    """A class representing a book with magic methods for enhanced functionality."""
    
    def __init__(self, title, author, year):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """Destructor that prints a deletion message when the book object is deleted."""
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        String representation method.
        
        Returns:
            str: A formatted string in the format "(title) by (author), published in (year)"
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Official representation method.
        
        Returns:
            str: A string that would recreate the Book instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
