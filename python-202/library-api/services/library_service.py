import json
import os
from typing import List, Optional
from models.book_model import Book, create_book_from_dict

class LibraryService:
    """Manages library operations and book storage."""
    
    def __init__(self, filename: str = "library.json"):
        self.filename = filename
        self.books: List[Book] = []
        self.load_books()
    
    def add_book(self, book: Book) -> bool:
        """Adds a book if ISBN doesn't already exist."""
        if self.find_book(book.isbn):
            return False
        
        self.books.append(book)
        self.save_books()
        return True
    
    def remove_book(self, isbn: str) -> bool:
        """Removes a book by ISBN, returns True if found and removed."""
        book = self.find_book(isbn)
        if book:
            self.books.remove(book)
            self.save_books()
            return True
        return False
    
    def list_books(self) -> List[Book]:
        return self.books.copy()
    
    def find_book(self, isbn: str) -> Optional[Book]:
        """Returns the book with matching ISBN, or None if not found."""
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def load_books(self) -> None:
        """Loads books from JSON file, creates empty list if file doesn't exist."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    self.books = []
                    for book_data in data:
                        self.books.append(create_book_from_dict(book_data))
            except (json.JSONDecodeError, FileNotFoundError):
                self.books = []
        else:
            self.books = []
    
    def save_books(self) -> None:
        """Saves current book list to JSON file."""
        data = []
        for book in self.books:
            data.append(book.to_dict())
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
