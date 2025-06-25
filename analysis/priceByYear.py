import pandas as pandas
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def analyze_year(df,chosen_marks):
    plt.figure(figsize=(12,6))
    for mark in chosen_marks:
        df_chosen_mark = df[df['mark'].str.lower() == mark]
        average_prices_year = df_chosen_mark.groupby('year')['price'].mean().reset_index()
        sns.lineplot(x='year', y='price', data=average_prices_year, marker='o', label=mark.capitalize())

    plt.title("Średnia cena od roku produkcji dla wybranych marek")
    plt.xlabel("Rok produkcji")
    plt.ylabel("Średnia cena (PLN)")
    plt.legend(title="Marka")
    plt.tight_layout()
    plt.show()
    st.pyplot(plt.gcf())
    plt.clf()

