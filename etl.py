import os
import psycopg2
import requests
from datetime import datetime
from dotenv import load_dotenv
import analytics

#--------------------------------------------------------------------------------------------------------------
#czesc wykorzystywana do napisnia kodu zmienianego w funkcje
#--------------------------------------------------------------------------------------------------------------


#korzystamy w celu bezpiecznego przechowania poufnych informacji
#load_dotenv() #funkcja do wczytywania zmiennych srodowiskowych z pliku .env

#api = os.getenv('API_KEY') #pobieranie klucza API z zmiennych srodowiskowych
#base = os.getenv('DB_URL') #pobieranie URL bazy danych z zmiennych srodowisowych

#print("API Key:", os.getenv('API_KEY')[:5]) sprawdzenie

#polaczenie z baza danych
#try:
#    conn = psycopg2.connect(base) #link ma wszystko co potrzebne do polaczenia
#    cursor = conn.cursor()
#    query = "CREATE TABLE IF NOT EXISTS weather_log " \
#    "(id SERIAL PRIMARY KEY, " \
#    "city VARCHAR(50), " \
#    "temperature FLOAT, " \
#    "humidity INT, " \
#    "weather_description VARCHAR(100), " \
#    "timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
#    cursor.execute(query) #wykonanie zapytania
#    conn.commit() #zatwierdzenie zmian w bazie danych

#    print("Utworzono tabelę lub już istnieje.") #sprawdzenie

#    cursor.close() #zamkniecie kursora
#    conn.close() #zamkniecie polaczenia z baza danych
#except Exception as e:
#    print(f"Nie można połączyć z bazą danych: {e}") # rzuca wyjatek

#ekstrakcja danych z API i zapis do bazy
#cities = ["Warszawa", "Kraków", "Radom", "Wrocław", "Poznań"] #lista miast do sledzenia pogody

#connect = psycopg2.connect(base)
#cursor = connect.cursor()

#for city in cities:
#    #print(miasto) #sprawdzenie
#    # 'miasto' to zmienna z Twojej pętli for, a 'api' to Twój klucz z pliku .env
#    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric" #tworzenie URL do zapytania API
#    response = requests.get(url) #wyslanie zapytania do API
#    if response.status_code == 200:
#        #transformacja danych
#        data = response.json() #przetwarzanie odpowiedzi z API na format JSON
#        temperature = round(data['main']['temp'], 1) #pobieranie temperatury
#        humidity = data['main']['humidity'] #pobieranie wilgotnosci
#        weather_description = data['weather'][0]['description'] #pobieranie opisu pogody
#        date = data['dt'] #pobieranie daty i czasu
#        normal_date = datetime.fromtimestamp(date) #konwersja daty na czytelna forme
#        #print(f"Data: {normal_date}, Miasto: {city}, Temperatura: {temperature}, Wilgotność: {humidity}, Opis: {weather_description}") #sprawdzenie
#        #zapis do bazy danych
#        sql = "INSERT INTO weather_log (city, temperature, humidity, weather_description, timestamp) VALUES" \
#        "(%s, %s, %s, %s, %s)" #zapytanie SQL do wstawiania danych do tabeli nigdy nie uzywam yf string do zapytan sql, moze prowadzic do atakow SQL injection
#        values = (city, temperature, humidity, weather_description, normal_date) # wartosci do wstawienia dla bezpieczenstwa i czytelnosci
#        cursor.execute(sql, values) #wykonanie zapytania z podanymi wartosciami
#    else:
#        print(f"Nie udało się pobrać danych dla miasta {city}") #sprawdzenie
#        continue #przejscie do 

#connect.commit() #zatwierdzenie zmian w bazie danych
#cursor.close()    
#connect.close()

#zamiana kodu na funkcje
def fetch_weather_data(city, api_key):
    #pobieranie danych pogodowych dla danego miasta z API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def transform_data(city, data):
    #przetwarzanie danych z API na format odpowiedni do zapisu
    temperature = round(data['main']['temp'], 1)
    humidity = data['main']['humidity']
    weather_description = data['weather'][0]['description']
    date = data['dt']
    normal_date = datetime.fromtimestamp(date)
    return (city, temperature, humidity, weather_description, normal_date)

def load_to_db(data_tuple, db_url):
    #zapis do bazy dnych
    try:
        conn = psycopg2.connect(db_url)
        cursor = conn.cursor()
        sql = "INSERT INTO weather_log (city, temperature, humidity, weather_description, timestamp) VALUES" \
        "(%s, %s, %s, %s, %s)"
        cursor.execute(sql, data_tuple)
        conn.commit()
        cursor.close()    
        conn.close()
    except Exception as e:
        print(f"Nie mozna polaczyc z baza danych: {e}")

def main():
    #glowna funkcja do wykonania procesu ETL
    load_dotenv() #funkcja do wczytywania zmiennych srodowiskowych z pliku .env
    api = os.getenv('API_KEY') #pobieranie klucza API z zmiennych srodowiskowych
    base = os.getenv('DB_URL') #pobieranie URL bazy danych z zmiennych srodowisowych
    cities = ["Warszawa", "Kraków", "Radom", "Wrocław", "Poznań"] #lista miast do sledzenia pogody
    for city in cities:
        data = fetch_weather_data(city, api)
        if data:
            transformed = transform_data(city, data)
            load_to_db(transformed, base)
    analytics.generuj_raport()

if __name__ == "__main__":
    main()