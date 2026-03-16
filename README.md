# 🌤️ Automatyczny Monitor Pogody (ETL Pipeline)

Projekt typu ETL (Extract, Transform, Load) pobierający dane o pogodzie z API (OpenWeatherMap) i zapisujący je w chmurowej relacyjnej bazie danych PostgreSQL (Neon.tech).

## 🛠️ Technologie
* **Python 3**
* **PostgreSQL (Neon)** - Chmurowa baza danych
* **API:** OpenWeatherMap
* **Biblioteki:** `requests`, `psycopg2`, `python-dotenv`

## 🚀 Jak uruchomić projekt lokalnie?
1. Sklonuj repozytorium.
2. Stwórz i aktywuj wirtualne środowisko: `python -m venv venv`
3. Zainstaluj pakiety: `pip install -r requirements.txt`
4. Stwórz plik `.env` na wzór `.env.example` i wpisz tam swoje klucze dostępowe.
5. (Kolejne kroki dodamy w miarę pisania kodu...)