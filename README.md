# 🚗 Analiza Rynku Samochodowego w Polsce

Interaktywna aplikacja webowa do analizy danych o cenach i ofercie samochodów w Polsce, zbudowana w Streamlit.

## 📊 Funkcjonalności

### Dostępne Analizy:
- **📈 Zależność ceny od przebiegu** - Analiza korelacji między przebiegiem a ceną pojazdu
- **📅 Średnia cena od roku produkcji** - Trendy cenowe w zależności od rocznika
- **🗺️ Liczba ofert w województwach** - Geograficzne rozmieszczenie ofert
- **💰 Najdroższe i najtańsze modele** - Ranking modeli według cen
- **⭐ Najbardziej i najmniej popularny model** - Analiza popularności modeli
- **⛽ Rodzaje paliwa** - Rozkład typów napędu na rynku
- **🏙️ TOP 10 miast z największą liczbą ofert** - Koncentracja ofert w miastach
- **🔧 Zależność ceny od pojemności silnika** - Wpływ pojemności na cenę

### Kluczowe Cechy:
- 🎯 **Filtrowanie według marek** - Wybierz interesujące Cię marki samochodów
- 📊 **Interaktywne wykresy** - Wizualizacje wykonane w matplotlib i seaborn
- 🔍 **Analiza w czasie rzeczywistym** - Natychmiastowe wyniki po zmianie filtrów
- 📱 **Responsywny interfejs** - Działa na różnych urządzeniach

## 🛠️ Technologie

- **Frontend**: Streamlit
- **Backend**: Python 3.11+
- **Baza danych**: SQLite
- **Wizualizacje**: Matplotlib, Seaborn
- **Analiza danych**: Pandas, NumPy


### Kroki instalacji:

1. **Sklonuj repozytorium:**
```bash
git clone https://github.com/Michalek111/AnalizaAut
cd AnalizaAut
```

2. **Zainstaluj wymagane pakiety:**
```bash
pip install streamlit pandas matplotlib seaborn sqlite3
```

3. **Przejdź do katalogu aplikacji:**
```bash
cd KosztyAutPolska
```

4. **Uruchom aplikację:**
```bash
python -m streamlit run app.py
```

5. **Otwórz przeglądarkę:**
Aplikacja będzie dostępna pod adresem: `http://localhost:xxxx`

## 📖 Jak używać

1. **Wybierz marki samochodów** z listy rozwijanej (możesz wybrać kilka marek jednocześnie)
2. **Wybierz typ analizy** z dostępnych opcji
3. **Przeglądaj wyniki** w formie wykresów i statystyk
4. **Eksperymentuj** z różnymi kombinacjami marek i analiz

