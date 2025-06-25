import pandas as pandas
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def analyze_mileage(df,chosen_marks):
    plt.figure(figsize=(12,6))
    for mark in chosen_marks:
        df_chosen_mark = df[df['mark'].str.lower() == mark]
        df_chosen_mark['mileage_group'] = (df_chosen_mark['mileage'] // 10000) * 10000
        average_prices = df_chosen_mark.groupby('mileage_group')['price'].mean().reset_index()
        sns.lineplot(x='mileage_group', y='price', data=average_prices, marker='o', label=mark.capitalize())

    plt.title("Zależność ceny od przebiegu dla wybranych marek")
    plt.xlabel("Przebieg (km)")
    plt.ylabel("Cena (PLN)")
    plt.legend(title="Marka")
    plt.tight_layout()
    plt.show()
    st.pyplot(plt.gcf())
    plt.clf()
