# Book API

REST API do zarządzania książkami, stworzone w Pythonie z użyciem Flask.

## Technologie
- Python  
- Flask  
- SQLite  

## Jak uruchomić lokalnie

1. Zainstaluj wymagania:
pip install -r requirements.txt
2. Uruchom serwer:
python app.py
3. API będzie dostępne pod adresem `http://127.0.0.1:5000`

## Endpointy

| Metoda | URL           | Opis                   |
|--------|---------------|------------------------|
| GET    | /books        | Pobierz listę książek  |
| GET    | /books/<id>   | Pobierz książkę po ID  |
| POST   | /books        | Dodaj nową książkę     |
| PUT    | /books/<id>   | Edytuj książkę         |
| DELETE | /books/<id>   | Usuń książkę           |

---

## Autor  
BoosTer  

