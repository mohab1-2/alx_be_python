#!/usr/bin/env python3
"""
Library Management System
Author: Assistant
Date: June 2025

This module implements a Library Management System with Book and Library classes
for managing book collections, checkouts, and returns.
"""

class Book:
    """
    A class representing a book in the library system.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
        isbn (str): The ISBN of the book
        is_checked_out (bool): Whether the book is currently checked out
    """
    
    def __init__(self, title, author, isbn):
        """
        Initialize a new book.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            isbn (str): The ISBN of the book
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False
    
    def check_out(self):
        """
        Check out the book if it's available.
        
        Returns:
            bool: True if successfully checked out, False if already checked out
        """
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """
        Return the book if it's currently checked out.
        
        Returns:
            bool: True if successfully returned, False if not checked out
        """
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False
    
    def __str__(self):
        """
        String representation of the book.
        
        Returns:
            str: Formatted string with book information
        """
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"


class Library:
    """
    A class representing a library that manages a collection of books.
    
    Attributes:
        books (list): List of Book objects in the library
        name (str): Name of the library
    """
    
    def __init__(self, name="Library"):
        """
        Initialize a new library.
        
        Args:
            name (str): Name of the library (default: "Library")
        """
        self.books = []
        self.name = name
    
    def add_book(self, book):
        """
        Add a book to the library collection.
        
        Args:
            book (Book): The book object to add to the library
            
        Returns:
            bool: True if book was added successfully
        """
        if isinstance(book, Book):
            self.books.append(book)
            return True
        return False
    
    def check_out_book(self, isbn):
        """
        Check out a book by its ISBN.
        
        Args:
            isbn (str): The ISBN of the book to check out
            
        Returns:
            bool: True if book was successfully checked out, False otherwise
        """
        for book in self.books:
            if book.isbn == isbn and not book.is_checked_out:
                return book.check_out()
        return False
    
    def return_book(self, isbn):
        """
        Return a book by its ISBN.
        
        Args:
            isbn (str): The ISBN of the book to return
            
        Returns:
            bool: True if book was successfully returned, False otherwise
        """
        for book in self.books:
            if book.isbn == isbn and book.is_checked_out:
                return book.return_book()
        return False
    
    def list_available_books(self):
        """
        Get a list of all available (not checked out) books.
        
        Returns:
            list: List of Book objects that are available for checkout
        """
        available_books = []
        for book in self.books:
            if not book.is_checked_out:
                available_books.append(book)
        return available_books
    
    def list_all_books(self):
        """
        Get a list of all books in the library.
        
        Returns:
            list: List of all Book objects in the library
        """
        return self.books.copy()
    
    def find_book_by_title(self, title):
        """
        Find books by title (case-insensitive partial match).
        
        Args:
            title (str): The title to search for
            
        Returns:
            list: List of Book objects matching the title
        """
        matching_books = []
        for book in self.books:
            if title.lower() in book.title.lower():
                matching_books.append(book)
        return matching_books
    
    def find_book_by_author(self, author):
        """
        Find books by author (case-insensitive partial match).
        
        Args:
            author (str): The author to search for
            
        Returns:
            list: List of Book objects by the author
        """
        matching_books = []
        for book in self.books:
            if author.lower() in book.author.lower():
                matching_books.append(book)
        return matching_books
    
    def get_library_stats(self):
        """
        Get statistics about the library.
        
        Returns:
            dict: Dictionary containing library statistics
        """
        total_books = len(self.books)
        available_books = len(self.list_available_books())
        checked_out_books = total_books - available_books
        
        return {
            'total_b
