import pandas as pandas
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def analyze_mark_by_province(df,chosen_marks):
    for mark in chosen_marks:
        df_chosen_mark = df[df['mark'].str.lower() == mark]

      
        province_counts = df_chosen_mark['province'].value_counts().reset_index()
        province_counts.columns = ['Province', 'Count']

       
        plt.figure(figsize=(12,6))
        sns.barplot(x='Province', y='Count', data=province_counts, palette='viridis')
        
        
        for i, row in enumerate(province_counts.itertuples()):
            plt.text(i, row.Count + 50, f"{row.Count}", ha='center', fontsize=10, color='black')

        plt.title(f"Liczba samochodów marki {mark.capitalize()} w poszczególnych województwach")
        plt.xlabel("Województwo")
        plt.ylabel("Liczba samochodów")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        st.pyplot(plt.gcf())
        plt.clf()