import pandas as pandas
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def analyze_MostCountOfferts(df, chosen_marks):
    # Filtrowanie danych według wybranych marek
    df_filtered = df[df['mark'].str.lower().isin(chosen_marks)]

    top_10_cities = df_filtered['city'].value_counts().head(10).reset_index()
    top_10_cities.columns = ['City', 'Count']

    print(f"TOP 10 miast pod względem liczby ofert dla marek: {', '.join(chosen_marks)}")
    print(top_10_cities)

    plt.figure(figsize=(12,6))
    sns.barplot(x='City', y='Count', data=top_10_cities, palette='viridis')
    plt.title(f"TOP 10 miast pod względem liczby ofert\nDla marek: {', '.join(chosen_marks)}")
    plt.xlabel("Miasto")
    plt.ylabel("Liczba ofert")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    st.pyplot(plt.gcf())
    plt.clf()

