import json
import os
from typing import List, Optional

import httpx

from models.book_model import Book, create_book_from_dict


class LibraryService:
    """Manages library operations and book storage."""

    def __init__(self, filename: str = "library.json"):
        self.filename = filename
        self.books: List[Book] = []
        self.load_books()

    def add_book_by_isbn(self, isbn: str) -> bool:
        """Fetches book data by ISBN via Open Library and saves it.
        Returns True if added, False otherwise.
        """
        if self.find_book(isbn):
            return False

        fetched = self._fetch_book_from_open_library(isbn)
        if not fetched:
            return False

        title, author = fetched
        book = Book(title=title, author=author, isbn=isbn)
        self.books.append(book)
        self.save_books()
        return True

    def add_book(self, isbn: str) -> bool:
        return self.add_book_by_isbn(isbn)

    def remove_book(self, isbn: str) -> bool:
        book = self.find_book(isbn)
        if book:
            self.books.remove(book)
            self.save_books()
            return True
        return False

    def list_books(self) -> List[Book]:
        return self.books.copy()

    def find_book(self, isbn: str) -> Optional[Book]:
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def load_books(self) -> None:
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
        data = []
        for book in self.books:
            data.append(book.to_dict())
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def _fetch_book_from_open_library(self, isbn: str) -> Optional[tuple[str, str]]:
        base_url = f"https://openlibrary.org/isbn/{isbn}.json"
        try:
            headers = {
                "User-Agent": "python-202-library-api/1.0",
                "Accept": "application/json",
            }
            with httpx.Client(timeout=10.0, headers=headers, follow_redirects=True) as client:
                resp = client.get(base_url)
                if resp.status_code == 404:
                    return None
                resp.raise_for_status()
                try:
                    data = resp.json()
                except json.JSONDecodeError:
                    return None

                title = data.get("title")
                authors_field = data.get("authors", [])

                authors: List[str] = []
                for a in authors_field:
                    key = a.get("key")
                    if not key:
                        continue
                    a_resp = client.get(f"https://openlibrary.org{key}.json")
                    if a_resp.status_code == 404:
                        continue
                    try:
                        a_resp.raise_for_status()
                        a_data = a_resp.json()
                        name = a_data.get("name")
                        if name:
                            authors.append(name)
                    except (httpx.HTTPError, json.JSONDecodeError):
                        continue

                author_joined = ", ".join(authors) if authors else ""

                if not title:
                    return None
                return title, author_joined
        except httpx.HTTPStatusError:
            return None
        except httpx.RequestError:
            return None
