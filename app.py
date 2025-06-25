import streamlit as st
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


st.title("Analiza Danych o Samochodach w Polsce")

available_marks = sorted(df['mark'].str.lower().unique())
chosen_marks = st.multiselect("Wybierz marki samochodów:", available_marks)

if chosen_marks:
    analysis = st.selectbox("Wybierz analizę:", [
        "Zależność ceny od przebiegu",
        "Średnia cena od roku produkcji",
        "Liczba ofert w województwach",
        "Najdroższe i najtańsze modele",
        "Najbardziej i najmniej popularny model",
        "Rodzaje paliwa",
        "TOP 10 miast z największą liczbą ofert",
        "Zależność ceny od pojemności silnika"
    ])

    if analysis == "Zależność ceny od przebiegu":
        analyze_mileage(df, chosen_marks)
    elif analysis == "Średnia cena od roku produkcji":
        analyze_year(df, chosen_marks)
    elif analysis == "Liczba ofert w województwach":
        analyze_mark_by_province(df, chosen_marks)
    elif analysis == "Najdroższe i najtańsze modele":
        analyze_top_models(df, chosen_marks)
    elif analysis == "Najbardziej i najmniej popularny model":
        analyze_popular_models(df, chosen_marks)
    elif analysis == "Rodzaje paliwa":
        analyze_fuel_types(df, chosen_marks)
    elif analysis == "TOP 10 miast z największą liczbą ofert":
        analyze_MostCountOfferts(df, chosen_marks)
    elif analysis == "Zależność ceny od pojemności silnika":
        analyze_price_by_engine_volume(df,chosen_marks)

else:
    st.info("👉 Wybierz co najmniej jedną markę, aby rozpocząć analizę.")
