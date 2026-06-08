# Python 202 - Library API

Bu klasor, Python 202 egitiminde gelistirilen kucuk bir kutuphane uygulamasini
icerir. Calisma once komut satiri uygulamasi olarak baslar, ardindan Open
Library entegrasyonu ve FastAPI endpointleriyle genisler.

## Kapsam

- `models/`: `Book` modeli ve veri donusum yardimcilari
- `services/`: kitap ekleme, silme, arama ve JSON kaliciligi
- `main.py`: CLI uygulamasi
- `api.py`: FastAPI servisi
- `tests/`: servis ve API testleri

## Kurulum

```bash
cd python-202/library-api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`uv` kullaniyorsaniz:

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

## Kullanım

CLI:

```bash
python main.py
```

API:

```bash
uvicorn api:app --reload
```

API dokumantasyonu yerelde `/docs` ve `/redoc` uzerinden acilir.

## Test

```bash
python -m pytest tests -v
```

## Teknik Notlar

- Kitap verileri `library.json` dosyasinda tutulur.
- ISBN ile otomatik kitap bilgisi almak icin Open Library kullanilir.
- Harici API hatalarinda uygulamanin kontrollu hata donmesi hedeflenmistir.
- Bu calisma egitim amaclidir; kimlik dogrulama, rate limit ve production
  deployment kapsama alinmamistir.
