import pandas as pandas
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def analyze_fuel_types(df,chosen_marks):
    for mark in chosen_marks:
        df_chosen_mark = df[df['mark'].str.lower() == mark]

       
        fuel_counts = df_chosen_mark['fuel'].value_counts().reset_index()
        fuel_counts.columns = ['Fuel', 'Count']

       
        plt.figure(figsize=(10,6))
        sns.barplot(x='Fuel', y='Count', data=fuel_counts, palette='viridis')
        
        
        for i, row in enumerate(fuel_counts.itertuples()):
            plt.text(i, row.Count + 50, f"{row.Count}", ha='center', fontsize=10, color='black')

        plt.title(f"Liczba samochodów marki {mark.capitalize()} z podziałem na rodzaj paliwa")
        plt.xlabel("Rodzaj paliwa")
        plt.ylabel("Liczba samochodów")
        plt.tight_layout()
        plt.show()
        st.pyplot(plt.gcf())
        plt.clf()
