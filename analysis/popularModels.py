import pandas as pandas
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def analyze_popular_models(df,chosen_marks):
    for mark in chosen_marks:
        df_chosen_mark = df[df['mark'].str.lower() == mark]

        most_popular = df_chosen_mark['model'].value_counts().idxmax()
        least_popular = df_chosen_mark['model'].value_counts().idxmin()

        
        most_popular_count = df_chosen_mark['model'].value_counts().max()
        least_popular_count = df_chosen_mark['model'].value_counts().min()

        
        popular_models = pandas.DataFrame({
            'Model': [most_popular, least_popular],
            'Count': [most_popular_count, least_popular_count],
            'Type': ['Najbardziej popularny', 'Najmniej popularny']
        })

    
        plt.figure(figsize=(10,6))
        sns.barplot(x='Model', y='Count', hue='Type', data=popular_models, palette=['#4e79a7', '#e15759'])

       
        for i, row in enumerate(popular_models.itertuples()):
            plt.text(i, row.Count + 5, f"{row.Count} aut", ha='center', fontsize=10, color='black')

        plt.title(f"Najbardziej i najmniej popularny model {mark.capitalize()}")
        plt.xlabel("Model")
        plt.ylabel("Liczba samochodów")
        plt.tight_layout()
        plt.show()
        st.pyplot(plt.gcf())
        plt.clf()

