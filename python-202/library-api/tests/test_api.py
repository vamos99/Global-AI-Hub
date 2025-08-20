from fastapi.testclient import TestClient
from unittest.mock import patch, Mock
import httpx
import tempfile
import os

from api import app
from services.library_service import LibraryService


def override_library(tmp_path):
    db = tmp_path / "api_lib.json"
    app.state.library = LibraryService(str(db))
    return app.state.library


def test_get_books_empty(tmp_path):
    library = override_library(tmp_path)
    client = TestClient(app)

    resp = client.get("/books")
    assert resp.status_code == 200
    assert resp.json() == []


def test_post_books_success_with_openlibrary(tmp_path):
    library = override_library(tmp_path)
    client = TestClient(app)

    # Mock httpx flow (book + author)
    book_resp = Mock(); book_resp.status_code = 200; book_resp.json.return_value = {
        "title": "Dune", "authors": [{"key": "/authors/OL2162288A"}]
    }
    author_resp = Mock(); author_resp.status_code = 200; author_resp.json.return_value = {"name": "Frank Herbert"}

    client_mock = Mock()
    client_mock.get.side_effect = [book_resp, author_resp]
    client_mock.__enter__ = Mock(return_value=client_mock)
    client_mock.__exit__ = Mock(return_value=None)

    with patch("httpx.Client", return_value=client_mock):
        resp = client.post("/books", json={"isbn": "9780441172719"})
        assert resp.status_code == 201
        body = resp.json()
        assert body["title"] == "Dune"
        assert body["author"] == "Frank Herbert"
        assert body["isbn"] == "9780441172719"


def test_post_books_conflict(tmp_path):
    library = override_library(tmp_path)
    client = TestClient(app)

    # İlk ekleme mock ile başarılı olsun
    book_resp = Mock(); book_resp.status_code = 200; book_resp.json.return_value = {
        "title": "Dune", "authors": []
    }
    client_mock = Mock(); client_mock.get.side_effect = [book_resp]
    client_mock.__enter__ = Mock(return_value=client_mock)
    client_mock.__exit__ = Mock(return_value=None)

    with patch("httpx.Client", return_value=client_mock):
        resp = client.post("/books", json={"isbn": "9780000000001"})
        assert resp.status_code == 201

    # Aynı ISBN tekrar eklenirse 409
    resp2 = client.post("/books", json={"isbn": "9780000000001"})
    assert resp2.status_code == 409


def test_post_books_not_found(tmp_path):
    library = override_library(tmp_path)
    client = TestClient(app)

    # 404 akışı
    book_resp = Mock(); book_resp.status_code = 404
    client_mock = Mock(); client_mock.get.side_effect = [book_resp]
    client_mock.__enter__ = Mock(return_value=client_mock)
    client_mock.__exit__ = Mock(return_value=None)

    with patch("httpx.Client", return_value=client_mock):
        resp = client.post("/books", json={"isbn": "000"})
        assert resp.status_code == 404


def test_delete_books_ok_and_404(tmp_path):
    library = override_library(tmp_path)
    client = TestClient(app)

    # Önce bir kitap ekleyelim (mock ile)
    book_resp = Mock(); book_resp.status_code = 200; book_resp.json.return_value = {
        "title": "Dune", "authors": []
    }
    client_mock = Mock(); client_mock.get.side_effect = [book_resp]
    client_mock.__enter__ = Mock(return_value=client_mock)
    client_mock.__exit__ = Mock(return_value=None)

    with patch("httpx.Client", return_value=client_mock):
        resp = client.post("/books", json={"isbn": "9780000000002"})
        assert resp.status_code == 201

    # Silme 204
    resp_del = client.delete("/books/9780000000002")
    assert resp_del.status_code == 204

    # Tekrar silme 404
    resp_del2 = client.delete("/books/9780000000002")
    assert resp_del2.status_code == 404


