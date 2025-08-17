from services.library_service import LibraryService
from models.book_model import Book

def main() -> None:
    """Main application loop."""
    library = LibraryService()
    
    while True:
        print("\n=== KÜTÜPHANE YÖNETİM SİSTEMİ ===")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitapları Listele")
        print("4. Kitap Ara")
        print("5. Çıkış")
        
        choice = input("\nSeçiminizi yapın (1-5): ").strip()
        
        if choice == "1":
            add_book_interface(library)
        elif choice == "2":
            remove_book_interface(library)
        elif choice == "3":
            list_books_interface(library)
        elif choice == "4":
            find_book_interface(library)
        elif choice == "5":
            print("Program sonlandırılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen 1-5 arası bir sayı girin.")

def add_book_interface(library: LibraryService) -> None:
    """Handles book addition with ISBN validation."""
    print("\n--- KİTAP EKLEME ---")
    title = input("Kitap başlığı: ").strip()
    author = input("Yazar adı: ").strip()
    isbn = input("ISBN: ").strip()
    
    if not title or not author or not isbn:
        print("Tüm alanlar doldurulmalıdır!")
        return
    
    try:
        book = Book(title, author, isbn)
        if library.add_book(book):
            print(f"Kitap başarıyla eklendi: {book}")
        else:
            print("Bu ISBN ile kitap zaten mevcut!")
    except ValueError as e:
        print(f"Hata: {e}")
        print("ISBN formatı: 10 veya 13 haneli olmalı (örn: 978-0-7475-3269-9)")

def remove_book_interface(library: LibraryService) -> None:
    """Handles book removal by ISBN."""
    print("\n--- KİTAP SİLME ---")
    isbn = input("Silinecek kitabın ISBN'i: ").strip()
    
    if library.remove_book(isbn):
        print("Kitap başarıyla silindi.")
    else:
        print("Bu ISBN ile kitap bulunamadı!")

def list_books_interface(library: LibraryService) -> None:
    """Displays all books in the library."""
    print("\n--- KİTAP LİSTESİ ---")
    books = library.list_books()
    
    if not books:
        print("Kütüphanede kitap bulunmuyor.")
    else:
        for i, book in enumerate(books, 1):
            print(f"{i}. {book}")

def find_book_interface(library: LibraryService) -> None:
    """Searches for a book by ISBN."""
    print("\n--- KİTAP ARAMA ---")
    isbn = input("Aranacak kitabın ISBN'i: ").strip()
    
    book = library.find_book(isbn)
    if book:
        print(f"Kitap bulundu: {book}")
    else:
        print("Bu ISBN ile kitap bulunamadı!")

if __name__ == "__main__":
    main()
