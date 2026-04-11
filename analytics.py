import os
import psycopg2
from dotenv import load_dotenv

#polaczenie z baza danych i wczytanie zmiennych srodowiskowych
def generuj_raport():
    load_dotenv()
    api = os.getenv('API_KEY')
    base = os.getenv('DB_URL')
        
    nazwy_miesiecy = {1: "Styczeń", 
                    2: "Luty", 
                    3: "Marzec", 
                    4: "Kwiecień", 
                    5: "Maj", 
                    6: "Czerwiec", 
                    7: "Lipiec",
                    8: "Sierpień",
                    9: "Wrzesień",
                    10: "Październik",
                    11: "Listopad",
                    12: "Grudzień"}

    try:
        conn = psycopg2.connect(base)
        cursor = conn.cursor()
        #zapytanie do sql liczace srednia temperature dla kazdego z miast
        sql = "SELECT city, AVG(temperature), EXTRACT(MONTH from timestamp) FROM weather_log " \
            "GROUP BY city, EXTRACT(MONTH from timestamp) ORDER BY city ASC, EXTRACT(MONTH from timestamp) ASC"
        #aby czytac uzywamy cursor.fetchall()
        cursor.execute(sql)
        wyniki = cursor.fetchall()
        #print(wyniki)
        #prezentacja
        with open("average_temp.txt", mode="w", encoding="UTF-8") as plik:
            #zapisujemy dane do pliku
            plik.write("Analiza średniej temperatury powietrza w danym mieście:\n\n")

            for wartosc in wyniki:
                city = wartosc[0]
                avg_temp = round(wartosc[1], 1)
                month_num = int(wartosc[2])
                month = nazwy_miesiecy.get(month_num, "Nieznany")
                linijka = f"Srednia wartosci temperatury dla {city} w miesiacu {month} wynosi {avg_temp}°C\n"
                plik.write(linijka)
                plik.write("*"*60+"\n")
        #zamkniecie
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Nie można połączyć z bazą danych: {e}")

if __name__ == "__main__":
    generuj_raport()