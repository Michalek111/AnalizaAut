import pandas as pandas
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def analyze_price_by_engine_volume(df,chosen_marks):

    df_filtered = df[(df['vol_engine'] > 0) & (df['mark'].str.lower().isin(chosen_marks))]
    plt.figure(figsize=(12,6))
    for mark in chosen_marks:
        df_chosen_mark = df_filtered[df_filtered['mark'].str.lower() == mark]
        avg_price_engine = df_chosen_mark.groupby('vol_engine')['price'].mean().reset_index()
        sns.lineplot(x='vol_engine', y='price', data=avg_price_engine, marker='o', label=mark.capitalize())

    plt.title("Średnia cena w zależności od pojemności silnika")
    plt.xlabel("Pojemność silnika (cm3)")
    plt.ylabel("Średnia cena (PLN)")
    plt.legend(title="Marka")
    plt.tight_layout()
    plt.show()
    st.pyplot(plt.gcf())
    plt.clf()