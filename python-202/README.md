# Python 202 Bootcamp - Library API

Bu klasör, **Python 202 Bootcamp** eğitim programında geliştirilen **Library API** projesini içerir.

## Proje: Library API

Bu proje, **Python 202 Bootcamp**'inde öğrenilen üç temel konuyu (OOP, Harici API Kullanımı, FastAPI) birleştiren kapsamlı bir kütüphane yönetim sistemidir.

### Proje Amacı

Bu proje, Python 202 Bootcamp'inde öğreneceğiniz üç temel konuyu (OOP, Harici API Kullanımı, Kendi API'nizi FastAPI ile Yazma) birleştirerek somut bir ürün ortaya çıkarmanızı amaçlamaktadır. Proje üç aşamadan oluşur ve her aşama bir önceki üzerine inşa edilir.

Amacımız, basit bir komut satırı uygulamasından başlayarak, onu harici verilerle zenginleştirmek ve son olarak bir web servisi haline getirmektir.

## Proje Yapısı

```
Global-AI-Hub/
└── python-202/
    └── library-api/
        ├── models/              # Veri modelleri (Book sınıfı)
        │   └── book_model.py
        ├── services/            # İş mantığı (LibraryService)
        │   └── library_service.py
        ├── tests/              # Birim testleri
        │   └── test_library_service.py
        ├── main.py             # CLI uygulaması
        └── requirements.txt    # Python bağımlılıkları
```

## Kurulum

### Gereksinimler
- **Python 3.13+**
- **UV paket yöneticisi** (modern ve hızlı)

### Kurulum Adımları (UV ile)

1. **Projeyi klonlayın:**
```bash
git clone https://github.com/vamos99/Global-AI-Hub.git
cd Global-AI-Hub/python-202/library-api
```

2. **UV ile sanal ortam oluşturun:**
```bash
uv venv
source .venv/bin/activate
```

3. **Bağımlılıkları kurun:**
```bash
uv pip install -r requirements.txt
```

### Alternatif (pip ile)

1. Sanal ortam oluşturun ve aktive edin:
```bash
python -m venv .venv
source .venv/bin/activate
```
2. Bağımlılıkları kurun:
```bash
pip install -r requirements.txt
```

## Kullanım (Aşama 1 → Aşama 2 → Aşama 3)

### Aşama 1: CLI Uygulaması

Terminal uygulamasını çalıştırın:
```bash
python main.py
```

**Menü Seçenekleri:**
- `1` - Kitap Ekle (Aşama 2’de ISBN ile otomatik ekleme)
- `2` - Kitap Sil (ISBN ile)
- `3` - Kitapları Listele
- `4` - Kitap Ara (ISBN ile)
- `5` - Çıkış

**Veri Saklama:** Kitaplar `library.json` dosyasında kalıcı olarak saklanır.

**ISBN Validasyonu:** 10 veya 13 haneli ISBN formatı kontrol edilir.

### Aşama 2: ISBN ile Otomatik Ekleme (CLI)

1. Uygulamayı çalıştırın:
```bash
python main.py
```
2. `1` seçeneğini girin ve yalnızca ISBN yazın (ör: `9780441172719`).
3. Başarılıysa `library.json` güncellenir, `3` ile listeleyebilirsiniz.

Notlar:
- İnternet bağlantısı gereklidir.
- Open Library API yoğun kullanımda tanımlı bir User-Agent bekleyebilir.
## Testler (Tüm Aşamalar)

Tüm testleri çalıştırın:
```bash
uv run python -m pytest tests/ -v
```

Yalnız Aşama 1-2 testleri:
```bash
uv run python -m pytest tests/test_library_service.py -v
```

Yalnız Aşama 3 testleri:
```bash
uv run python -m pytest tests/test_api.py -v
```

 

## Teknik Özellikler

### OOP Tasarım
- **Book Sınıfı:** Kitap verilerini temsil eder
  - `title`, `author`, `isbn` nitelikleri
  - `__str__()` metodu ile okunaklı gösterim ("Ulysses by James Joyce (ISBN: 978-0199535675)")
  - `to_dict()` ve `create_book_from_dict()` yardımcıları
  - ISBN format validasyonu

- **LibraryService Sınıfı:** Kütüphane işlemlerini yönetir
  - `add_book(isbn)`, `add_book_by_isbn(isbn)`, `remove_book(isbn)`, `find_book(isbn)`
  - `list_books()`, `load_books()`, `save_books()`
  - JSON dosya entegrasyonu
  - Open Library entegrasyonu için `httpx` kullanımı, User-Agent ve yönlendirme (follow_redirects) desteği

### Veri Yönetimi
- **JSON Formatı:** İnsan okunabilir veri saklama
- **Kalıcılık:** Uygulama kapatılıp açıldığında veriler korunur
- **Hata Yönetimi:** Dosya okuma/yazma hatalarına karşı koruma
- **ISBN Validasyonu:** Geçersiz ISBN formatları reddedilir

## Geliştirme Aşamaları

### Aşama 1: OOP ile CLI Uygulaması
- [x] Book sınıfı (title, author, ISBN)
- [x] LibraryService
- [x] CLI menü sistemi (1-5 seçenekler)
- [x] JSON veri saklama (library.json)
- [x] ISBN format validasyonu
- [x] Birim testleri (pytest)

### Aşama 2: Harici API Entegrasyonu
- [x] Open Library Books API entegrasyonu (httpx)
- [x] ISBN ile otomatik kitap bilgisi çekme (title, authors)
- [x] Hata yönetimi (404, ağ/HTTP, JSON)
- [x] Mock’lu birim testleri (başarı, 404, network senaryoları)

### Aşama 3: FastAPI Web Servisi (Yakında)
- [x] FastAPI endpoint'leri (GET /books, POST /books, DELETE /books/{isbn})
- [x] Pydantic modelleri
- [x] Otomatik dokümantasyon (/docs)
- [x] API testleri

## Aşama 3 Kullanım (FastAPI)

1. Bağımlılıkları kurun:
```bash
uv pip install -r requirements.txt
```
2. API’yi başlatın:
```bash
uv run uvicorn api:app --reload
```
3. Dokümantasyon:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

4. Örnek istekler:
- GET /books
- POST /books  Body: {"isbn": "9780441172719"}
- DELETE /books/{isbn}

#### cURL örnekleri

- GET /books
```bash
curl -s http://127.0.0.1:8000/books
```

- POST /books
```bash
curl -s -X POST http://127.0.0.1:8000/books \
  -H "Content-Type: application/json" \
  -d '{"isbn":"9780441172719"}'
```

- DELETE /books/{isbn}
```bash
curl -i -X DELETE http://127.0.0.1:8000/books/9780441172719
```

#### Python httpx ile örnek (isteğe bağlı)
```python
import httpx

with httpx.Client() as c:
    r = c.post("http://127.0.0.1:8000/books", json={"isbn": "9780441172719"})
    print(r.status_code, r.json())
```


## Geliştirme

### Kod Standartları
- **Type Hints:** Tüm fonksiyonlarda tip belirtimi
- **Docstrings:** Sınıf ve metod açıklamaları
- **Error Handling:** Try-except blokları
- **Testing:** Pytest ile kapsamlı test kapsamı

### Katkıda Bulunma
1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## Lisans

Bu proje eğitim amaçlıdır

## İletişim

Sorularınız için GitHub Issues kullanabilirsiniz.
