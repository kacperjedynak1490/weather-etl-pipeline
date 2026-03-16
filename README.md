# 🌤️ Automatyczny Monitor Pogody (ETL Pipeline)

Profesjonalny projekt typu **End-to-End ETL** (Extract, Transform, Load), który w pełni automatycznie gromadzi dane meteorologiczne, zapisuje je w chmurowej bazie danych i generuje cykliczne raporty analityczne.

## 🏗️ Architektura Projektu
Projekt realizuje pełny obieg danych w architekturze nowoczesnego Data Pipeline:

1.  **Extract (Pobieranie):** Automatyczne pobieranie danych pogodowych (temperatura, wilgotność, opis) z API OpenWeatherMap dla 5 kluczowych miast Polski.
2.  **Transform (Przetwarzanie):** Walidacja danych, konwersja jednostek oraz obsługa błędów za pomocą Pythona.
3.  **Load (Ładowanie):** Zapis przetworzonych informacji do relacyjnej, chmurowej bazy danych **PostgreSQL (Neon.tech)**.
4.  **Analyze (Analiza):** Wykonywanie zapytań SQL w celu obliczenia średnich temperatur miesięcznych i generowanie raportu tekstowego.

## 🤖 Automatyzacja (CI/CD)
System jest całkowicie bezobsługowy dzięki wykorzystaniu **GitHub Actions**:
* **Harmonogram:** Pipeline uruchamia się automatycznie **co 6 godzin**.
* **Workflow:** Robot w chmurze konfiguruje środowisko Python, instaluje zależności, wykonuje skrypt ETL i generuje raport.
* **Auto-Update:** Po każdym przebiegu system automatycznie aktualizuje plik `average_temp.txt` w repozytorium, informując o najświeższych wynikach.

## 🛠️ Stack Technologiczny
* **Język:** Python 3.11
* **Baza Danych:** PostgreSQL (Hostowana na Neon.tech)
* **Automatyzacja:** GitHub Actions
* **Komunikacja:** REST API (Requests)
* **Biblioteki:** `psycopg2-binary`, `python-dotenv`, `requests`

## 📊 Przykładowy Raport
Wygenerowany automatycznie raport (`average_temp.txt`) zawiera dane w formacie:
> `Srednia wartosci temperatury dla Warszawa w miesiacu Marzec wynosi 7.0°C`
> `************************************************************`

## 🚀 Uruchomienie lokalne
Jeśli chcesz przetestować system na własnym komputerze:

1.  **Sklonuj repozytorium:**
    ```bash
    git clone [https://github.com/TWOJA-NAZWA/weather-etl-pipeline.git](https://github.com/TWOJA-NAZWA/weather-etl-pipeline.git)
    cd weather-etl-pipeline
    ```
2.  **Skonfiguruj środowisko:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
3.  **Zmienne środowiskowe:**
    Stwórz plik `.env` i uzupełnij go swoimi danymi:
    ```env
    API_KEY=twój_klucz_openweathermap
    DB_URL=link_do_twojej_bazy_neon_postgres
    ```
4.  **Uruchom proces:**
    ```bash
    python etl.py
    ```