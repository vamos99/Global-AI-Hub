from typing import List

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import Response
from pydantic import BaseModel

from services.library_service import LibraryService


class IsbnIn(BaseModel):
    isbn: str


class BookOut(BaseModel):
    title: str
    author: str
    isbn: str


app = FastAPI(title="Library API", version="3.0.0")
app.state.library = LibraryService()


@app.get("/books", response_model=List[BookOut])
def get_books(request: Request) -> List[BookOut]:
    library: LibraryService = request.app.state.library
    books = library.list_books()
    return [BookOut(title=b.title, author=b.author, isbn=b.isbn) for b in books]


@app.post("/books", response_model=BookOut, status_code=status.HTTP_201_CREATED)
def create_book(payload: IsbnIn, request: Request) -> BookOut:
    library: LibraryService = request.app.state.library
    isbn = payload.isbn.strip()

    if not isbn:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ISBN boş olamaz")

    # Duplicate kontrolü
    existing = library.find_book(isbn)
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Bu ISBN ile kitap zaten mevcut")

    added = library.add_book(isbn)
    if not added:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Kitap bulunamadı veya eklenemedi")

    created = library.find_book(isbn)
    if not created:
        # Beklenmeyen durum
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Kitap ekleme başarısız")

    return BookOut(title=created.title, author=created.author, isbn=created.isbn)


@app.delete("/books/{isbn}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(isbn: str, request: Request) -> Response:
    library: LibraryService = request.app.state.library
    ok = library.remove_book(isbn)
    if not ok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bu ISBN ile kitap bulunamadı")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


