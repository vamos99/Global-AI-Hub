# Global AI Hub Egitim Calismalari

Bu repo, Global AI Hub egitimleri sirasinda hazirlanan pratik calismalari
toplar. Ana odak Python 202 kapsamindaki kucuk Library API projesidir.

## Icerik

| Klasor | Kapsam | Not |
| --- | --- | --- |
| `python-202/library-api/` | CLI + FastAPI kutuphane uygulamasi | OOP, harici API kullanimi, test yazimi |

## One Cikan Calisma

`python-202/library-api/` klasoru ISBN ile kitap ekleme, JSON dosyasina
kalici kayit tutma ve ayni is mantigini FastAPI endpointleriyle sunma
akisini gosterir. Proje egitim amaclidir; production servisi gibi
konumlandirilmamistir.

## Calistirma

```bash
git clone https://github.com/vamos99/Global-AI-Hub.git
cd Global-AI-Hub/python-202/library-api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

API servisi icin:

```bash
uvicorn api:app --reload
```

Testler:

```bash
python -m pytest tests -v
```

## Notlar

- Bu repo egitim/odev arsivi niteligindedir.
- API ornekleri Open Library gibi dis kaynaklara bagli oldugu icin internet
  baglantisi gerektirebilir.
