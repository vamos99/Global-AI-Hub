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

### Kurulum Adımları

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

## Kullanım

### Aşama 1: CLI Uygulaması

Terminal uygulamasını çalıştırın:
```bash
python main.py
```

**Menü Seçenekleri:**
- `1` - Kitap Ekle (title, author, ISBN)
- `2` - Kitap Sil (ISBN ile)
- `3` - Kitapları Listele
- `4` - Kitap Ara (ISBN ile)
- `5` - Çıkış

**Veri Saklama:** Kitaplar `library.json` dosyasında kalıcı olarak saklanır.

**ISBN Validasyonu:** 10 veya 13 haneli ISBN formatı kontrol edilir.

### Testler

Birim testlerini çalıştırmak için:
```bash
python -m pytest tests/ -v
```

**Test Kapsamı:**
- ✅ Book sınıfı testleri
- ✅ LibraryService metodları
- ✅ JSON dosya işlemleri
- ✅ ISBN validasyon testleri
- ✅ Hata durumları

## Teknik Özellikler

### OOP Tasarım
- **Book Sınıfı:** Kitap verilerini temsil eder
  - `title`, `author`, `isbn` nitelikleri
  - `__str__()` metodu ile okunaklı gösterim ("Ulysses by James Joyce (ISBN: 978-0199535675)")
  - `to_dict()` ve `from_dict()` metodları
  - ISBN format validasyonu

- **LibraryService Sınıfı:** Kütüphane işlemlerini yönetir
  - `add_book()`, `remove_book()`, `find_book()`
  - `list_books()`, `load_books()`, `save_books()`
  - JSON dosya entegrasyonu

### Veri Yönetimi
- **JSON Formatı:** İnsan okunabilir veri saklama
- **Kalıcılık:** Uygulama kapatılıp açıldığında veriler korunur
- **Hata Yönetimi:** Dosya okuma/yazma hatalarına karşı koruma
- **ISBN Validasyonu:** Geçersiz ISBN formatları reddedilir

## Geliştirme Aşamaları

### ✅ Aşama 1: OOP ile CLI Uygulaması
- [x] Book sınıfı oluşturuldu (title, author, ISBN)
- [x] LibraryService sınıfı oluşturuldu
- [x] CLI menü sistemi (1-5 seçenekler)
- [x] JSON veri saklama (library.json)
- [x] ISBN format validasyonu
- [x] Kapsamlı birim testleri (pytest)

### 🔄 Aşama 2: Harici API Entegrasyonu (Yakında)
- [ ] Open Library Books API entegrasyonu
- [ ] ISBN ile otomatik kitap bilgisi çekme
- [ ] httpx kütüphanesi kullanımı
- [ ] Hata yönetimi ("Kitap bulunamadı.")

### ⏳ Aşama 3: FastAPI Web Servisi (Yakında)
- [ ] FastAPI endpoint'leri (GET /books, POST /books, DELETE /books/{isbn})
- [ ] Pydantic modelleri
- [ ] Otomatik dokümantasyon (/docs)
- [ ] API testleri

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
