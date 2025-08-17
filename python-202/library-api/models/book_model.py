import re

class Book:
    """Represents a single book in our library."""
    
    def __init__(self, title: str, author: str, isbn: str):
        if not self._validate_isbn(isbn):
            raise ValueError("Geçersiz ISBN formatı")
        
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def _validate_isbn(self, isbn: str) -> bool:
        """Validates ISBN format (10 or 13 digits, supports ISBN-10 with 'X')."""
        if not isbn or not isbn.strip():
            return False
        
        clean_isbn = re.sub(r'[-\s]', '', isbn)
        
        if len(clean_isbn) not in [10, 13]:
            return False
        
        if not clean_isbn[:-1].isdigit():
            return False
        
        # ISBN-10: last character can be digit or 'X'
        if len(clean_isbn) == 10 and not (clean_isbn[-1].isdigit() or clean_isbn[-1].upper() == 'X'):
            return False
        
        # ISBN-13: last character must be digit
        if len(clean_isbn) == 13 and not clean_isbn[-1].isdigit():
            return False
        
        return True
    
    def __str__(self) -> str:
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
    
    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn
        }

def create_book_from_dict(data: dict) -> Book:
    return Book(
        title=data["title"],
        author=data["author"],
        isbn=data["isbn"]
    )
