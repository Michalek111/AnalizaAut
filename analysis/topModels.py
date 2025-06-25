import pandas as pandas
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def analyze_top_models(df,chosen_marks):
    for mark in chosen_marks:
        df_chosen_mark = df[df['mark'].str.lower() == mark]
        top_expensive = df_chosen_mark.loc[df_chosen_mark['price'].idxmax()]
        top_cheap = df_chosen_mark.loc[df_chosen_mark['price'].idxmin()]

        top_models = pandas.DataFrame([top_expensive, top_cheap])
        top_models['Type'] = ['Najdroższy', 'Najtańszy']


        plt.figure(figsize=(10,6))
        sns.barplot(x='model', y='price', hue='Type', data=top_models, palette=['#4e79a7', '#e15759'])

      
        for i, row in enumerate(top_models.itertuples()):
            plt.text(i, row.price + 5000, f"{row.price:.0f} PLN", ha='center', fontsize=10, color='black')

        plt.title(f"Najdroższy i najtańszy model {mark.capitalize()}")
        plt.xlabel("Model")
        plt.ylabel("Cena (PLN)")
        plt.tight_layout()
        plt.show()
        st.pyplot(plt.gcf())
        plt.clf()
