from tools.db_handler import get_data_from_db
from analysis.priceByMileage import analyze_mileage
from analysis.priceByYear import analyze_year
from analysis.markByProvince import analyze_mark_by_province
from analysis.topModels import analyze_top_models
from analysis.popularModels import analyze_popular_models
from analysis.fuelTypes import analyze_fuel_types
from analysis.mostCountOfferts import analyze_MostCountOfferts
from analysis.priceByEngineVolume import analyze_price_by_engine_volume

DB_PATH = 'data/bazaAut.db'
TABLE_NAME = 'tabelaAutPolska'  

df = get_data_from_db(DB_PATH, TABLE_NAME)

available_marks = df['mark'].str.lower().unique()
print("Dostępne marki:", ", ".join(sorted(available_marks)))

def choose_marks():
    chosen_marks = []
    while not chosen_marks:
        chosen_marks = input("\nPodaj marki samochodów (oddzielone przecinkami): ").lower().split(',')
        chosen_marks = [mark.strip() for mark in chosen_marks]
        invalid = [mark for mark in chosen_marks if mark not in available_marks]
        if invalid:
            print(f"Niepoprawne: {', '.join(invalid)}. Spróbuj ponownie.")
            chosen_marks = []
    return chosen_marks

def main_menu():
    print("\nWybierz analizę:")
    print("1. Zależność ceny od przebiegu")
    print("2. Średnia cena od roku produkcji")
    print("3. Liczba wystąpień marki w województwach")
    print("4. Najdroższe i najtańsze modele")
    print("5. Najbardziej i najmniej popularny model")
    print("6. Wystąpienia w zależności od rodzaju paliwa")
    print("7. TOP 10 miast z największą liczbą ofert")
    print("8. Zależność ceny od pojemności silnika")
    print("0. Zakończ")
    return input("Wybierz opcję: ")


chosen_marks = choose_marks()


while True:
    choice = main_menu()
    if choice == '0':
        print("Dziękujemy za skorzystanie z analizy!")
        break
    elif choice == '1':
        analyze_mileage(df, chosen_marks)
    elif choice == '2':
        analyze_year(df, chosen_marks)
    elif choice == '3':
        analyze_mark_by_province(df, chosen_marks)
    elif choice == '4':
        analyze_top_models(df, chosen_marks)
    elif choice == '5':
        analyze_popular_models(df, chosen_marks)
    elif choice == '6':
        analyze_fuel_types(df, chosen_marks)
    elif choice == '7':
        analyze_MostCountOfferts(df)
    elif choice == '8':
        analyze_price_by_engine_volume(df,chosen_marks)
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")