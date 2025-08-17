import pytest
import tempfile
import os
from services.library_service import LibraryService
from models.book_model import Book, create_book_from_dict

def test_add_book_success():
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json').name
    library_service = LibraryService(temp_file)
    sample_book = Book("Test Kitap", "Test Yazar", "978-1234567890")
    
    result = library_service.add_book(sample_book)
    assert result is True
    assert len(library_service.books) == 1
    assert library_service.books[0] == sample_book
    
    os.unlink(temp_file)

def test_add_book_duplicate_isbn():
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json').name
    library_service = LibraryService(temp_file)
    sample_book = Book("Test Kitap", "Test Yazar", "978-1234567890")
    
    library_service.add_book(sample_book)
    duplicate_book = Book("Farklı Kitap", "Farklı Yazar", sample_book.isbn)
    result = library_service.add_book(duplicate_book)
    assert result is False
    assert len(library_service.books) == 1
    
    os.unlink(temp_file)

def test_remove_book_success():
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json').name
    library_service = LibraryService(temp_file)
    sample_book = Book("Test Kitap", "Test Yazar", "978-1234567890")
    
    library_service.add_book(sample_book)
    result = library_service.remove_book(sample_book.isbn)
    assert result is True
    assert len(library_service.books) == 0
    
    os.unlink(temp_file)

def test_remove_book_not_found():
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json').name
    library_service = LibraryService(temp_file)
    
    result = library_service.remove_book("978-9999999999")
    assert result is False
    
    os.unlink(temp_file)

def test_find_book_success():
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json').name
    library_service = LibraryService(temp_file)
    sample_book = Book("Test Kitap", "Test Yazar", "978-1234567890")
    
    library_service.add_book(sample_book)
    found_book = library_service.find_book(sample_book.isbn)
    assert found_book == sample_book
    
    os.unlink(temp_file)

def test_find_book_not_found():
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json').name
    library_service = LibraryService(temp_file)
    
    found_book = library_service.find_book("978-9999999999")
    assert found_book is None
    
    os.unlink(temp_file)

def test_list_books():
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json').name
    library_service = LibraryService(temp_file)
    sample_book = Book("Test Kitap", "Test Yazar", "978-1234567890")
    
    library_service.add_book(sample_book)
    books = library_service.list_books()
    assert len(books) == 1
    assert books[0] == sample_book
    
    os.unlink(temp_file)

def test_save_and_load_books():
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json').name
    
    service1 = LibraryService(temp_file)
    book = Book("Test Kitap", "Test Yazar", "978-1234567890")
    service1.add_book(book)
    
    service2 = LibraryService(temp_file)
    assert len(service2.books) == 1
    assert service2.books[0].title == book.title
    assert service2.books[0].author == book.author
    assert service2.books[0].isbn == book.isbn
    
    os.unlink(temp_file)

def test_book_creation():
    book = Book("Test Kitap", "Test Yazar", "978-1234567890")
    assert book.title == "Test Kitap"
    assert book.author == "Test Yazar"
    assert book.isbn == "978-1234567890"

def test_book_str_representation():
    book = Book("Ulysses", "James Joyce", "978-0199535675")
    expected = "Ulysses by James Joyce (ISBN: 978-0199535675)"
    assert str(book) == expected

def test_book_to_dict():
    book = Book("Test Kitap", "Test Yazar", "978-1234567890")
    book_dict = book.to_dict()
    expected = {
        "title": "Test Kitap",
        "author": "Test Yazar",
        "isbn": "978-1234567890"
    }
    assert book_dict == expected

def test_create_book_from_dict():
    book_data = {
        "title": "Test Kitap",
        "author": "Test Yazar",
        "isbn": "978-1234567890"
    }
    book = create_book_from_dict(book_data)
    assert book.title == "Test Kitap"
    assert book.author == "Test Yazar"
    assert book.isbn == "978-1234567890"

# ISBN Validation Tests
def test_valid_isbn_13():
    book = Book("Test Kitap", "Test Yazar", "978-0-7475-3269-9")
    assert book.isbn == "978-0-7475-3269-9"

def test_valid_isbn_10():
    book = Book("Test Kitap", "Test Yazar", "0-7475-3269-9")
    assert book.isbn == "0-7475-3269-9"

def test_valid_isbn_10_with_x():
    book = Book("Test Kitap", "Test Yazar", "0-7475-3269-X")
    assert book.isbn == "0-7475-3269-X"

def test_invalid_isbn_too_short():
    with pytest.raises(ValueError, match="Geçersiz ISBN formatı"):
        Book("Test Kitap", "Test Yazar", "123")

def test_invalid_isbn_too_long():
    with pytest.raises(ValueError, match="Geçersiz ISBN formatı"):
        Book("Test Kitap", "Test Yazar", "1234567890123456")

def test_invalid_isbn_with_letters():
    with pytest.raises(ValueError, match="Geçersiz ISBN formatı"):
        Book("Test Kitap", "Test Yazar", "abc-def-ghi-j")

def test_invalid_isbn_empty():
    with pytest.raises(ValueError, match="Geçersiz ISBN formatı"):
        Book("Test Kitap", "Test Yazar", "")

def test_invalid_isbn_whitespace():
    with pytest.raises(ValueError, match="Geçersiz ISBN formatı"):
        Book("Test Kitap", "Test Yazar", "   ")

def test_isbn_without_hyphens():
    book = Book("Test Kitap", "Test Yazar", "9780747532699")
    assert book.isbn == "9780747532699"
